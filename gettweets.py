import sys, os
import twitter
from pprint import pprint
from time import sleep

def scrapeTweetsFromPublicStream():
	pass

def gettweetsfromfile(filename):
	api = twitter.Api(consumer_key='CbCL6QCau7DcVcEebAD8iQwVI',
		consumer_secret='yuZZyBjaMDWA7WgNLkwIYl4j5aiq33Jtq6KaTedFprAJSN916i',
		access_token_key='798741552424099840-eTcd1voITUaC6bDppSJfIc4h3fr1Yat',
		access_token_secret='hbrTGlXnu4WilRcNxLZhIaHTnzdqWb2U89czXuKJeXal4')

	api.VerifyCredentials() #to debug

	print("\n\nGetting tweets...")
	print("You will see some SSL errors..ignore them\n")
	sleep(2)

	outfile = open("out", "w")

	linecnt = 0
	skippedlines = []

	for line in open(filename, "r"):
		linecnt+=1
		conversation = []
		for id in line.split():		
			try:
				tweet = api.GetStatus(status_id=id)
				#print("\n>> FOUND TWEET AT ID..."+str(id)+"<<\n")
				conversation.append(tweet)

			except twitter.error.TwitterError as e:
				skippedlines.append(linecnt)
				if e.message[0]['message']:
					if "Rate limit" in e.message[0]['message']:
						print("Rate limit exceeded..wait 15 minutes.")
						sleep(15*60+5)
					elif "No status found with that ID" in e.message[0]['message']:
						print("\n>> "+id+" tweet doesn't exist<<\n")
					else:
						print(e)
					break			

		#if len(conversation) < 3 and len(conversation) > 0:
		#	outfile.write(">>> Something missing here! <<<")
		#	outfile.write(conversation[0].id_str)

		if len(conversation) == 3:
			outfile.write("\n\n")
			for t in conversation:
				try:
					outs = "%20s: %s\n" %(t.user.screen_name, t.text)
					outfile.write(outs)
				except UnicodeError:
					outfile.write(">>> this tweet or user has a non-ascii character <<<")
					outs = "".join(i for i in outs if ord(i)<128) #remove nonAscii
					outfile.write(outs)

	outfile.write("Skipped "+str(len(skippedlines))+" lines")

if __name__ == "__main__":
	try:
		if os.exist(sys.argv[1]):
			gettweetsfromfile(sys.argv[1])
		else:
			scrapeTweetsFromPublicStream()
	except KeyboardInterrupt:
		pass

#########################################
### METHODS FOR A TWITTER STATUS OBJECT
#########################################
'''
        self.param_defaults = {
            'contributors': None,
            'coordinates': None,
            'created_at': None,
            'current_user_retweet': None,
            'favorite_count': None,
            'favorited': None,
            'full_text': None,
            'geo': None,
            'hashtags': None,
            'id': None,
            'id_str': None,
            'in_reply_to_screen_name': None,
            'in_reply_to_status_id': None,
            'in_reply_to_user_id': None,
            'lang': None,
            'location': None,
            'media': None,
            'place': None,
            'possibly_sensitive': None,
            'retweet_count': None,
            'retweeted': None,
            'retweeted_status': None,
            'scopes': None,
            'source': None,
            'text': None,
            'truncated': None,
            'urls': None,
            'user': None,
            'user_mentions': None,
            'withheld_copyright': None,
            'withheld_in_countries': None,
            'withheld_scope': None,
        }
'''


###################################
### EXAMPLE JSON RESPONSE:
###################################
'''
HTTP/1.1 200 OK
x-frame-options:
SAMEORIGIN
x-rate-limit-remaining:
898
last-modified:
Sun, 27 Nov 2016 18:23:03 GMT
status:
200 OK
Content-Length:
2208
x-response-time:
102
Connection:
keep-alive
x-transaction:
004798080052f4a9
Server:
tsa_b
pragma:
no-cache
cache-control:
no-cache, no-store, must-revalidate, pre-check=0, post-check=0
x-connection-hash:
3e9749204035caa492e39f48bffd0d2c
x-xss-protection:
1; mode=block
x-content-type-options:
nosniff
x-rate-limit-limit:
900
expires:
Tue, 31 Mar 1981 05:00:00 GMT
Date:
Sun, 27 Nov 2016 18:23:03 GMT
set-cookie:
lang=en; Path=/
set-cookie:
guest_id=v1%3A148027098337324941; Domain=.twitter.com; Path=/; Expires=Tue, 27-Nov-2018 18:23:03 UTC
x-rate-limit-reset:
1480271519
content-disposition:
attachment; filename=json.json
x-twitter-response-tags:
BouncerCompliant
strict-transport-security:
max-age=631138519
x-access-level:
read-write-directmessages
Content-Type:
application/json;charset=utf-8

{
  "created_at": "Tue Jun 26 21:50:30 +0000 2012",
  "id": 217736622647676930,
  "id_str": "217736622647676928",
  "text": "@MiaBiersack good thanks, you?",
  "truncated": false,
  "entities":  {
    "hashtags":  [],
    "symbols":  [],
    "user_mentions":  [],
    "urls":  []
  },
  "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user":  {
    "id": 509221062,
    "id_str": "509221062",
    "name": "Josh ",
    "screen_name": "JoshBrett6",
    "location": "Somerset, UK",
    "description": "20 | Summer is my life ",
    "url": null,
    "entities":  {
      "description":  {
        "urls":  []
      }
    },
    "protected": false,
    "followers_count": 443,
    "friends_count": 505,
    "listed_count": 3,
    "created_at": "Wed Feb 29 20:48:58 +0000 2012",
    "favourites_count": 550,
    "utc_offset": 0,
    "time_zone": "London",
    "geo_enabled": false,
    "verified": false,
    "statuses_count": 3545,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FCEBB6",
    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/719716932/20cf729dad8fa42e71bfa3c34c6d1e2e.jpeg",
    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/719716932/20cf729dad8fa42e71bfa3c34c6d1e2e.jpeg",
    "profile_background_tile": true,
    "profile_image_url": "http://pbs.twimg.com/profile_images/577451340261126144/vxw9BfVj_normal.jpeg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/577451340261126144/vxw9BfVj_normal.jpeg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/509221062/1426869102",
    "profile_link_color": "CE7834",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "78C0A8",
    "profile_text_color": "5E412F",
    "profile_use_background_image": true,
    "has_extended_profile": false,
    "default_profile": false,
    "default_profile_image": false,
    "following": false,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "none"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
'''