from mastodon import Mastodon
import praw
import sqlite3
from secret import *

m = Mastodon(
	access_token = mastodon_3054_access_token,
	api_base_url = 'https://7.62x54r.ru'
)

r = praw.Reddit(
	client_id = reddit_id,
	client_secret = reddit_secret,
	user_agent = '30-54 post request bot version 0.2'

)

db_connection = sqlite3.connect('shitbot.db')
db = db_connection.cursor()

reddit_domain = 'https://old.reddit.com'

tooted_reddit_post_ids = []

def dump_tooted_reddit_post_ids():
	dump_str = ''
	for item in tooted_reddit_post_ids:
		dump_str += item + ' '
	with open('tooted_reddit_post_ids.dat', 'w') as f:
		f.write(dump_str)

def load_tooted_reddit_post_ids():
	with open('tooted_reddit_post_ids.dat') as f:
		contents = f.read()
		print (contents)
		loaded_ids = contents.split()
		print (loaded_ids)
		return loaded_ids
		#tooted_reddit_post_ids = loaded_ids

def get_tooted_posts_from_db():
	id_list = []
	query = db.execute('SELECT post_id FROM reddit_posts;')
	for row in query:
		#print (row[0])
		id_list.append(row[0])
	return id_list

def record_reddit_post(reddit_post):
	response = db.execute('INSERT INTO reddit_posts (post_id) VALUES ("' + reddit_post + '");')
	db_connection.commit()
	#for line in response:
	#	print (line)
	return response

# Unnecessary, I was reading the printed output wrong
def strip_sql_wrappers(sql_output):
	output_list = []
	for entry in sql_output:
		entry.replace("('", "")
		entry.replace("')", "")
		output_list.append(entry)
		print(entry)

def get_subreddit_posts(sub_name, min_score = 50):
	#for i in tooted_reddit_post_ids: print (i)
	for submission in r.subreddit(sub_name).hot(limit = 10):
		print (submission.title + '\n    ' + submission.id + '\n    ' + reddit_domain + submission.permalink)
		if min_score <= submission.score:
			if submission.id not in tooted_reddit_post_ids:
				m.toot('New post on r/' +  sub_name  + ':\n' +
					submission.title + '\n'
					+ reddit_domain + submission.permalink + '\n'
					'#rslash' + sub_name
				)
				tooted_reddit_post_ids.append(submission.id)
				record_reddit_post(submission.id)
	#dump_tooted_reddit_post_ids()

if __name__ == '__main__':

#shitbot's first post, leave commented
#m.toot('Hello, world!')

	tooted_reddit_post_ids = get_tooted_posts_from_db() #load_tooted_reddit_post_ids()

	get_subreddit_posts('Firearms')
	get_subreddit_posts('BrandonHerrara')
	get_subreddit_posts('2aLiberals')
	get_subreddit_posts('LiberalGunOwners')
	get_subreddit_posts('DGU')
	get_subreddit_posts('GunPolitics')
	get_subreddit_posts('ProGun')
	get_subreddit_posts('1022')
	get_subreddit_posts('1911')
	get_subreddit_posts('AR15')
	get_subreddit_posts('AK47')
	get_subreddit_posts('OpenCarry')
	get_subreddit_posts('SocialistRA')
	get_subreddit_posts('SRAweekend')
	get_subreddit_posts('LiberalGunRetards')
	get_subreddit_posts('NFA')
	get_subreddit_posts('JewishGuns')
	get_subreddit_posts('Hunting')
	get_subreddit_posts('HomeDefense')
	get_subreddit_posts('ForgottenWeapons')
	get_subreddit_posts('CZfirearms')
	get_subreddit_posts('HecklerKoch')
	get_subreddit_posts('Makarov')
	get_subreddit_posts('SpringfieldArmory')
	get_subreddit_posts('Ruger')
	get_subreddit_posts('Beretta')
	get_subreddit_posts('Glocks')



#for submission in r.subreddit('brandonherrara').hot(limit=15):
#	print (submission.title + '\n    ' + submission.id + '\n    ' + submission.permalink)

db.close()