# Data Story: Customer Retention — 2024 (Quarterly analysis)

**Author / Contact:** 23f3004196@ds.study.iitm.ac.in

## Executive summary
The company's quarterly customer retention rates for 2024 show a rising trend from **65.02%** in Q1 to **75.86%** in Q4, with a computed average retention of **71.18%** for the year. The industry benchmark target is **85%**, so the company currently lags by **13.82 percentage points** on average. This gap is significant and warrants targeted retention campaigns combined with product/experience improvements.

> **Key numbers**
> - Q1 2024: 65.02  
> - Q2 2024: 71.48  
> - Q3 2024: 72.37  
> - Q4 2024: 75.86  
> - **Average (2024): 71.18**  
> - Industry target: 85

## What I did (method)
- Computed average retention from quarterly numbers.
- Created a time series visualization (quarterly trend) and plotted the industry benchmark line (85%).
- Identified business implications and actionable recommendations to close the gap to 85%.

This analysis was generated with human oversight and with the assistance of an LLM-powered coding assistant (documented in commit messages / PR labels).

## Key findings
1. **Clear upward trend** across quarters — retention improved steadily (Q1 → Q4).
2. **Average is below benchmark**: 71.18 vs 85 — a 13.82 point gap.
3. **Improvement is real but insufficient** — while growth between quarters is encouraging, the current pace will not reach 85 in the short term without focused effort.
4. **Potential root areas (hypotheses)**:
   - Early-stage onboarding friction (low Q1 suggests acquisition-to-retention leakage).
   - Post-purchase experience or product value perception issues.
   - Insufficient personalization or loyalty incentives.
   - Churn concentrated in specific segments (e.g., low-ARPU customers or certain cohorts).

## Business implications
- Continued underperformance will reduce LTV and increase CAC payback time.
- Resource allocation decisions (marketing, product improvements, CX) should prioritize experiments with the highest expected retention lift per dollar.
- Investors/executive leadership may require clear plans for retention KPIs for the next fiscal year.

## Specific recommendations to reach 85 (actionable roadmap)
**Goal:** Move average retention from 71.18 → 85.

### 1. Segment + Targeted Retention Campaigns (high priority)
- **Segment customers by behavior** (recency, frequency, monetary, product usage).
- **Design campaigns per segment**: onboarding drip for new users, re-engagement offers for at-risk users, premium nudges for high-value customers.
- **Metrics:** cohort retention after 30/60/90 days; lift in retention per segment.

### 2. Onboarding and Activation fixes
- Audit the first 7–14 days experience; reduce friction and accelerate “aha” moment.
- Run A/B tests on onboarding flows & measure 7/30-day retention.

### 3. Personalization & Product Value
- Use product usage signals and simple ML rules to personalize messages, recommendations, and offers.
- Implement targeted in-app messages and emails at important moments.

### 4. Loyalty & Rewards
- Introduce a lightweight loyalty program (points, small discounts, referral bonuses).
- Test “win-back” coupons for churned-but-reengageable users.

### 5. Proactive feedback loops
- NPS and quick in-product surveys to catch dissatisfaction early.
- Rapid response playbook for low-NPS or negative feedback users.

### 6. Dashboard & Experimentation
- Build a retention dashboard tracking cohorts and experiment results.
- Run prioritized A/B tests; measure statistical significance on retention.

### 7. Timeline & targets
- Short-term (3 months): launch segmentation and 1–2 targeted campaigns; aim to increase average by 2–4 points.
- Mid-term (6–12 months): onboarding overhaul + loyalty program; aim for an additional 4–6 points.
- Long-term: continuous personalization and product improvements to approach 85.

## Example technical artifacts
- `analysis/retention_analysis.py` — code used to compute average and create the retention chart.
- `analysis/out/retention_plot.png` — chart (quarterly trend and benchmark).
- All code commits include LLM-assistance labels for traceability.

## How to reproduce locally
1. Clone the repo:
```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
