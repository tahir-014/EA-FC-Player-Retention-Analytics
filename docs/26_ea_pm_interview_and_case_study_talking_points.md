# EA PM Interview & Case Study Talking Points

## EA FC Player Retention & Onboarding Analytics

> Portfolio case study based on synthetic data. No proprietary EA data, telemetry, research, or internal product information was used.

---

# 1. 30-Second Project Pitch

I built a product analytics case study around new-player retention in a football gaming experience.

I used 50,000 synthetic player records to analyze onboarding, engagement, progression, rewards, social adoption, and Day-7 retention.

The biggest opportunity I identified was the Moderate Engagement segment, which represented about 45% of players but had only 27.16% D7 retention.

I translated that insight into a Week 1 Player Journey concept and designed a simulated A/B test that produced a 3.16 percentage-point D7 lift.

The project combines product analytics, player research, growth experimentation, and product strategy.

---

# 2. One-Minute Version

The project started with a simple product question:

> Why do some new players fail to develop a repeat-play habit during their first week?

I created a synthetic dataset of 50,000 players and analyzed the new-player journey across onboarding, first-match conversion, engagement, progression, rewards, social behavior, and retention.

The most important segment was Moderate Engagement players.

They represented 45.02% of the population and had 27.16% D7 retention, compared with 44.27% among High Engagement players.

I investigated the behavioral differences and found that the biggest gaps were in sessions, matches, progression, and rewards rather than average session duration.

That led to the hypothesis that players may benefit from clearer short-term goals and stronger connections between gameplay, progression, rewards, and the next reason to return.

I proposed a Week 1 Player Journey and designed an A/B experiment around it.

The simulated experiment showed a +3.16 percentage-point D7 lift, with a p-value of 0.0021.

The project then expanded into player personas, journey mapping, research, competitive analysis, player communication, experimentation, and roadmap prioritization.

---

# 3. Three-Minute Case Study

## Step 1 — Problem

The initial question was:

> How can we improve early retention among new players?

The focus was on the first 30 days, with D7 retention selected as the primary KPI because the product problem concerns early repeat-play behavior.

---

## Step 2 — Data

I created a synthetic dataset containing:

- 50,000 players
- Acquisition channel
- Age group
- Region
- Platform
- Tutorial completion
- First-match participation
- Sessions
- Matches
- Session duration
- Progression
- Rewards
- Social feature usage
- D1 retention
- D7 retention
- D30 retention
- Churn

The data was intentionally designed to contain realistic variation and behavioral relationships without representing real EA telemetry.

---

## Step 3 — Analysis

Overall D7 retention was:

**32.68%**

I segmented players based on Week-1 session frequency.

| Segment | Sessions | Players | D7 |
|---|---:|---:|---:|
| Low | 0–3 | 10,296 | 15.75% |
| Moderate | 4–10 | 22,511 | 27.16% |
| High | 11–20 | 12,885 | 44.27% |
| Very High | 21–35 | 4,308 | 67.34% |

The Moderate segment stood out because it was both:

- Large
- Under-retained

---

## Step 4 — Insight

Moderate players averaged:

- 7.00 sessions
- 7.88 matches
- 8.37 progression
- 3.04 rewards

High players averaged:

- 15.04 sessions
- 17.27 matches
- 18.12 progression
- 6.33 rewards

Average session duration was almost identical:

- Moderate: 39.88 minutes
- High: 39.92 minutes

This suggested that the difference was not simply that High players spent much longer per session.

They returned more often, played more matches, progressed further, and claimed more rewards.

---

# 4. Product Problem

The resulting problem statement was:

> A large share of new players reach an initial level of engagement but fail to develop strong repeat-play behavior during their first week.

---

# 5. How Might We

> How might we help moderately engaged new players discover meaningful reasons to return and play more frequently during their first week, so that more players develop an early gameplay habit and improve Day-7 retention?

---

# 6. Product Hypothesis

The hypothesis was:

> A structured Week 1 experience with clear gameplay objectives, visible progression, meaningful rewards, and a clear next step may help players develop stronger repeat-play behavior.

This was treated as a hypothesis rather than a causal conclusion from observational data.

---

# 7. Product Concept

## Week 1 Player Journey

The MVP includes:

1. Personalized Daily Objective
2. Progress Tracker
3. Meaningful Reward
4. Next-Step Recommendation
5. Journey Progress

The intended loop is:

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

---

# 8. Experiment

I designed a 50/50 player-level A/B test.

### Control

Existing experience.

### Treatment

Week 1 Player Journey.

### Sample

3,921 players per group.

### Primary KPI

D7 retention.

### Guardrails

- Crash rate
- Session failures
- Uninstall rate
- Negative feedback
- Reward abuse
- Core gameplay participation

---

# 9. Simulated Result

| Group | Players | D7 Retention |
|---|---:|---:|
| Control | 3,921 | 27.52% |
| Treatment | 3,921 | 30.68% |

### Absolute Lift

**+3.16 percentage points**

### Relative Lift

**+11.48%**

### p-value

**0.0021**

### 95% Confidence Interval

**+1.15 to +5.17 pp**

The simulated result was statistically significant.

My recommendation was:

> Gradual rollout, subject to guardrail and production validation.

---

# 10. Why Gradual Rollout?

A statistically significant result does not automatically mean:

> "Ship to 100% of players."

I would first:

1. Validate guardrails.
2. Monitor player feedback.
3. Check segment behavior.
4. Gradually increase exposure.
5. Monitor longer-term retention.
6. Compare production behavior with the experiment result.

---

# 11. Segment Analysis

The simulated experiment showed:

| Segment | Control | Treatment | Lift |
|---|---:|---:|---:|
| Low | 26.77% | 34.73% | +7.96 pp |
| Moderate | 26.96% | 30.02% | +3.06 pp |
| High | 28.71% | 28.33% | -0.38 pp |
| Very High | 28.57% | 31.49% | +2.92 pp |

The strongest statistically supported effects appeared among Low and Moderate players.

The High segment showed no meaningful evidence of improvement.

This suggests that different player segments may require different product strategies.

---

# 12. Important Statistical Caveat

The segment analysis contains multiple comparisons.

Therefore, individual segment significance should not automatically be interpreted as definitive proof.

Segment results should ideally be:

- Pre-specified
- Validated with follow-up experiments
- Interpreted alongside player research
- Considered as supporting evidence

---

# 13. Why D7 Retention?

D7 was selected because the problem focuses on early repeat-play behavior.

The goal is not simply to maximize short-term activity.

The goal is to determine whether players develop a sustainable reason to return.

I would also monitor:

- D1
- D30
- Second-session conversion
- Sessions
- Matches
- Progression
- Rewards

---

# 14. Why Not Optimize Session Duration?

One of the most interesting findings was that Moderate and High players had nearly identical average session duration.

Moderate:

**39.88 minutes**

High:

**39.92 minutes**

But their session frequency and gameplay depth were substantially different.

Therefore, I would avoid treating longer sessions as the primary growth objective.

The better product question is:

> How do we create meaningful reasons for players to return?

---

# 15. Why Not Just Increase Rewards?

Increasing rewards could increase short-term activity without creating sustainable player value.

Potential risks include:

- Reward inflation
- Reward farming
- Reduced reward meaning
- Economy imbalance

Therefore, the hypothesis focuses on:

**Meaningful progression + meaningful rewards**

rather than simply:

**More rewards**

---

# 16. Why Not Focus on Social First?

Social adoption showed a supporting difference:

- Moderate: 33.73%
- High: 39.86%

Gap:

**6.13 percentage points**

However, the strongest behavioral differences were in:

- Sessions
- Matches
- Progression
- Rewards

Therefore, social discovery was prioritized later rather than making it the MVP.

---

# 17. Why Not Focus Only on Tutorial Completion?

Tutorial completion showed a strong association with D7 retention.

However, the root-cause analysis showed only a relatively small difference in tutorial completion between Moderate and High players:

- Moderate: 75.38%
- High: 77.72%

Difference:

**2.34 percentage points**

This suggested that tutorial completion alone did not explain the main Moderate → High engagement gap.

Therefore, the product strategy moved beyond onboarding into the broader Week 1 experience.

---

# 18. Player Research Plan

The analytics cannot tell us exactly why players behave this way.

Therefore, I would validate the hypothesis using:

- Player interviews
- Usability testing
- Surveys
- In-game feedback
- Community research
- Telemetry

The research question would be:

> What prevents moderately engaged players from developing a stronger reason to return?

---

# 19. Competitive Analysis

Competitive analysis was used to understand common product patterns around:

- Short-term goals
- Progression
- Rewards
- Social interaction
- Live events
- Player communication

The purpose was not to copy competitor features.

The PM question is:

> What player need does this product pattern solve, and do our players have the same need?

---

# 20. Player Marketing Strategy

The proposed player communication strategy supports the Week 1 experience.

Example communication journey:

```text
WELCOME
 ↓
FIRST GOAL
 ↓
PROGRESS
 ↓
REWARD
 ↓
NEXT GOAL
 ↓
RETURN
```

Potential message variants could test:

- Goal-focused messaging
- Progress-focused messaging
- Reward-focused messaging
- Discovery-focused messaging

The primary outcome should still be D7 retention rather than message opens alone.

---

# 21. Roadmap

## NOW

- First-match activation
- Week 1 Player Journey MVP
- A/B test

## NEXT

- Progression visibility
- Reward relevance
- Player communication

## LATER

- Social discovery
- Personalization
- Advanced engagement

This roadmap deliberately avoids building too many features before validating the core hypothesis.

---

# 22. How I Would Work Cross-Functionally

As PM, I would work with:

### Data / Analytics

Define metrics, instrumentation, experiment analysis, and dashboards.

### UX / Design

Design the Week 1 journey, progression visibility, objectives, and rewards presentation.

### Engineering

Implement the MVP and event instrumentation.

### User Research

Validate player motivations, confusion, and friction.

### Marketing

Develop relevant player communication and campaign variants.

### Game Design

Ensure objectives and progression reinforce meaningful gameplay.

The PM role is to align these functions around the player problem and measurable outcome.

---

# 23. What Would I Do If Engineering Said the Feature Was Too Expensive?

I would reduce scope while protecting the core hypothesis.

For example:

Instead of building a highly personalized journey:

### MVP

- Simple objective
- Basic progress tracker
- Existing reward system
- Simple next-step recommendation

The goal would be:

> Test the player need before investing in a complex solution.

---

# 24. What If the Experiment Fails?

I would not immediately conclude:

> "The idea was bad."

I would investigate:

1. Did players use the feature?
2. Did they understand it?
3. Did objectives get completed?
4. Did progression improve?
5. Did rewards feel meaningful?
6. Did player sentiment change?
7. Was D7 the right outcome window?

Then I would decide whether to:

- Iterate
- Change the hypothesis
- Test another solution
- Stop the initiative

A failed experiment can still create valuable learning.

---

# 25. What If D7 Improves but Player Sentiment Gets Worse?

I would not automatically scale the feature.

The team would need to understand the trade-off.

Possible causes:

- Notification fatigue
- Excessive objectives
- Reward pressure
- Repetitive gameplay
- Poor experience quality

The product goal is sustainable player value, not retention at any cost.

---

# 26. What If the CEO/Leadership Wants a Different Feature?

I would first understand the underlying goal.

For example:

> "Why is this feature important right now?"

Then I would compare it against:

- Player impact
- Strategic alignment
- Evidence
- Effort
- Risk
- Learning potential

If the leadership request is strategically important, I would incorporate it into prioritization rather than blindly rejecting it.

---

# 27. What I Learned From the Project

### 1. Data is not the product decision

Analytics identify patterns.

PMs translate patterns into decisions.

---

### 2. Correlation is not causation

Behavioral associations should generate hypotheses.

Experiments are needed to establish causal impact.

---

### 3. Large segments matter

A smaller high-value segment may not always be the biggest product opportunity.

The Moderate segment was important because it combined:

**Large population + low retention + meaningful behavioral gap**

---

### 4. More engagement is not always better

The objective should be meaningful engagement rather than maximizing activity metrics.

---

### 5. Player research matters

Telemetry tells us what happened.

Research helps us understand why.

---

### 6. Experiments reduce uncertainty

The purpose of experimentation is not simply to prove that a feature works.

It is to learn whether our assumptions are correct.

---

# 28. Final Case Study Narrative

The complete story is:

```text
PLAYER DATA
    ↓
RETENTION PROBLEM
    ↓
SEGMENTATION
    ↓
MODERATE PLAYER OPPORTUNITY
    ↓
BEHAVIORAL ANALYSIS
    ↓
PLAYER PERSONA
    ↓
JOURNEY & FRICTION
    ↓
RESEARCH HYPOTHESIS
    ↓
PRODUCT CONCEPT
    ↓
A/B EXPERIMENT
    ↓
SEGMENT ANALYSIS
    ↓
GROWTH & MARKETING
    ↓
ROADMAP
    ↓
PRODUCT DECISION
```

---

# 29. Final Interview Answer

If asked:

> "Tell me about a product you've worked on."

Answer:

> "I built a product analytics case study focused on new-player retention in a football gaming experience. I created a synthetic dataset of 50,000 players and analyzed the onboarding and early engagement journey. The most interesting finding was that Moderate Engagement players represented about 45% of the population but had only 27.16% D7 retention, compared with 44.27% for High Engagement players.
>
> I looked beyond the retention number and found that the main behavioral differences were repeat sessions, matches, progression, and rewards, while average session duration was almost identical. That led me to hypothesize that the opportunity wasn't simply getting players to spend more time in a session, but giving them clearer reasons to return.
>
> I designed a Week 1 Player Journey with objectives, progression, rewards, and next-step recommendations, then created a simulated A/B test. The simulated treatment improved D7 retention by 3.16 percentage points. I then extended the work into player personas, journey mapping, research, competitive analysis, player communication, experimentation, and roadmap prioritization.
>
> The biggest thing I learned is that good product management is about connecting player needs, data, experimentation, and cross-functional execution rather than just building features."

---

# 30. One-Sentence Portfolio Pitch

> **I use player analytics, research, experimentation, and product strategy to identify growth opportunities and design better player experiences.**

---

# 31. EA-Relevant Skills Demonstrated

This project demonstrates:

### Product Management

- Problem definition
- Product discovery
- User stories
- PRD
- Prioritization
- Roadmapping
- MVP definition

### Growth

- Funnel analysis
- Retention
- Engagement
- Player lifecycle
- Growth hypotheses
- Campaign strategy

### Analytics

- Python
- Pandas
- SQL
- Segmentation
- KPI analysis
- Statistical testing
- A/B experimentation

### Player Understanding

- Personas
- Journey mapping
- Friction analysis
- Player research
- Feedback frameworks

### Experimentation

- Hypothesis design
- Control/treatment
- Sample-size planning
- Statistical significance
- Confidence intervals
- Guardrails
- Rollout strategy

### Cross-Functional Thinking

- Design
- Engineering
- Analytics
- Research
- Game Design
- Marketing

---

# 32. Final Disclaimer

This project is a portfolio simulation.

All player data is synthetic.

The project does not use:

- Proprietary EA telemetry
- Internal EA research
- Confidential EA information
- Internal EA product roadmaps
- Real EA experiment results
