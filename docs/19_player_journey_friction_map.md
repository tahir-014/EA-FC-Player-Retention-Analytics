# Player Journey & Friction Map

## EA FC Player Retention & Onboarding Analytics

> Portfolio concept based on synthetic player data. Journey assumptions are product hypotheses and should be validated through real player research.

---

# 1. Journey Objective

The analysis identified an opportunity to improve early repeat-play behavior among new players.

The primary target is the Moderate Engagement segment:

- 22,511 players
- 45.02% of the population
- 27.16% D7 retention
- 4–10 Week-1 sessions

The journey map focuses on the first seven days because this is the period in which players are expected to develop an early gameplay habit.

---

# 2. Current-State Player Journey

```text
DISCOVER
   ↓
START GAME
   ↓
ONBOARD
   ↓
PLAY FIRST MATCH
   ↓
EXPLORE GAMEPLAY
   ↓
PROGRESS
   ↓
DECIDE WHETHER TO RETURN
```

Each stage represents a potential opportunity to understand player motivation, friction, and behavior.

---

# 3. Detailed Journey Map

| Stage | Player Goal | Product Experience | Potential Friction | Behavioral Signal | PM Opportunity |
|---|---|---|---|---|---|
| Discover | Understand why to try the game | Acquisition / entry experience | Expectations may not match experience | Acquisition channel | Improve expectation setting |
| Start Game | Get into gameplay quickly | Initial setup and onboarding | Complexity or uncertainty | Tutorial completion | Reduce unnecessary friction |
| Onboard | Understand how to play | Tutorial / guidance | Information overload | Tutorial completion | Improve clarity and pacing |
| First Match | Experience meaningful gameplay | First playable match | Poor first experience | First-match conversion | Improve first-play experience |
| Explore | Understand available activities | Game modes / features | Too many or unclear choices | Sessions | Improve discovery |
| Progress | Feel improvement | Progression / rewards | Progress may feel unclear | Progression, rewards | Strengthen progression visibility |
| Return | Have a reason to come back | Goals / activities / rewards | No compelling next step | D1 / D7 retention | Create return motivation |

---

# 4. Key Friction Hypotheses

## Friction 1 — Unclear Next Step

### Hypothesis

After completing an activity, a new player may not clearly understand what they should do next.

### Evidence

Moderate and High Engagement players have similar average session duration:

- Moderate: 39.88 minutes
- High: 39.92 minutes

However, High Engagement players return much more frequently.

### Product Implication

The opportunity may not be simply increasing time spent in a session.

Instead, the product could provide a clear next action that creates a reason to return.

---

# 5. Friction 2 — Weak Progression Visibility

### Hypothesis

Players may not perceive enough meaningful progression during the first week.

### Evidence

| Metric | Moderate | High |
|---|---:|---:|
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |

High Engagement players progress further and claim more rewards.

### Product Implication

A clearer progression path could help players understand:

**Where am I?**

**What can I achieve next?**

**What do I get for completing it?**

---

# 6. Friction 3 — Limited Repeat-Play Motivation

### Hypothesis

Some players may complete a few sessions without developing a strong reason to return.

### Evidence

| Metric | Moderate | High |
|---|---:|---:|
| Sessions | 7.00 | 15.04 |
| Matches | 7.88 | 17.27 |
| D7 Retention | 27.16% | 44.27% |

The strongest behavioral difference is repeated gameplay rather than session duration.

### Product Implication

A product experience should create a loop:

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

# 7. Friction 4 — Social Discovery

### Hypothesis

Some players may not discover or use social features that could contribute to repeat engagement.

### Evidence

| Metric | Moderate | High |
|---|---:|---:|
| Social Adoption | 33.73% | 39.86% |

This is a supporting signal rather than the primary product problem.

### Product Implication

The experience could surface relevant social opportunities without making social participation mandatory.

---

# 8. Proposed Future-State Journey

The proposed Week 1 Player Journey introduces additional structure:

```text
START
  ↓
UNDERSTAND
  ↓
PLAY
  ↓
COMPLETE OBJECTIVE
  ↓
SEE PROGRESS
  ↓
CLAIM REWARD
  ↓
RECEIVE NEXT GOAL
  ↓
RETURN
```

---

# 9. Example Seven-Day Experience

| Day | Player Objective | Desired Behavior | Product Feedback |
|---|---|---|---|
| Day 1 | Complete first meaningful activity | First successful gameplay loop | Immediate progress + reward |
| Day 2 | Complete multiple matches | Repeat gameplay | Progress toward milestone |
| Day 3 | Explore another activity | Discovery | New objective |
| Day 4 | Complete a progression milestone | Continued engagement | Meaningful reward |
| Day 5 | Complete a gameplay challenge | Skill development | Progress feedback |
| Day 6 | Engage with another player or social activity | Social discovery | Social reinforcement |
| Day 7 | Complete Week 1 milestone | Habit formation | Summary + next goal |

These are hypothetical product concepts, not claims about existing EA FC mechanics.

---

# 10. Friction-to-Feature Mapping

| Potential Friction | Product Response |
|---|---|
| Unclear next step | Next-Step Recommendation |
| Weak short-term goals | Daily Player Objective |
| Progression not obvious | Progress Tracker |
| Rewards lack context | Meaningful Reward |
| No reason to return | Next-Day Objective |
| Limited social discovery | Relevant Social Prompt |

---

# 11. Experience Principle

The proposed experience should avoid turning the first week into a checklist that feels like work.

The objective is:

> **Guide players toward meaningful gameplay, not force them through activities.**

Therefore, objectives should be:

- Easy to understand
- Relevant to player progression
- Achievable
- Clearly connected to rewards
- Optional where appropriate
- Designed around gameplay value

---

# 12. Product Success

The journey is successful if it helps players develop stronger repeat-play behavior.

### Primary KPI

**D7 Retention**

### Supporting Metrics

- D1 Retention
- Second-session conversion
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
- Negative player feedback
- Reward abuse
- Core gameplay participation

---

# 13. Research Plan

The journey map contains hypotheses that should be validated before production implementation.

### Qualitative Research

Conduct interviews or usability sessions to understand:

- Where players feel confused
- Why players stop playing
- Which goals feel meaningful
- Whether rewards feel motivating
- Whether progression is understandable
- What creates a reason to return

### Quantitative Research

Use telemetry to investigate:

- Tutorial completion
- First-match conversion
- Second-session conversion
- Objective completion
- Progression
- Reward claims
- D1 / D7 retention
- Social adoption

### Community Research

Review player feedback from relevant communities and feedback channels to identify recurring onboarding and progression complaints.

---

# 14. Key PM Takeaway

The journey analysis suggests that the opportunity is not simply:

> "Make players play longer."

Instead:

> **Help players understand what to do, experience meaningful gameplay, see progress, receive meaningful rewards, and have a clear reason to return.**

This reframes the retention problem from a pure engagement metric into a player-experience problem.

---

# 15. Analytical Limitation

The journey map is based on synthetic behavioral data and product hypotheses.

It does not prove that any specific friction causes churn or low retention.

Real product decisions would require:

- Real telemetry
- Player research
- Usability testing
- Player feedback
- Controlled experimentation
