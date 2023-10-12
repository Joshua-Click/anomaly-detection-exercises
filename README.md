{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project - Anomaly Detection Final Notebook\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project Goals"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- To answer questions refering to Codeup Curriculum Access Logs\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project Description\n",
    "- I've been asked a few questions about Codeup's curriculum access logs and have provided answers to them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The Plan"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Initial Hypothesis\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?\n",
    "2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?\n",
    "3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?\n",
    "4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?\n",
    "5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?\n",
    "6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?\n",
    "7. Which lessons are least accessed?\n",
    "8. Anything else I should be aware of?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Acquire:\n",
    "- Acquired from MySql\n",
    "- Dataframes contained 900,223 rows, 6 columns for the first one\n",
    "- Second one contained 53 rows, 9 columns\n",
    "- Each Row after combining 2 dataframes represented user access\n",
    "- Each Column represented information about the cohort, user, what they accessed, when their cohort was active."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Prepare:\n",
    "- First Combine both dataframes\n",
    "- Fill NaN's with -1\n",
    "- Change 'cohort_id' to an 'int' type\n",
    "- Set index to date column as date type\n",
    "- Create 2 Columns, 'endpoint' and 'startpoint'\n",
    "- Drop 'time', 'slack', 'deleted_at', 'created_at', 'updated_at' Since we didn't use them for explore.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explore:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Specifically explored these questions to find the answers\n",
    "\n",
    "1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?\n",
    "2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?\n",
    "3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?\n",
    "6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?\n",
    "7. Which lessons are least accessed?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data dictionary:\n",
    "\n",
    "| Feature | Definition |\n",
    "|--------|-----------|\n",
    "|date| date accessed, datetime64|\n",
    "|path| complete filepath, object|\n",
    "|user_id| user specific id number, int64|\n",
    "|cohort_id| number associated with cohort name, int64|\n",
    "|ip| ip address, object|\n",
    "|id| number associated with cohort name, float|\n",
    "|name| cohort name, object|\n",
    "|start_date| start date for user in cohort|\n",
    "|end_date| end date for user in cohort|\n",
    "|program_id| number associated with program type, float|\n",
    "|endpoint| end of file path, object|\n",
    "|startpoint| start of file path, object|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to Reproduce\n",
    "- Clone this repo\n",
    "- Acquire data from MySql (Should make a zillow.csv after)\n",
    "- Run Notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Key findings "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Takeaways and Conclusions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?<p>\n",
    "Program 1 - Javascript i <p>\n",
    "Program 2 - Javascript i<p>\n",
    "Program 3 - Classification<p>\n",
    "Program 4 - HTML-CSS<p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?\n",
    "- We can say that the 'Apollo' Cohort spent alot more time in HTML-CSS than others from 40% proportion of access."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?<p>\n",
    "Low access to lessons TOP 10: <p>\n",
    "Users that dropped courses: 918, 879, 940, 619, 388 956<p>\n",
    "User 832: Didn't access course until halfway through course<p>\n",
    "User 278: Accessed more after graduating and appeared to have access to both DS and Webdev access.<p>\n",
    "User 539: Graduated and then became a Staff member<p>\n",
    "User 812: Accessed more after graduation than during course.<p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?<p>\n",
    "\n",
    "    The top 3 per program were:<p>\n",
    "    Program 1 and 2 (WebDev): Javascript-i, Spring, HTML-CSS<p>\n",
    "    Program 3 (DS): SQL, Classification, Anomaly-Detection<p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Which lessons are least accessed?\n",
    "\n",
    "    There are alot of lessons that were accessed appx 0.000001% of the time.\n",
    "    The first 10 are:<p>\n",
    "    javascript-functions<p>\n",
    "    handouts\t<p>\n",
    "    learn-to-code\t<p>\n",
    "    wp-login\t<p>\n",
    "    register.\t<p>\n",
    "    13-storytelling\t<p>\n",
    "    2-sql\t<p>\n",
    "    wp-admin\t<p>\n",
    "    .git\t<p>\n",
    "    8._Time_Series.md\t<p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Recommendations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With more time I could've answered all questions pertaining to the received request. I recommend making a category for lessons in the future to make working with the data easier."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
