# Thanks to github subredditarchive repo
# -*- coding: utf-8 -*-
import time
import datetime
import praw
import os
import traceback
import requests

b = "timestamp:"
d = ".."

SCR_CLIENT_ID = os.environ["SCR_CLIENT_ID"]
SCR_CLIENT_SECRET = os.environ["SCR_CLIENT_SECRET"]
SCR_PASSWORD = os.environ["SCR_PASSWORD"]
SCR_USERAGENT = os.environ["SCR_USERAGENT"]
SCR_USERNAME = os.environ["SCR_USERNAME"]

#Config Details
r = praw.Reddit(client_id = SCR_CLIENT_ID,
                client_secret = SCR_CLIENT_SECRET, password = SCR_PASSWORD,
                user_agent = SCR_USERAGENT, username = SCR_USERNAME)

def resume():
    if os.path.exists('config.txt'):
        line = file('config.txt').read()
        startStamp, endStamp, step, subName=line.split(', ')
        startStamp, endStamp, step=int(startStamp), int(endStamp), int(step)
        return startStamp, endStamp, step, subName
    else:
        return 0

choice = input('\nMENU\nPlease choose one of the following:\n1. Start New Archive\n2. Continue Archiving\n3. Exit\n(Input the number)\n')

if choice == 1:
    subName = raw_input('Input the subreddit to archive: ')
    sdate = raw_input('Input start date in the format dd/mm/yyyy: ')
    startStamp = int(time.mktime(datetime.datetime.strptime(sdate,  "%d/%m/%Y").timetuple()))
    edate = raw_input('Input end date in the format dd/mm/yyyy: ')
    endStamp = int(time.mktime(datetime.datetime.strptime(edate,  "%d/%m/%Y").timetuple()))
    step = input('Input seconds between each search,  30 recommended: ')
    obj = file('config.txt', 'w')
    obj.write(str(startStamp) + ', ' + str(endStamp) + ', ' + str(step) + ', ' + str(subName))
    obj.close()

elif choice == 2:
    try:
        startStamp, endStamp, step, subName=resume()
    except:
        print('Nothing to continue.')
        exit()
else:
    exit()


sdate = datetime.datetime.fromtimestamp(int(startStamp)).strftime('%d-%m-%Y')
edate = datetime.datetime.fromtimestamp(int(endStamp)).strftime('%d-%m-%Y')
folderName = str(subName+'_'+str(sdate)+'_'+str(edate))

if not os.path.exists(folderName):
    os.makedirs(folderName)

def getNew(subName, folderName):

    subreddit_comment = r.get_comments(subName,  limit=1000)
    subreddit_posts = r.get_submissions(subName,  limit=1000)

    for comment in subreddit_comment:
        print comment
        url= "https://reddit.com" + comment.permalink
        data= {'user-agent':'archive by /u/healdb'}
        # anually grabbing this file is faster than loading the individual json
        response = requests.get(url+'.json', headers=data)
        # eate a folder called dogecoinArchive before running the script
        filename=folderName+"/"+comment.name
        obj=open(filename,  'w')
        obj.write(response.text)
        obj.close()

    for post in subreddit_posts:
        print ("posted is:", post)
        url1= "https://reddit.com" + post.permalink
        #pprint(vars(post))
        data= {'user-agent':'archive by /u/healdb'}
        #manually grabbing this file is much faster than loading the individual json files of every single comment,  as this json provides all of it
        if submission.id not in already_done:
            response = requests.get(url1+'.json', headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+post.name
            obj=open(filename,  'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            already_done.add(submission.id)
        else:
            continue


def main(startStamp, endStamp, step, folderName, subName, progress):

    count=step

    try:
        startStamp = open(folderName + "/lastTimestamp.txt").read()
        print("Resuming from timestamp: " + startStamp)
        time.sleep(3)
        startStamp = int(startStamp)
        progress = startStamp
    except:
        pass

    c = 1

    for currentStamp in range(startStamp, endStamp, step):
        e = ' --'
        if(c % 2 == 0):
            e=' |'
        f = str(currentStamp)
        g = str(currentStamp+step)
        search_results = r.subreddit(subName).search(b+f+d+g,  syntax='cloudsearch')
        end=str((int((float(count)/float(progress)*20.0))*10)/2) + '%'
        print(('\n'*1000) + 'Archiving posts and comments...\n[' + '*'*int((float(count) / float(progress) * 20.0)) + '_' * (20 - int(float(count) / float(progress) * 20.0)) + ']' + end + e)
        count += step

        for post in search_results:
            #print("---I found a post! It\'s called:" + str(post))
            url = "https://reddit.com" + (post.permalink).replace('?ref=search_posts', '')
            #pprint(vars(post))
            data = {'user-agent':'archive by /u/healdb'}
            #manually grabbing this file is much faster than loading the individual json files of every single comment,  as this json provides all of it
            response = requests.get(url+'.json', headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename = folderName+"/"+post.name+'.json'
            obj = open(filename,  'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            #print("I saved the post and named it " + str(post.name) + " .---")
            time.sleep(1)

        obj = open(folderName+"/lastTimestamp.txt",  'w')
        obj.write(str(currentStamp))
        obj.close()
        c += 1

    print('Welp,  all done here! Stopped at timestamp '+ str(currentStamp))

progress = endStamp - startStamp

while True:
    try:
        main(startStamp, endStamp, step, folderName, subName, progress)
        print("Succesfully got all posts within parameters.")
        choice=input('You can now either\n1. Exit\n2. Get new posts\n(Input the number)\n')
        if(choice == 1):
            exit()
        else:
            while True:
                getNew(subName, folderName)
    except KeyboardInterrupt:
        exit()
    except SystemExit:
        exit()
    except:
        print("Error in the program! The error was as follows: ")
        error = traceback.format_exc()
        time.sleep(5)
        print(error)
        time.sleep(5)
        print("Resuming in 5 seconds...")
        time.sleep(5)
