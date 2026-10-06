# EA FC Player Retention & Onboarding Analytics — Data Generation Design

## 1. Dataset Size

The primary synthetic dataset will contain:

**50,000 unique players**

Each player will occupy one row in the primary player-level dataset.

The dataset size is intentionally large enough to support:

- Segmentation analysis
- Funnel analysis
- Retention analysis
- Churn analysis
- SQL queries
- Statistical comparisons
- Power BI visualization


## 2. Analysis Period

Player acquisition dates will span:

**January 1, 2026 → June 30, 2026**

Players will have sufficient lifecycle time for D1, D7, and D30 retention analysis.

The generator will ensure that players included in retention calculations have reached the required observation window.


## 3. Acquisition Channel Distribution

| Acquisition Channel | Target Share |
|---|---:|
| Organic | 25% |
| YouTube | 15% |
| Instagram | 15% |
| TikTok | 15% |
| Influencer | 10% |
| Paid Ads | 20% |
| **Total** | **100%** |


## 4. Region Distribution

| Region | Target Share |
|---|---:|
| India | 25% |
| North America | 20% |
| Europe | 25% |
| Asia Pacific | 15% |
| Latin America | 10% |
| Middle East & Africa | 5% |
| **Total** | **100%** |


## 5. Platform Distribution

| Platform | Target Share |
|---|---:|
| PC | 25% |
| PlayStation | 35% |
| Xbox | 20% |
| Mobile | 20% |
| **Total** | **100%** |


## 6. Age Group Distribution

| Age Group | Target Share |
|---|---:|
| Under 18 | 15% |
| 18-24 | 45% |
| 25-34 | 25% |
| 35+ | 15% |
| **Total** | **100%** |


## 7. Baseline Onboarding Probabilities

The initial probability of tutorial completion will be approximately:

**75%**

The actual probability for an individual player will vary based on player characteristics and acquisition source.

Tutorial completion will therefore not be identical across all players.

### First Match Probability

Players who complete the tutorial will have a substantially higher probability of playing their first match.

Target probabilities:

- Tutorial completed → approximately 88% first-match probability
- Tutorial not completed → approximately 35% first-match probability

These values represent probabilistic relationships rather than deterministic rules.


## 8. First Match Result Distribution

For players who play their first match:

| Result | Target Share |
|---|---:|
| Win | 42% |
| Draw | 18% |
| Loss | 40% |
| **Total** | **100%** |

Players who do not play a first match will receive:

`Not Played`


## 9. Engagement Distribution

### Sessions During Week 1

The number of sessions during the first seven days will be generated using a right-skewed distribution.

Most players will have relatively low session counts, while a smaller group of highly engaged players will have substantially more sessions.

Target range:

**0–35 sessions**

Approximate behavioral pattern:

- Low engagement: 0–3 sessions
- Moderate engagement: 4–10 sessions
- High engagement: 11–20 sessions
- Very high engagement: 21–35 sessions


## 10. Match Distribution

`matches_week1` will depend on whether the player reaches the first match and their overall engagement.

Target range:

**0–60 matches**

Players who do not play their first match:

`matches_week1 = 0`

Players who reach gameplay will generally have at least one match.

Highly engaged players may play substantially more matches.


## 11. Session Duration Distribution

Average session duration will be measured in minutes.

Target range:

**0–120 minutes**

Typical players will cluster around moderate session durations, while some highly engaged players will have longer sessions.

Players with zero sessions will have:

`avg_session_minutes = 0`


## 12. Progression Distribution

`progression_level` will range approximately from:

**0–50**

Progression will be influenced primarily by:

- Sessions
- Matches
- Gameplay participation

Players with greater engagement will generally progress further.

Progression will include random variation so that players with similar engagement do not always have identical progression levels.


## 13. Rewards Distribution

`rewards_claimed` will generally increase with:

- Progression level
- Engagement
- Participation in gameplay

Target range:

**0–30 rewards**

Players with little or no gameplay activity will generally claim few or no rewards.


## 14. Social Feature Usage

The overall baseline probability of using at least one social feature will be approximately:

**35%**

Social feature usage probability will increase for players with stronger engagement.

For example:

- Low-engagement players → lower probability
- Moderate-engagement players → moderate probability
- Highly engaged players → higher probability

Social feature usage will not guarantee retention.


## 15. Retention Model

Retention will be generated probabilistically rather than assigned directly.

The model will consider multiple behavioral factors.

Potential positive influences include:

- Tutorial completion
- First-match participation
- Higher session frequency
- Higher match participation
- Higher progression
- Social feature usage
- Certain acquisition channels

Negative influences may include:

- Failure to complete onboarding
- Failure to reach gameplay
- Very low engagement
- Low progression

### Target Retention Benchmarks

The synthetic dataset should approximately produce:

| Metric | Target Range |
|---|---:|
| D1 Retention | 45–55% |
| D7 Retention | 25–35% |
| D30 Retention | 12–20% |

These are design targets for the synthetic dataset, not claims about actual EA player behavior.


## 16. Behavioral Influence Design

The following relationships will be intentionally embedded at moderate strength:

| Factor | Expected Effect on Retention |
|---|---|
| Tutorial completion | Positive |
| First match played | Positive |
| Sessions | Positive |
| Matches | Positive |
| Progression | Positive |
| Social feature usage | Positive |
| Strong early gameplay outcome | Slight positive |
| Very low engagement | Negative |
| No first match | Negative |

No single factor should completely determine retention.


## 17. Acquisition Channel Behavioral Effects

Different acquisition channels will have slightly different behavioral profiles.

The synthetic model will allow:

- Organic players to have relatively strong engagement.
- Influencer-acquired players to show strong initial engagement but greater variation.
- YouTube players to show moderate-to-strong onboarding behavior.
- Instagram and TikTok players to have relatively strong acquisition volume with somewhat lower early retention.
- Paid Ads to produce a broader range of player quality.

These differences are hypotheses embedded into the synthetic dataset and must be validated through analysis.


## 18. Churn Design

The synthetic dataset should produce an overall churn rate of approximately:

**65–75%**

Churn probability should be higher among players with:

- No tutorial completion
- No first match
- Very low sessions
- Very low matches
- Low progression
- No social engagement

Players with strong engagement should have a substantially lower probability of churn.


## 19. Behavioral Noise

The generator will introduce controlled randomness to prevent perfect relationships.

For example:

- Some highly engaged players may churn.
- Some low-engagement players may return.
- Some players who lose their first match may continue playing.
- Some players who complete onboarding may still leave.
- Some players may use social features but have low retention.

This ensures that analytical findings require investigation rather than simply reproducing deterministic rules.


## 20. Data Quality Requirements

After generation, the dataset must pass automated validation checks.

The validation process must verify:

- Exactly 50,000 players
- Unique player IDs
- No unexpected null values
- Valid categorical values
- Valid Boolean values
- Valid numeric ranges
- Correct onboarding relationships
- Correct first-match logic
- Correct engagement relationships
- Valid retention fields
- Valid churn fields
- No impossible combinations


## 21. Generation Pipeline

The Python generator will follow this sequence:

1. Set random seed
2. Generate player IDs
3. Generate acquisition dates
4. Generate acquisition channels
5. Generate player attributes
6. Generate tutorial completion
7. Generate first-match participation
8. Generate first-match result
9. Generate sessions
10. Generate matches
11. Generate session duration
12. Generate progression
13. Generate rewards
14. Generate social feature usage
15. Generate D1 retention
16. Generate D7 retention
17. Generate D30 retention
18. Generate churn
19. Run validation checks
20. Export `players.csv`