# Product Requirements Document

## Product

EA FC Player Retention & Onboarding Analytics

## Feature

Week 1 Player Journey

## Status

Portfolio Concept — Proposed MVP

## Data Disclaimer

This project uses synthetic data created for portfolio purposes.

It does not use proprietary EA or EA SPORTS FC player telemetry, internal data, or confidential information.



## 1. Problem Statement

Analysis of 50,000 synthetic new-player records identified a significant difference between moderately engaged and highly engaged players.

Moderate Engagement players:

- 22,511 players
- 45.02% of the player base
- 27.16% D7 retention
- 7.00 average Week-1 sessions
- 7.88 average Week-1 matches
- 8.37 average progression level
- 3.04 average rewards claimed

High Engagement players:

- 12,885 players
- 25.77% of the player base
- 44.27% D7 retention
- 15.04 average Week-1 sessions
- 17.27 average Week-1 matches
- 18.12 average progression level
- 6.33 average rewards claimed

The D7 retention difference between the two segments is approximately 17.11 percentage points.

The opportunity is to help moderately engaged new players develop stronger repeat-play behavior during their first week.



## 2. Product Goal

Create a structured Week 1 experience that helps moderately engaged new players:

1. Understand what to do next.
2. Participate in meaningful gameplay.
3. See visible progression.
4. Receive meaningful rewards.
5. Discover reasons to return.
6. Develop stronger early gameplay habits.

### Primary Goal

Improve Day-7 retention among the target player segment.

### Primary KPI

Day-7 Retention (D7)



## 3. Target User

### Primary User

New players classified as Moderate Engagement players.

### Segment Definition

Players with:

- 4–10 sessions during Week 1.

### Segment Size

22,511 players in the synthetic dataset.

### Player Need

A clearer reason to continue playing and make meaningful progress during the first week.



## 4. User Story

### Primary User Story

> As a new EA FC player, I want clear and achievable goals during my first week so that I know what to do next, can see my progress, earn meaningful rewards, and have a reason to return.



## 5. Functional Requirements

### FR-01 — Week 1 Journey

The product should provide eligible new players with a structured Week 1 journey.

### FR-02 — Daily Objective

The system should present a clear gameplay objective appropriate to the player's current progression.

### FR-03 — Progress Tracking

The player should be able to see progress toward the current objective.

### FR-04 — Objective Completion

The system should detect when the player completes the required activity.

### FR-05 — Reward

The player should receive a predefined reward after completing an objective.

### FR-06 — Next Objective

After completing an objective, the system should present the next recommended objective.

### FR-07 — Journey Progress

The player should be able to see overall Week 1 journey progress.

### FR-08 — Eligibility

The feature should primarily target eligible new players during their first-week experience.

### FR-09 — Analytics Events

The product should capture relevant events including:

- Journey Viewed
- Objective Viewed
- Objective Started
- Objective Completed
- Reward Claimed
- Next Objective Viewed
- Journey Completed



## 6. Acceptance Criteria

### Objective Display

- Given an eligible player enters the game,
- When the Week 1 Journey is available,
- Then the player should see their current objective.

### Progress Tracking

- Given the player starts an objective,
- When the player completes part of the required activity,
- Then the displayed progress should update correctly.

### Objective Completion

- Given the objective requirements are satisfied,
- When the relevant gameplay activity is completed,
- Then the objective should be marked as completed.

### Reward

- Given an objective has been completed,
- When completion is confirmed,
- Then the player should become eligible to claim the associated reward.

### Next Objective

- Given the player completes an objective,
- When the completion state is recorded,
- Then the next objective should become available.

### Analytics

- Given a player interacts with the journey,
- When a defined journey action occurs,
- Then the corresponding analytics event should be recorded.



## 7. Non-Goals

The MVP will not:

- Redesign the core gameplay experience.
- Introduce a new game mode.
- Replace existing onboarding.
- Introduce major monetization changes.
- Build a complete social system.
- Introduce complex AI personalization.
- Optimize solely for increasing session duration.



## 8. Success Metrics

### Primary Metric

**D7 Retention**

Measure the percentage of eligible players who return on Day 7.

### Secondary Metrics

- Sessions per player
- Matches per player
- Progression level
- Rewards claimed
- Second-session conversion
- Week 1 journey completion
- Objective completion rate
- Social feature adoption

### Guardrail Metrics

- Crash rate
- Session failure rate
- Uninstall rate
- Negative player feedback
- Reward abuse/farming
- Core gameplay participation

### Success Principle

The feature should improve D7 retention without creating negative effects on player experience or simply increasing low-value activity.



## 9. Risks

### Risk 1 — Players Ignore Objectives

Players may not find the objectives relevant or motivating.

**Mitigation:** Test objective clarity and relevance through experimentation and player research.

### Risk 2 — Reward Farming

Players may optimize specifically for rewards rather than meaningful gameplay.

**Mitigation:** Monitor gameplay quality and reward-abuse signals.

### Risk 3 — Notification Fatigue

Too many reminders could negatively affect player experience.

**Mitigation:** Limit communication frequency and test messaging carefully.

### Risk 4 — Short-Term Engagement Without Retention

The feature could increase sessions without improving long-term player value.

**Mitigation:** Use D7 retention as the primary KPI rather than sessions alone.

### Risk 5 — Causal Uncertainty

The existing analysis is observational and cannot establish that the proposed feature will improve retention.

**Mitigation:** Validate the hypothesis through a controlled A/B experiment.







