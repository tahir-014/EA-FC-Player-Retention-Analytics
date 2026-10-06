# EA FC Player Retention & Onboarding Analytics — Data Logic

## 1. Dataset Objective

The synthetic dataset should represent realistic new-player behavior during the early lifecycle of a football gaming product.

The generated data should contain meaningful behavioral relationships so that the analysis can identify patterns in onboarding, engagement, progression, retention, and churn.

The dataset should not consist of completely independent random values.


## 2. Player Identity Rules

1. Every player must have a unique `player_id`.
2. Player IDs will follow the format `P000001`, `P000002`, etc.
3. Each row represents exactly one player.
4. No player ID may appear more than once.


## 3. Acquisition Rules

1. Every player must have an acquisition date.
2. Acquisition dates will fall within a defined analysis period.
3. Every player must have exactly one primary acquisition channel.
4. Acquisition channels will include:
   - Organic
   - YouTube
   - Instagram
   - TikTok
   - Influencer
   - Paid Ads
5. Acquisition channel distribution will not be perfectly equal.
6. Different acquisition channels may have different retention and engagement patterns.


## 4. Player Attribute Rules

### Age Group

Players will be assigned to one of:

- Under 18
- 18-24
- 25-34
- 35+

The distribution will be weighted rather than perfectly equal.

### Region

Players will be assigned to:

- India
- North America
- Europe
- Asia Pacific
- Latin America
- Middle East & Africa

### Platform

Players will be assigned to:

- PC
- PlayStation
- Xbox
- Mobile

Platform distributions will be intentionally varied.


## 5. Onboarding Logic

### Tutorial Completion

Each player will have a probability of completing the tutorial.

Tutorial completion may vary based on player attributes and acquisition characteristics.

Players who complete the tutorial should generally have a higher probability of:

- Playing their first match
- Returning for additional sessions
- Progressing further
- Retaining on Day 7

However, tutorial completion must not guarantee retention.

### First Match

Players who do not complete the tutorial can still have a small probability of reaching the first match, representing players who skip or bypass parts of onboarding.

Players who complete the tutorial should have a significantly higher probability of playing their first match.

### First Match Result

If `first_match_played = False`, then:

`first_match_result = Not Played`

If `first_match_played = True`, then:

`first_match_result` must be one of:

- Win
- Draw
- Loss


## 6. Engagement Logic

Engagement variables should be related to player behavior.

### Sessions

`sessions_week1` must be an integer greater than or equal to 0.

Players who are more engaged should generally have:

- More sessions
- More matches
- Longer session duration
- Higher progression
- Higher probability of retention

### Matches

`matches_week1` must be greater than or equal to 0.

Players who do not play their first match should have:

`matches_week1 = 0`

Players who play their first match should generally have at least one match during the first week.

### Session Duration

`avg_session_minutes` must be greater than 0 for players with gameplay sessions.

Players with zero gameplay sessions should have:

`avg_session_minutes = 0`


## 7. Progression Logic

Progression should be related to engagement.

Players with more matches and sessions should generally have higher progression levels.

Players with very low engagement should generally have lower progression levels.

`progression_level` must be a non-negative integer.

Players with zero gameplay activity should have minimal or zero progression.

`rewards_claimed` should generally increase with progression and engagement.

Rewards claimed must be a non-negative integer.


## 8. Social Feature Logic

`social_feature_used` is a Boolean value.

Players with higher engagement should have a higher probability of using social features.

Social feature usage should also be associated with somewhat higher retention probability.

However, social feature usage must not guarantee retention.


## 9. Retention Logic

Retention variables will represent whether a player returned to the product on the corresponding lifecycle day.

### Day-1 Retention

`day_1_retained = True` if the player returns on Day 1 after acquisition.

### Day-7 Retention

`day_7_retained = True` if the player returns on Day 7 after acquisition.

### Day-30 Retention

`day_30_retained = True` if the player returns on Day 30 after acquisition.

Retention is probabilistic and should be influenced by behavioral characteristics such as:

- Tutorial completion
- First-match participation
- Sessions
- Matches
- Progression
- Social feature usage
- Acquisition channel

No single variable should deterministically determine retention.


## 10. Churn Definition

For this project, a player will be classified as churned if they show no meaningful return to the product during the defined observation window after their initial acquisition and early gameplay activity.

For the synthetic dataset, churn will be generated as a behavioral outcome associated with low engagement and weak retention.

Churn probability may increase with:

- Failure to complete onboarding
- Failure to reach the first match
- Low session frequency
- Low match participation
- Low progression
- Lack of social engagement

Churn will not be determined by a single variable.


## 11. Data Integrity Rules

The following conditions must always be satisfied:

1. `player_id` must be unique.

2. If `first_match_played = False`:
   - `first_match_result = Not Played`
   - `matches_week1 = 0`

3. If `first_match_played = True`:
   - `first_match_result` must be Win, Draw, or Loss.
   - `matches_week1 >= 1`

4. `sessions_week1 >= 0`

5. `matches_week1 >= 0`

6. `avg_session_minutes >= 0`

7. `progression_level >= 0`

8. `rewards_claimed >= 0`

9. If `sessions_week1 = 0`:
   - `avg_session_minutes = 0`

10. If `matches_week1 = 0`:
   - `progression_level` should be zero or minimal.

11. All Boolean fields must contain only True or False.

12. All categorical fields must use only predefined category values.

13. D1, D7, and D30 retention must be Boolean values.

14. Retention must be probabilistically related to player behavior rather than directly assigned from a single variable.


## 12. Realism Rules

The synthetic dataset should reflect realistic behavioral variation.

The generator should avoid:

- Perfectly equal category distributions
- Identical behavior across players
- Perfect linear relationships
- Impossible values
- Deterministic retention outcomes
- Artificially perfect correlations

The dataset should include natural variation and some behavioral noise so that analysis requires investigation rather than producing obvious predetermined answers.


## 13. Expected Behavioral Relationships

The synthetic dataset should be designed so that analysis may reveal the following relationships:

### Relationship 1 — Onboarding

Players who complete the tutorial should generally have higher first-match conversion and retention.

### Relationship 2 — Engagement

Players with more sessions and matches should generally show higher retention.

### Relationship 3 — Progression

Players who progress further should generally show stronger engagement and retention.

### Relationship 4 — Social Features

Players who use social features should generally have higher engagement and retention.

### Relationship 5 — Churn

Players with low engagement and weak progression should generally have higher churn probability.

### Relationship 6 — Acquisition

Some acquisition channels may produce players with different engagement and retention characteristics.

These are hypotheses built into the synthetic data generation process and must be validated through analysis rather than treated as confirmed findings.


## 14. Data Generation Principle

The dataset will be generated using a probabilistic approach.

Player attributes will influence behavioral probabilities, which will influence engagement, progression, retention, and churn.

The generation process should therefore follow a logical chain:

Player Attributes
        ↓
Onboarding Behavior
        ↓
Early Engagement
        ↓
Progression
        ↓
Retention / Churn

The purpose is to create a synthetic environment that behaves sufficiently like a real product analytics dataset for educational and portfolio analysis.


