import datetime, time, codecs, pytz, twitter, io, json

api = twitter.Api(consumer_key = 'h0rZYPs6iDq4orLJzBLJ0iFYl', consumer_secret = 'y6A4U5QsfdIRzbbUNY493d696BmSVZdb4NPHRvPNp8jFpzduI4',access_token_key = '3414398440-4mTyg8QLeBuovdW8ZoOQYJOhAPmMjPynfi927HQ',access_token_secret = 'oeoXapgN6EUnUYm7Ee0ZbvddXdMLFImoany0tEmm8Xwhy')

inp = raw_input("Enter the term to search for-->")
tlang = raw_input("Language-->")
num = raw_input("Number of search terms-->")
results = api.GetSearch(term = inp, lang = tlang, count = num, include_entities=True)

if (tlang == "en"):
    target_file = open('english.txt', 'a')
elif (tlang == 'de'):
    target_file = io.open('german.txt', 'a', encoding='utf-8')
elif (tlang == 'ru'):
    target_file = io.open('russian.txt','a', encoding='utf-8')

data = {}

for tweet in results:
    data['id'] = str(tweet.id)
    data['text'] = tweet.text
    data['lang'] = tlang
    date = str(tweet.created_at)
    fmt = "%Y-%m-%d %H:%M:%S"
    temp = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
    #print str(temp).replace("+00:00", "")
    data['created_at'] = str(temp).replace("+00:00", "")
    hashtag = []
    for i in tweet.hashtags:
        hashtag.append(i.text)
    data['twitter_hashtags'] = hashtag
    urlz = []
    for j in tweet.urls:
        urlz.append(j.url)
    data['twitter_urls'] = urlz
    if (tlang != 'en'):
        target_file.write(unicode(json.dumps(data, ensure_ascii=False)) + '\n')
    else:
        target_file.write(str(data) + '\n')

target_file.close()
