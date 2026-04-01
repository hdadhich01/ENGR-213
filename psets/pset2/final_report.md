# PSET 2 Final Report: SQL-Based Business Analytics for NJ Teacher Salaries

## Overview

For this assignment, I worked through four business scenarios using the NJ Teachers Salaries dataset. The goal was to write SQL queries, see what patterns show up in the data, and then use those patterns to come up with some recommendations. Each scenario looks at a different education policy question, and I tried to stick to what the data actually shows rather than guessing.

---

## Scenario 1: Budget Optimization in School Districts

**Problem Statement:** A school district is dealing with budget constraints and needs to figure out if its salary spending makes sense. Before suggesting any changes, I wanted to understand the basics first - which districts are paying the most, which are paying the least, and how does salary change as teachers get more experience.

### Task 1: Salary Distribution Analysis

**Top 5 Districts by Average Salary:**

| District | Average Salary |
|----------|----------------|
| Northern Valley Regional | $101,840.40 |
| Passaic County Vocational | $95,298.63 |
| Pascack Valley Regional | $95,191.84 |
| Palisades Park | $93,754.00 |
| Hackensack City | $92,813.21 |

**Bottom 5 Districts by Average Salary:**

| District | Average Salary |
|----------|----------------|
| West Cape May Boro | $43,184.27 |
| Classical Academy Charter School | $45,000.00 |
| Hope Community Cs | $45,762.33 |
| Hudson Arts And Science Charter School | $46,439.29 |
| The Kingdom Charter School Of Leadership | $46,807.83 |

### Task 2: Experience vs. Salary Analysis

**Average Salary by Years of Experience (First 10 Years):**

| Year | Average Salary |
|------|----------------|
| 0 | $55,158.68 |
| 1 | $57,323.85 |
| 2 | $57,567.87 |
| 3 | $58,297.50 |
| 4 | $59,165.91 |
| 5 | $60,408.58 |
| 6 | $61,454.77 |
| 7 | $62,983.57 |
| 8 | $65,514.38 |
| 9 | $67,338.71 |

### Task 3: Recommendations

1. Right away, the gap between the highest and lowest paying districts jumped out at me - nearly $58,000, which is more than double. That's a big difference and it probably deserves a closer look at how funding gets spread around the state.

2. What also caught my attention is that 4 of the 5 lowest-paying districts are charter schools. That feels like more than a coincidence, and I think charter school pay might need to be looked at separately.

3. On the experience side, salary goes up pretty steadily - around $1,200 per year on average. One thing that could help with the big gap between districts is having standard salary ranges based on experience, so teachers don't get paid less just because of where they work.

---

## Scenario 2: Retention of High-Performing Teachers

**Problem Statement:** Passaic County is worried about losing experienced teachers to neighboring counties or out-of-state jobs. That makes sense as a concern, but I wanted to check if the data actually backs it up. Is Passaic really behind, or does it just feel that way?

### Task 1: Passaic County Salary vs Experience

**Passaic Avg Salary for Years 10-15:**

| Year | Average Salary |
|------|----------------|
| 10 | $68,490.36 |
| 11 | $73,041.86 |
| 12 | $76,403.78 |
| 13 | $78,529.07 |
| 14 | $80,081.32 |
| 15 | $84,373.50 |

### Task 2: Passaic Retention Strategy (>10 Years Experience)

| Metric | Value |
|--------|-------|
| Passaic Avg Salary (>10 Years) | $90,709.14 |
| Passaic Teacher Count (>10 Years) | 8,238 |

### Task 3: Cross-County Comparison (>10 Years Experience)

**Average Salary for Experienced Teachers (>10 Years):**

| County | Average Salary |
|--------|----------------|
| Bergen | $93,020.49 |
| Passaic | $90,709.14 |
| Essex | $89,280.30 |
| Morris | $86,276.51 |
| Sussex | $86,153.71 |

### Task 4: Retention Strategy Recommendations

1. Honestly, Passaic is doing better than I thought it would. It's 2nd out of the 5 neighboring counties, and the gap with Bergen at the top is only about $2,300. That's close enough that some small bonuses or incentives could close it without spending a ton of money.

2. Passaic also has a good foundation - 8,238 teachers with over 10 years of experience. And salaries go from $68k at year 10 to $84k at year 15, which is about $3,200 per year in raises. That kind of growth probably helps explain why retention isn't as bad as people thought.

3. Going forward, I'd say Passaic should keep its lead over Essex, Morris, and Sussex while looking for ways to catch up to Bergen. Bonuses at year 10 or 15 could be enough to make the difference.

---

## Scenario 3: Cost-Benefit Analysis of Certification Programs

**Problem Statement:** The state education board wants to know if funding certification programs is worth it. The thinking is simple - if certified teachers earn more and stay longer, then helping teachers get certified should save money by reducing turnover. But I wanted to see what the data actually shows before assuming that's true.

### Task 1: Salary Difference by Certification

| Certification Status | Average Salary |
|---------------------|----------------|
| Standard | $75,824.50 |
| Non-Standard | $59,497.05 |

### Task 2: Average Experience by Certification

| Certification Status | Average Experience |
|---------------------|-------------------|
| Standard | 13.2 years |
| Non-Standard | 3.7 years |

### Task 3 & 4: Cost-Benefit Recommendations

1. There's definitely a salary gap - about $16,000 between standard and non-standard certification. But here's the thing: standard certified teachers also have almost 10 more years of experience on average (13.2 years vs 3.7). So it's hard to tell how much of that salary difference is because of the certification versus just being there longer.

2. That 9.5-year experience gap tells me that most non-standard teachers are probably newer and still working on getting fully certified. If the state can help them finish that process faster, it could keep more teachers around and save money on turnover down the road.

3. Putting it all together, I think funding certification programs is probably worth it. Even if we can't say exactly how much the certification itself matters, the data shows that certified teachers tend to stay longer. And since losing teachers and hiring new ones is expensive - all the recruiting, training, getting them up to speed - the money spent on certification probably pays off.

---

## Scenario 4: Optimal Salary Structures for New Teachers

**Problem Statement:** The Department of Education wants to bring in more recent graduates and is thinking about how to set up salaries for teachers early in their careers. The question I really wanted to answer is: when exactly are we losing new teachers, and would paying them more at the right time actually help keep them?

### Task 1: Starting Salary Analysis (0-5 Years)

| Metric | Value |
|--------|-------|
| Average Salary for New Teachers (0-5 Years) | $57,904.97 |

### Task 2: Salary Progression (Year 0 to 5)

| Year | Average Salary |
|------|----------------|
| 0 | $55,158.68 |
| 1 | $57,323.85 |
| 2 | $57,567.87 |
| 3 | $58,297.50 |
| 4 | $59,165.91 |
| 5 | $60,408.58 |

### Task 3: Retention Factors (Teacher Count Drop-off)

| Year | Teacher Count |
|------|---------------|
| 0 | 12,140 |
| 1 | 16,328 |
| 2 | 13,612 |
| 3 | 13,364 |
| 4 | 11,858 |
| 5 | 10,872 |
| 6 | 8,462 |
| 7 | 9,012 |
| 8 | 10,428 |
| 9 | 11,156 |
| 10 | 11,706 |

### Task 4: Salary Structure Recommendations

1. This one surprised me. I thought the biggest drop would be in the first year or two, but it's actually between year 5 and year 6 - teacher count goes from 10,872 down to 8,462, which is a 22% drop in just one year. So if we're going to give out retention bonuses, year 5 is probably when to do it.

2. That said, something's also happening early on. The raise from year 1 to year 2 is barely anything - just $244. And during that same time, we lose almost 2,700 teachers. Giving a bigger raise at year 2 might help keep people through that rough early stretch.

3. One more thing I noticed: after year 6, the numbers actually go back up through year 10. Teachers who make it past year 6 seem to stick around. That backs up the idea that we should focus on keeping teachers during those first 6 years - if they make it that far, they're probably staying.

---

## Conclusion

Looking back at all four scenarios, a few things stand out:

- **The gap between districts is huge.** Nearly $58,000 between the top and bottom, and charter schools are mostly at the bottom. That's not going to change on its own.

- **Certification and experience are mixed together.** Certified teachers make more, but they also have way more experience on average. I can't say for sure how much certification alone matters, but helping teachers get certified faster still seems like a good idea since they tend to stay longer.

- **Teachers are leaving around year 5-6, not year 1-2.** That was the biggest surprise. If we want to keep teachers in the job, that's when to step in with bonuses or something.

- **Passaic is actually doing fine.** It's 2nd out of its neighbors for experienced teacher pay, only $2,300 behind Bergen. Some small changes could close that gap without costing too much.

At the end of the day, the data suggests a few things worth doing: look at charter school pay, help teachers get certified faster, and give retention bonuses around year 5-6. These aren't huge changes - they're just fixes aimed at where the problems actually seem to be.
