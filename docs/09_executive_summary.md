# EA FC Player Retention & Onboarding Analytics
## Product Analytics Executive Summary

> Portfolio project using synthetic data. No proprietary EA or EA SPORTS FC data was used.

---

## 1. Business Problem

New players may enter the game and participate in early gameplay without developing a strong habit of returning during their first week.

The goal was to identify where early engagement weakens and determine a product opportunity that could improve Day-7 retention.

---

## 2. Primary KPI

### Day-7 Retention

Overall D7 retention:

**32.68%**

- Total players: 50,000
- D7 retained: 16,342

---

## 3. Key Data Insights

### Onboarding

Players who completed the tutorial had:

**39.03% D7 retention**

vs.

**13.09%** for players who did not complete it.

**Gap: +25.94 pp**

---

### First Gameplay

Players who played their first match had:

**40.24% D7 retention**

vs.

**9.91%** for players who did not.

**Gap: +30.33 pp**

---

### Engagement

| Segment | Player Share | D7 Retention |
|---|---:|---:|
| Low | 20.59% | 15.75% |
| Moderate | **45.02%** | **27.16%** |
| High | 25.77% | 44.27% |
| Very High | 8.62% | 67.34% |

---

## 4. Biggest Product Opportunity

### Moderate Engagement Players

The Moderate segment represents the largest opportunity:

- **22,511 players**
- **45.02% of player base**
- **27.16% D7 retention**

Compared with High Engagement players:

- Moderate: 7.00 sessions
- High: 15.04 sessions

- Moderate: 7.88 matches
- High: 17.27 matches

- Moderate: 8.37 progression
- High: 18.12 progression

- Moderate: 3.04 rewards
- High: 6.33 rewards

### Key Insight

The largest behavioral differences are not in session duration.

They are in:

**Repeat sessions → Matches → Progression → Rewards**

---

## 5. Product Problem

> **How might we help moderately engaged new players discover meaningful reasons to return and play more frequently during their first week?**

---

## 6. Proposed Product Solution

# Week 1 Player Journey

A structured seven-day experience designed around:

**Play → Progress → Reward → New Goal → Return**

### MVP

1. Personalized daily objective
2. Progress tracker
3. Meaningful reward
4. Next-step recommendation
5. Return reminder

---

## 7. Experiment Design

### Control

Existing new-player experience.

### Treatment

Week 1 Player Journey.

### Primary Metric

D7 retention.

### Experiment Size

**7,842 players**

- 3,921 Control
- 3,921 Treatment

---

## 8. Synthetic Experiment Result

| Group | D7 Retention |
|---|---:|
| Control | 27.52% |
| Treatment | 30.68% |

### Result

**+3.16 pp absolute lift**

**+11.48% relative lift**

Statistical result:

**p = 0.0021**

95% confidence interval:

**+1.15 pp to +5.17 pp**

---

## 9. Product Decision

### SHIP WITH GRADUAL ROLLOUT

The simulated experiment produced a statistically significant positive D7 result.

However, this is a synthetic simulation.

A real production experiment would be required before making a live product decision.

---

## 10. Rollout Strategy

### Phase 1
Controlled experiment with guardrail monitoring.

### Phase 2
Gradually increase exposure if D7 improves without negative guardrail movement.

### Phase 3
Expand rollout.

### Phase 4
Iterate using player feedback and experiment results.

---

## 11. Metrics

### Primary

- D7 retention

### Secondary

- Sessions per player
- Matches per player
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

## 12. PM Workflow

**Problem**

→ **Data**

→ **Insight**

→ **Segmentation**

→ **Opportunity**

→ **Hypothesis**

→ **Product Concept**

→ **Experiment**

→ **Decision**

→ **Iteration**

---

## 13. Skills Demonstrated

### Product Management

- Product problem definition
- Product metrics
- User segmentation
- Product hypothesis development
- PRD
- Feature prioritization
- A/B testing
- Experiment design
- Product decision-making

### Analytics

- Python
- Pandas
- SQL
- SQLite
- Statistical testing
- Retention analysis
- Cohort/segment analysis
- Data visualization

### Product Thinking

- Player journey analysis
- Growth and retention
- Onboarding
- Engagement
- Progression
- Rewards
- Social adoption
- Guardrail metrics