
# Dashboard Storytelling

> Portfolio dashboard based on synthetic player analytics. No proprietary EA or EA SPORTS FC data was used.

---

# 1. Dashboard Objective

The dashboard is designed to help a Product Manager quickly understand:

1. How well new players are retained.
2. Where players struggle during the first-week journey.
3. Which player segments represent the biggest opportunity.
4. What behavioral differences are associated with retention.
5. Whether the proposed product intervention shows promising experimental evidence.
6. What product decision should be made next.

The dashboard follows the principle:

> **Insight first, visualization second.**

Charts should support a product decision rather than simply display data.

---

# 2. Dashboard Story

The dashboard follows this narrative:

```text
Business Problem
      ↓
Current Retention
      ↓
Player Behavior
      ↓
Opportunity Segment
      ↓
Root Cause Signals
      ↓
Product Hypothesis
      ↓
Experiment Result
      ↓
Product Decision
```

---

# 3. Executive KPI Layer

The first section should provide a quick executive view.

## KPI 1 — Total New Players

**50,000**

Purpose:

Shows the size of the synthetic player population analyzed.

---

## KPI 2 — D7 Retention

**32.68%**

Purpose:

Provides the primary product outcome.

---

## KPI 3 — Moderate Engagement Share

**45.02%**

Purpose:

Shows that the Moderate Engagement segment represents the largest opportunity population.

---

## KPI 4 — Moderate Engagement D7

**27.16%**

Purpose:

Shows that the largest segment has substantially lower retention than the High Engagement segment.

---

## KPI 5 — Moderate → High D7 Gap

**17.10 percentage points**

Purpose:

Highlights the size of the retention opportunity.

---

# 4. Insight 1 — Retention Is Closely Associated With Early Engagement

The engagement analysis shows:

| Segment | D7 Retention |
|---|---:|
| Low | 15.75% |
| Moderate | 27.16% |
| High | 44.27% |
| Very High | 67.34% |

The relationship shows a strong association between early engagement and D7 retention.

However:

> This is observational analysis and does not establish that increasing sessions will directly cause higher retention.

---

# 5. Insight 2 — Moderate Engagement Is the Main Opportunity

The Moderate Engagement segment contains:

- 22,511 players
- 45.02% of the population
- 27.16% D7 retention

High Engagement players have:

- 12,885 players
- 25.77% of the population
- 44.27% D7 retention

The difference in D7 retention is:

**17.10 percentage points**

This makes Moderate Engagement an attractive product opportunity because it combines:

**Large population + meaningful retention gap**

---

# 6. Insight 3 — The Problem Is Not Simply Session Duration

Moderate and High Engagement players have almost identical average session duration:

| Metric | Moderate | High |
|---|---:|---:|
| Average Session Duration | 39.88 min | 39.92 min |

Difference:

**0.05 minutes**

However:

| Metric | Moderate | High |
|---|---:|---:|
| Sessions | 7.00 | 15.04 |
| Matches | 7.88 | 17.27 |
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |

This suggests that the product opportunity may be more about encouraging **meaningful repeat gameplay and progression** than simply increasing the amount of time spent in each session.

---

# 7. Insight 4 — Onboarding Signals Are Important

Tutorial completion:

- Tutorial completed: 39.03% D7
- Tutorial not completed: 13.09% D7

Gap:

**25.94 percentage points**

First-match participation:

- First match played: 40.24% D7
- First match not played: 9.91% D7

Gap:

**30.33 percentage points**

These findings suggest that successful onboarding and reaching the first meaningful gameplay experience are important signals.

However, they are associations rather than causal estimates.

---

# 8. Insight 5 — Acquisition Channel Differences Are Relatively Small

Synthetic D7 retention by channel:

| Channel | D7 Retention |
|---|---:|
| Organic | 33.79% |
| Influencer | 33.51% |
| Instagram | 32.59% |
| TikTok | 32.51% |
| YouTube | 32.37% |
| Paid Ads | 31.33% |

The current dataset does not include:

- CAC
- ROAS
- LTV
- Acquisition cost
- Campaign spend

Therefore, the dashboard should not make claims about marketing ROI or budget allocation.

---

# 9. Insight 6 — Platform Is Not a Major Differentiator

Synthetic D7 retention:

| Platform | D7 Retention |
|---|---:|
| Mobile | 32.13% |
| PC | 32.88% |
| PlayStation | 32.76% |
| Xbox | 32.86% |

The range is relatively narrow.

Therefore, the current analysis does not provide strong evidence for a platform-specific retention strategy.

---

# 10. Product Opportunity

The dashboard should lead to the following product question:

> **How might we help moderately engaged new players discover meaningful reasons to return, progress, earn rewards, and develop a stronger early gameplay habit?**

---

# 11. Proposed Product Concept

## Week 1 Player Journey

The proposed experience includes:

1. Personalized or relevant daily objectives
2. Visible progress tracking
3. Meaningful rewards
4. Next-step recommendations
5. Return reminders

Core loop:

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
```

---

# 12. Experiment Results

The synthetic A/B experiment produced:

| Group | D7 Retention |
|---|---:|
| Control | 27.52% |
| Treatment | 30.68% |

Absolute lift:

**+3.16 percentage points**

Relative lift:

**+11.48%**

Statistical significance:

**p = 0.0021**

95% confidence interval:

**+1.15 to +5.17 percentage points**

---

# 13. Product Decision

The simulated experiment supports:

## SHIP WITH GRADUAL ROLLOUT

The result is statistically significant in the synthetic experiment.

However, the result should not be presented as an actual EA result.

Real-world validation would require:

- Production telemetry
- Real player behavior
- Controlled experimentation
- Guardrail monitoring
- Player feedback
- Statistical validation

---

# 14. Recommended Dashboard Layout

The dashboard should be organized from executive-level information to deeper analysis.

```text
┌──────────────────────────────────────────────┐
│          PLAYER RETENTION OVERVIEW           │
├──────────┬──────────┬──────────┬─────────────┤
│ Players  │ D7       │ Moderate │ D7 Gap      │
│ 50,000   │ 32.68%   │ 45.02%   │ 17.10 pp    │
└──────────┴──────────┴──────────┴─────────────┘

┌───────────────────────┬──────────────────────┐
│ D7 by Engagement      │ D7 by Acquisition    │
│                       │ Channel              │
└───────────────────────┴──────────────────────┘

┌───────────────────────┬──────────────────────┐
│ D7 by Platform        │ Onboarding Signals   │
│                       │ Tutorial / Match     │
└───────────────────────┴──────────────────────┘

┌──────────────────────────────────────────────┐
│        MODERATE → HIGH OPPORTUNITY           │
│ Sessions | Matches | Progression | Rewards   │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│             A/B EXPERIMENT                   │
│ Control → Treatment → Lift → Significance   │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│              PRODUCT DECISION                │
│          SHIP WITH GRADUAL ROLLOUT           │
└──────────────────────────────────────────────┘
```

---

# 15. Visualization Principles

Every visualization should answer a specific question.

### Good

**Question:** Which engagement segment has the strongest retention?

**Chart:** D7 retention by engagement segment.

### Good

**Question:** Did the proposed product intervention improve D7?

**Chart:** Control vs Treatment D7 retention.

### Good

**Question:** Which segment appears to benefit most?

**Chart:** Treatment lift by engagement segment.

### Avoid

Charts that exist only because the data is available.

For example:

- Random demographic charts
- Excessive pie charts
- Charts without a product question
- Decorative visualizations
- Too many KPIs

---

# 16. Dashboard Design Principle

The dashboard should allow a recruiter or PM to understand the project in approximately one minute.

The intended reading order is:

### 1. What is happening?

D7 retention is 32.68%.

### 2. Where is the opportunity?

Moderate Engagement represents 45.02% of players but has only 27.16% D7 retention.

### 3. What appears to differentiate stronger engagement?

High Engagement players show more sessions, matches, progression and rewards.

### 4. What should we build?

Week 1 Player Journey.

### 5. Did we test it?

Yes — through a simulated A/B experiment.

### 6. What happened?

Treatment improved simulated D7 retention by 3.16 pp.

### 7. What would we do?

Gradual rollout with guardrail monitoring.

---

# 17. Final Dashboard Narrative

The dashboard tells the following story:

> New-player D7 retention is 32.68% in the synthetic dataset. The largest opportunity is the Moderate Engagement segment, representing 45.02% of players while achieving only 27.16% D7 retention. Compared with High Engagement players, Moderate players have similar session duration but substantially fewer sessions, matches, progression levels, and rewards claimed. This suggests an opportunity to strengthen the early gameplay and progression loop rather than simply increasing session duration.
>
> Based on this insight, I proposed a Week 1 Player Journey that gives players clear short-term objectives, visible progression, meaningful rewards, and stronger reasons to return. In a simulated A/B experiment, D7 retention increased from 27.52% to 30.68%, a 3.16 percentage-point lift with p = 0.0021. I would therefore recommend a gradual rollout, subject to validation with real production data and guardrail monitoring.

---

# 18. Portfolio Principle

The dashboard is not the final product.

The dashboard is a decision-making tool.

The complete PM workflow is:

**Data → Insight → Product Problem → Hypothesis → Experiment → Decision**

The purpose of analytics is not simply to report what happened.

It is to help the product team decide:
