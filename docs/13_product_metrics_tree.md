# Experiment Rollout Plan

> Portfolio framework based on synthetic player analytics. No proprietary EA or EA SPORTS FC data was used.

---

# 1. Experiment Objective

The objective of the experiment is to determine whether the proposed **Week 1 Player Journey** can improve Day-7 retention among new players.

The intervention provides:

- Personalized or relevant daily objectives
- Visible progress tracking
- Meaningful rewards
- Clear next-step recommendations
- A structured first-week journey

The primary hypothesis is:

> Providing new players with clearer short-term goals, visible progression, meaningful rewards, and stronger reasons to return will increase early repeat engagement and Day-7 retention.

---

# 2. Experiment Design

## Control

Players receive the existing new-player experience.

## Treatment

Players receive the proposed Week 1 Player Journey.

## Randomization

Players are randomly assigned at the player level.

### Allocation

- Control: 50%
- Treatment: 50%

Randomization should occur before observing post-treatment engagement behavior.

This prevents assigning players to treatment based on behavior that the treatment itself could influence.

---

# 3. Primary Success Metric

## Day-7 Retention

The experiment evaluates whether the Treatment group produces a meaningful increase in D7 retention compared with Control.

---

# 4. Secondary Metrics

The following metrics help explain how the intervention affects player behavior:

- Second-session conversion
- Sessions per player
- Matches per player
- Progression level
- Rewards claimed
- Objective completion
- Journey completion
- Social feature adoption

These metrics are diagnostic and supporting metrics.

They should not replace D7 as the primary success metric.

---

# 5. Guardrail Metrics

The experiment must also monitor:

### Technical

- Crash rate
- Session failures
- Technical errors

### Player Experience

- Negative feedback
- Uninstall rate

### Economy / Gameplay

- Reward abuse
- Core gameplay participation

A feature should not be considered successful if retention increases while player experience or technical quality deteriorates materially.

---

# 6. Sample Size

The planning assumptions were:

- Baseline D7 retention: 27.16%
- Minimum Detectable Effect: +3 percentage points
- Target Treatment D7: 30.16%
- Significance level: 5%
- Statistical power: 80%
- Allocation: 50/50

Required sample:

- Base requirement: approximately 7,128 players
- Recommended operational sample: approximately 7,842 players

Recommended allocation:

| Group | Players |
|---|---:|
| Control | 3,921 |
| Treatment | 3,921 |
| **Total** | **7,842** |

The +3 percentage-point improvement is a hypothetical planning assumption, not a prediction of actual product impact.

---

# 7. Synthetic Experiment Result

The simulated experiment produced:

| Group | Players | D7 Retention |
|---|---:|---:|
| Control | 3,921 | 27.52% |
| Treatment | 3,921 | 30.68% |

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### Statistical Test

- z-score: 3.08
- p-value: 0.0021
- 95% confidence interval for lift: +1.15 pp to +5.17 pp

The simulated result is statistically significant.

---

# 8. Product Interpretation

The synthetic experiment suggests that the Week 1 Player Journey could improve D7 retention.

However, statistical significance alone does not mean the feature should immediately reach 100% of players.

A controlled rollout is preferable because the experiment is synthetic and because real production behavior can differ from simulated data.

---

# 9. Segment-Level Result

The simulated experiment was also analyzed by engagement segment.

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

Statistical results:

| Segment | p-value | Significant? |
|---|---:|---|
| Low | 0.0006 | Yes |
| Moderate | 0.0438 | Yes |
| High | 0.8506 | No |
| Very High | 0.4074 | No |

---

# 10. Segment Interpretation

The strongest statistically supported effects appear in:

### Low Engagement

Treatment lift:

**+7.96 pp**

### Moderate Engagement

Treatment lift:

**+3.06 pp**

This supports the broader product hypothesis that structured early goals and progression may be particularly useful for players who have not yet developed strong engagement habits.

The High Engagement segment showed no meaningful evidence of improvement in this simulation.

The Very High segment showed a positive estimated lift, but the result was not statistically significant.

---

# 11. Important Statistical Caveat

Segment-level analysis introduces multiple comparisons.

Therefore, segment results should be treated as directional evidence unless the segmentation strategy was predefined and the analysis plan accounts for multiple testing.

The overall experiment result should remain the primary decision criterion.

---

# 12. Rollout Recommendation

## Decision

### SHIP WITH GRADUAL ROLLOUT

The synthetic experiment supports moving forward with a controlled rollout, subject to validation using real production data.

---

# 13. Rollout Strategy

## Stage 1 — Limited Rollout

Release the feature to a small percentage of eligible new players.

Monitor:

- D7 retention
- Crash rate
- Session failures
- Negative feedback
- Reward abuse
- Core gameplay participation

Goal:

Confirm that the production implementation behaves safely and consistently.

---

## Stage 2 — Expanded Rollout

If guardrails remain healthy, increase exposure gradually.

Continue monitoring:

- D7 retention
- Second-session conversion
- Sessions
- Matches
- Progression
- Rewards
- Objective completion

Compare results against the original control experience.

---

## Stage 3 — Broader Rollout

If the positive effect remains consistent and no material guardrail deterioration appears, expand the feature to a larger portion of eligible new players.

Continue maintaining a holdout/control population when practical to measure longer-term impact.

---

## Stage 4 — Full Rollout

Move toward full deployment only after:

1. Production results replicate the expected direction.
2. D7 improvement remains meaningful.
3. Guardrails remain healthy.
4. No major player-experience problems are identified.
5. The team has confidence in the feature's operational stability.

---

# 14. Rollout Decision Framework

```text
                 EXPERIMENT RESULT
                         │
                         ▼
              Does D7 improve?
                    /       \
                  YES        NO
                   │          │
                   ▼          ▼
          Check guardrails   Investigate
                │             hypothesis
          ┌─────┴─────┐
        Healthy     Unhealthy
          │             │
          ▼             ▼
     Gradual        Stop / Redesign
     Rollout
          │
          ▼
   Validate production
       performance
          │
          ▼
   Expand if sustained
```

---

# 15. If Results Are Mixed

A PM should not treat every experiment as simply "win" or "lose."

### Scenario 1

D7 increases and guardrails are healthy.

**Decision:** Continue rollout.

### Scenario 2

D7 increases but reward abuse increases.

**Decision:** Investigate reward design before scaling.

### Scenario 3

Sessions increase but D7 does not.

**Decision:** The intervention may be increasing short-term activity without creating meaningful retention.

### Scenario 4

D7 increases but negative feedback increases.

**Decision:** Investigate player experience before rollout.

### Scenario 5

D7 does not change but progression improves.

**Decision:** The feature may be improving intermediate behavior without affecting the ultimate business outcome.

### Scenario 6

D7 decreases.

**Decision:** Stop or redesign the intervention and investigate the underlying cause.

---

# 16. Post-Launch Monitoring

After rollout, monitor:

### Daily / Near-Term

- Technical failures
- Crash rate
- Reward issues
- Player feedback

### Weekly

- D7 retention
- Sessions
- Matches
- Progression
- Rewards
- Objective completion

### Longer-Term

- D30 retention
- Longer-term engagement
- Social adoption
- Player sentiment
- Sustainable gameplay behavior

---

# 17. Product Learning Loop

The rollout should not be treated as the end of the product process.

The intended loop is:

```text
Launch
  ↓
Measure
  ↓
Analyze
  ↓
Identify Player Behavior
  ↓
Learn
  ↓
Improve Experience
  ↓
Run Next Experiment
  ↓
Measure Again
```

This creates a continuous product experimentation cycle.

---

# 18. PM Decision Principle

> **Do not ship a feature because the experiment is statistically significant. Ship when the evidence indicates that the feature creates meaningful player value, improves the target product outcome, and does not introduce unacceptable trade-offs.**

---

# 19. Final Recommendation

Based on the synthetic experiment:

**Recommendation: SHIP WITH GRADUAL ROLLOUT**

The simulated Treatment group improved D7 retention from **27.52% to 30.68%**, representing:

- **+3.16 percentage points absolute lift**
- **+11.48% relative lift**
- **p = 0.0021**
- **95% CI: +1.15 to +5.17 pp**

The strongest segment-level evidence appeared among Low and Moderate Engagement players.

However, these results are simulated portfolio results and must not be presented as real EA results.

A real product decision would require production experimentation, real telemetry, player feedback, statistical validation, and guardrail monitoring.

---

# 20. Interview Takeaway

If asked:

> "What would you do after getting a positive A/B test?"

My answer:

> "I wouldn't immediately roll it out to everyone. I'd first validate the primary D7 retention result, check guardrail metrics such as crashes, negative feedback and reward abuse, and verify that the effect is consistent in the intended player population. If those signals remain healthy, I'd move through a gradual rollout while maintaining measurement and a control or holdout where practical. I'd use the rollout to learn whether the experiment result replicates in real production behavior."
```
