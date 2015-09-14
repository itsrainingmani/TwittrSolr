from TwitterSearch import *

try:
	hashtag = raw_input("Enter the keyword-->")
	lang = raw_input("enter the target language-->")
	num_tweets = int(raw_input("How many tweets do you want?-->"))
	print "Starting the tweet scraping"
	tso = TwitterSearchOrder()
	tso.set_keywords([hashtag])
	tso.set_language(lang)
	tso.set_include_entities(False)
	if (lang == "en"):
		target_file = open('english.txt', 'w')
	elif (lang == 'de'):
		target_file = open('germantweets.txt', 'a')
	elif (lang == 'ru'):
		target_file = open('russiantweets.txt', 'a')

	print "Authenticating"
	ts = TwitterSearch(consumer_key = 'h0rZYPs6iDq4orLJzBLJ0iFYl', consumer_secret = 'y6A4U5QsfdIRzbbUNY493d696BmSVZdb4NPHRvPNp8jFpzduI4',access_token = '3414398440-4mTyg8QLeBuovdW8ZoOQYJOhAPmMjPynfi927HQ',access_token_secret = 'oeoXapgN6EUnUYm7Ee0ZbvddXdMLFImoany0tEmm8Xwhy')

	todo = True
	i = 1
	for tweet in ts.search_tweets_iterable(tso):
		if (i > num_tweets):
			break
		#target_file.write(str(tweet) + '/n')
		print tweet['user']
		#print str(tweet['id']) + "|" + str(tweet['lang']) + "|" + tweet['text'] + "|" + str(tweet['statuses']['created_at'])
		#target_file.flush()
		i = i+1
	print "All snazziness complete"
	target_file.close()

except TwitterSearchException as e:
	print e
