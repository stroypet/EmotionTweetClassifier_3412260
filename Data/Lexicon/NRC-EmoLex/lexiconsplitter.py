lex = open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt')
for i, line in enumerate(lex):
	if 'anger\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/ang.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'anticipation\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/ant.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'disgust\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/dis.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'fear\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/fea.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'joy\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/joy.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'negative\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/neg.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'positive\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/pos.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'sadness\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/sad.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'surprise\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/sur.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()
	if 'trust\t1' in line:
		f=open('/Users/stroypet/PycharmProjects/EmotionTweetClassifier_3412260/Data/Lexicon/NRC-EmoLex/tru.txt','a')
		f.write(line.split()[0] + "\n")
		f.close()