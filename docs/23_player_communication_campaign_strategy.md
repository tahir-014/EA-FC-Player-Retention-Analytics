# Player Communication & Campaign Strategy

## EA FC Player Retention & Onboarding Analytics

> Portfolio strategy based on synthetic analytics and product hypotheses. This does not represent actual EA player communication campaigns or proprietary EA data.

---

# 1. Objective

The purpose of player communication is to help players discover relevant experiences, understand their progress, and identify meaningful reasons to return.

Communication should support the player journey rather than interrupt it.

The primary growth objective is:

> Help new players develop meaningful repeat-play behavior during their first week.

Primary KPI:

**Day-7 Retention**

---

# 2. Target Audience

The primary analytical target is the:

## Moderate Engagement Player

Characteristics:

- 4–10 Week-1 sessions
- 22,511 players
- 45.02% of player population
- 27.16% D7 retention

Compared with High Engagement players:

| Metric | Moderate | High |
|---|---:|---:|
| Sessions | 7.00 | 15.04 |
| Matches | 7.88 | 17.27 |
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |
| Social Adoption | 33.73% | 39.86% |
| D7 Retention | 27.16% | 44.27% |

The communication strategy should therefore focus on helping players discover meaningful next actions rather than simply increasing message volume.

---

# 3. Communication Principles

## Principle 1 — Relevance

Only communicate information that is useful to the player's current journey.

---

## Principle 2 — Timing

Messages should appear when they can help the player take a useful next action.

---

## Principle 3 — Player Control

Players should have control over communication preferences.

---

## Principle 4 — Value First

Every communication should provide a clear player benefit.

---

## Principle 5 — Avoid Notification Fatigue

The goal is not to maximize messages sent.

The goal is to improve meaningful player outcomes.

---

# 4. Proposed Week 1 Communication Journey

```text
PLAYER STARTS
      ↓
WELCOME
      ↓
FIRST GOAL
      ↓
FIRST MATCH
      ↓
PROGRESS UPDATE
      ↓
REWARD
      ↓
NEXT GOAL
      ↓
RETURN
```

Communication should complement the in-game experience.

---

# 5. Day 1 — Welcome

## Objective

Help the player understand what to do first.

### Example Message

> Welcome! Start your first match and complete your first Week 1 objective.

### Intended Behavior

- Start gameplay
- Complete first objective
- Understand the next step

### Metrics

- First-match conversion
- Objective start rate
- Objective completion

---

# 6. Day 2 — Progress Reminder

## Objective

Give the player a clear reason to return.

### Example Message

> You're making progress. Complete today's objective to continue your Week 1 journey.

### Intended Behavior

- Return to game
- Complete objective
- Continue progression

### Metrics

- Return-to-game rate
- Second-session conversion
- Objective completion
- D2 retention

---

# 7. Day 3–5 — Progression & Discovery

Communication can introduce relevant experiences based on player behavior.

Examples:

- New objective
- Progress milestone
- Reward availability
- Relevant gameplay activity
- Social discovery

### Example

> Your next Week 1 objective is ready. Complete it to unlock your next reward.

The communication should remain concise and action-oriented.

---

# 8. Day 7 — Week 1 Milestone

## Objective

Create a meaningful reflection point.

### Example

> You've completed your first week. See your progress and discover what's next.

### Intended Behavior

- Review progress
- Continue playing
- Discover next goal

### Metrics

- D7 retention
- Journey completion
- Next-goal interaction
- Continued engagement

---

# 9. Communication Channel Strategy

Potential channels include:

| Channel | Best Use |
|---|---|
| In-Game | Immediate gameplay guidance |
| Push Notification | Timely return reminder |
| Email | Broader updates and summaries |
| In-Game Events | Contextual discovery |
| Social/Community | Community and event awareness |

Channel selection should depend on player preference, consent, and context.

---

# 10. Campaign Variants

Different communication approaches can be tested.

## Variant A — Goal Focused

> Your next objective is ready.

Focus:

**Action**

---

## Variant B — Progress Focused

> You're halfway through your Week 1 journey.

Focus:

**Progress**

---

## Variant C — Reward Focused

> Complete today's objective to unlock your reward.

Focus:

**Reward**

---

## Variant D — Discovery Focused

> Explore your next Week 1 challenge.

Focus:

**Discovery**

---

# 11. A/B Test Design

The communication strategy can be evaluated through controlled experimentation.

## Example Experiment

### Control

No additional Week 1 communication.

### Treatment A

Goal-focused communication.

### Treatment B

Progress-focused communication.

### Treatment C

Reward-focused communication.

### Treatment D

Discovery-focused communication.

If sample size permits, a multi-arm experiment could compare these variants.

---

# 12. Primary Metric

**D7 Retention**

The communication should ultimately demonstrate that it improves meaningful player retention.

---

# 13. Secondary Metrics

### Engagement

- Return-to-game rate
- Sessions
- Matches
- Session frequency

### Progression

- Objective completion
- Progression level
- Rewards claimed

### Communication

- Open rate
- Click-through rate
- Message interaction rate

---

# 14. Guardrail Metrics

Communication experiments should monitor:

- Notification opt-out
- Notification disablement
- Negative feedback
- Uninstall rate
- Session failures
- Technical errors
- Player complaints

A campaign that increases clicks but damages player sentiment should not automatically be considered successful.

---

# 15. Communication Funnel

```text
MESSAGE SENT
      ↓
MESSAGE DELIVERED
      ↓
MESSAGE OPENED
      ↓
PLAYER RETURNS
      ↓
PLAYER TAKES ACTION
      ↓
OBJECTIVE COMPLETED
      ↓
PROGRESSES
      ↓
RETURNS AGAIN
      ↓
D7 RETENTION
```

This prevents the team from optimizing only for communication metrics.

---

# 16. Example Campaign Dashboard

A PM could monitor:

| Metric | Purpose |
|---|---|
| Messages Sent | Campaign scale |
| Delivery Rate | Technical reach |
| Open Rate | Communication engagement |
| Return Rate | Behavioral impact |
| Objective Completion | Product action |
| Sessions | Engagement |
| Matches | Meaningful gameplay |
| D7 Retention | Primary outcome |
| Opt-Out Rate | Player sentiment guardrail |

---

# 17. Campaign Decision Framework

## Scenario 1 — High Engagement + High D7

The communication appears effective.

Next step:

**Consider gradual rollout.**

---

## Scenario 2 — High Opens + No D7 Improvement

Players are interested in the message but are not changing meaningful behavior.

Next step:

**Investigate message-to-product experience alignment.**

---

## Scenario 3 — Low Opens + Positive D7

The message may have limited direct engagement but could still influence behavior.

Next step:

**Investigate channel, timing, and attribution before scaling.**

---

## Scenario 4 — Higher D7 + Negative Guardrails

The campaign may improve retention while damaging player experience.

Next step:

**Do not scale automatically. Investigate trade-offs.**

---

# 18. Attribution Considerations

Communication impact should not automatically be attributed to a single message.

Players may:

- Return organically
- See multiple messages
- Interact with in-game experiences
- Receive external marketing
- Play with friends
- Encounter live events

Therefore, controlled experiments are preferred when measuring causal impact.

---

# 19. Personalization Opportunity

Future versions could personalize communication based on player behavior.

Potential signals:

- Engagement level
- Progression
- Previous objectives
- Gameplay activity
- Social adoption
- Recent sessions

Example:

### Low Engagement

Focus on:

**Simple next step**

### Moderate Engagement

Focus on:

**Progress + meaningful objective**

### High Engagement

Focus on:

**Advanced challenge**

Personalization should be introduced carefully and validated experimentally.

---

# 20. Communication and Product Alignment

Communication should never become a substitute for product quality.

The ideal relationship is:

```text
GOOD PRODUCT EXPERIENCE
        +
RELEVANT COMMUNICATION
        =
STRONGER PLAYER JOURNEY
```

Poor product experiences cannot be solved simply by sending more messages.

---

# 21. Proposed Campaign

## Campaign Name

**Week 1: Your Next Play**

### Objective

Increase meaningful repeat engagement among new players.

### Audience

New players during their first week.

### Core Message

> Here's what you can accomplish next.

### Experience

```text
NEXT GOAL
    ↓
PLAY
    ↓
PROGRESS
    ↓
REWARD
    ↓
NEXT GOAL
```

### Primary KPI

D7 retention.

### Supporting Metrics

- Second-session conversion
- Sessions
- Matches
- Objective completion
- Progression
- Rewards

### Guardrails

- Opt-outs
- Negative feedback
- Uninstalls
- Technical issues

---

# 22. PM Takeaway

Player marketing should not be treated as simply:

> "Send more messages."

A strong Growth PM approach is:

> **Identify the player need → deliver relevant value → communicate at the right moment → measure behavior → experiment → learn.**
