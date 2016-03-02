# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals

import codecs

class EmotionClassifier(object):

    # Constructor
    def __init__(self):
        self.ang_words = []
        self.ant_words = []
        self.dis_words = []
        self.fea_words = []
        self.joy_words = []
        self.sad_words = []
        self.sur_words = []
        self.tru_words = []

        with codecs.open('./Data/Lexicon/NRC-EmoLex/ang.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.ang_words = [w for w in words if not w.startswith(';')]
        #self.ang_words.remove('')
        self.ang_words = {k:1 for k in self.ang_words}

        # read anticipation words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/ant.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.ant_words = [w for w in words if not w.startswith(';')]
        #self.ant_words.remove('')
        self.ant_words = {k:1 for k in self.ant_words}

        # read disgust words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/dis.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.dis_words = [w for w in words if not w.startswith(';')]
        #self.dis_words.remove('')
        self.dis_words = {k:1 for k in self.dis_words}

        # read fear words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/fea.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.dis_words = [w for w in words if not w.startswith(';')]
        #self.fea_words.remove('')
        self.fea_words = {k:1 for k in self.fea_words}

        # read joy words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/joy.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.joy_words = [w for w in words if not w.startswith(';')]
        #self.joy_words.remove('')
        self.joy_words = {k:1 for k in self.joy_words}

        # read sad words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/sad.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.sad_words = [w for w in words if not w.startswith(';')]
        #self.sad_words.remove('')
        self.sad_words = {k:1 for k in self.sad_words}

        # read surprise words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/sur.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.sur_words = [w for w in words if not w.startswith(';')]
        #self.sur_words.remove('')
        self.sur_words = {k:1 for k in self.sur_words}

        # read anger words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/ang.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.ang_words = [w for w in words if not w.startswith(';')]
        #self.ang_words.remove('')
        self.ang_words = {k:1 for k in self.ang_words}

        # read trust words
        with codecs.open('./Data/Lexicon/NRC-EmoLex/ang.txt', 'r', encoding='utf8') as f:
            words = f.read().splitlines()
        self.tru_words = [w for w in words if not w.startswith(';')]
       #self.tru_words.remove('')
        self.tru_words = {k:1 for k in self.tru_words}

        # http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary

    def classify(self, tweet_tokens):
        ang_so = 0
        ant_so = 0
        dis_so = 0
        joy_so = 0
        fea_so = 0
        sad_so = 0
        sur_so = 0
        tru_so = 0
        tweet_tokens = [w.lower() for w,tag in tweet_tokens]
        for i,w in enumerate(tweet_tokens):
            # search for hashtags
            # it is a better signal for polarity than common sentiment words in tweet
            if w in self.ang_words:
                ang_so += 1
            if w in self.ant_words:
                ant_so += 1
            if w in self.dis_words:
                dis_so += 1
            if w in self.fea_words:
                fea_so += 1
            if w in self.joy_words:
                joy_so += 1
            if w in self.sad_words:
                sad_so += 1
            if w in self.sur_words:
                sur_so += 1
            if w in self.tru_words:
                tru_so += 1
        return (ang_so,ant_so,dis_so,fea_so,joy_so,sad_so,sur_so,tru_so)