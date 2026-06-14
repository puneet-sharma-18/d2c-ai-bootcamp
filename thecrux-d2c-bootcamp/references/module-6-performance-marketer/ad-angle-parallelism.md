# Parallel Subagent Dispatch — The Teaching

This document goes deeper than the BRIEF on the new primitive Module 6 introduces. Instructors read it before the demo. Power-plan founders read it if they want to understand what is happening when they run POWER scope.

## The one rule that makes this work

The dispatcher is the **orchestrator** — your top-level Claude session in the terminal — not a subagent. A subagent cannot spawn subagents in Claude Code: nesting is capped at one level. So the parallel fan-out has to live one level up, at the orchestrator, the session that sits above every subagent.

(An earlier version of this module wired the fan-out *inside* the Performance Marketer subagent — "a parent subagent spawns 5 children." That does not run in parallel. A spawned subagent has no power to spawn its own children, so it just works the angles one after another. The fix is to keep the fan-out at the orchestrator.)

## What "parallel dispatch" means

A subagent runs in its own context window. Each spawn is a fresh thread with its own token budget.

In Day 1 / Module 4, the Content Lead was one subagent doing one big job. The orchestrator (main Claude in your terminal) spawned it once via the Task tool and waited for it to finish.

In Day 2 / Module 6 POWER scope, the orchestrator spawns **5 Performance Marketer subagents at once** via Task, one per angle. Each spawn gets:

- A copy of the shared context (CLAUDE.md, Market Analyst report, VoC report, Content Lead index) — each subagent reads it in its own context
- A single angle to work on (pinned with `ANGLES=N`)
- A specific output spec (10+ Meta ads + 5 Google headlines + 1 creative brief)

The 5 subagents run in **parallel**, not sequentially. From the orchestrator's perspective, all 5 Task calls fire roughly at once. The orchestrator waits for all 5 to return, then aggregates the results into one index file.

## Why this pattern exists

Three reasons.

### 1. Wall-clock time

Sequential: 5 angles × ~3 min each = ~15 min total wall-clock time.

Parallel: 5 angles fire at once, each ~3 min, the orchestrator waits for the slowest. ~3 to 4 min total wall-clock time.

For a 75-minute workshop slot with 30 founders, the difference between 15 min per founder and 4 min per founder is the difference between "the module fits" and "the module does not fit".

### 2. Context isolation

Each subagent has its own context window. If one angle is heavy (say, the Competitor-gap angle pulled in 30K tokens of Market Analyst data), the others are unaffected. The orchestrator's main context stays clean.

If you ran this sequentially in the orchestrator's context, by the time you got to angle 5, the main context would be carrying the artifacts from angles 1 to 4. You either burn tokens re-reading them, or you drop them and lose continuity.

### 3. Failure isolation

If one subagent fails (rate limit hit, prompt confused it, context overflow), the orchestrator gets back 4 successful results and 1 failure. It flags the failure in the index. Founder re-runs just that angle.

In a single big subagent, one failure crashes the entire run. The founder loses everything and starts over.

## When to reach for parallel dispatch

A pattern fits parallel dispatch when ALL of these are true:

- The work splits into N independent units
- The units share input context (so you do not have to brief each one separately)
- The units do not depend on each other's output
- N is small enough that the rate limit can absorb N parallel calls (typically 3 to 8; do not go higher without testing)

D2C examples that fit:
- Ad variations across N angles (Module 6)
- PDPs for N SKUs (Module 7 power scope)
- WhatsApp templates for N customer segments (Module 8 power scope)
- Competitor research split across N competitors (could be a power-scope variant of Day 1 Market Analyst)

D2C examples that do NOT fit:
- Content calendar planning (each day's piece depends on the prior day's)
- A single landing page (one artifact, not N)
- Voice of Customer synthesis (themes emerge by reading the whole, not by splitting)

## How the orchestrator dispatches

The orchestrator's job, in order:

1. **Collect scope and angles from the founder first.** A subagent cannot pause to ask, so scope (`SCOPE=power`) and any `ANGLES=` overrides are settled before any spawn.
2. **Decide the N units.** For Performance Marketer POWER, that is the 5 angles. The orchestrator could fan out fewer if some angles have weak data, but defaults to all 5.
3. **Spawn N subagents in one batch.** Each spawn is one Performance Marketer pinned to a single angle (`ANGLES=N`) with the output spec and its save path (`my-work/performance-marketer/<date>-angle-<N>-<slug>/`). They are sent together so they run concurrently.
4. **Spawn with `run_in_background: false`** so the orchestrator waits on the batch. (Background mode is for fire-and-forget; here the orchestrator is gated on results.)
5. **Wait for all N to return.** Each subagent returns a short summary and has already saved its own files, so the orchestrator does not need to re-read the full outputs.
6. **Aggregate into one index.** The orchestrator reads each subagent's summary (and folders if needed) and writes the single `<date>-index.md` per the spec in `performance-marketer.md` Step 6.
7. **Present to the founder.** The orchestrator surfaces the index and the flag count. The founder opens the index, not the 50 raw ads.

## Failure modes and how the orchestrator handles them

| Mode | What happens | Orchestrator's response |
|---|---|---|
| One subagent times out | Task returns with error after timeout | Mark that angle as failed in the index. Aggregate the rest. |
| One subagent hits rate limit | Task returns with rate-limit error | Same. Recommend founder re-run that angle later. |
| All 5 succeed but one is empty | Subagent returned but produced no files | Inspect the file system. Flag the empty angle. |
| A spawn straggles | One subagent starts late or runs long while the others finish | Expected. The batch is bounded by the slowest spawn; on Pro some may queue rather than all firing at once. Just wait for it. |
| Orchestrator context gets heavy after the batch | The 5 summaries plus the index push the main context | Keep the aggregation lean: read summaries, not every raw ad file. The subagents already saved the detail to disk. |

## Cost discipline

Five parallel subagents is roughly 5x the token cost of a single subagent for the same total work. There is no magic; parallelism saves wall-clock time, not money.

For Pro plan ($20/mo), running POWER once a week is fine. Running it 3 times a day in tests or experiments will hit limits.

For Max plan ($200/mo), POWER weekly + occasional re-runs is comfortably in budget.

The DEFAULT scope on Performance Marketer (2 angles sequential, one subagent) is roughly 1/5 the cost of POWER and stays under most rate limits even on Pro.

## What this is not

- **Not nested subagents.** The orchestrator spawns the 5, not a parent subagent. Subagents cannot spawn subagents.
- **Not multi-agent collaboration in the strong sense.** The 5 subagents do not message each other. They run independently and return to the orchestrator.
- **Not a swarm.** Not autonomous. The orchestrator makes all the decisions about what to dispatch and when.
- **Not always faster.** If the rate limit is the bottleneck (which it can be on Pro), the 5 spawns may queue and the wall-clock saving shrinks. Test with your own plan before relying on parallel for time-critical runs.

## Reading further

- The Performance Marketer subagent definition: `.claude/agents/performance-marketer.md`
- The 5 ad angles in detail: `ad-angle-templates.md` in this folder
- Content Lead's single-subagent pattern (the contrast): `.claude/agents/content-lead.md`
