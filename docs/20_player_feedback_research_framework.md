# Player Feedback & Research Framework

## EA FC Player Retention & Onboarding Analytics

> Portfolio framework based on synthetic analytics and product hypotheses. It does not represent actual EA player research.

---

# 1. Research Objective

The analytics identified a retention opportunity among new players, particularly the Moderate Engagement segment.

The next step is to understand **why** some players fail to develop stronger repeat-play behavior.

The research objective is:

> Understand the motivations, frustrations, expectations, and barriers that influence new-player engagement and return behavior during the first week.

---

# 2. Core Research Questions

## Onboarding

- Do new players understand what they are expected to do?
- Is the onboarding experience easy to understand?
- Where do players feel confused?
- Does the player feel successful after the first interaction?

## Gameplay

- Does the first match provide a satisfying experience?
- What motivates players to play another match?
- What causes players to stop playing?
- Which gameplay activities feel most meaningful?

## Progression

- Do players understand how they are progressing?
- Are milestones clear?
- Does progression feel rewarding?
- What type of progress motivates players to continue?

## Rewards

- Do players understand why they received a reward?
- Do rewards feel meaningful?
- Do rewards create motivation to return?
- Are there rewards players consider unimportant?

## Return Motivation

- What makes a player decide to return the next day?
- What causes a player to stop returning?
- Does the player know what they can do next?
- Does the experience create anticipation for the next session?

## Social

- Do players discover social features?
- Which social experiences are valuable?
- What prevents players from using social features?

---

# 3. Research Methods

A combination of qualitative and quantitative research should be used.

| Method | Purpose |
|---|---|
| Player Interviews | Understand motivations and frustrations |
| Usability Testing | Identify experience friction |
| Surveys | Measure attitudes across larger samples |
| In-Game Feedback | Capture contextual player reactions |
| Community Research | Identify recurring themes |
| Telemetry Analysis | Quantify behavioral patterns |
| A/B Testing | Validate causal product impact |

---

# 4. Player Interview Framework

## Target Participants

Focus on newly acquired players across different engagement levels.

### Suggested groups

- Low Engagement
- Moderate Engagement
- High Engagement
- Players who churn early
- Players who return consistently

---

# 5. Interview Questions

## First Experience

1. Tell me about your first experience with the game.
2. What were you expecting when you started?
3. Was anything confusing?
4. What was the first thing you wanted to accomplish?

## First Match

5. How did you feel after your first match?
6. What made you want to play another match?
7. Was there anything that discouraged you from continuing?

## Progression

8. Did you understand how you were progressing?
9. What goals were you trying to achieve?
10. Did you feel like your actions were leading toward something meaningful?

## Rewards

11. Which rewards felt valuable?
12. Were any rewards confusing or unimportant?
13. Did receiving rewards make you want to return?

## Return Behavior

14. What made you come back after your first session?
15. What made you decide not to play on a particular day?
16. What would make you more likely to return tomorrow?

## Social

17. Did you discover social features?
18. Did social interaction affect your interest in returning?

---

# 6. Usability Testing

The proposed Week 1 Player Journey should be tested with new players before broad rollout.

## Example Tasks

### Task 1

"Start the game and tell us what you think you should do next."

### Observe

- Time to understand next step
- Confusion
- Navigation behavior
- Questions asked

---

### Task 2

"Complete your first meaningful gameplay objective."

### Observe

- Objective comprehension
- Completion difficulty
- Feedback clarity
- Reward understanding

---

### Task 3

"Show us how you would know what to do tomorrow."

### Observe

- Understanding of next goal
- Recognition of progression
- Return motivation

---

# 7. Feedback Taxonomy

Player feedback should be categorized consistently.

| Category | Example Signal |
|---|---|
| Onboarding | "I don't know what to do." |
| Gameplay | "The first experience wasn't fun." |
| Progression | "I don't understand how I'm progressing." |
| Rewards | "The reward doesn't feel useful." |
| Discovery | "I didn't know this feature existed." |
| Social | "I didn't know I could play with others." |
| Technical | Crashes / errors / loading |
| Difficulty | Experience feels too easy or difficult |
| Motivation | No reason to return |

---

# 8. Feedback Prioritization

Not every piece of feedback should immediately become a product requirement.

Evaluate feedback using:

**Frequency × Severity × Strategic Relevance**

### Frequency

How often is the issue reported?

### Severity

How strongly does the issue affect the player experience?

### Strategic Relevance

How closely does the issue relate to the product goal?

---

# 9. Example Insight Synthesis

Suppose research produced the following themes:

| Theme | Frequency | Severity | Product Interpretation |
|---|---|---|---|
| Players don't know what to do next | High | High | Strong opportunity |
| Rewards are unclear | Medium | Medium | Investigate |
| Players want more social discovery | Medium | Medium | Supporting opportunity |
| Advanced players want deeper challenges | Low | Low for target | Not MVP priority |

The PM should prioritize the issue that has the strongest combination of player impact and strategic relevance.

---

# 10. Connecting Research With Analytics

The strongest product insights come from combining behavioral data with player feedback.

Example:

```text
TELEMETRY

Moderate players:
7.00 sessions
27.16% D7 retention

        ↓

RESEARCH

Players report:
"I wasn't sure what to do next."

        ↓

HYPOTHESIS

Lack of clear next-step guidance may reduce
repeat-play motivation.

        ↓

PRODUCT RESPONSE

Next-Step Recommendation
+
Daily Objective
+
Progress Tracker

        ↓

EXPERIMENT

Measure impact on D7 retention.
```

This is a hypothesis-generation framework, not proof of causality.

---

# 11. Feedback-to-Product Loop

```text
PLAYER FEEDBACK
      ↓
THEME IDENTIFICATION
      ↓
QUANTITATIVE VALIDATION
      ↓
PROBLEM DEFINITION
      ↓
PRODUCT HYPOTHESIS
      ↓
FEATURE / EXPERIENCE
      ↓
EXPERIMENT
      ↓
MEASURE
      ↓
LEARN
      ↓
ITERATE
```

---

# 12. Research Success Criteria

Research is successful when it helps the team:

- Understand player motivations
- Identify meaningful friction
- Validate or challenge analytics findings
- Prioritize product problems
- Generate testable hypotheses
- Improve product decisions

The goal is not to collect the largest amount of feedback.

The goal is to make better product decisions.

---

# 13. Example PM Decision

### Evidence

Telemetry indicates that Moderate Engagement players:

- Represent 45.02% of the population
- Have 27.16% D7 retention
- Average 7.00 sessions
- Average 7.88 matches

### Research Hypothesis

Players may lack clear reasons to return after completing early activities.

### Product Response

Test a structured Week 1 Player Journey.

### Validation

Measure:

- D7 retention
- Second-session conversion
- Sessions
- Matches
- Progression
- Rewards
- Player feedback

### Decision

Use experiment results and qualitative feedback to determine whether to:

- Scale
- Iterate
- Modify
- Stop

---

# 14. Important Limitation

This project does not contain real player interviews, surveys, community data, or production feedback.

Therefore, the research framework describes **how a PM should validate the analytical hypotheses**, rather than claiming that these research findings already exist.

---

# 15. PM Takeaway

A strong product decision should not be:

> "The data says build this feature."

It should be:

> "The data identifies a problem, player research helps us understand why it happens, and experimentation tells us whether our solution actually improves the outcome."
