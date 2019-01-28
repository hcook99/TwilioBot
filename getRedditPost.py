import praw
from random import randint

reddit = praw.Reddit(client_id='************',
                     client_secret='******************',
                     user_agent='*********')


def getRedditPost(subReddit):
    listOfPost = reddit.subreddit(subReddit).hot(limit=100)
    randNum = randint(0,99)
    postTemp =[]

    for postCon in listOfPost:
        postTemp.append(postCon)

    post = postTemp[randNum]

    while('imgur' in post.url) or len(post.selftext)+len(post.title)>1600:
        randNum = randint(0, 99)
        post=postTemp[randNum]

    if ('.jpg' or '.png') in post.url:
        return post.title+"(#)"+post.url
    
    else: 
        return post.title + "\n" + post.selftext

