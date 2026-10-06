# Product Analytics Case Study

## EA FC Player Retention & Onboarding Analytics

### Portfolio Project

**Author:** Shaik Tahir Hussain  
**Focus:** Product Management | Product Analytics | Growth | AI

> **Disclaimer:** This is a portfolio project using synthetic player data. It does not use proprietary EA or EA SPORTS FC telemetry, player data, or internal business information.

---

# 1. Executive Summary

The objective of this analysis was to understand early player behavior and identify opportunities to improve Day-7 retention among new players.

The analysis focused on the first-week player journey, including:

- Tutorial completion
- First-match participation
- Session frequency
- Match participation
- Progression
- Rewards
- Social feature adoption
- Acquisition channel
- Day-7 retention
- Churn

The primary KPI for the analysis was **Day-7 retention (D7)**.

The analysis identified a significant opportunity among moderately engaged players.

Approximately **45.02% of players** belonged to the Moderate Engagement segment, defined as players with 4–10 sessions during Week 1.

This segment had only **27.16% D7 retention**, compared with **44.27%** among High Engagement players.

This represents a **17.11 percentage-point retention gap**.

The analysis therefore focused on the following product question:

> **How might we help moderately engaged new players develop stronger repeat-play behavior during their first week?**

---

# 2. Business Problem

New players may enter the game, complete some onboarding activities, and participate in early gameplay without developing a strong habit of returning.

If players fail to discover meaningful gameplay, progression, rewards, or social value during their first week, they may become less likely to return.

The product challenge is therefore to identify where early engagement weakens and determine which product opportunities could encourage stronger repeat behavior.

---

# 3. Analytical Objective

The analysis aimed to answer five questions:

1. Where do new players experience early engagement drop-off?
2. Which onboarding behaviors are associated with D7 retention?
3. Which player segments represent the largest retention opportunity?
4. What behaviors distinguish more-retained players from less-retained players?
5. What product intervention should be tested?

---

# 4. Primary KPI

## Day-7 Retention

D7 retention measures the percentage of players who return on Day 7.

It was selected as the primary KPI because the product problem focuses on whether new players develop an early habit of returning to the game.

### Overall Result

- Total players: **50,000**
- D7 retained players: **16,342**
- Overall D7 retention: **32.68%**

---

# 5. Dataset

The dataset contains **50,000 synthetic players**.

Each player has attributes and behavioral metrics including:

- Acquisition channel
- Age group
- Region
- Platform
- Tutorial completion
- First-match participation
- Week-1 sessions
- Week-1 matches
- Average session duration
- Progression level
- Rewards claimed
- Social feature usage
- D1 retention
- D7 retention
- D30 retention
- Churn

The dataset was generated specifically for this portfolio project.

---

# 6. Key Finding 1 — Tutorial Completion

Tutorial completion was associated with higher D7 retention.

| Tutorial Status | Players | D7 Retention |
|---|---:|---:|
| Not Completed | 12,229 | 13.09% |
| Completed | 37,771 | 39.03% |

The difference is:

**39.03% − 13.09% = 25.94 percentage points**

### Product Interpretation

Players who completed the tutorial showed substantially higher D7 retention.

This suggests that the onboarding experience is an important area for further product investigation.

However, this is an observational association and does not prove that tutorial completion itself caused the retention difference.

---

# 7. Key Finding 2 — First-Match Participation

First-match participation showed an even larger association with D7 retention.

| First Match | Players | D7 Retention |
|---|---:|---:|
| Not Played | 12,455 | 9.91% |
| Played | 37,545 | 40.24% |

The difference is:

**40.24% − 9.91% = 30.33 percentage points**

### Product Interpretation

Players who reached their first match had substantially higher D7 retention.

This suggests that getting new players into meaningful gameplay may be an important part of the early player journey.

Again, this is an association rather than causal evidence.

---

# 8. Key Finding 3 — Engagement and Retention

Week-1 engagement showed a strong relationship with D7 retention.

| Engagement Segment | Players | D7 Retention |
|---|---:|---:|
| Low | 10,296 | 15.75% |
| Moderate | 22,511 | 27.16% |
| High | 12,885 | 44.27% |
| Very High | 4,308 | 67.34% |

The difference between Moderate and High engagement is:

**44.27% − 27.16% = 17.11 percentage points**

The difference between Low and Very High engagement is:

**67.34% − 15.75% = 51.59 percentage points**

### Product Interpretation

Players who demonstrate stronger early engagement are also more likely to be retained on Day 7.

The most strategically interesting group is not necessarily the Very High segment.

Instead, the **Moderate segment represents a large population that may have room to improve**.

---

# 9. Key Finding 4 — Moderate Engagement Opportunity

The Moderate Engagement segment contains:

- **22,511 players**
- **45.02% of all players**
- **27.16% D7 retention**
- **7.00 average sessions**
- **7.88 average matches**
- **8.37 average progression**
- **3.04 average rewards**

This makes Moderate Engagement the largest clearly defined opportunity segment in the analysis.

### Product Opportunity

Instead of focusing only on acquiring more players, the product could investigate how to help existing moderately engaged players develop stronger repeat-play behavior.

---

# 10. Key Finding 5 — Acquisition Channels

| Acquisition Channel | Players | D7 Retention | Churn |
|---|---:|---:|---:|
| Organic | 12,431 | 33.79% | 69.45% |
| Influencer | 5,055 | 33.51% | 71.04% |
| Instagram | 7,518 | 32.59% | 72.36% |
| TikTok | 7,512 | 32.51% | 70.31% |
| YouTube | 7,483 | 32.37% | 71.07% |
| Paid Ads | 10,001 | 31.33% | 72.02% |

Organic had the highest D7 retention in the synthetic dataset, while Paid Ads had the lowest.

However, the dataset does not contain CAC, ROAS, LTV, or campaign-level cost information.

Therefore, the analysis does **not** make a budget-allocation recommendation based only on retention.

---

# 11. Primary Product Problem

The analysis leads to the following product problem:

> **A large share of new players reach an initial level of engagement but fail to develop strong repeat-play behavior during their first week.**

The most important evidence is the Moderate Engagement segment:

- 45.02% of players
- 27.16% D7 retention
- 7.00 average sessions
- 7.88 average matches
- 8.37 average progression
- 3.04 average rewards

High Engagement players showed:

- 44.27% D7 retention
- 15.04 average sessions
- 17.27 average matches
- 18.12 average progression
- 6.33 average rewards

---

# 12. Root-Cause Analysis

The Moderate and High Engagement segments were compared to understand behavioral differences.

| Metric | Moderate | High | Gap |
|---|---:|---:|---:|
| Tutorial Completion | 75.38% | 77.72% | 2.34 pp |
| First Match Rate | 75.02% | 76.90% | 1.88 pp |
| Average Sessions | 7.00 | 15.04 | 8.03 |
| Average Matches | 7.88 | 17.27 | 9.40 |
| Avg Session Duration | 39.88 min | 39.92 min | 0.05 min |
| Progression | 8.37 | 18.12 | 9.75 |
| Rewards | 3.04 | 6.33 | 3.29 |
| Social Adoption | 33.73% | 39.86% | 6.13 pp |
| D7 Retention | 27.16% | 44.27% | 17.11 pp |

### Main Insight

Tutorial completion and first-match participation differ only slightly between Moderate and High players.

Average session duration is also almost identical.

The strongest differences are:

- Number of sessions
- Number of matches
- Progression
- Rewards
- Social adoption

This suggests that the opportunity may be less about making individual sessions longer and more about helping players find reasons to **return, play meaningful matches, progress, and earn rewards**.

---

# 13. How Might We?

> **How might we help moderately engaged new players discover meaningful reasons to return and play more frequently during their first week, so that more players develop an early gameplay habit and improve Day-7 retention?**

---

# 14. Product Hypotheses

## Hypothesis 1 — Meaningful Gameplay Loop

If new players receive clearer short-term gameplay goals, they may have stronger reasons to return and participate in additional matches.

### Evidence

Moderate players:

- 7.88 average matches

High players:

- 17.27 average matches

Difference:

- 9.40 matches

---

## Hypothesis 2 — Progression and Reward Loop

If progression and rewards are made more visible and meaningful during the first week, players may have stronger motivation to continue.

### Evidence

Progression:

- Moderate: 8.37
- High: 18.12

Rewards:

- Moderate: 3.04
- High: 6.33

---

## Hypothesis 3 — Social Discovery

If new players discover relevant social features earlier, this may contribute to stronger repeat engagement.

### Evidence

Social adoption:

- Moderate: 33.73%
- High: 39.86%

Difference:

**6.13 percentage points**

---

# 15. Proposed Product Concept

## Week 1 Player Journey

A structured seven-day experience designed to help new players understand:

**What should I do next?**

**Why should I play another match?**

**How am I progressing?**

**What reward can I earn?**

### Core Loop

**Play → Progress → Reward → New Goal → Return**

---

# 16. MVP Components

### 1. Personalized Daily Objective

Give the player one clear, achievable gameplay objective.

### 2. Progress Tracker

Show progress toward the current objective and overall Week 1 journey.

### 3. Meaningful Reward

Provide a reward for completing objectives or milestones.

### 4. Next-Step Recommendation

After completing an objective, clearly communicate what the player can do next.

### 5. Return Reminder

Provide an appropriate reminder or in-game reason to return.

---

# 17. Success Metrics

## Primary KPI

**D7 Retention**

## Secondary Metrics

- Sessions per player
- Matches per player
- Progression
- Rewards claimed
- Objective completion rate
- Journey completion rate
- Second-session conversion
- Social feature adoption

## Guardrail Metrics

- Crash rate
- Session failures
- Uninstall rate
- Negative player feedback
- Reward abuse
- Core gameplay participation

---

# 18. Experimentation

The proposed feature should be evaluated through an A/B test.

### Control

Existing new-player experience.

### Treatment

Week 1 Player Journey.

### Randomization

Players are randomly assigned at the player level.

### Primary Metric

D7 retention.

### Hypothesis

The treatment will increase D7 retention compared with the control.

The experiment should be randomized before observing Week-1 engagement so that players are not assigned to treatment based on post-treatment behavior.

---

# 19. Experiment Result — Synthetic Simulation

A synthetic experiment was simulated using:

- 3,921 players per group
- 7,842 total players
- 50/50 Control/Treatment split

### Result

| Group | Players | D7 Retention |
|---|---:|---:|
| Control | 3,921 | 27.52% |
| Treatment | 3,921 | 30.68% |

### Lift

Absolute lift:

**+3.16 percentage points**

Relative lift:

**+11.48%**

Statistical test:

- z = 3.08
- p = 0.0021
- 95% CI for lift: **+1.15 pp to +5.17 pp**

The simulated result is statistically significant.

---

# 20. Segment Experiment Result

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

The strongest statistically supported simulated effects were observed in the Low and Moderate segments.

The Moderate segment is particularly important because it represents a large portion of the player base.

---

# 21. Product Decision

### Recommendation

**SHIP WITH GRADUAL ROLLOUT**, subject to production validation and guardrail monitoring.

The synthetic experiment suggests that the Week 1 Player Journey could improve D7 retention.

However, this result is a simulation and should not be presented as an actual EA experiment or real player result.

A real production experiment would be required before making a live product decision.

---

# 22. Rollout Plan

### Phase 1 — Controlled Test

Launch to a limited eligible player population.

Monitor:

- D7 retention
- Objective completion
- Sessions
- Matches
- Progression
- Rewards
- Guardrails

### Phase 2 — Gradual Expansion

If results remain positive and guardrails are healthy, gradually increase exposure.

### Phase 3 — Broader Rollout

Expand to a larger new-player population while continuing to monitor retention and player experience.

### Phase 4 — Iteration

Use experiment results and player feedback to improve objectives, rewards, progression, and recommendations.

---

# 23. Limitations

This analysis has several limitations.

### Synthetic Data

The dataset is artificially generated for portfolio purposes.

### No Proprietary EA Data

No EA or EA SPORTS FC internal telemetry, player data, or business information was used.

### Correlation vs Causation

Observed relationships between behavior and retention do not prove causal relationships.

### Limited Monetization Data

The dataset does not contain revenue, conversion, CAC, ROAS, or LTV.

### Limited Player Feedback

The analysis does not include real qualitative research, interviews, surveys, or community sentiment.

### Synthetic Experiment

The A/B test results are simulated and do not represent an actual production experiment.

---

# 24. Final Product Takeaway

The analysis shows that the largest opportunity is not simply acquiring more players.

A significant portion of new players already engage with the game but do not develop strong repeat-play behavior.

The **Moderate Engagement segment represents 45.02% of players and has 27.16% D7 retention**.

The product opportunity is therefore to create stronger reasons for these players to:

**Play → Progress → Earn → Discover → Return**

The proposed **Week 1 Player Journey** provides a testable product intervention focused on meaningful gameplay, progression, rewards, and return motivation.

The recommended approach is to validate the concept through controlled experimentation rather than assuming that observational relationships are causal.

---

# 25. PM Decision Framework

This project demonstrates the following product analytics workflow:

**Business Problem**

↓

**Product Question**

↓

**Define KPI**

↓

**Analyze Player Behavior**

↓

**Segment Players**

↓

**Identify Opportunity**

↓

**Generate Product Hypotheses**

↓

**Design Product Intervention**

↓

**Define Experiment**

↓

**Analyze Results**

↓

**Make Product Decision**

↓

**Measure and Iterate**