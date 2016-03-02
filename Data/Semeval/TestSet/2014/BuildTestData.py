import re

with open("/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/ADD_TO_NOUNKWNSSemEval2014-task9-test-B-gold copy.txt") as f1, open("/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/NO_UNKWNS_SemEval2014-task9-test-B-input copy.txt") as f2:
    for line1, line2 in zip(f1, f2):
        f3=open("/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/JOINED_GOLD_TEST_DATA.txt", 'a')
        testline = line2.split("\t")
        line2write = line2.split()[0] + '\t' + line2.split()[1] + '\t' + line1.split()[2] + '\t' + testline[3]
        checkfile=open("/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Semeval/TestSet/2014/SemEval2014-task9-test-B-input.txt")
        checkline = checkfile.readline()
        f3.write(line2write)