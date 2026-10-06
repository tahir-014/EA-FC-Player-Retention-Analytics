import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)

# Dataset configuration
N_PLAYERS = 50_000

START_DATE = pd.Timestamp("2026-01-01")
END_DATE = pd.Timestamp("2026-06-30")

player_ids = [
    f"P{i:06d}"
    for i in range(1, N_PLAYERS + 1)
]

date_range = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

acquisition_dates = np.random.choice(
    date_range,
    size=N_PLAYERS
)

acquisition_channels = np.random.choice(
    [
        "Organic",
        "YouTube",
        "Instagram",
        "TikTok",
        "Influencer",
        "Paid Ads"
    ],
    size=N_PLAYERS,
    p=[
        0.25,
        0.15,
        0.15,
        0.15,
        0.10,
        0.20
    ]
)

age_groups = np.random.choice(
    [
        "Under 18",
        "18-24",
        "25-34",
        "35+"
    ],
    size=N_PLAYERS,
    p=[
        0.15,
        0.45,
        0.25,
        0.15
    ]
)

regions = np.random.choice(
    [
        "India",
        "North America",
        "Europe",
        "Asia Pacific",
        "Latin America",
        "Middle East & Africa"
    ],
    size=N_PLAYERS,
    p=[
        0.25,
        0.20,
        0.25,
        0.15,
        0.10,
        0.05
    ]
)

platforms = np.random.choice(
    [
        "PC",
        "PlayStation",
        "Xbox",
        "Mobile"
    ],
    size=N_PLAYERS,
    p=[
        0.25,
        0.35,
        0.20,
        0.20
    ]
)

tutorial_probability = np.full(
    N_PLAYERS,
    0.75
)

tutorial_probability += np.where(
    acquisition_channels == "Organic",
    0.05,
    0
)

tutorial_probability += np.where(
    acquisition_channels == "Paid Ads",
    -0.05,
    0
)

tutorial_probability += np.where(
    acquisition_channels == "Influencer",
    0.02,
    0
)

tutorial_probability += np.random.normal(
    loc=0,
    scale=0.04,
    size=N_PLAYERS
)

tutorial_probability = np.clip(
    tutorial_probability,
    0.50,
    0.95
)

tutorial_completed = (
    np.random.random(N_PLAYERS)
    < tutorial_probability
)

first_match_probability = np.where(
    tutorial_completed,
    0.88,
    0.35
)

first_match_probability += np.random.normal(
    loc=0,
    scale=0.03,
    size=N_PLAYERS
)

first_match_probability = np.clip(
    first_match_probability,
    0.15,
    0.95
)

first_match_played = (
    np.random.random(N_PLAYERS)
    < first_match_probability
)

first_match_result = np.full(
    N_PLAYERS,
    "Not Played",
    dtype=object
)

played_mask = first_match_played

first_match_result[played_mask] = np.random.choice(
    [
        "Win",
        "Draw",
        "Loss"
    ],
    size=played_mask.sum(),
    p=[
        0.42,
        0.18,
        0.40
    ]
)

# ============================================================
# WEEK-1 SESSION GENERATION
# ============================================================

engagement_segment = np.random.choice(
    [
        "Low",
        "Moderate",
        "High",
        "Very High"
    ],
    size=N_PLAYERS,
    p=[
        0.25,
        0.45,
        0.23,
        0.07
    ]
)

sessions_week1 = np.zeros(N_PLAYERS, dtype=int)

low_mask = engagement_segment == "Low"
moderate_mask = engagement_segment == "Moderate"
high_mask = engagement_segment == "High"
very_high_mask = engagement_segment == "Very High"

sessions_week1[low_mask] = np.random.randint(
    0,
    4,
    size=low_mask.sum()
)

sessions_week1[moderate_mask] = np.random.randint(
    4,
    11,
    size=moderate_mask.sum()
)

sessions_week1[high_mask] = np.random.randint(
    11,
    21,
    size=high_mask.sum()
)

sessions_week1[very_high_mask] = np.random.randint(
    21,
    36,
    size=very_high_mask.sum()
)

# ============================================================
# ONBOARDING INFLUENCE ON ENGAGEMENT
# ============================================================

# Successful onboarding increases engagement,
# but does not guarantee another session.

first_match_boost = (
    np.random.random(N_PLAYERS) < 0.50
) & first_match_played

tutorial_boost = (
    np.random.random(N_PLAYERS) < 0.40
) & tutorial_completed

sessions_week1 += first_match_boost.astype(int)
sessions_week1 += tutorial_boost.astype(int)

sessions_week1 = np.clip(
    sessions_week1,
    0,
    35
)
matches_week1 = np.where(
    first_match_played,
    np.maximum(
        1,
        np.round(
            sessions_week1 *
            np.random.uniform(
                0.8,
                2.2,
                N_PLAYERS
            )
        )
    ),
    0
).astype(int)

matches_week1 = np.clip(
    matches_week1,
    0,
    60
)

avg_session_minutes = np.where(
    sessions_week1 > 0,
    np.random.gamma(
        shape=4,
        scale=10,
        size=N_PLAYERS
    ),
    0
)

avg_session_minutes = np.clip(
    avg_session_minutes,
    0,
    120
)

avg_session_minutes = np.round(
    avg_session_minutes,
    1
)

progression_level = (
    sessions_week1 * 0.8
    + matches_week1 * 0.35
    + np.random.normal(
        0,
        2.5,
        N_PLAYERS
    )
)

progression_level = np.clip(
    progression_level,
    0,
    50
)

progression_level = np.round(
    progression_level
).astype(int)

rewards_claimed = (
    progression_level * 0.35
    + np.random.normal(
        0,
        2,
        N_PLAYERS
    )
)

rewards_claimed = np.clip(
    rewards_claimed,
    0,
    30
)

rewards_claimed = np.round(
    rewards_claimed
).astype(int)

social_probability = (
    0.20
    + 0.02 * np.minimum(sessions_week1, 10)
)

social_probability = np.clip(
    social_probability,
    0.10,
    0.70
)

social_feature_used = (
    np.random.random(N_PLAYERS)
    < social_probability
)


# ============================================================
# RETENTION MODEL
# ============================================================

# Base retention probability
retention_score = (
    0.00

    # Onboarding
    + np.where(tutorial_completed, 0.08, -0.08)
    + np.where(first_match_played, 0.08, -0.10)

    # Engagement
    + sessions_week1 * 0.012
    + matches_week1 * 0.004

    # Session quality
    + np.minimum(avg_session_minutes, 60) * 0.001

    # Progression
    + progression_level * 0.003

    # Rewards
    + rewards_claimed * 0.002

    # Social engagement
    + np.where(social_feature_used, 0.06, 0)

    # First match result
    + np.where(first_match_result == "Win", 0.03, 0)
    + np.where(first_match_result == "Loss", -0.01, 0)

    # Random behavioral variation
    + np.random.normal(
        loc=0,
        scale=0.06,
        size=N_PLAYERS
    )
)

retention_score = np.clip(
    retention_score,
    0.01,
    0.95
)

# Day-1 retention
d1_probability = retention_score + 0.18

d1_probability = np.clip(
    d1_probability,
    0.05,
    0.95
)

day_1_retained = (
    np.random.random(N_PLAYERS)
    < d1_probability
)

# Day-7 retention
d7_probability = retention_score - 0.03

d7_probability = np.clip(
    d7_probability,
    0.03,
    0.85
)

day_7_retained = (
    np.random.random(N_PLAYERS)
    < d7_probability
)

# Day-30 retention
d30_probability = (
    retention_score - 0.18
)

d30_probability = np.clip(
    d30_probability,
    0.01,
    0.70
)

day_30_retained = (
    np.random.random(N_PLAYERS)
    < d30_probability
)



# ============================================================
# CHURN MODEL
# ============================================================

churn_probability = (
    0.95

    # Strong onboarding reduces churn
    + np.where(tutorial_completed, -0.05, 0.08)
    + np.where(first_match_played, -0.05, 0.10)

    # Engagement reduces churn
    - sessions_week1 * 0.010
    - matches_week1 * 0.004

    # Progression reduces churn
    - progression_level * 0.003

    # Social engagement reduces churn
    - np.where(social_feature_used, 0.06, 0)

    # Random behavioral variation
    + np.random.normal(
        loc=0,
        scale=0.07,
        size=N_PLAYERS
    )
)

churn_probability = np.clip(
    churn_probability,
    0.05,
    0.95
)

churned = (
    np.random.random(N_PLAYERS)
    < churn_probability
)


# ============================================================
# BUILD FINAL DATAFRAME
# ============================================================

players = pd.DataFrame({
    "player_id": player_ids,
    "acquisition_date": acquisition_dates,
    "acquisition_channel": acquisition_channels,
    "age_group": age_groups,
    "region": regions,
    "platform": platforms,
    "tutorial_completed": tutorial_completed,
    "first_match_played": first_match_played,
    "first_match_result": first_match_result,
    "sessions_week1": sessions_week1,
    "matches_week1": matches_week1,
    "avg_session_minutes": avg_session_minutes,
    "progression_level": progression_level,
    "rewards_claimed": rewards_claimed,
    "social_feature_used": social_feature_used,
    "day_1_retained": day_1_retained,
    "day_7_retained": day_7_retained,
    "day_30_retained": day_30_retained,
    "churned": churned
})

print("\nDataset created successfully!")
print(f"Rows: {len(players):,}")
print(f"Columns: {len(players.columns)}")

print("\nFirst 5 rows:")
print(players.head())

# ============================================================
# DATA VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

# 1. Row count
assert len(players) == N_PLAYERS
print("✓ Row count:", len(players))

# 2. Player IDs must be unique
assert players["player_id"].is_unique
print("✓ Player IDs are unique")

# 3. Missing values
missing_values = players.isnull().sum().sum()

assert missing_values == 0
print("✓ No missing values")

# 4. Sessions cannot be negative
assert (players["sessions_week1"] >= 0).all()
print("✓ Sessions are valid")

# 5. Matches cannot be negative
assert (players["matches_week1"] >= 0).all()
print("✓ Matches are valid")

# 6. Session duration cannot be negative
assert (players["avg_session_minutes"] >= 0).all()
print("✓ Session duration is valid")

# 7. Progression must be between 0 and 50
assert players["progression_level"].between(0, 50).all()
print("✓ Progression levels are valid")

# 8. Rewards must be between 0 and 30
assert players["rewards_claimed"].between(0, 30).all()
print("✓ Rewards are valid")

# 9. Players who did not play first match
#    must have zero matches
assert (
    players.loc[
        ~players["first_match_played"],
        "matches_week1"
    ] == 0
).all()

print("✓ First-match logic is valid")

# 10. Players who did not play first match
#     must have result = Not Played
assert (
    players.loc[
        ~players["first_match_played"],
        "first_match_result"
    ] == "Not Played"
).all()

print("✓ First-match result logic is valid")


# ============================================================
# RETENTION VALIDATION
# ============================================================

d1_rate = players["day_1_retained"].mean()
d7_rate = players["day_7_retained"].mean()
d30_rate = players["day_30_retained"].mean()
churn_rate = players["churned"].mean()

print("\nRetention Metrics:")
print(f"D1 Retention:  {d1_rate:.2%}")
print(f"D7 Retention:  {d7_rate:.2%}")
print(f"D30 Retention: {d30_rate:.2%}")
print(f"Churn Rate:    {churn_rate:.2%}")

# ============================================================
# DISTRIBUTION CHECKS
# ============================================================

print("\n" + "=" * 60)
print("DISTRIBUTION CHECKS")
print("=" * 60)

print("\nAcquisition Channel:")
print(
    players["acquisition_channel"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nRegion:")
print(
    players["region"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nPlatform:")
print(
    players["platform"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nAge Group:")
print(
    players["age_group"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# ============================================================
# ONBOARDING METRICS
# ============================================================

tutorial_rate = players["tutorial_completed"].mean()

first_match_rate = players["first_match_played"].mean()

second_session_rate = (
    players["sessions_week1"] >= 2
).mean()

print("\n" + "=" * 60)
print("ONBOARDING METRICS")
print("=" * 60)

print(
    f"Tutorial Completion Rate: "
    f"{tutorial_rate:.2%}"
)

print(
    f"First Match Conversion Rate: "
    f"{first_match_rate:.2%}"
)

print(
    f"Second Session Conversion Rate: "
    f"{second_session_rate:.2%}"
)

# ============================================================
# EXPORT DATASET
# ============================================================

output_path = Path("data/players.csv")

players.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("EXPORT COMPLETE")
print("=" * 60)

print(f"Dataset saved to: {output_path}")
print(f"File size: {output_path.stat().st_size / (1024 * 1024):.2f} MB")

