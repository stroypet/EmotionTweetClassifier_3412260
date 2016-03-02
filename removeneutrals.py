bad_words = ['neutral']

with open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/ML-ONLY-task9-NILC_USP-B-twitter-constrained.output') as oldfile, open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/ML-PRUNED-NEUTRALS.txt', 'w') as newfile, open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/JOINED_GOLD_TEST_DATA.txt') as checkfile:
    for line1, line2 in zip(oldfile, checkfile):
        if not any(bad_word in line1 for bad_word in bad_words):
            newfile.write(line2)