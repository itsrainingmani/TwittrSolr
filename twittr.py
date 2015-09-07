from twython import Twython

APP_KEY = "h0rZYPs6iDq4orLJzBLJ0iFYl"
APP_SECRET = "y6A4U5QsfdIRzbbUNY493d696BmSVZdb4NPHRvPNp8jFpzduI4"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token = ACCESS_TOKEN)
results = twitter.cursor(twitter.search, q='#DeflateGate')

target = open("TwittrSolrData.txt", 'w')
#target = open("TwittrSolrData.txt", 'a') For appending to the file

i = 0
key = raw_input("Enter the key-->")
for result in results:
    #target.write(result)
    #target.write('\n')
    print result
    target.write(str(result[key]) + '\n')
    #target.write(str(result) + '\n')
    i = i+1
    if (i > 1):
		break
    
#print "File has been written to"
target.close()
