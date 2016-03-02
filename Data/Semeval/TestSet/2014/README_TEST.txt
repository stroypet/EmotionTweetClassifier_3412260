TEST dataset for SemEval-2014 Task #9: Sentiment Analysis on Twitter

Task organizers:
Sara Rosenthal  Columbia University
Alan Ritter  University of Washington
Veselin Stoyanov Johns Hopkins University 
Preslav Nakov  Qatar Computing Research Institute


NOTE

Please note that by downloading the Twitter data you agree to abide
by the Twitter terms of service (https://twitter.com/tos),
and in particular you agree not to redistribute the data
and to delete tweets that are marked deleted in the future.
You MUST NOT re-distribute the tweets, the annotations or the corpus obtained,
as this violates the Twitter Terms of Use.


Version 1.0: March 24, 2014

Please note that by downloading the Twitter data you agree to abide by the Twitter terms of service (https://twitter.com/tos), and in particular you agree not to redistribute the data and to delete tweets that are marked deleted in the future. You MUST NOT re-distribute the tweets, the annotations or the corpus obtained, as this violates the Twitter Terms of Use.


SUMMARY

TASK A:
SemEval2014-task9-test-A-input.txt -- test input for task A

TASK B:
SemEval2014-task9-test-B-input.txt -- test input for task B


IMPORTANT

To use this test dataset, the participants should download (1), and most likely also (2) and (3):

1. the official scorer and format checker
2. the training dataset
3. the dev dataset

You can find them here: http://alt.qcri.org/semeval2014/task9/index.php?id=data-and-tools

The format checker released should be used to check the output before submitting the results.


INPUT DATA FORMAT

-----------------------TASK A-----------------------------------------
--Test Data--

The format for the test file is as follows:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101        2       2       unknwn  amoure wins oscar
NA      15115101        3       4       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file is:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>pred_class<TAB>tweet_text

where the text field is optional. For example:
NA      15115101        2       2       positive  amoure wins oscar
NA      15115101        3       4       neutral  who's a master brogramer now?


--Gold Standard--
The gold standard will follow the same format as the example system output above.

-----------------------TASK B-----------------------------------------
(Task B uses the same format as Task A, but it excludes the start and end token fields.)
--Test Data--

The format for the test file is as follows:
id1<TAB>id2<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101       unknwn  amoure wins oscar
NA      15115101       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file is:
id1<TAB>id2<TAB>pred_class<TAB>tweet_text

where the text field is optional. For example:
NA      15115101        positive  amoure wins oscar
NA      15115101        neutral  who's a master brogramer now?

--Gold Standard--
The gold standard will follow the same format as the example system output above.



INPUT DATA FORMAT NOTES

1. For subtask A, the annotations are at the token level, where the tokenization is on a single " " (space). Note that in the case of two consecutive spaces, this creates an empty token, which is counted! Also, token counting starts from zero.

2. Some punctuation characters are escaped, e.g.,:

@BarackObama\u002c Clinton\u002c Panetta\u002c Petraeus we will not #StandDown on Nov 6 or Nov 7 or Nov 8th. Do the right thing now. #WeWillNotLetThisGo



EVALUATION

The metric for evaluating the participants' systems will be average F-measure (averaged F-positive and F-negative, and ignoring F-neutral; note that this does not make the task binary!), as well as F-measure for each class (positive, negative, neutral), which can be illuminating when comparing the performance of different systems.
For each subtask, the systems will be ranked based on their average F-measure.  Separate rankings for each test dataset will be produced.

See also the scorer for details on scoring the output.


DATASET USE

The development dataset is intended to be used as a development-time evaluation dataset as the participants develop their systems. However, the participants are free to use the dataset in any way they like, e.g., they can add it to their training dataset as well.


TEST PROCEDURE

Task participants must submit their runs by the final deadline of March 30, 2014 (23:59 at Midway, Midway Islands, United States: see http://www.timeanddate.com/worldclock/city.html?n=1890). Late submissions will not be counted.
Note that you can make new submissions, which will substitute your earlier submissions on the FTP server,
multiple times, but only before the deadline.
Thus, we advise that you submit your runs early, and possibly resubmit later if there is time for that.

For *each task*, each team may submit two runs: one constrained and one unconstrained:

(1) Constrained - using the provided training AND development data only; other resources, such as lexicons are allowed; however, it is not allowed to use additional Tweet messages or additional sentences with sentiment annotations; and

(2) Unconstrained - using additional data, e.g., additional Tweet messages or additional sentences annotated for sentiment.


SUBMISSION PROCEDURE

1. Each participating team should have registered on http://alt.qcri.org/semeval2014/index.php?id=registration-1. Only one registration is necessary per team even when participating in multiple tasks. Registered participants should have received instructions on how to access the FTP server. If not, please tell us immediately: semevaltweet@googlegroups.com
The results should be uploaded to the FTP server!

2. Each team's submission can include runs for each combination of subtask (A or B) and training condition (constrained or unconstrained). This makes a total of 4 runs allowed.

3. Name of the submission:  "TEAMID.zip".

4. Format of the submission: the ZIP file should contain two files *for each run* (i.e., there should be 2, 4, 6 or 8 files zipped)

- task2-GROUP-SUBTASK-CONDITION.output
- task2-GROUP-SUBTASK-CONDITION.description

Where GROUP is the group name, SUBTASK is "A" or "B", and CONDITION is "constrained" or "unconstrained"
For example: "QCRI-A-constrained.output" + "QCRI-A-constrained.description"

The first file should follow the output format specified above.

The second file should have the format of the SUBMISSION_DESCRIPTION_TEMPLATE.txt.
It contains the following information:

	1. Team ID

	2. Team affiliation

	3. Contact information

	4. Submission, i.e., ZIP file name

	5. System specs

	- 5.1 Core approach

	- 5.2 Supervised or unsupervised

	- 5.3 Critical features used

	- 5.4 Critical tools used

	- 5.5 Significant data pre/post-processing

	- 5.6 Other data used (outside of the provided)

	- 5.7 Size of the training Twitter data used (some teams could only download part of the data)

	- 5.8 Did you participate in SemEval-2013 task 2?

	6 References (if applicable)



USEFUL LINKS:

Google group: semevaltweet@googlegroups.com
Task website: http://alt.qcri.org/semeval2014/task9/
SemEval-2014 website: http://alt.qcri.org/semeval2014/


TASK SCHEDULE

Trial data ready October 30, 2013
Training data ready December 15, 2013
Test data released March 24, 2014
Evaluation ends March 30, 2014
Paper submission due April 30, 2014
Paper reviews due May 30, 2014
Camera ready due June 30, 2014
SemEval workshop August 23-30, 2014 [TBC]
