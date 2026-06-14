#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv"]
# ///
import os, json, requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN      = os.getenv('META_ACCESS_TOKEN')
ACCOUNT_ID = os.getenv('META_AD_ACCOUNT_ID')
BASE       = 'https://graph.facebook.com/v23.0'

def fetch(endpoint, params=None):
    params = dict(params or {})
    params['access_token'] = TOKEN
    r = requests.get(f'{BASE}/{endpoint}', params=params)
    if not r.ok:
        print(f'API error {r.status_code} on {endpoint}: {r.text[:300]}')
        r.raise_for_status()
    return r.json()

def pull_account():
    return fetch(f'act_{ACCOUNT_ID}', {
        'fields': 'name,account_status,currency,amount_spent'
    })

def pull_campaigns(days=7):
    data = fetch(f'act_{ACCOUNT_ID}/campaigns', {
        'fields': 'name,status,objective,insights.date_preset(last_7d){spend,impressions,clicks,ctr,cpc,actions,action_values}',
        'limit': 50
    })
    return data.get('data', [])

def pull_insights(days=7):
    preset_map = {7: 'last_7d', 14: 'last_14d', 28: 'last_28d', 30: 'last_30d', 90: 'last_90d'}
    preset = preset_map.get(days, 'last_7d')
    data = fetch(f'act_{ACCOUNT_ID}/insights', {
        'fields': 'spend,impressions,clicks,ctr,cpc,actions,action_values',
        'date_preset': preset,
        'level': 'account'
    })
    results = data.get('data', [])
    if results:
        return results[0]
    print(f'  No data for {preset}, falling back to all-time data...')
    fallback = fetch(f'act_{ACCOUNT_ID}/insights', {
        'fields': 'spend,impressions,clicks,ctr,cpc,actions,action_values',
        'date_preset': 'maximum',
        'level': 'account'
    })
    return fallback.get('data', [{}])[0] if fallback.get('data') else {}

def compute_metrics(insights, campaigns, days=7):
    spend       = float(insights.get('spend', 0))
    impressions = int(insights.get('impressions', 0))
    clicks      = int(insights.get('clicks', 0))
    ctr         = float(insights.get('ctr', 0))
    cpc         = float(insights.get('cpc', 0))

    # Meta returns purchases under multiple action_type keys depending on pixel setup
    PURCHASE_TYPES = {'purchase', 'offsite_conversion.fb_pixel_purchase', 'omni_purchase'}
    purchases = 0
    revenue   = 0.0
    for action in insights.get('actions', []):
        if action.get('action_type') in PURCHASE_TYPES:
            purchases += int(action.get('value', 0))
    for av in insights.get('action_values', []):
        if av.get('action_type') in PURCHASE_TYPES:
            revenue += float(av.get('value', 0))

    roas = round(revenue / spend, 2) if spend > 0 else 0
    active_campaigns = [c for c in campaigns if c.get('status') == 'ACTIVE']

    return {
        'period_days':      days,
        'spend':            round(spend, 2),
        'impressions':      impressions,
        'clicks':           clicks,
        'ctr':              round(ctr, 2),
        'cpc':              round(cpc, 2),
        'purchases':        purchases,
        'revenue':          round(revenue, 2),
        'roas':             roas,
        'active_campaigns': len(active_campaigns),
        'total_campaigns':  len(campaigns),
        'pulled_at':        datetime.now().isoformat()
    }

def run_sync(days=7):
    os.makedirs('data-sync/raw', exist_ok=True)
    os.makedirs('data-sync/processed', exist_ok=True)

    print(f'Pulling Meta Ads data ({days} days)...')
    account   = pull_account()
    campaigns = pull_campaigns(days)
    insights  = pull_insights(days)
    metrics   = compute_metrics(insights, campaigns, days)

    snapshot = {
        'account':   account,
        'metrics':   metrics,
        'campaigns': campaigns[:20],
        'insights':  insights
    }

    date_str = datetime.now().strftime('%Y-%m-%d')
    with open(f'data-sync/raw/meta_{date_str}.json', 'w') as f:
        json.dump(snapshot, f, indent=2)
    with open('data-sync/processed/meta_latest.json', 'w') as f:
        json.dump(snapshot, f, indent=2)

    print(f'Meta sync done -> Spend: Rs.{metrics["spend"]:,} | ROAS: {metrics["roas"]}x | Clicks: {metrics["clicks"]} | CPC: Rs.{metrics["cpc"]}')
    return snapshot

if __name__ == '__main__':
    import sys
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    run_sync(days)
