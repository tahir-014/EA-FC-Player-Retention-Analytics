# Product Analytics Storyline

## 1. Situation

The project analyzes the early journey of 50,000 synthetic new players to understand factors associated with Day-7 retention.

The goal is to identify a product opportunity rather than simply describe player behavior.

---

## 2. Business Question

How can the product improve early player retention by helping new players develop stronger repeat-play behavior?

---

## 3. What I Analyzed

I analyzed:

- Onboarding
- First-match participation
- Week-1 engagement
- Progression
- Rewards
- Social adoption
- Acquisition channels
- D7 retention
- Churn

---

## 4. What I Found

### Finding 1 — Onboarding matters

Tutorial completion was associated with:

**39.03% D7 retention**

versus:

**13.09%**

for players who did not complete the tutorial.

---

### Finding 2 — First gameplay matters

Players who played their first match showed:

**40.24% D7 retention**

versus:

**9.91%**

for players who did not.

---

### Finding 3 — Engagement is strongly associated with retention

D7 retention increased across engagement segments:

- Low: 15.75%
- Moderate: 27.16%
- High: 44.27%
- Very High: 67.34%

---

## 5. The Key Insight

The biggest opportunity was not the Very High engagement group.

It was the **Moderate Engagement segment** because it was:

- Large: 45.02% of players
- Retention-challenged: 27.16% D7
- Behaviorally between low and high engagement

The analysis showed that High Engagement players had substantially more:

- Sessions
- Matches
- Progression
- Rewards

while average session duration was almost identical.

---

## 6. Product Interpretation

This suggested that the opportunity may not be simply:

> "Make players play longer."

Instead:

> "Give players stronger reasons to return, play meaningful matches, progress, and earn rewards."

---

## 7. Product Hypothesis

If new players receive clear short-term goals, visible progression, meaningful rewards, and a clear next step, they may develop stronger repeat-play behavior during their first week.

---

## 8. Product Concept

### Week 1 Player Journey

Core loop:

**Play → Progress → Reward → New Goal → Return**

The MVP includes:

1. Personalized daily objective
2. Progress tracker
3. Meaningful reward
4. Next-step recommendation
5. Return reminder

---

## 9. Experiment

I designed a player-level A/B test.

### Control

Existing new-player experience.

### Treatment

Week 1 Player Journey.

### Primary KPI

D7 retention.

### Sample

7,842 players:

- 3,921 Control
- 3,921 Treatment

---

## 10. Simulated Result

Control:

**27.52% D7**

Treatment:

**30.68% D7**

Absolute lift:

**+3.16 pp**

Relative lift:

**+11.48%**

p-value:

**0.0021**

95% confidence interval:

**+1.15 pp to +5.17 pp**

---

## 11. Product Decision

### Ship with gradual rollout

The simulated experiment produced a statistically significant positive D7 result.

The rollout would still require:

- Production validation
- Guardrail monitoring
- Player feedback
- Continued experimentation

---

## 12. Important Analytical Caveat

The observational analysis does not prove causality.

For example:

Players with higher engagement also have higher retention.

This does not necessarily mean increasing sessions will automatically cause retention to increase.

That is why the product hypothesis must be validated through randomized experimentation.

---

## 13. Interview Answer

### "Tell me about a product analytics project you worked on."

I built a product analytics case study around new-player retention in a synthetic EA FC-style dataset.

I started by defining D7 retention as the primary KPI and analyzed onboarding, first-match participation, engagement, progression, rewards, social adoption, and acquisition channels.

The key insight was that the Moderate Engagement segment represented about 45% of the player base but had only 27.16% D7 retention, compared with 44.27% for High Engagement players.

I found that the biggest behavioral differences were in repeat sessions, matches, progression, and rewards rather than session duration.

Based on that, I proposed a Week 1 Player Journey with daily objectives, progress tracking, meaningful rewards, and clear next steps.

I then designed an A/B test using D7 retention as the primary metric. In my synthetic simulation, the treatment increased D7 retention from 27.52% to 30.68%.

The main lesson was to move from data → insight → product hypothesis → experiment → decision rather than stopping at descriptive analytics.

---

## 14. One-Line Portfolio Summary

> **Used Python and SQL to analyze 50,000 synthetic new-player records, identify a 45% moderate-engagement opportunity, design a Week 1 retention product concept, and validate the hypothesis through a simulated A/B experiment.**