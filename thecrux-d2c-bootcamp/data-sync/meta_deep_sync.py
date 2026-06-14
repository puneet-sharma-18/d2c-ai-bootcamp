#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv"]
# ///
"""Deep Meta Ads sync: account -> campaigns -> ad sets (with targeting) -> ads (with creative).

Run with uv (installs deps automatically, no venv needed):
    uv run data-sync/meta_deep_sync.py 30

Day windows: 7, 14, 28, 30, 90 (anything else defaults to 7). Writes
data-sync/processed/meta_deep_latest.json, which the Meta Ads analyst prompt reads.
"""
import os
import json
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('META_ACCESS_TOKEN')
ACCOUNT_ID = os.getenv('META_AD_ACCOUNT_ID')
BASE = 'https://graph.facebook.com/v23.0'

PRESET_MAP = {7: 'last_7d', 14: 'last_14d', 28: 'last_28d', 30: 'last_30d', 90: 'last_90d'}

INSIGHT_FIELDS = 'spend,impressions,clicks,ctr,cpc,reach,frequency,actions,action_values'

# Meta reports purchases under different action_type keys depending on pixel/CAPI setup.
# Matching only 'purchase' makes a standard-pixel account look like it had zero sales.
PURCHASE_TYPES = {'purchase', 'offsite_conversion.fb_pixel_purchase', 'omni_purchase'}


def fetch(endpoint, params=None):
    params = dict(params or {})
    params['access_token'] = TOKEN
    r = requests.get(f'{BASE}/{endpoint}', params=params)
    if not r.ok:
        print(f'API error {r.status_code} on {endpoint}: {r.text[:300]}')
        r.raise_for_status()
    return r.json()


def paginate(endpoint, params, hard_cap=500):
    out = []
    data = fetch(endpoint, params)
    while True:
        out.extend(data.get('data', []))
        if len(out) >= hard_cap:
            return out[:hard_cap]
        next_url = data.get('paging', {}).get('next')
        if not next_url:
            return out
        r = requests.get(next_url)
        if not r.ok:
            return out
        data = r.json()


def pull_account():
    return fetch(f'act_{ACCOUNT_ID}', {
        'fields': 'name,account_status,currency,amount_spent,timezone_name,business_country_code'
    })


def determine_window(days):
    """Probe account insights with requested preset. If empty, fall back to 'maximum'."""
    preset = PRESET_MAP.get(days, 'last_7d')
    data = fetch(f'act_{ACCOUNT_ID}/insights', {
        'fields': INSIGHT_FIELDS,
        'date_preset': preset,
        'level': 'account',
    })
    if data.get('data'):
        return preset, data['data'][0]

    print(f'  No data for {preset}, falling back to all-time (maximum)...')
    fb = fetch(f'act_{ACCOUNT_ID}/insights', {
        'fields': INSIGHT_FIELDS,
        'date_preset': 'maximum',
        'level': 'account',
    })
    fb_data = fb.get('data', [])
    return 'maximum', (fb_data[0] if fb_data else {})


def pull_campaigns(preset):
    return paginate(f'act_{ACCOUNT_ID}/campaigns', {
        'fields': (
            'name,status,objective,buying_type,start_time,stop_time,daily_budget,lifetime_budget,'
            f'insights.date_preset({preset}){{{INSIGHT_FIELDS}}}'
        ),
        'limit': 100,
    })


def pull_adsets(preset):
    return paginate(f'act_{ACCOUNT_ID}/adsets', {
        'fields': (
            'name,status,campaign_id,optimization_goal,billing_event,bid_strategy,'
            'daily_budget,lifetime_budget,start_time,end_time,targeting,'
            f'insights.date_preset({preset}){{{INSIGHT_FIELDS}}}'
        ),
        'limit': 100,
    })


def pull_ads(preset):
    return paginate(f'act_{ACCOUNT_ID}/ads', {
        'fields': (
            'name,status,adset_id,campaign_id,'
            'creative{id,name,title,body,call_to_action_type,object_story_spec,'
            'image_url,thumbnail_url,video_id,effective_object_story_id,object_type},'
            f'insights.date_preset({preset}){{{INSIGHT_FIELDS}}}'
        ),
        'limit': 100,
    })


def extract_purchase_metrics(insight_obj):
    purchases = 0
    revenue = 0.0
    for a in insight_obj.get('actions', []) or []:
        if a.get('action_type') in PURCHASE_TYPES:
            purchases += int(float(a.get('value', 0)))
    for av in insight_obj.get('action_values', []) or []:
        if av.get('action_type') in PURCHASE_TYPES:
            revenue += float(av.get('value', 0))
    return purchases, revenue


def flatten_entity_insights(entities):
    """Pull the (singleton) insights array up one level on each entity for easier downstream use."""
    for e in entities:
        ins_block = e.get('insights')
        if isinstance(ins_block, dict):
            ins_list = ins_block.get('data', [])
            ins = ins_list[0] if ins_list else {}
        else:
            ins = {}
        purchases, revenue = extract_purchase_metrics(ins)
        spend = float(ins.get('spend', 0) or 0)
        e['perf'] = {
            'spend': round(spend, 2),
            'impressions': int(ins.get('impressions', 0) or 0),
            'clicks': int(ins.get('clicks', 0) or 0),
            'ctr': round(float(ins.get('ctr', 0) or 0), 2),
            'cpc': round(float(ins.get('cpc', 0) or 0), 2),
            'reach': int(ins.get('reach', 0) or 0),
            'frequency': round(float(ins.get('frequency', 0) or 0), 2),
            'purchases': purchases,
            'revenue': round(revenue, 2),
            'roas': round(revenue / spend, 2) if spend > 0 else 0,
        }
        e.pop('insights', None)
    return entities


def compute_account_metrics(insights, days, window_used, n_campaigns, n_adsets, n_ads):
    spend = float(insights.get('spend', 0) or 0)
    purchases, revenue = extract_purchase_metrics(insights)
    return {
        'period_days': days,
        'window_used': window_used,
        'spend': round(spend, 2),
        'impressions': int(insights.get('impressions', 0) or 0),
        'clicks': int(insights.get('clicks', 0) or 0),
        'ctr': round(float(insights.get('ctr', 0) or 0), 2),
        'cpc': round(float(insights.get('cpc', 0) or 0), 2),
        'reach': int(insights.get('reach', 0) or 0),
        'frequency': round(float(insights.get('frequency', 0) or 0), 2),
        'purchases': purchases,
        'revenue': round(revenue, 2),
        'roas': round(revenue / spend, 2) if spend > 0 else 0,
        'campaign_count': n_campaigns,
        'adset_count': n_adsets,
        'ad_count': n_ads,
        'pulled_at': datetime.now().isoformat(),
    }


def run_deep_sync(days=30):
    if not TOKEN or not ACCOUNT_ID:
        sys.exit('Missing META_ACCESS_TOKEN or META_AD_ACCOUNT_ID in .env')

    os.makedirs('data-sync/raw', exist_ok=True)
    os.makedirs('data-sync/processed', exist_ok=True)

    print(f'Pulling Meta Ads deep data ({days} days)...')
    account = pull_account()

    window_used, account_insights = determine_window(days)
    print(f'  Window resolved: {window_used}')

    print('  Fetching campaigns...')
    campaigns = flatten_entity_insights(pull_campaigns(window_used))
    print(f'    {len(campaigns)} campaigns')

    print('  Fetching ad sets (with targeting)...')
    adsets = flatten_entity_insights(pull_adsets(window_used))
    print(f'    {len(adsets)} ad sets')

    print('  Fetching ads (with creative)...')
    ads = flatten_entity_insights(pull_ads(window_used))
    print(f'    {len(ads)} ads')

    metrics = compute_account_metrics(
        account_insights, days, window_used, len(campaigns), len(adsets), len(ads)
    )

    snapshot = {
        'account': account,
        'metrics': metrics,
        'account_insights': account_insights,
        'campaigns': campaigns,
        'adsets': adsets,
        'ads': ads,
    }

    date_str = datetime.now().strftime('%Y-%m-%d')
    raw_path = f'data-sync/raw/meta_deep_{date_str}.json'
    latest_path = 'data-sync/processed/meta_deep_latest.json'
    with open(raw_path, 'w') as f:
        json.dump(snapshot, f, indent=2)
    with open(latest_path, 'w') as f:
        json.dump(snapshot, f, indent=2)

    currency = account.get('currency', '')
    print(
        f'Deep sync done [{window_used}] -> '
        f'Spend: {currency} {metrics["spend"]:,} | '
        f'ROAS: {metrics["roas"]}x | '
        f'Clicks: {metrics["clicks"]:,} | '
        f'CPC: {currency} {metrics["cpc"]} | '
        f'{metrics["campaign_count"]} campaigns / {metrics["adset_count"]} adsets / {metrics["ad_count"]} ads'
    )
    print(f'  -> {latest_path}')
    return snapshot


if __name__ == '__main__':
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    run_deep_sync(days)
