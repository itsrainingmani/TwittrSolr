from twython import Twython

APP_KEY = "h0rZYPs6iDq4orLJzBLJ0iFYl"
APP_SECRET = "y6A4U5QsfdIRzbbUNY493d696BmSVZdb4NPHRvPNp8jFpzduI4"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token = ACCESS_TOKEN)
tag = raw_input("Enter the term to search for-->")
results = twitter.cursor(twitter.search, q=tag)

target = open("TwittrSolrData.txt", 'a')
#target = open("TwittrSolrData.txt", 'a') For appending to the file

#number_of_tweets = raw_input("Enter the number of tweets that you want to collect-->")
i = 0

key = raw_input("Enter the key-->")
for result in results:
    #target.write(result)
    #target.write('\n')
    print result
    target.write(str(result[key]).encode("utf-8") + '\n')
    #target.write(str(result) + '\n')
    i = i+1
    if (i > 4):
		break

#print "File has been written to"
twitter.disconnect()
target.close()
