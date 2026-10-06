# Project Quality Review

> Portfolio quality assessment for the EA FC Player Retention & Onboarding Analytics project.

---

# 1. Project Objective

The project aims to demonstrate Product Management and Product Analytics skills by analyzing synthetic new-player behavior, identifying an early-retention opportunity, proposing a product intervention, designing an experiment, and making a product rollout decision.

---

# 2. End-to-End Workflow

The project follows:

**Problem → Data → Insight → Product → Experiment → Decision**

Detailed workflow:

1. Define business problem
2. Define target user
3. Define product KPI
4. Create metric framework
5. Define data dictionary
6. Define synthetic data logic
7. Generate player dataset
8. Analyze player behavior
9. Segment players
10. Identify product opportunity
11. Prioritize opportunities
12. Perform root-cause analysis
13. Create product hypotheses
14. Design product concept
15. Create PRD
16. Design A/B experiment
17. Estimate sample size
18. Simulate experiment
19. Analyze experiment results
20. Design rollout strategy
21. Build dashboard
22. Create executive case study
23. Prepare interview narrative

---

# 3. Product Thinking Checklist

| Capability | Demonstrated? |
|---|---|
| Problem Definition | Yes |
| Target User | Yes |
| User Need | Yes |
| Product Goal | Yes |
| KPI Definition | Yes |
| Metrics Tree | Yes |
| Hypothesis Creation | Yes |
| Feature Concept | Yes |
| PRD | Yes |
| Prioritization | Yes |
| Experiment Design | Yes |
| Rollout Planning | Yes |
| Product Decision | Yes |

---

# 4. Product Analytics Checklist

| Capability | Demonstrated? |
|---|---|
| Python | Yes |
| Pandas | Yes |
| SQL | Yes |
| SQLite | Yes |
| Segmentation | Yes |
| Funnel Analysis | Yes |
| Retention Analysis | Yes |
| Cohort-style Thinking | Partially |
| Behavioral Analysis | Yes |
| Statistical Testing | Yes |
| A/B Analysis | Yes |
| Dashboard | Yes |
| Data Storytelling | Yes |

---

# 5. Experimentation Checklist

| Capability | Demonstrated? |
|---|---|
| Control Group | Yes |
| Treatment Group | Yes |
| Randomization | Yes |
| Primary Metric | Yes |
| Secondary Metrics | Yes |
| Guardrails | Yes |
| Sample Size | Yes |
| MDE | Yes |
| Statistical Significance | Yes |
| Confidence Interval | Yes |
| Segment Analysis | Yes |
| Rollout Decision | Yes |

---

# 6. PM Decision Quality

The project should demonstrate that metrics are not used only for reporting.

The analysis leads to a specific product decision:

> Help lower-engagement new players develop stronger early gameplay and progression habits through a structured Week 1 Player Journey.

The proposed intervention includes:

- Daily objectives
- Progress tracking
- Meaningful rewards
- Next-step recommendations
- Return reminders

---

# 7. Evidence Quality

## Strong Evidence

The project has strong evidence for:

- Size of the Moderate Engagement segment
- D7 retention differences across engagement segments
- Behavioral differences between Moderate and High Engagement
- Tutorial/D7 association
- First-match/D7 association
- Synthetic A/B experiment result

## Evidence That Requires Caution

The project should not claim that:

- More sessions cause higher retention
- Tutorial completion causes D7 retention
- First-match participation causes D7 retention
- Social features cause retention
- The Week 1 Player Journey will definitely improve real EA retention

These require controlled real-world experimentation.

---

# 8. Synthetic Data Disclosure

The following statement should remain visible throughout the project:

> **This is a portfolio project using synthetic player data. No proprietary EA or EA SPORTS FC data was used. Experiment results are simulated and should not be interpreted as actual EA results.**

This protects the credibility of the case study.

---

# 9. Dashboard Quality Checklist

The dashboard should answer:

### Question 1

What is the current retention level?

**D7 = 32.68%**

### Question 2

Where is the largest opportunity?

**Moderate Engagement = 45.02% of players**

### Question 3

What is different about stronger-engagement players?

Higher:

- Sessions
- Matches
- Progression
- Rewards

### Question 4

What product intervention is proposed?

**Week 1 Player Journey**

### Question 5

Was the concept tested?

**Yes — simulated A/B experiment**

### Question 6

What happened?

**+3.16 pp D7 lift**

### Question 7

What is the recommendation?

**Gradual rollout**

---

# 10. Interview Readiness

The project should be explainable in three levels.

## 30-Second Version

> I built a product analytics case study around new-player retention in an EA FC-style gaming environment using synthetic data. I analyzed 50,000 players and identified Moderate Engagement as the largest opportunity segment. I found that stronger engagement was associated with higher retention and proposed a Week 1 Player Journey focused on goals, progression and rewards. I then designed and simulated an A/B experiment, which showed a 3.16 percentage-point D7 retention lift, leading to a gradual-rollout recommendation.

---

## 2-Minute Version

> I started by defining the product problem as early-player retention. I chose D7 retention as the primary KPI because the goal was to understand whether new players were developing a repeat-play habit.
>
> I analyzed 50,000 synthetic players using Python and SQL across onboarding, engagement, progression, rewards, social behavior and retention.
>
> The largest opportunity was Moderate Engagement. This group represented 45.02% of players but had only 27.16% D7 retention, compared with 44.27% for High Engagement players.
>
> When I compared those groups, session duration was almost identical, but High Engagement players had substantially more sessions, matches, progression and rewards. That led me to focus on meaningful repeat gameplay rather than simply increasing session duration.
>
> I proposed a Week 1 Player Journey with daily objectives, progress tracking, meaningful rewards and next-step recommendations.
>
> I then designed a 50/50 A/B experiment using D7 as the primary metric. In the simulated experiment, D7 increased from 27.52% to 30.68%, a 3.16 percentage-point lift with a p-value of 0.0021.
>
> Based on that simulated evidence, I recommended a gradual rollout with guardrail monitoring. I would validate the result with real production telemetry before making a full rollout decision.

---

## 5-Minute Version

Use the full case-study presentation:

**Problem → Data → Insight → Opportunity → Product → Experiment → Result → Rollout**

---

# 11. Questions an Interviewer May Ask

## Product Questions

### Why did you choose D7?

Because the product problem focuses on whether new players develop an early repeat-play habit.

### Why did you choose Moderate Engagement?

Because it represents the largest segment while showing a substantial D7 retention gap versus High Engagement.

### Why not focus only on tutorial completion?

Tutorial completion is an important onboarding signal, but the larger strategic opportunity identified in the analysis was meaningful repeat engagement.

### Why not optimize session duration?

Because Moderate and High Engagement players had almost identical average session duration.

The stronger difference was in:

- Session frequency
- Matches
- Progression
- Rewards

---

# 12. Analytics Questions

### Is correlation causation?

No.

The observational analysis identifies associations.

Causal claims require controlled experimentation.

### Why use synthetic data?

Because proprietary game telemetry is not publicly available and should not be represented as if it were.

The synthetic dataset allows the project to demonstrate the analytical and PM workflow without misrepresenting real company data.

### Why use a simulated A/B test?

To demonstrate the complete experimentation workflow:

**Hypothesis → Sample Size → Randomization → Analysis → Statistical Test → Decision**

---

# 13. Experiment Questions

### Why D7 instead of sessions?

Sessions are a behavioral driver.

D7 is the primary product outcome.

### Why include guardrails?

Because increasing retention should not come at the expense of technical reliability or player experience.

### Why gradual rollout?

Because a synthetic experiment cannot validate real production behavior.

Production rollout should confirm:

- Effect size
- Stability
- Guardrails
- Player experience
- Operational reliability

---

# 14. Credibility Rules

During interviews:

### Say

> "In my synthetic dataset..."

### Say

> "The analysis suggests..."

### Say

> "The simulated experiment showed..."

### Say

> "I would validate this with production telemetry..."

### Do Not Say

> "EA players behave this way."

### Do Not Say

> "EA's D7 retention is 32.68%."

### Do Not Say

> "EA's experiment increased retention by 3.16 pp."

The numbers belong to the synthetic portfolio environment.

---

# 15. Current Project Strengths

The strongest parts of the project are:

1. Clear product problem
2. Strong KPI framework
3. Large synthetic dataset
4. Behavioral segmentation
5. Product opportunity identification
6. Root-cause thinking
7. Concrete product concept
8. PRD
9. A/B experimentation
10. Statistical analysis
11. Rollout strategy
12. Dashboard
13. Executive storytelling

---

# 16. Areas for Future Improvement

Potential future enhancements include:

- Real or publicly available gaming datasets
- More detailed cohort analysis
- Player lifecycle cohorts
- Survival analysis
- Churn prediction
- LTV modeling
- Monetization analysis
- Player survey simulation
- Qualitative player research
- BI dashboard implementation
- Advanced SQL analysis
- Product funnel instrumentation
- Event taxonomy
- Experiment monitoring framework

These should be treated as future extensions rather than requirements for the current MVP.

---

# 17. Final Quality Assessment

The project demonstrates an end-to-end Product Management workflow:

**Business Problem**
↓
**Data**
↓
**Analysis**
↓
**Player Insight**
↓
**Product Opportunity**
↓
**Feature**
↓
**Experiment**
↓
**Statistical Evidence**
↓
**Product Decision**
↓
**Rollout**

The project should therefore be presented primarily as a:

> **Product Analytics + Growth Product Management case study**

rather than simply a data analytics project.

---

# 18. Final Portfolio Positioning

## Project Title

**EA FC Player Retention & Onboarding Analytics**

## Positioning

**Product Analytics | Growth | Player Experience | Experimentation**

## Core PM Skills Demonstrated

- Product Discovery
- Product Analytics
- Growth
- Retention
- User Segmentation
- KPI Design
- SQL
- Python
- A/B Testing
- Product Strategy
- PRD Writing
- Prioritization
- Dashboarding
- Data Storytelling

---

# 19. Final One-Line Description

> **Analyzed 50K synthetic new-player records to identify a high-value retention opportunity, designed a Week 1 Player Journey, and simulated an A/B test that produced a +3.16 pp D7 retention lift.**

---

# 20. Project Status

## COMPLETE — CORE PRODUCT CASE STUDY

The project currently contains:

- Problem Definition
- Metrics Framework
- Data Dictionary
- Data Logic
- Data Generation
- Python Analysis
- SQL Analytics
- Product Opportunity
- Root-Cause Analysis
- Product Hypotheses
- Feature Concept
- PRD
- A/B Experiment
- Sample Size Analysis
- Experiment Simulation
- Dashboard
- Case Study
- Executive Summary
- Product Storyline
- Prioritization
- Player Journey
- Metrics Tree
- Rollout Plan
- Dashboard Storytelling
- Interview Presentation
- Quality Review

---

# Final Product Principle

> **The strongest PM projects do not stop at finding an insight. They show how the insight changes a product decision.**