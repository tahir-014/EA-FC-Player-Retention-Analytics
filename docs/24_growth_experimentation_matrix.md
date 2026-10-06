# Growth Experimentation Matrix

## EA FC Player Retention & Onboarding Analytics

> Portfolio experimentation framework based on synthetic player analytics. Experiment results in this project are simulated and do not represent actual EA experiments or proprietary EA data.

---

# 1. Experimentation Objective

The purpose of experimentation is to determine whether product changes create meaningful improvements in player outcomes.

The experimentation framework follows:

```text
PLAYER PROBLEM
      ↓
HYPOTHESIS
      ↓
PRODUCT INTERVENTION
      ↓
EXPERIMENT
      ↓
PRIMARY KPI
      ↓
GUARDRAILS
      ↓
ANALYSIS
      ↓
DECISION
```

The goal is not to run experiments simply because an experiment is possible.

The goal is to reduce product uncertainty.

---

# 2. Experiment Prioritization Principles

Experiments should be prioritized based on:

- Player impact
- Business/product impact
- Evidence strength
- Confidence
- Implementation effort
- Experiment feasibility
- Learning potential

A high-priority experiment should address an important player problem while producing meaningful learning.

---

# 3. Experimentation Matrix

| Experiment | Player Problem | Hypothesis | Product Intervention | Primary KPI | Key Guardrails |
|---|---|---|---|---|---|
| Week 1 Player Journey | Players may lack clear reasons to return | Structured goals and progression may improve D7 | Week 1 Journey | D7 Retention | Uninstall, negative feedback, crashes |
| First-Match Guidance | Some players fail to reach meaningful gameplay | Better guidance may increase first-match conversion | Improved first-match guidance | First-Match Conversion | Session failures |
| Progression Visibility | Players may not understand their progress | Clear progress indicators may increase repeat engagement | Progress tracker | D7 Retention | Player sentiment |
| Reward Relevance | Early rewards may not create enough motivation | More meaningful rewards may improve continuation | Reward redesign | D7 Retention | Reward abuse |
| Social Discovery | Some players may not discover social value | Better social discovery may increase engagement | Social discovery prompts | Social Adoption | Negative feedback |
| Player Communication | Players may not know what to do next | Relevant communication may increase return behavior | Week 1 campaign | D7 Retention | Opt-outs, complaints |

---

# 4. Experiment 1 — Week 1 Player Journey

## Problem

Moderate Engagement players represent 45.02% of the population and have 27.16% D7 retention.

High Engagement players have 44.27% D7 retention.

The observed difference is 17.10 percentage points.

---

## Hypothesis

> Providing new players with clear short-term objectives, visible progression, meaningful rewards, and a next-step recommendation will increase meaningful repeat gameplay and D7 retention.

---

## Control

Existing player experience.

---

## Treatment

Week 1 Player Journey:

- Daily objective
- Progress tracker
- Milestone
- Meaningful reward
- Next objective
- Journey progress

---

## Primary KPI

**D7 Retention**

---

## Secondary Metrics

- Second-session conversion
- Sessions
- Matches
- Progression
- Rewards
- Objective completion
- Journey completion
- Social adoption

---

## Guardrails

- Crash rate
- Session failure
- Uninstall rate
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# 5. Experiment 2 — First-Match Guidance

## Problem

First-match participation has a strong association with D7 retention.

Observed synthetic data:

- Did not play first match: 9.91% D7
- Played first match: 40.24% D7

Difference:

**30.33 percentage points**

---

## Hypothesis

> Helping new players understand and successfully reach their first meaningful match will increase early activation and improve retention.

---

## Potential Intervention

Improve the first-match journey through:

- Clear call-to-action
- Simple explanation
- Reduced confusion
- Contextual guidance
- Immediate feedback after the match

---

## Primary KPI

**First-Match Conversion Rate**

---

## Secondary Metrics

- First-session completion
- Second-session conversion
- D1 retention
- D7 retention

---

## Guardrails

- Tutorial abandonment
- Session failures
- Negative feedback
- Time-to-gameplay

---

# 6. Experiment 3 — Progression Visibility

## Problem

Moderate players show lower progression than High Engagement players.

| Metric | Moderate | High |
|---|---:|---:|
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |

---

## Hypothesis

> Making early progression more visible and understandable will increase player motivation to continue playing.

---

## Potential Intervention

Introduce:

- Progress indicator
- Milestone visibility
- Next milestone preview
- Clear progression feedback

---

## Primary KPI

**D7 Retention**

---

## Secondary Metrics

- Progression
- Matches
- Sessions
- Objective completion
- Reward claims

---

## Guardrails

- Player confusion
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# 7. Experiment 4 — Reward Relevance

## Problem

Moderate players claim fewer rewards than High Engagement players.

Moderate:

**3.04 rewards**

High:

**6.33 rewards**

---

## Hypothesis

> More meaningful and clearly communicated early rewards will increase motivation to continue the gameplay loop.

---

## Potential Intervention

Test different reward structures:

### Control

Existing reward experience.

### Treatment

More clearly connected rewards tied to meaningful gameplay objectives.

---

## Primary KPI

**D7 Retention**

---

## Secondary Metrics

- Reward claims
- Objective completion
- Matches
- Sessions
- Progression

---

## Guardrails

- Reward abuse
- Economy imbalance
- Negative feedback
- Core gameplay participation

---

# 8. Experiment 5 — Social Discovery

## Problem

Social adoption is lower among Moderate Engagement players.

| Segment | Social Adoption |
|---|---:|
| Moderate | 33.73% |
| High | 39.86% |

Difference:

**6.13 percentage points**

---

## Hypothesis

> Helping players discover relevant social experiences may increase engagement and return behavior.

---

## Potential Intervention

Introduce contextual social discovery:

- Friend suggestions
- Relevant social prompts
- Team/club discovery
- Multiplayer recommendations

---

## Primary KPI

**Social Feature Adoption**

---

## Secondary Metrics

- Sessions
- Matches
- D7 retention
- Social interactions

---

## Guardrails

- Negative feedback
- Social opt-outs
- Disruption to gameplay
- Notification fatigue

---

# 9. Experiment 6 — Player Communication

## Problem

Players may not always know what meaningful action they can take next.

---

## Hypothesis

> Relevant and timely player communication can increase return behavior when it points players toward meaningful in-game experiences.

---

## Potential Intervention

Test communication variants:

### Control

No additional campaign communication.

### Variant A

Goal-focused.

> Your next objective is ready.

### Variant B

Progress-focused.

> You're making progress in your Week 1 journey.

### Variant C

Reward-focused.

> Complete today's objective to unlock your reward.

### Variant D

Discovery-focused.

> Explore your next Week 1 challenge.

---

## Primary KPI

**D7 Retention**

---

## Secondary Metrics

- Return-to-game rate
- Objective completion
- Sessions
- Matches
- Progression

---

## Guardrails

- Opt-out rate
- Notification disablement
- Negative feedback
- Uninstall rate

---

# 10. Experiment Prioritization

A simple prioritization framework can be used:

```text
Priority Score =
Impact × Confidence / Effort
```

The score should help identify experiments worth testing first.

However, numerical prioritization should not replace PM judgment.

---

# 11. Prioritized Experiment Roadmap

| Priority | Experiment | Why |
|---|---|---|
| 1 | Week 1 Player Journey | Addresses the primary retention opportunity |
| 2 | First-Match Guidance | Strong activation signal |
| 3 | Progression Visibility | Addresses a major behavioral gap |
| 4 | Reward Relevance | Strengthens the progression loop |
| 5 | Player Communication | Supports return motivation |
| 6 | Social Discovery | Supporting opportunity |

---

# 12. Experiment Dependencies

Experiments should not always be launched independently.

A logical sequence could be:

```text
FIRST-MATCH EXPERIENCE
        ↓
WEEK 1 JOURNEY
        ↓
PROGRESSION
        ↓
REWARDS
        ↓
COMMUNICATION
        ↓
SOCIAL DISCOVERY
```

This sequence allows the team to improve the core player journey before adding additional communication or social interventions.

---

# 13. Statistical Thinking

An experiment should define the following before launch:

- Primary metric
- Secondary metrics
- Guardrails
- Baseline
- Minimum detectable effect
- Sample size
- Experiment duration
- Statistical significance threshold
- Decision criteria

The team should avoid changing the primary KPI after observing the results.

---

# 14. Existing Simulated A/B Test

The Week 1 Player Journey experiment was simulated using:

### Sample

3,921 players per group.

### Control

D7 retention:

**27.52%**

### Treatment

D7 retention:

**30.68%**

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### p-value

**0.0021**

### 95% Confidence Interval

**+1.15 to +5.17 percentage points**

---

# 15. Experiment Decision

The simulated experiment produced a statistically significant positive result.

Therefore:

**Recommendation: Gradual Rollout**

However, the result should be interpreted as a simulated portfolio exercise.

A real production decision would require:

- Real player data
- Guardrail validation
- Longer-term retention analysis
- Player feedback
- Technical validation
- Segment analysis
- Rollout monitoring

---

# 16. Segment-Level Experimentation

The simulated experiment produced the following results:

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

The strongest statistically supported effects were observed in:

- Low Engagement
- Moderate Engagement

The High Engagement segment showed no meaningful evidence of improvement.

The Very High estimate was positive but did not provide sufficient statistical evidence.

---

# 17. Important Experimentation Principle

Segment analysis should be interpreted carefully.

Testing many segments increases the chance of observing apparently significant differences by chance.

Therefore:

> Segment results should be treated as supporting evidence and ideally validated through pre-specified hypotheses or follow-up experiments.

---

# 18. What If the Experiment Fails?

A failed experiment is still useful if it reduces uncertainty.

### Scenario

D7 does not improve.

### Possible Interpretation

The proposed intervention may not address the true retention barrier.

### Next Steps

Investigate:

- Player feedback
- Objective completion
- Progression behavior
- Reward perception
- First-match experience
- Social behavior

Then refine the hypothesis.

---

# 19. What If Engagement Increases But D7 Does Not?

This is an important PM scenario.

Suppose:

- Sessions increase
- Matches increase
- Objectives increase

But:

- D7 remains unchanged

The team should not automatically declare success.

Possible explanations:

- Short-term activity without long-term value
- Players complete objectives but do not develop a habit
- Rewards create temporary behavior
- The experience increases activity without improving satisfaction

The next step would be to investigate longer-term retention and player sentiment.

---

# 20. What If D7 Improves But Player Sentiment Declines?

The team should investigate whether the experience is creating:

- Pressure
- Notification fatigue
- Reward frustration
- Excessive repetition
- Forced engagement

A retention improvement should not automatically justify scaling an experience that damages player trust or satisfaction.

---

# 21. Experimentation Learning Loop

```text
HYPOTHESIS
    ↓
DESIGN
    ↓
RANDOMIZE
    ↓
LAUNCH
    ↓
MEASURE
    ↓
ANALYZE
    ↓
LEARN
    ↓
ITERATE
```

The purpose of experimentation is to continuously reduce uncertainty.

---

# 22. PM Takeaway

Strong experimentation is not:

> "Let's A/B test a feature."

It is:

> **"We have a meaningful player problem, evidence supporting a hypothesis, a measurable intervention, clearly defined success criteria, and a decision framework before we launch."**
