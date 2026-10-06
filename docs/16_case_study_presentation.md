# EA FC Player Retention & Onboarding Analytics
## Product Management Case Study Presentation

> Portfolio project using synthetic data. No proprietary EA or EA SPORTS FC data was used.

---

# Slide 1 — Title

## EA FC Player Retention & Onboarding Analytics

### Turning Player Behavior Into a Product Growth Opportunity

**Shaik Tahir Hussain**

B.Tech — Computer Science & Engineering (Artificial Intelligence)

Product Management | AI | Product Analytics | Growth

---

# Slide 2 — The Business Problem

## New players may not develop a strong repeat-play habit during their first week.

The key product question:

> How can we help new players discover meaningful reasons to return and continue playing?

The analysis focuses on:

- Onboarding
- First-match experience
- Early engagement
- Progression
- Rewards
- Social behavior
- Day-7 retention

---

# Slide 3 — The Product Goal

## Improve Early Player Retention

### Primary KPI

**Day-7 Retention**

Synthetic baseline:

**32.68%**

The goal is not simply to maximize playtime.

The goal is to help players:

**Play → Progress → Earn Value → Discover the Next Goal → Return**

---

# Slide 4 — What I Analyzed

## Dataset

**50,000 synthetic players**

Analyzed dimensions:

- Acquisition channel
- Age group
- Region
- Platform
- Tutorial completion
- First-match participation
- Week-1 sessions
- Matches
- Session duration
- Progression
- Rewards
- Social adoption
- D1 / D7 / D30 retention
- Churn

Tools:

- Python
- Pandas
- SQL
- SQLite
- Matplotlib
- Seaborn
- Statistical testing

---

# Slide 5 — First Major Finding

## Early engagement is strongly associated with D7 retention.

| Engagement | D7 Retention |
|---|---:|
| Low | 15.75% |
| Moderate | 27.16% |
| High | 44.27% |
| Very High | 67.34% |

The relationship suggests that stronger early engagement is associated with stronger retention.

### Caveat

This is observational analysis.

It does not prove that increasing sessions directly causes higher retention.

---

# Slide 6 — The Biggest Opportunity

## Moderate Engagement

**22,511 players**

**45.02% of the population**

**27.16% D7 retention**

High Engagement:

**44.27% D7 retention**

### Gap

**17.10 percentage points**

This segment combines:

**Large population + meaningful retention opportunity**

---

# Slide 7 — What Differentiates Moderate vs High Players?

| Metric | Moderate | High |
|---|---:|---:|
| Sessions | 7.00 | 15.04 |
| Matches | 7.88 | 17.27 |
| Session Duration | 39.88 min | 39.92 min |
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |
| Social Adoption | 33.73% | 39.86% |

## Key Insight

Session duration is almost identical.

But High Engagement players:

- Return more often
- Play more matches
- Progress further
- Claim more rewards

This suggests an opportunity around **meaningful repeat gameplay and progression**, rather than simply increasing session length.

---

# Slide 8 — Supporting Onboarding Evidence

## Tutorial Completion

D7 retention:

- Completed: **39.03%**
- Not completed: **13.09%**

Gap:

**25.94 pp**

## First Match

D7 retention:

- Played: **40.24%**
- Not played: **9.91%**

Gap:

**30.33 pp**

### Product Interpretation

Getting players through onboarding and into meaningful gameplay appears strongly associated with retention.

Again, these are associations rather than causal estimates.

---

# Slide 9 — Product Opportunity

## How Might We?

> **How might we help moderately engaged new players discover meaningful reasons to return and play more frequently during their first week, so that more players develop an early gameplay habit and improve Day-7 retention?**

Target:

**New players with 4–10 Week-1 sessions**

---

# Slide 10 — Product Hypotheses

### Hypothesis 1 — Meaningful Gameplay

Clear short-term gameplay goals may encourage players to return.

### Hypothesis 2 — Progression & Rewards

Visible milestones and meaningful rewards may encourage continued progression.

### Hypothesis 3 — Social Discovery

Relevant social opportunities may provide additional reasons to return.

---

# Slide 11 — Proposed Product

# Week 1 Player Journey

A structured first-week experience designed to help new players understand:

**What should I do next?**

### MVP

1. Daily Player Objective
2. Progress Tracker
3. Meaningful Reward
4. Next-Step Recommendation
5. Return Reminder

---

# Slide 12 — Product Loop

```text
                 PLAY
                   ↓
              PROGRESS
                   ↓
                REWARD
                   ↓
              NEW GOAL
                   ↓
                RETURN
                   ↓
              MORE PLAY
```

The objective is to create a meaningful gameplay loop rather than simply increase activity.

---

# Slide 13 — Experiment Design

## A/B Test

### Control

Existing player experience.

### Treatment

Week 1 Player Journey.

### Allocation

**50% Control / 50% Treatment**

### Primary KPI

**D7 Retention**

### Secondary Metrics

- Sessions
- Matches
- Progression
- Rewards
- Objective completion
- Journey completion
- Second-session conversion
- Social adoption

### Guardrails

- Crash rate
- Session failures
- Uninstall rate
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# Slide 14 — Sample Size

Planning assumptions:

- Baseline D7: **27.16%**
- MDE: **+3 percentage points**
- Alpha: **5%**
- Power: **80%**
- Allocation: **50/50**

Required base sample:

**7,128 players**

Recommended with 10% operational buffer:

**7,842 players**

### Allocation

**3,921 Control**

**3,921 Treatment**

The +3 pp MDE is a planning assumption, not a prediction.

---

# Slide 15 — Synthetic Experiment Result

| Group | D7 Retention |
|---|---:|
| Control | 27.52% |
| Treatment | 30.68% |

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### Statistical Result

**p = 0.0021**

### 95% Confidence Interval

**+1.15 to +5.17 pp**

The simulated result is statistically significant.

---

# Slide 16 — Segment-Level Result

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

### Interpretation

The strongest statistically supported effects appeared among:

- Low Engagement
- Moderate Engagement

High Engagement showed no meaningful evidence of improvement.

Very High Engagement showed a positive estimate, but insufficient statistical evidence.

---

# Slide 17 — Product Decision

# SHIP WITH GRADUAL ROLLOUT

Why?

The synthetic experiment produced:

- Positive D7 lift
- Statistically significant result
- Stronger effects in lower-engagement segments

But rollout should remain controlled.

---

# Slide 18 — Rollout Plan

### Stage 1

Limited production rollout.

Monitor:

- D7
- Crashes
- Session failures
- Feedback
- Reward abuse

### Stage 2

Expand exposure if guardrails remain healthy.

### Stage 3

Validate whether the D7 effect remains consistent.

### Stage 4

Move toward broader rollout if evidence remains positive.

---

# Slide 19 — Product Decision Framework

```text
Positive D7
     +
Healthy Guardrails
     ↓
Gradual Rollout

Positive D7
     +
Unhealthy Guardrails
     ↓
Investigate / Redesign

No D7 Improvement
     ↓
Revisit Hypothesis

Negative D7
     ↓
Stop / Redesign
```

---

# Slide 20 — What I Learned

This project demonstrates my ability to:

### Product Thinking

- Define a product problem
- Identify target users
- Create hypotheses
- Design product concepts
- Write requirements

### Analytics

- Define KPIs
- Analyze player behavior
- Segment users
- Use SQL
- Build metrics frameworks

### Experimentation

- Design A/B tests
- Estimate sample size
- Analyze statistical significance
- Interpret confidence intervals
- Make rollout decisions

### PM Decision-Making

- Prioritize opportunities
- Balance impact and effort
- Define guardrails
- Translate data into product action

---

# Slide 21 — Limitations

This is a portfolio simulation.

The data is:

**Synthetic**

It does not represent:

- Actual EA telemetry
- Actual EA player behavior
- Actual EA business metrics
- Actual EA experiment results

The analysis also does not include:

- CAC
- ROAS
- LTV
- Real player research
- Production telemetry
- Real player feedback
- Actual monetization behavior

Therefore, conclusions should be treated as portfolio hypotheses rather than real-world EA findings.

---

# Slide 22 — Final Product Story

## Problem

New players may fail to develop a repeat-play habit.

↓

## Data

50,000 synthetic player records analyzed.

↓

## Insight

Moderate Engagement represents 45.02% of players but has only 27.16% D7 retention.

↓

## Opportunity

Help players discover meaningful gameplay, progression and rewards.

↓

## Product

Week 1 Player Journey.

↓

## Experiment

A/B test with D7 as the primary KPI.

↓

## Result

+3.16 pp simulated D7 lift.

↓

## Decision

Gradual rollout with guardrail monitoring.

---

# Slide 23 — Final Takeaway

> **I used player behavior data to identify a high-value retention opportunity, translated the insight into a concrete product concept, designed an experiment around D7 retention, and used the simulated result to make a rollout decision.**

### Product Analytics Workflow

**Problem → Data → Insight → Product → Experiment → Decision**

---

# Slide 24 — Thank You

## Shaik Tahir Hussain

**Product Management | AI | Product Analytics | Growth**

B.Tech — Computer Science & Engineering (Artificial Intelligence)

### Project

**EA FC Player Retention & Onboarding Analytics**

> Synthetic portfolio project — no proprietary EA data used.
```
