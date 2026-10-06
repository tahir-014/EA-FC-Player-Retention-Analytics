# EA FC Player Retention & Onboarding Analytics — Metrics Framework

## 1. Metrics Hierarchy

The metrics framework is designed to measure the new-player journey from acquisition through early engagement, retention, progression, and churn.

The hierarchy is:

Acquisition
    ↓
Onboarding
    ↓
Engagement
    ↓
Progression
    ↓
Retention
    ↓
Churn
    ↓
Monetization


## 2. Acquisition Metrics

### New Players

Definition:

The number of unique players who enter the product during the analysis period.

Formula:

New Players = Count of unique player IDs

Purpose:

Measures the size of the incoming player population and provides the denominator for downstream funnel and retention analysis.


## 3. Onboarding Metrics

### Tutorial Completion Rate

Definition:

Percentage of new players who successfully complete the onboarding tutorial.

Formula:

Tutorial Completion Rate =
Players who completed tutorial / Total new players × 100

Purpose:

Measures whether players successfully progress through the initial onboarding experience.

---

### First Match Conversion Rate

Definition:

Percentage of new players who play their first match after entering the game.

Formula:

First Match Conversion =
Players who played first match / Total new players × 100

Purpose:

Measures conversion from initial onboarding into the core gameplay experience.

---

### Second Session Conversion Rate

Definition:

Percentage of players who return for a second gameplay session after their initial session.

Formula:

Second Session Conversion =
Players with a second session / Eligible new players × 100

Purpose:

Provides an early indicator of whether players are finding enough value to return.


## 4. Engagement Metrics

### Sessions per Player

Definition:

Average number of gameplay sessions per player during the defined analysis period.

Formula:

Sessions per Player =
Total sessions / Unique players

Purpose:

Measures frequency of player engagement.

---

### Matches per Player

Definition:

Average number of matches played per player.

Formula:

Matches per Player =
Total matches / Unique players

Purpose:

Measures participation in the core gameplay loop.

---

### Average Session Duration

Definition:

Average amount of time spent per gameplay session.

Formula:

Average Session Duration =
Total session minutes / Total sessions

Purpose:

Provides an indication of depth of engagement during gameplay sessions.


## 5. Progression Metrics

### Average Progression Level

Definition:

Average progression level reached by players during the analysis period.

Purpose:

Measures how far players progress through the game's progression system.

---

### Rewards Claimed per Player

Definition:

Average number of rewards claimed by each player.

Formula:

Rewards per Player =
Total rewards claimed / Unique players

Purpose:

Helps evaluate player interaction with reward and progression systems.

---

### Progression Completion Rate

Definition:

Percentage of eligible players who complete a defined progression milestone.

Purpose:

Measures participation in structured progression experiences.


## 6. Retention Metrics

### Day-1 Retention (D1)

Definition:

Percentage of new players who return to the game one day after acquisition.

Formula:

D1 Retention =
Players returning on Day 1 / Eligible new players × 100

Purpose:

Measures very early return behavior.

---

### Day-7 Retention (D7)

Definition:

Percentage of new players who return to the game seven days after acquisition.

Formula:

D7 Retention =
Players returning on Day 7 / Eligible new players × 100

Purpose:

Primary success metric for this project because it provides an indication of whether players continue engaging beyond the initial experience.

---

### Day-30 Retention (D30)

Definition:

Percentage of new players who return to the game thirty days after acquisition.

Formula:

D30 Retention =
Players returning on Day 30 / Eligible new players × 100

Purpose:

Provides a longer-term view of player retention.


## 7. Churn Metrics

### Churn Rate

Definition:

Percentage of eligible players who meet the project's churn definition during the analysis period.

Formula:

Churn Rate =
Churned players / Eligible players × 100

Purpose:

Measures the proportion of players who stop returning.

---

### Churn by Segment

Definition:

Churn rate calculated separately for player segments such as platform, acquisition channel, engagement level, and player type.

Purpose:

Identifies segments with disproportionately high churn.


## 8. Social Engagement Metrics

### Social Feature Adoption

Definition:

Percentage of players who use at least one defined social feature.

Formula:

Social Feature Adoption =
Players using social features / Eligible players × 100

Purpose:

Measures participation in social experiences and allows comparison between players who use social features and those who do not.


## 9. Monetization Metrics

Monetization metrics will be treated as secondary analytical dimensions in this portfolio project.

Potential metrics include:

### Conversion Rate

Percentage of eligible players who complete a defined purchase action.

### Revenue per Paying Player

Average revenue generated among players who make a purchase.

### Paying Player Rate

Percentage of eligible players who make at least one purchase.

These metrics will not be treated as primary success metrics because the primary focus of this project is new-player retention and onboarding.


## 10. Primary and Secondary Metrics

### Primary Metric

**Day-7 Retention (D7)**

Reason:

The project focuses on understanding early player retention and identifying opportunities to improve the transition from initial onboarding into sustained engagement.

### Secondary Metrics

- D1 Retention
- D30 Retention
- Tutorial Completion Rate
- First Match Conversion
- Second Session Conversion
- Sessions per Player
- Matches per Player
- Average Session Duration
- Progression Level
- Rewards Claimed
- Churn Rate
- Social Feature Adoption


## 11. Metric-to-Question Mapping

| Product Question | Primary Metric |
|---|---|
| Are players completing onboarding? | Tutorial Completion Rate |
| Are players reaching core gameplay? | First Match Conversion |
| Are players returning after the first session? | D1 Retention |
| Are players continuing to engage? | D7 Retention |
| Are players becoming longer-term users? | D30 Retention |
| How frequently are players engaging? | Sessions per Player |
| How deeply are players engaging? | Matches per Player / Session Duration |
| Are players progressing? | Progression Level |
| Are players leaving? | Churn Rate |
| Are players engaging socially? | Social Feature Adoption |


## 12. Guardrail Metrics

When evaluating future product experiments, improvements in the primary metric should not come at the expense of important player experience indicators.

Potential guardrail metrics include:

- Crash rate
- Uninstall rate
- Negative player feedback
- Session failures
- Technical errors
- Significant decreases in core gameplay participation

A product experiment should only be considered successful when the primary metric improves without unacceptable deterioration in important guardrail metrics.


## 13. Metrics Tree

New Player Growth
│
├── Acquisition
│   └── New Players
│
├── Onboarding
│   ├── Tutorial Completion
│   ├── First Match Conversion
│   └── Second Session Conversion
│
├── Engagement
│   ├── Sessions per Player
│   ├── Matches per Player
│   └── Session Duration
│
├── Progression
│   ├── Progression Level
│   └── Rewards Claimed
│
├── Retention
│   ├── D1
│   ├── D7 ⭐ Primary
│   └── D30
│
├── Churn
│   └── Churn Rate
│
├── Social
│   └── Social Feature Adoption
│
└── Monetization
    ├── Paying Player Rate
    ├── Conversion Rate
    └── Revenue per Paying Player


    