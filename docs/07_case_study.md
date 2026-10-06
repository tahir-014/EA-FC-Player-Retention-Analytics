# EA FC Player Retention & Onboarding Analytics

## Product Analytics & Growth Case Study

### Overview

This portfolio project explores how early player behavior can be analyzed to identify opportunities for improving new-player retention.

The project focuses on the first 30 days of the player journey, with particular attention to onboarding, early engagement, progression, rewards, social behavior, and Day-7 retention.

The project culminates in a proposed **Week 1 Player Journey** and a synthetic A/B experiment evaluating its potential impact on D7 retention.

> **Disclaimer:** All data, experiment results, and feature concepts are synthetic and created for portfolio demonstration. No proprietary EA or EA SPORTS FC data was used.

---

# 1. Business Problem

New players may complete the initial onboarding experience but fail to develop a consistent gameplay habit during their first week.

The product question was:

> How might we help new players discover meaningful reasons to return and play more frequently during their first week?

The primary success metric was:

**Day-7 Retention (D7)**

---

# 2. Dataset

The synthetic dataset contains:

- 50,000 players
- 19 player and behavioral attributes
- Acquisition channels
- Regions
- Platforms
- Age groups
- Tutorial completion
- First-match participation
- Week-1 sessions
- Week-1 matches
- Session duration
- Progression
- Rewards
- Social feature usage
- D1, D7 and D30 retention
- Churn

The dataset was generated using Python with intentionally realistic variation and behavioral relationships.

---

# 3. Key Analytical Findings

## Onboarding

Tutorial completion was associated with substantially higher D7 retention.

Players completing the tutorial had approximately 39% D7 retention compared with approximately 13% among players who did not.

This represents an approximately 26 percentage-point difference.

---

## First Match

Players who played their first match showed approximately 40% D7 retention compared with approximately 10% among players who did not.

This represents an approximately 30 percentage-point difference.

---

## Engagement

D7 retention increased substantially across engagement levels.

| Segment | D7 Retention |
|---|---:|
| Low | 15.75% |
| Moderate | 27.16% |
| High | 44.27% |
| Very High | 67.34% |

Moderate Engagement was the largest segment, representing approximately 45% of players.

---

# 4. Primary Product Opportunity

Moderate Engagement players were selected as the primary strategic opportunity.

### Moderate Engagement

- Players: 22,511
- Player share: 45.02%
- D7 retention: 27.16%
- Average sessions: 7.00
- Average matches: 7.88
- Average progression: 8.37
- Average rewards: 3.04

### High Engagement

- Players: 12,885
- Player share: 25.77%
- D7 retention: 44.27%
- Average sessions: 15.04
- Average matches: 17.27
- Average progression: 18.12
- Average rewards: 6.33

The resulting D7 retention gap was:

**17.10 percentage points**

---

# 5. Root Cause Analysis

The comparison between Moderate and High Engagement players suggested that the main differences were not driven by session duration.

Average session duration was almost identical:

- Moderate: approximately 39.88 minutes
- High: approximately 39.92 minutes

However, High Engagement players:

- Returned more frequently
- Played substantially more matches
- Progressed further
- Claimed more rewards
- Had somewhat higher social adoption

This suggested an opportunity around the **quality and frequency of the early gameplay loop**, rather than simply increasing session length.

---

# 6. Product Hypothesis

The core hypothesis was:

> A structured Week 1 player journey with clear gameplay objectives, visible progression, meaningful rewards, and clear next actions can encourage meaningful repeat gameplay and improve D7 retention.

---

# 7. Proposed Feature

## Week 1 Player Journey

The proposed MVP includes:

1. Personalized daily objectives
2. Progress tracking
3. Meaningful rewards
4. Next-step recommendations
5. Return reminders

The intended product loop is:

**Play → Progress → Reward → New Goal → Return**

---

# 8. PRD

The feature requirements included:

- Week 1 journey eligibility
- Daily objectives
- Progress tracking
- Objective completion
- Reward claiming
- Next objective recommendation
- Journey completion
- Product analytics events

Example analytics events:

- Journey Viewed
- Objective Viewed
- Objective Started
- Objective Completed
- Reward Claimed
- Next Objective Viewed
- Journey Completed

---

# 9. Experiment Design

A synthetic A/B experiment was designed.

### Control

Existing player experience.

### Treatment

Week 1 Player Journey.

### Randomization

Player-level 50/50 randomization.

### Primary Metric

D7 retention.

### Guardrails

- Crash rate
- Session failures
- Uninstall rate
- Negative player feedback
- Reward abuse
- Core gameplay participation

The experiment was designed before evaluating behavioral segments to avoid assigning treatment based on post-treatment behavior.

---

# 10. Sample Size

The experiment used:

- Baseline D7 retention: 27.16%
- Hypothetical MDE: +3 percentage points
- Significance level: 5%
- Statistical power: 80%
- 50/50 allocation
- 10% operational buffer

Recommended experiment population:

**7,842 players**

or approximately:

**3,921 players per group**

---

# 11. A/B Test Result

| Metric | Control | Treatment |
|---|---:|---:|
| Players | 3,921 | 3,921 |
| D7 Retention | 27.52% | 30.68% |
| D7 Retained | 1,079 | 1,203 |

### Impact

**Absolute lift:** +3.16 percentage points

**Relative lift:** +11.48%

**Z-statistic:** 3.0828

**P-value:** 0.0021

**95% Confidence Interval:** +1.15 pp to +5.17 pp

The result was statistically significant in the synthetic experiment.

---

# 12. Segment Experiment Results

| Segment | Control | Treatment | Lift | P-value |
|---|---:|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp | 0.0006 |
| Moderate | 26.96% | 30.02% | +3.06 pp | 0.0438 |
| High | 28.71% | 28.33% | -0.38 pp | 0.8506 |
| Very High | 28.57% | 31.49% | +2.92 pp | 0.4074 |

The strongest statistically supported effects were observed among Low and Moderate Engagement players.

---

# 13. Product Recommendation

## SHIP WITH GRADUAL ROLLOUT

The synthetic experiment provides statistically significant evidence of a positive D7 retention effect.

The initial rollout should prioritize Low-to-Moderate Engagement new players while continuing to monitor the broader player population.

High Engagement players did not demonstrate a measurable retention benefit in this experiment and may require a different product strategy.

---

# 14. Rollout Plan

### Phase 1 — Limited Rollout

Release to a small percentage of eligible players.

Monitor:

- D7 retention
- D30 retention
- Sessions
- Matches
- Progression
- Rewards
- Player feedback
- Crashes
- Session failures
- Reward abuse

### Phase 2 — Expanded Rollout

Increase exposure if the positive effect remains consistent and guardrails remain healthy.

### Phase 3 — Optimization

Use behavioral data and player feedback to refine:

- Objective difficulty
- Reward value
- Progression pacing
- Next-action recommendations
- Return messaging

---

# 15. Product Metrics Framework

### Primary KPI

**D7 Retention**

### Secondary Metrics

- D1 Retention
- D30 Retention
- Sessions per player
- Matches per player
- Progression
- Rewards claimed
- Objective completion
- Journey completion
- Social adoption

### Guardrails

- Crash rate
- Session failures
- Uninstall rate
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# 16. Tools Used

### Analytics

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Experimentation

- Statistical hypothesis testing
- Proportion z-test
- Confidence intervals
- Sample-size and power analysis

### Product Management

- Product problem framing
- KPI design
- Segmentation
- Root-cause analysis
- Product hypothesis development
- PRD
- A/B test design
- Experiment decision framework
- Rollout planning

---

# 17. Final Product Takeaway

The analysis suggests that the opportunity is not simply to make players play longer.

The opportunity is to create a stronger early gameplay loop:

**Play → Progress → Reward → New Goal → Return**

A successful Week 1 experience should help new players understand what to do next, experience meaningful progress, receive useful rewards, and develop a reason to return.

---

# 18. Limitations

This project is a portfolio simulation.

The dataset and experiment results are synthetic and do not represent:

- EA internal telemetry
- EA player behavior
- EA experiments
- EA product strategy
- EA proprietary data

The observational analysis identifies associations rather than proving causality.

The synthetic A/B experiment demonstrates experimental methodology and statistical decision-making but would require validation using real production data.

---

# 19. Portfolio Outcome

This project demonstrates an end-to-end Product Analytics and Product Management workflow:

**Business Problem**

↓

**KPI Framework**

↓

**Synthetic Data Generation**

↓

**Behavioral Analysis**

↓

**Player Segmentation**

↓

**Product Opportunity**

↓

**Product Hypothesis**

↓

**Feature Concept**

↓

**PRD**

↓

**A/B Experiment**

↓

**Statistical Validation**

↓

**Segment Analysis**

↓

**Rollout Recommendation**