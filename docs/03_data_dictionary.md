# EA FC Player Retention & Onboarding Analytics — Data Dictionary

## 1. Dataset Overview

The primary dataset represents synthetic new-player behavior during the early lifecycle of a football gaming experience.

Each row represents one unique player.

The dataset is designed to support analysis of:

- Player acquisition
- Onboarding
- Engagement
- Progression
- Retention
- Churn
- Social feature adoption
- Monetization

The dataset is synthetic and created solely for educational and portfolio purposes.


## 2. Player Identity

### player_id

**Type:** String

**Example:** P000001

**Description:** Unique identifier assigned to each player.

**Purpose:** Allows individual players to be uniquely identified and analyzed.


## 3. Acquisition Data

### acquisition_date

**Type:** Date

**Example:** 2026-01-15

**Description:** Date on which the player entered the product.

**Purpose:** Used to establish the player's lifecycle start date and calculate retention windows.

---

### acquisition_channel

**Type:** Categorical

**Possible values:**

- Organic
- YouTube
- Instagram
- TikTok
- Influencer
- Paid Ads

**Description:** The primary channel through which the player was acquired.

**Purpose:** Compare acquisition sources based on engagement and retention.


## 4. Player Attributes

### age_group

**Type:** Categorical

**Possible values:**

- Under 18
- 18-24
- 25-34
- 35+

**Description:** Player age segment.

**Purpose:** Allows analysis of behavioral differences across broad age groups.

---

### region

**Type:** Categorical

**Possible values:**

- India
- North America
- Europe
- Asia Pacific
- Latin America
- Middle East & Africa

**Description:** Broad geographic region associated with the player.

**Purpose:** Enables regional comparison of player behavior.

---

### platform

**Type:** Categorical

**Possible values:**

- PC
- PlayStation
- Xbox
- Mobile

**Description:** Platform used by the player.

**Purpose:** Compare engagement and retention across platforms.


## 4. Player Attributes

### age_group

**Type:** Categorical

**Possible values:**

- Under 18
- 18-24
- 25-34
- 35+

**Description:** Player age segment.

**Purpose:** Allows analysis of behavioral differences across broad age groups.

---

### region

**Type:** Categorical

**Possible values:**

- India
- North America
- Europe
- Asia Pacific
- Latin America
- Middle East & Africa

**Description:** Broad geographic region associated with the player.

**Purpose:** Enables regional comparison of player behavior.

---

### platform

**Type:** Categorical

**Possible values:**

- PC
- PlayStation
- Xbox
- Mobile

**Description:** Platform used by the player.

**Purpose:** Compare engagement and retention across platforms.


## 5. Onboarding Data

### tutorial_completed

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player completed the onboarding tutorial.

**Purpose:** Used to analyze the relationship between onboarding completion and subsequent engagement and retention.

---

### first_match_played

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player completed their first gameplay match.

**Purpose:** Measures conversion from onboarding into the core gameplay experience.

---

### first_match_result

**Type:** Categorical

**Possible values:**

- Win
- Draw
- Loss
- Not Played

**Description:** Outcome of the player's first match.

**Purpose:** Used to investigate whether early gameplay outcomes are associated with subsequent engagement.


## 6. Engagement Data

### sessions_week1

**Type:** Integer

**Example:** 5

**Description:** Number of gameplay sessions completed during the player's first seven days.

**Purpose:** Measures frequency of early engagement.

---

### matches_week1

**Type:** Integer

**Example:** 8

**Description:** Number of matches played during the player's first seven days.

**Purpose:** Measures participation in the core gameplay loop.

---

### avg_session_minutes

**Type:** Numeric

**Example:** 42.5

**Description:** Average duration of a gameplay session during the first seven days.

**Purpose:** Measures depth of engagement.


## 7. Progression Data

### progression_level

**Type:** Integer

**Example:** 12

**Description:** Player progression level reached during the observation period.

**Purpose:** Measures how far players progress through the game's progression system.

---

### rewards_claimed

**Type:** Integer

**Example:** 6

**Description:** Number of rewards claimed by the player during the observation period.

**Purpose:** Measures interaction with reward and progression systems.


## 8. Social Engagement Data

### social_feature_used

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player used at least one defined social feature.

**Purpose:** Allows comparison between players who engage with social features and those who do not.


## 9. Retention Data

### day_1_retained

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player returned to the product on Day 1 after acquisition.

**Purpose:** Measures early retention.

---

### day_7_retained

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player returned to the product on Day 7 after acquisition.

**Purpose:** Primary retention metric for this project.

---

### day_30_retained

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player returned to the product on Day 30 after acquisition.

**Purpose:** Measures longer-term retention.


## 10. Churn Data

### churned

**Type:** Boolean

**Possible values:** True / False

**Description:** Indicates whether the player meets the project's defined churn criteria during the observation period.

**Purpose:** Enables analysis of player loss and identification of high-risk player segments.


## 11. Complete Dataset Schema

| Column | Type | Category |
|---|---|---|
| player_id | String | Identity |
| acquisition_date | Date | Acquisition |
| acquisition_channel | Categorical | Acquisition |
| age_group | Categorical | Player |
| region | Categorical | Player |
| platform | Categorical | Player |
| tutorial_completed | Boolean | Onboarding |
| first_match_played | Boolean | Onboarding |
| first_match_result | Categorical | Gameplay |
| sessions_week1 | Integer | Engagement |
| matches_week1 | Integer | Engagement |
| avg_session_minutes | Numeric | Engagement |
| progression_level | Integer | Progression |
| rewards_claimed | Integer | Progression |
| social_feature_used | Boolean | Social |
| day_1_retained | Boolean | Retention |
| day_7_retained | Boolean | Retention |
| day_30_retained | Boolean | Retention |
| churned | Boolean | Churn |