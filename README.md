# EA FC Player Retention & Onboarding Analytics

### Product Analytics + Growth Product Management Case Study

> **Portfolio project using synthetic player data. No proprietary EA or EA SPORTS FC data was used. Experiment results are simulated and should not be interpreted as actual EA results.**

---

## 🎯 Project Overview

How can a game improve the early experience of new players and encourage them to develop a repeat-play habit?

This project analyzes **50,000 synthetic new-player records** to identify early retention opportunities, understand player behavior, and translate the findings into a product intervention.

The project follows an end-to-end Product Management workflow:

**Problem → Data → Insight → Product → Experiment → Decision**

---

# 🧩 Business Problem

New players may reach initial gameplay but fail to develop a strong repeat-play habit during their first week.

The objective was to understand:

- Where new players drop off
- Which early behaviors are associated with retention
- Which player segment represents the biggest opportunity
- What product experience could improve early engagement
- How the proposed solution could be experimentally validated

---

# 📊 Key Product KPI

## Day-7 Retention

**32.68%**

D7 was selected as the primary KPI because the product problem focuses on whether new players develop an early repeat-play habit.

---

# 🔍 Key Findings

## 1. Moderate Engagement Is the Largest Opportunity

| Metric | Moderate Engagement |
|---|---:|
| Players | 22,511 |
| Population Share | 45.02% |
| D7 Retention | 27.16% |

High Engagement players had:

**44.27% D7 retention**

### Retention Gap

**17.10 percentage points**

This segment combines a large player population with a meaningful retention opportunity.

---

## 2. Stronger Engagement Is Associated With Higher Retention

| Engagement Segment | D7 Retention |
|---|---:|
| Low | 15.75% |
| Moderate | 27.16% |
| High | 44.27% |
| Very High | 67.34% |

This shows a strong association between early engagement and D7 retention.

> This is observational analysis and does not establish causality.

---

## 3. High-Engagement Players Return More Often

| Metric | Moderate | High |
|---|---:|---:|
| Sessions | 7.00 | 15.04 |
| Matches | 7.88 | 17.27 |
| Session Duration | 39.88 min | 39.92 min |
| Progression | 8.37 | 18.12 |
| Rewards | 3.04 | 6.33 |
| Social Adoption | 33.73% | 39.86% |

### Key Insight

Moderate and High Engagement players spend almost the same amount of time per session.

However, High Engagement players:

- Return more frequently
- Play more matches
- Progress further
- Claim more rewards

This suggests an opportunity around **meaningful repeat gameplay and progression**, rather than simply increasing session duration.

---

## 4. Onboarding Signals Are Strongly Associated With Retention

### Tutorial Completion

| Tutorial | D7 Retention |
|---|---:|
| Not Completed | 13.09% |
| Completed | 39.03% |

**Gap: +25.94 pp**

### First Match

| First Match | D7 Retention |
|---|---:|
| Not Played | 9.91% |
| Played | 40.24% |

**Gap: +30.33 pp**

These results suggest that successfully reaching meaningful gameplay is an important early retention signal.

---

# 💡 Product Opportunity

## How Might We?

> **How might we help moderately engaged new players discover meaningful reasons to return and play more frequently during their first week, so that more players develop an early gameplay habit and improve Day-7 retention?**

---

# 🚀 Proposed Product

## Week 1 Player Journey

A structured first-week experience designed to help new players understand:

> **What should I do next?**

### MVP Components

1. **Daily Player Objective**
2. **Progress Tracker**
3. **Meaningful Reward**
4. **Next-Step Recommendation**
5. **Return Reminder**

### Core Product Loop

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

The objective is not simply to increase playtime.

The goal is to create **meaningful repeat engagement**.

---

# 🧪 Experiment Design

The proposed product was evaluated through a simulated A/B experiment.

### Control

Existing player experience.

### Treatment

Week 1 Player Journey.

### Allocation

**50% Control / 50% Treatment**

### Primary Metric

**D7 Retention**

### Secondary Metrics

- Sessions per player
- Matches per player
- Progression
- Rewards claimed
- Objective completion
- Journey completion
- Second-session conversion
- Social adoption

### Guardrails

- Crash rate
- Session failures
- Uninstall rate
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# 📈 Experiment Result

| Group | Players | D7 Retention |
|---|---:|---:|
| Control | 3,921 | 27.52% |
| Treatment | 3,921 | 30.68% |

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### Statistical Result

**p = 0.0021**

### 95% Confidence Interval

**+1.15 to +5.17 percentage points**

The simulated result is statistically significant.

> These are simulated portfolio results, not actual EA experiment results.

---

# 👥 Segment Experiment

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

The strongest statistically supported effects appeared among:

- Low Engagement
- Moderate Engagement

The High Engagement segment showed no meaningful evidence of improvement.

---

# 🎯 Product Decision

## SHIP WITH GRADUAL ROLLOUT

The simulated experiment supports moving forward with controlled rollout.

### Rollout Strategy

**Stage 1 — Limited Rollout**

Validate:

- D7 retention
- Technical stability
- Player feedback
- Reward behavior

↓

**Stage 2 — Expanded Rollout**

Monitor retention and engagement drivers.

↓

**Stage 3 — Broader Rollout**

Validate whether the effect remains consistent.

↓

**Stage 4 — Full Rollout**

Only after production evidence supports the decision.

---

# 📐 Product Analytics Framework

```text
                    BUSINESS GOAL
                          ↓
             Stronger New-Player Retention
                          ↓
                     D7 RETENTION
                          ↓
       ┌──────────────────┼──────────────────┐
       ↓                  ↓                  ↓
  ONBOARDING         ENGAGEMENT         PROGRESSION
       ↓                  ↓                  ↓
 Tutorial            Sessions          Progression
 First Match         Matches           Rewards
       ↓                  ↓                  ↓
       └──────────────────┼──────────────────┘
                          ↓
                    SOCIAL VALUE
                          ↓
                  PLAYER EXPERIENCE
                          ↓
                    GUARDRAILS
```

---

# 🛠️ Tools & Technologies

### Product Management

- Product Discovery
- Product Strategy
- Product Requirements Documents
- Product Prioritization
- User Journey Mapping
- Metrics Frameworks
- A/B Experimentation
- Rollout Planning

### Analytics

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Statistical Testing
- Segmentation
- Retention Analysis
- Funnel Analysis

### Visualization

- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📁 Project Structure

```text
EA-FC-Player-Retention-Analytics/
│
├── data/
│   ├── player_analytics.db
│   └── players.csv
│
├── dashboard/
│   └── ea_fc_dashboard.ipynb
│
├── notebooks/
│
├── sql/
│   └── 01_product_analytics.sql
│
├── src/
│   └── generate_data.py
│
├── docs/
│   ├── 01_problem_statement.md
│   ├── 02_metrics_framework.md
│   ├── 03_data_dictionary.md
│   ├── 04_data_logic.md
│   ├── 05_data_generation_design.md
│   ├── 06_product_requirements_document.md
│   ├── 07_case_study.md
│   ├── 08_product_analytics_case_study.md
│   ├── 09_executive_summary.md
│   ├── 10_product_storyline.md
│   ├── 11_product_prioritization.md
│   ├── 12_player_journey_map.md
│   ├── 13_product_metrics_tree.md
│   ├── 14_experiment_rollout_plan.md
│   ├── 15_dashboard_storytelling.md
│   ├── 16_case_study_presentation.md
│   └── 17_project_quality_review.md
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 📚 Documentation

### Product Definition

- [Problem Statement](docs/01_problem_statement.md)
- [Metrics Framework](docs/02_metrics_framework.md)
- [Data Dictionary](docs/03_data_dictionary.md)
- [Data Logic](docs/04_data_logic.md)
- [Data Generation Design](docs/05_data_generation_design.md)

### Product Development

- [PRD](docs/06_product_requirements_document.md)
- [Case Study](docs/07_case_study.md)
- [Product Analytics Case Study](docs/08_product_analytics_case_study.md)
- [Executive Summary](docs/09_executive_summary.md)
- [Product Storyline](docs/10_product_storyline.md)
- [Prioritization](docs/11_product_prioritization.md)
- [Player Journey Map](docs/12_player_journey_map.md)
- [Metrics Tree](docs/13_product_metrics_tree.md)

### Experimentation & Storytelling

- [Experiment Rollout Plan](docs/14_experiment_rollout_plan.md)
- [Dashboard Storytelling](docs/15_dashboard_storytelling.md)
- [Case Study Presentation](docs/16_case_study_presentation.md)
- [Project Quality Review](docs/17_project_quality_review.md)

---

# ⚠️ Limitations

This project uses synthetic data created specifically for portfolio demonstration.

It does not represent:

- Actual EA telemetry
- Actual EA player behavior
- Actual EA business metrics
- Actual EA experiments
- Actual EA player research

The project also does not contain:

- CAC
- ROAS
- LTV
- Real production telemetry
- Real player feedback
- Real monetization data

Therefore, findings should be interpreted as **portfolio hypotheses and analytical demonstrations**, not real-world EA findings.

---

# 🎓 What This Project Demonstrates

This project demonstrates an end-to-end Product Management and Product Analytics workflow:

```text
PROBLEM
   ↓
DATA
   ↓
ANALYSIS
   ↓
PLAYER INSIGHT
   ↓
PRODUCT OPPORTUNITY
   ↓
HYPOTHESIS
   ↓
PRODUCT
   ↓
EXPERIMENT
   ↓
STATISTICAL EVIDENCE
   ↓
PRODUCT DECISION
   ↓
ROLLOUT
```

---

# 👤 Author

## Shaik Tahir Hussain

**B.Tech — Computer Science & Engineering (Artificial Intelligence)**

Interested in:

**PRODUCT MANAGEMENT | AI | PRODUCT ANALYTICS | GAMING**
