# J140_TwitterScraper

# Project Introduction
# Download "J140-TwitterAnalysis-Fall_2018.html" and open the HTML file in your browser to just examine the Fall 2018 results of the study/project.

**Project Outline**
* CSULB J104 - Student Twitter Engagement
    * <u>CSULB - J104</u> - Social Media Communication
    * <u>Professor Kehoe</u>
    * Assignment - <i>Students tweet twice per week, and must include #CSULB104</i>
* Phase 1 - Research Scope
    * Scrape Tweets including #CSULB104
    * Examine student/tweet sentiment, tweet frequency, and patterns in time posted or the subject of the week
* Role - 
   * Brandon Fletcher
   * Principle Researcher/Data Scientist

**Project Goals**
* <b>Objective - Analyze J104 tweets to establish baseline understanding of student tweet behavior and sentiment</b>
* Research Tools - 
    * Twitter Scraping - Twython
    * Data Processing - pandas/numpy
    * Visualization - seaborn
    * Sentiment Analysis - vaderSentiment
* Areas of Interest - 
    * <u>User/Tweet Sentiment</u> - positivity or negativity of a tweet, or a user's general positive or negative sentiment throughout the course. Sentiment scores fall between 1 (Completely Positive) and -1 (Completely Negative), while neutral scores are between .05 and -.05.     
    * <u>Tweet Frequency</u> - the number of times a user posts
    * <u>Course Topics</u> - weeks of study during the course, and the specific subjects students were tweeting about
    * <u>Day/Time tweeted</u> - time/day hour a tweet was posted
    

# Tweet-Query-Extraction Guide
* Script used to extract tweets for project - 
* Will extract tweets containing desired hashtag, which occurred in the dates queried.

## Setup --
1. Ensure proper twitter credentials are saved in "Twitter_Credentials.py", and that the appropriate versions of the following libraries are used - 
    - json - 2.0.9
    - pandas - .23.1
    - numpy - 1.14.5
    - Twython - 3.7.0
2. Enter desired path under variable "path". In this instance, I have files saved to a sub-folder called "SavedTweets". You may need to change this so the script outputs the variable in the desired location.
3. Enter required variable information - 
    * htag - the hashtag you're going to search for.
    * pull_start - start date of the query
    * pull_end - end date of the query, will only process tweets made UP TO this date.
4. Execute script


# Tweet-SentimentAnalysis
## Pre-Processing Script - Sentiment Analyzer

* Script used to process tweets and calculate project specific variables.
    * Project specific variables are currently commented out
    * Sentiment analysis and recoding is currently included

**Step By Step Instructions**
1. Adjust path to incorporate folder containing tweets you'd like to process
2. Run script - outputted file will be called "ProcessedTweets.csv"
