from twython import Twython
import csv

CONSUMER_KEY = 'pb9hqugm8DgPpX4e0hDRvndB9'
CONSUMER_SECRET = 'wbXFYN94IhDX9vjuQdwyF9ALBOxIsEjbioo4bDYUDDhZGynHMs'
ACCESS_TOKEN = '316821018-3veCZGMl2i7XT5OZmAlGT0TwCnkpLbxALmcwTjED'
ACCESS_TOKEN_SECRET = '9WkJuhcsLuJbgBbEu0eiX1nRUjaheLfcUdPZ5yvsmAJ0M'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='Guatemala', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Guatemala', result['text'].encode('utf-8'), url]]
        a.writerows((text))
