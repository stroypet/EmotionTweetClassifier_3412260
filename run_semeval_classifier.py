#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
############## Semeval - Sentiment Analysis in Twitter  #################
#########################################################################

####
#### Authors: Pedro Paulo Balage Filho e Lucas Avanço
#### Version: 2.0
#### Date: 26/03/14
####

#### This python script provides a tempalte to run the hybrid sentiment classifier for Semeval 2014 Task 9
#### Information about Semeval format can be found at:
####    http://alt.qcri.org/semeval2014/task9/
####

# Python 3 compatibility
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals

# Import the libraries created for this task
from SemevalTwitter import SemevalTwitter
from TwitterHybridClassifier import TwitterHybridClassifier
from nltk import ConfusionMatrix
from pprint import pprint
import codecs


# Print the confusion matrix for classification
def confusion_matrix(gold, guess):
    correct = 0
    total = len(gold)
    for i in range(len(gold)):
        if guess[i] == gold[i]:
            correct += 1
    accuracy = float(correct) / float(total)
    print('Accuracy: {:.2%}'.format(accuracy))

    # Confusion Matrix
    cm = ConfusionMatrix(gold, guess)
    print(cm)


# These are the paths I used in my experiment. Due SemEval constraints
# I could not provide these data. However, if you e-mail me,
# I could send you these datasets privately.

train_path = 'Data/Semeval/TrainSet/twitter-train-gold-B-2014.tsv'
dev_path = 'Data/Semeval/DevSet/twitter-dev-gold-B.tsv'
#test_path = 'Data/Semeval/TestSet/2014/SemEval2014-task9-test-B-input.txt'
#test_path = '/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/JOINED_GOLD_TEST_DATA.txt'
test_path = '/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/TweetVisualization/tweets.txt'
#test_path = '/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/ML-PRUNED-NEUTRALS.txt'

# TestSet from 2013
# test_path  = 'Data/Semeval/TestSet/2013/twitter-test-GOLD-B.tsv'

print('Reading Datasets and Pre-processing...')
# read the data in the format used by the library
semeval = SemevalTwitter(train_path, dev_path, test_path)
trainset = semeval.trainset
devset = semeval.devset
testset = semeval.testset

# Training the supervised model. You should send (tweet_message, label) for training
print('Training...')
tweets = [(tweet['MESSAGE'], tweet['SENTIMENT']) for tweet in trainset]
tweets += [(tweet['MESSAGE'], tweet['SENTIMENT']) for tweet in devset]
classifier = TwitterHybridClassifier(tweets)

# Apply the classifier for all tweets in the testset
print('Testing...')

# count how many instances were classified by each method
# RB: Rule-based, LB: Lexicon-base, ML: Machine Learning classifier IN THIS ORDER
count = {'RB': 0, 'LB': 0, 'ML': 0}

# Evaluate if tested with the gold standard
guess = list()
gold = list()

guessrb = list()
goldrb = list()

guesslb = list()
goldlb = list()

guessml = list()
goldml = list()

# Keep the predictions string
output = ''

# Load test set tweets, USED DEVSET SO TWEETS IN CM WORK
#tweets = [tweet['MESSAGE'] for tweet in devset]
tweets = [tweet['MESSAGE'] for tweet in testset]

# Classify each instance in the testset in the TwitterHybridClassifier loaded before
predictions = classifier.classify_batch(tweets)

# Output the semeval prediction file and the evaluation variables
# if testset if provided NOTE: USED DEVSET HERE OTHERWISE CM BREAKS
if len(testset) > 0:
    for index, tweet in enumerate(testset):
        prediction, method = predictions[index]
        count[method] += 1
        output += tweet['SID'] + '\t' + tweet['UID'] + '\t' + prediction + '\t' + tweet['MESSAGE'] + '\n'
        if method == 'RB':
            guessrb.append(prediction)
            goldrb.append(tweet['SENTIMENT'])
        if method == 'LB':
            guesslb.append(prediction)
            goldlb.append(tweet['SENTIMENT'])
        if method == 'ML':
            guessml.append(prediction)
            goldml.append(tweet['SENTIMENT'])
        guess.append(prediction)
        gold.append(tweet['SENTIMENT'])
    print("Hybrid Classifier:")
    confusion_matrix(gold, guess)
    print("Rule (hash) Classifier:")
    confusion_matrix(goldrb, guessrb)
    print("Lexicon Classifier:")
    confusion_matrix(goldlb, guesslb)
    print("Machine learning Classifier:")
    confusion_matrix(goldml, guessml)

    # READ IN TESTSET GOLD DATA HERE, CAN OVERWRITE LINE.SPLIT[2] OF GOLD INPUT WITH TESTSET AND RENAME.
    # Write Semeval output file
    output_file = 'task9-NILC_USP-B-twitter-constrained.output'
    codecs.open(output_file, 'w', 'utf8').write(output)

    # Print some statistics
    print('Statistics -  Number of instances processed by each method')
    print('Rule Based:       ', count['RB'])
    print('Lexicon Based:    ', count['LB'])
    print('Machine Learning: ', count['ML'])

    print('\nSemeval output file in: ', output_file)

# Print individual scores
tweets = [(tweet['MESSAGE'],tweet['SENTIMENT']) for tweet in testset] #devset used here
classifier.output_individual_scores(tweets)
