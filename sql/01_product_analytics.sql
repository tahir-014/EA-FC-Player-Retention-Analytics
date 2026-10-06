-- ============================================================
-- EA FC PLAYER RETENTION & ONBOARDING ANALYTICS
-- Product Analytics SQL
-- ============================================================


-- 1. Total Players

SELECT
    COUNT(*) AS total_players
FROM players;

-- 2. Overall D7 Retention

SELECT
    COUNT(*) AS total_players,
    SUM(CASE WHEN day_7_retained = 1 THEN 1 ELSE 0 END) AS d7_retained_players,
    ROUND(
        100.0 * SUM(CASE WHEN day_7_retained = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS d7_retention_pct
FROM players;

-- 3. Tutorial Completion Rate

SELECT
    ROUND(
        100.0 * SUM(CASE WHEN tutorial_completed = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS tutorial_completion_pct
FROM players;

-- 4. D7 Retention by Tutorial Completion

SELECT
    tutorial_completed,
    COUNT(*) AS players,
    ROUND(
        100.0 * AVG(CASE WHEN day_7_retained = 1 THEN 1.0 ELSE 0.0 END),
        2
    ) AS d7_retention_pct
FROM players
GROUP BY tutorial_completed
ORDER BY tutorial_completed;

-- 5. D7 Retention by First Match Participation

SELECT
    first_match_played,
    COUNT(*) AS players,
    ROUND(
        100.0 * AVG(CASE WHEN day_7_retained = 1 THEN 1.0 ELSE 0.0 END),
        2
    ) AS d7_retention_pct
FROM players
GROUP BY first_match_played
ORDER BY first_match_played;

-- 6. D7 Retention by Engagement Segment

SELECT
    CASE
        WHEN sessions_week1 BETWEEN 0 AND 3 THEN 'Low'
        WHEN sessions_week1 BETWEEN 4 AND 10 THEN 'Moderate'
        WHEN sessions_week1 BETWEEN 11 AND 20 THEN 'High'
        ELSE 'Very High'
    END AS engagement_segment,

    COUNT(*) AS players,

    ROUND(
        100.0 * AVG(
            CASE
                WHEN day_7_retained = 1 THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS d7_retention_pct

FROM players

GROUP BY engagement_segment

ORDER BY
    CASE engagement_segment
        WHEN 'Low' THEN 1
        WHEN 'Moderate' THEN 2
        WHEN 'High' THEN 3
        WHEN 'Very High' THEN 4
    END;

-- 7. Acquisition Channel Performance

SELECT
    acquisition_channel,
    COUNT(*) AS players,

    ROUND(
        100.0 * AVG(
            CASE
                WHEN day_7_retained = 1 THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS d7_retention_pct,

    ROUND(
        100.0 * AVG(
            CASE
                WHEN churned = 1 THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS churn_rate_pct,

    ROUND(AVG(sessions_week1), 2) AS avg_sessions,

    ROUND(AVG(matches_week1), 2) AS avg_matches

FROM players

GROUP BY acquisition_channel

ORDER BY d7_retention_pct DESC;

-- 8. Moderate Engagement Opportunity

SELECT
    COUNT(*) AS moderate_players,

    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM players),
        2
    ) AS player_share_pct,

    ROUND(
        100.0 * AVG(
            CASE
                WHEN day_7_retained = 1 THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS d7_retention_pct,

    ROUND(AVG(sessions_week1), 2) AS avg_sessions,

    ROUND(AVG(matches_week1), 2) AS avg_matches,

    ROUND(AVG(progression_level), 2) AS avg_progression,

    ROUND(AVG(rewards_claimed), 2) AS avg_rewards

FROM players

WHERE sessions_week1 BETWEEN 4 AND 10;