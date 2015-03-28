from textblob import TextBlob



def tweet_collector(text):

	blob = TextBlob(text)

	average_positivity = []
	total_positivity = 0

	for sentence in blob.sentences:
	    average_positivity.append(sentence.sentiment.polarity)

	for value in average_positivity:
		total_positivity += value

	ret_val = total_positivity/len(average_positivity)

	return ret_val



