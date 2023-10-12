# Project - Anomaly Detection Final Notebook

## Project Goals
- To answer questions refering to Codeup Curriculum Access Logs

## Project Description
- I've been asked a few questions about Codeup's curriculum access logs and have provided answers to them.

## The Plan

### Initial Hypothesis

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?

### Acquire:
- Acquired from MySql
- Dataframes contained 900,223 rows, 6 columns for the first one
- Second one contained 53 rows, 9 columns
- Each Row after combining 2 dataframes represented user access
- Each Column represented information about the cohort, user, what they accessed, when their cohort was active.

### Prepare:
- First Combine both dataframes
- Fill NaN's with -1
- Change 'cohort_id' to an 'int' type
- Set index to date column as date type
- Create 2 Columns, 'endpoint' and 'startpoint'
- Drop 'time', 'slack', 'deleted_at', 'created_at', 'updated_at' Since we didn't use them for explore.

### Explore:

### Specifically explored these questions to find the answers

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?

### Data dictionary:

| Feature | Definition |
|--------|-----------|
|date| date accessed, datetime64|
|path| complete filepath, object|
|user_id| user specific id number, int64|
|cohort_id| number associated with cohort name, int64|
|ip| ip address, object|
|id| number associated with cohort name, float|
|name| cohort name, object|
|start_date| start date for user in cohort|
|end_date| end date for user in cohort|
|program_id| number associated with program type, float|
|endpoint| end of file path, object|¡
|startpoint| start of file path, object|

### How to Reproduce
- Clone this repo
- Acquire data from MySql 
- Run Notebook

## Key findings 
### Takeaways and Conclusions

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?<p>
Program 1 - Javascript i <p>
Program 2 - Javascript i<p>
Program 3 - Classification<p>
Program 4 - HTML-CSS<p>

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
- We can say that the 'Apollo' Cohort spent alot more time in HTML-CSS than others from 40% proportion of access.

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?<p>
Low access to lessons TOP 10: <p>
Users that dropped courses: 918, 879, 940, 619, 388 956<p>
User 832: Didn't access course until halfway through course<p>
User 278: Accessed more after graduating and appeared to have access to both DS and Webdev access.<p>
User 539: Graduated and then became a Staff member<p>
User 812: Accessed more after graduation than during course.<p>

4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?<p>

    The top 3 per program were:<p>
    Program 1 and 2 (WebDev): Javascript-i, Spring, HTML-CSS<p>
    Program 3 (DS): SQL, Classification, Anomaly-Detection<p>

5. Which lessons are least accessed?

    There are alot of lessons that were accessed appx 0.000001% of the time.
    The first 10 are:<p>
    javascript-functions<p>
    handouts	<p>
    learn-to-code	<p>
    wp-login	<p>
    register.	<p>
    13-storytelling	<p>
    2-sql	<p>
    wp-admin	<p>
    .git	<p>
    8._Time_Series.md	<p>

### Recommendations
With more time I could've answered all questions pertaining to the received request. I recommend making a category for lessons in the future to make working with the data easier.
