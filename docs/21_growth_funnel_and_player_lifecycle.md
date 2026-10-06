# Growth Funnel & Player Lifecycle

## EA FC Player Retention & Onboarding Analytics

> Portfolio framework based on synthetic player data. Funnel stages and product opportunities are analytical hypotheses, not actual EA growth metrics.

---

# 1. Growth Objective

The goal of the product growth strategy is not simply to acquire more players.

The goal is to move players through a healthy lifecycle:

```text
DISCOVER
   ↓
START
   ↓
ONBOARD
   ↓
PLAY
   ↓
RETURN
   ↓
ENGAGE
   ↓
PROGRESS
   ↓
SOCIALIZE
   ↓
RETAIN
```

The project focuses primarily on the transition from:

**PLAY → RETURN → RETAIN**

---

# 2. Player Growth Funnel

## Stage 1 — Acquisition

### Question

How are players discovering the game?

### Current Dataset Signals

Acquisition channels include:

- Organic
- YouTube
- Instagram
- TikTok
- Influencer
- Paid Ads

### Product Metrics

- New players
- Acquisition channel
- Player share
- D7 retention by channel

### PM Opportunity

Understand which acquisition sources bring players who develop stronger early engagement.

---

# Stage 2 — Onboarding

### Question

Do new players successfully understand and enter the gameplay experience?

### Metrics

- Tutorial completion
- First-match conversion

### Observed Associations

Tutorial completion:

- Not completed: 13.09% D7
- Completed: 39.03% D7

First match:

- Not played: 9.91% D7
- Played: 40.24% D7

These are strong behavioral associations, not causal estimates.

### Product Opportunity

Reduce early friction and help players reach meaningful gameplay faster.

---

# Stage 3 — Early Engagement

### Question

Are players developing repeat-play behavior?

### Engagement Segments

| Segment | Week-1 Sessions | D7 Retention |
|---|---:|---:|
| Low | 0–3 | 15.75% |
| Moderate | 4–10 | 27.16% |
| High | 11–20 | 44.27% |
| Very High | 21–35 | 67.34% |

### Key Insight

The Moderate Engagement segment represents:

**45.02% of players**

but has:

**27.16% D7 retention**

This makes it the primary product opportunity.

---

# Stage 4 — Progression

### Question

Are players seeing meaningful progress?

### Metrics

- Progression level
- Rewards claimed
- Objectives completed
- Journey completion

### Behavioral Comparison

| Metric | Moderate | High |
|---|---:|---:|
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |

High Engagement players show substantially greater progression and reward activity.

### Product Opportunity

Make early progress easier to understand and connect progression to meaningful goals.

---

# Stage 5 — Social Engagement

### Question

Are players discovering social value?

### Metric

**Social Feature Adoption**

Moderate:

**33.73%**

High:

**39.86%**

### Interpretation

Social adoption is a supporting signal rather than the primary product problem.

### Product Opportunity

Improve discovery of relevant social experiences without forcing social participation.

---

# Stage 6 — Retention

### Primary KPI

**Day-7 Retention**

Overall D7 retention:

**32.68%**

### Why D7?

The product problem concerns whether new players develop an early repeat-play habit.

D7 provides a practical checkpoint for evaluating whether early engagement is translating into continued participation.

---

# 3. Lifecycle Metrics Framework

```text
ACQUISITION
    ↓
New Players
Channel Mix

    ↓

ONBOARDING
    ↓
Tutorial Completion
First Match Conversion

    ↓

ENGAGEMENT
    ↓
Sessions
Matches
Session Duration

    ↓

PROGRESSION
    ↓
Progression
Rewards
Objectives

    ↓

SOCIAL
    ↓
Social Adoption

    ↓

RETENTION
    ↓
D1
D7
D30

    ↓

LONGER-TERM VALUE
```

---

# 4. Growth Opportunity Matrix

| Lifecycle Stage | Current Signal | Opportunity |
|---|---|---|
| Acquisition | Channel differences in D7 | Understand acquisition quality |
| Onboarding | Strong association with retention | Improve early activation |
| Engagement | Moderate segment is largest | Increase meaningful repeat play |
| Progression | High players progress further | Strengthen early progression |
| Social | Moderate adoption gap | Improve social discovery |
| Retention | Overall D7 = 32.68% | Improve early player habit |

---

# 5. Primary Growth Opportunity

## Move Moderate Players Toward Stronger Repeat Engagement

The primary opportunity is not simply:

> Increase the number of sessions.

Instead:

> Help players discover enough meaningful gameplay, progression, rewards, and social value to create a sustainable reason to return.

This distinction is important because optimizing session count alone could increase short-term activity without improving the player experience.

---

# 6. Proposed Growth Loop

```text
ACQUIRE
   ↓
ACTIVATE
   ↓
PLAY
   ↓
PROGRESS
   ↓
REWARD
   ↓
DISCOVER NEXT GOAL
   ↓
RETURN
   ↓
RETAIN
   ↓
DEEPEN ENGAGEMENT
```

The Week 1 Player Journey is designed primarily to strengthen:

**PLAY → PROGRESS → REWARD → RETURN**

---

# 7. Growth Experiment

The proposed Week 1 Player Journey was evaluated through a simulated A/B test.

### Control

Existing experience.

### Treatment

Week 1 Player Journey.

### Allocation

50% Control / 50% Treatment.

### Sample

3,921 players per group.

### Primary KPI

D7 Retention.

---

# 8. Experiment Result

| Group | Players | D7 Retention |
|---|---:|---:|
| Control | 3,921 | 27.52% |
| Treatment | 3,921 | 30.68% |

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### Statistical Result

**p = 0.0021**

### 95% Confidence Interval

**+1.15 to +5.17 percentage points**

The simulated result is statistically significant.

> These are synthetic portfolio results and should not be interpreted as actual EA experiment results.

---

# 9. Growth Experiment Interpretation

The simulated experiment provides evidence that the proposed experience could improve D7 retention.

However, statistical significance alone is not sufficient for a product decision.

The team should also evaluate:

- Player feedback
- Technical stability
- Reward behavior
- Core gameplay participation
- Long-term retention
- Segment-level effects

---

# 10. Segment Growth Strategy

The simulated experiment showed:

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

The strongest statistically supported effects appeared among:

- Low Engagement
- Moderate Engagement

The High Engagement segment showed no meaningful evidence of improvement.

---

# 11. Growth Strategy by Player Stage

## Low Engagement

### Goal

Reduce early friction.

### Focus

- Onboarding clarity
- First meaningful gameplay
- Simple objectives
- Immediate feedback

---

## Moderate Engagement

### Goal

Create a stronger repeat-play habit.

### Focus

- Daily objectives
- Progression
- Rewards
- Next-step recommendations
- Return motivation

---

## High Engagement

### Goal

Protect and deepen existing engagement.

### Focus

- Advanced progression
- Mastery
- Challenges
- Social depth

---

## Very High Engagement

### Goal

Support long-term player value without disrupting the core experience.

### Focus

- Mastery
- Competitive depth
- Long-term progression
- Advanced social experiences

---

# 12. Player Marketing Opportunity

Growth is not only an in-game experience problem.

Player communication can also support the journey.

Potential communication moments include:

### Day 1

Welcome message and first objective.

### Day 2

Progress reminder and next recommended activity.

### Day 3–5

Relevant milestone or reward communication.

### Day 7

Week 1 progress summary and next goal.

The communication should be:

- Relevant
- Timely
- Useful
- Player-controlled
- Non-spammy

---

# 13. Communication Metrics

If player communications are introduced, evaluate:

### Engagement

- Message open rate
- Click-through rate
- Return-to-game rate

### Product

- Second-session conversion
- Sessions
- Matches
- Objective completion

### Retention

- D1
- D7
- D30

### Guardrails

- Opt-out rate
- Notification disablement
- Negative feedback
- Uninstall rate

Communication metrics should be evaluated alongside product outcomes rather than optimized independently.

---

# 14. Growth Decision Framework

```text
ACQUIRE
   ↓
ACTIVATE
   ↓
ENGAGE
   ↓
PROGRESS
   ↓
RETURN
   ↓
RETAIN
   ↓
LEARN
   ↓
OPTIMIZE
```

At each stage, the PM should ask:

1. What is the player trying to accomplish?
2. Where is the biggest friction?
3. What evidence supports the problem?
4. What product intervention could address it?
5. How will we measure success?
6. What are the risks?
7. What should we do if the experiment fails?

---

# 15. Key PM Takeaway

Growth Product Management is not simply:

> Acquire more users.

It is:

> **Build a product experience that moves the right players through a healthy lifecycle and creates sustainable reasons to return.**

For this project, the strongest opportunity is improving the transition from:

**Initial Gameplay → Meaningful Repeat Engagement → Retention**

while protecting the experience of already highly engaged players.

---

# 16. Limitations

This growth framework is based on synthetic portfolio data.

It does not include:

- Real acquisition costs
- CAC
- ROAS
- LTV
- Real campaign performance
- Real communication data
- Real player research
- Real EA telemetry

Therefore, the framework demonstrates product thinking rather than real EA growth performance.
