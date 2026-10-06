# Product Prioritization & Roadmap

## EA FC Player Retention & Onboarding Analytics

> Portfolio roadmap based on synthetic player analytics and product hypotheses. This does not represent an actual EA product roadmap or proprietary EA planning.

---

# 1. Roadmap Objective

The objective of the roadmap is to convert player insights into a focused sequence of product improvements.

The roadmap should answer:

- What problem should we solve first?
- Why is it important?
- What should we build?
- What should we test?
- What should we postpone?
- How will we know whether it worked?

The roadmap prioritizes improving the early player journey and developing stronger repeat-play behavior.

---

# 2. Product Strategy

The overall strategy is:

> Help new players move from initial gameplay to meaningful repeat engagement by making goals, progression, rewards, and next steps easier to understand.

The core product loop is:

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

# 3. Opportunity Areas

The project identified six major opportunity areas:

| Opportunity | Evidence | Strategic Importance |
|---|---|---|
| First-match conversion | Strong D7 association | High |
| Moderate → High engagement | 45.02% of players | Very High |
| Progression visibility | 9.75 progression gap | High |
| Reward relevance | 3.29 reward gap | Medium-High |
| Player communication | Return motivation opportunity | Medium |
| Social discovery | 6.13 pp adoption gap | Medium |

---

# 4. Prioritization Framework

The project uses:

```text
Priority Score =
Impact × Confidence / Effort
```

However, numerical scoring is only one input.

PM prioritization should also consider:

- Strategic alignment
- Player value
- Technical dependencies
- Experiment feasibility
- Risk
- Learning potential
- Time to validate

---

# 5. Prioritized Opportunities

## Priority 1 — Moderate Engagement → Stronger Repeat Engagement

### Why?

Moderate players represent:

**45.02% of players**

and have:

**27.16% D7 retention**

High Engagement players have:

**44.27% D7 retention**

The gap is:

**17.10 percentage points**

### Product Goal

Help moderate players discover meaningful reasons to return.

### Priority

**P0**

---

# 6. Priority 2 — Improve First-Match Activation

### Evidence

Players who played the first match:

**40.24% D7**

Players who did not:

**9.91% D7**

Observed difference:

**30.33 percentage points**

### Product Goal

Help new players reach meaningful gameplay faster.

### Priority

**P0/P1**

---

# 7. Priority 3 — Improve Progression Visibility

### Evidence

| Metric | Moderate | High |
|---|---:|---:|
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |

### Product Goal

Make early progress easier to understand and connect progress with meaningful gameplay.

### Priority

**P1**

---

# 8. Priority 4 — Improve Reward Relevance

### Evidence

Moderate players claim:

**3.04 rewards**

High players claim:

**6.33 rewards**

### Product Goal

Connect rewards more clearly to meaningful gameplay objectives.

### Priority

**P1**

---

# 9. Priority 5 — Player Communication

### Product Goal

Help players discover relevant next actions and return opportunities.

### Priority

**P1/P2**

Communication should support the product experience rather than compensate for a weak experience.

---

# 10. Priority 6 — Social Discovery

### Evidence

Moderate:

**33.73% social adoption**

High:

**39.86% social adoption**

Gap:

**6.13 percentage points**

### Product Goal

Improve discovery of relevant social experiences.

### Priority

**P2**

---

# 11. Now / Next / Later Roadmap

## NOW — Validate the Core Journey

### 1. First-Match Experience

Improve clarity around reaching the first meaningful match.

### 2. Week 1 Player Journey MVP

Introduce:

- Daily objective
- Progress tracker
- Meaningful reward
- Next-step recommendation
- Journey progress

### 3. A/B Test

Measure impact on:

- D7 retention
- Second-session conversion
- Sessions
- Matches
- Progression

### Goal

Validate whether the core hypothesis is correct.

---

# 12. NEXT — Strengthen the Loop

After validating the core journey:

### Progression Improvements

- Better milestone visibility
- Clearer progression feedback
- Next milestone preview

### Reward Improvements

- More meaningful early rewards
- Better reward explanation
- Gameplay-connected rewards

### Player Communication

- Goal-focused messaging
- Progress reminders
- Relevant return opportunities

### Goal

Strengthen:

```text
PLAY → PROGRESS → REWARD → RETURN
```

---

# 13. LATER — Deepen Engagement

After the foundational journey is validated:

### Social Discovery

Explore:

- Friend discovery
- Team/club discovery
- Social recommendations
- Multiplayer opportunities

### Advanced Personalization

Potentially personalize:

- Objectives
- Progression
- Rewards
- Communication
- Recommendations

### Advanced Engagement

Explore:

- Competitive challenges
- Mastery systems
- Longer-term progression
- Live events

These should be considered only after the core player journey is working well.

---

# 14. Roadmap Visualization

```text
NOW
│
├── First-Match Activation
│
├── Week 1 Player Journey MVP
│
└── A/B Test
        │
        ↓
NEXT
│
├── Progression Visibility
│
├── Reward Relevance
│
└── Player Communication
        │
        ↓
LATER
│
├── Social Discovery
│
├── Personalization
│
└── Advanced Engagement
```

---

# 15. Week 1 Player Journey MVP

The MVP should remain intentionally small.

## Feature 1 — Daily Objective

Give the player one clear short-term goal.

---

## Feature 2 — Progress Tracker

Show the player how far they have progressed.

---

## Feature 3 — Meaningful Reward

Provide a clear reward connected to the player's activity.

---

## Feature 4 — Next-Step Recommendation

Tell the player what they can do next.

---

## Feature 5 — Journey Progress

Show progress through the Week 1 experience.

---

# 16. MVP Non-Goals

The first release should NOT attempt to:

- Redesign core gameplay
- Build a new game mode
- Replace the entire onboarding system
- Build a complete social platform
- Introduce complex AI personalization
- Redesign the entire economy
- Maximize notification volume
- Optimize session duration alone

Keeping these out of the MVP reduces complexity and allows faster validation.

---

# 17. Product Trade-Offs

PM prioritization requires trade-offs.

## Trade-Off 1

### More Features vs Faster Learning

A smaller MVP allows the team to test the core hypothesis sooner.

**Decision: Favor faster learning.**

---

## Trade-Off 2

### More Notifications vs Player Experience

More messages may increase short-term engagement but could create fatigue.

**Decision: Optimize for relevant communication, not message volume.**

---

## Trade-Off 3

### More Rewards vs Economy Health

Increasing rewards may increase activity but could create reward inflation or abuse.

**Decision: Test reward relevance rather than simply increasing reward quantity.**

---

## Trade-Off 4

### Broad Personalization vs Simplicity

Complex personalization could increase development effort before the core problem is validated.

**Decision: Start with a simple rule-based experience.**

---

# 18. Dependencies

The roadmap depends on:

### Analytics

Reliable event tracking for:

- Objective viewed
- Objective started
- Objective completed
- Reward claimed
- Next objective viewed
- Journey completed

### Design

Player journey UX and progression visualization.

### Engineering

Implementation of:

- Objectives
- Progress tracking
- Rewards
- Event instrumentation

### Research

Player interviews and usability testing.

### Marketing

Communication strategy and campaign testing.

---

# 19. Success Metrics

## Primary

**D7 Retention**

---

## Secondary

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
- Session failures
- Uninstall rate
- Negative feedback
- Reward abuse
- Notification opt-outs
- Core gameplay participation

---

# 20. Roadmap Decision Gates

Each roadmap stage should have a decision gate.

## Gate 1 — MVP Validation

Question:

> Does the Week 1 Player Journey improve meaningful player outcomes?

If yes:

**Proceed to next stage.**

If no:

**Investigate and iterate.**

---

## Gate 2 — Progression & Reward

Question:

> Do progression and reward improvements strengthen the retention loop?

If yes:

**Expand.**

If no:

**Revisit player needs.**

---

## Gate 3 — Communication

Question:

> Does communication create incremental value beyond the product experience?

If yes:

**Scale carefully.**

If no:

**Modify targeting, timing, or messaging.**

---

## Gate 4 — Advanced Engagement

Question:

> Have we validated the foundational player journey sufficiently?

If yes:

**Explore personalization, social discovery, and deeper engagement.**

If no:

**Avoid adding complexity.**

---

# 21. Product Roadmap Principle

The roadmap should not be treated as a fixed list of features.

It should be treated as a sequence of:

```text
PROBLEMS
   ↓
HYPOTHESES
   ↓
EXPERIMENTS
   ↓
LEARNING
   ↓
INVESTMENT
```

If evidence changes, the roadmap should change.

---

# 22. Example PM Roadmap Decision

Suppose the Week 1 Player Journey produces:

- +3 pp D7
- Higher objective completion
- Higher progression
- No major guardrail deterioration

The PM could recommend:

> Gradual rollout followed by progression and reward optimization.

If D7 does not improve:

> Do not automatically build more features. Investigate why the proposed experience failed to change retention behavior.

---

# 23. Resource-Constrained Prioritization

If the team can only work on one initiative:

### Option A

Build multiple small features.

### Option B

Build and validate one focused experience.

The recommended approach is:

**Option B.**

Focus on the Week 1 Player Journey because it directly addresses the largest identified opportunity.

---

# 24. Long-Term Product Vision

The long-term vision is:

> Create a new-player experience where every meaningful action helps players understand their progress, discover their next goal, receive meaningful feedback, and develop sustainable reasons to return.

The experience evolves from:

```text
NEW PLAYER
    ↓
UNDERSTANDS THE GAME
    ↓
PLAYS
    ↓
PROGRESSES
    ↓
RECEIVES REWARD
    ↓
DISCOVERS NEXT GOAL
    ↓
RETURNS
    ↓
BECOMES ENGAGED
    ↓
DEVELOPS MASTERY
```

---

# 25. PM Takeaway

A strong product roadmap is not:

> "Here are all the features we want to build."

It is:

> **"Here is the most important player problem, the smallest valuable solution, how we will validate it, what evidence would justify further investment, and what we intentionally chose not to build yet."**

For this project, the roadmap prioritizes:

**First-Match Activation → Week 1 Journey → Progression → Rewards → Communication → Social → Personalization**

with experimentation and player research guiding each subsequent investment.

---

# 26. Limitations

This roadmap is a portfolio exercise based on synthetic analytics.

It does not account for:

- Actual EA engineering capacity
- Production dependencies
- Internal strategic priorities
- Real development costs
- Proprietary player research
- Live-service schedules
- Commercial constraints
- Actual EA roadmap decisions
