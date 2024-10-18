from __future__ import unicode_literals

import youtube_dl

import subprocess, os, json, time

from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from selenium import webdriver

from youtube_uploader_selenium import YouTubeUploader

#export PATH=$PATH:/Users/aman/Documents/real-time-video-automation-system/exporter

def scrap():
    presentday = datetime.now() # or presentday = datetime.today()
    
    tomorrow = presentday + timedelta(1)
    yesterday = presentday + timedelta(-1)

    #today
    #url = f"https://clipsgamelab.github.io/#/clips/games/Just%20Chatting/{presentday.strftime('%Y-%m-%d')}T00:00:00.000Z/{tomorrow.strftime('%Y-%m-%d')}T00:00:00.000Z"

    #yesterday
    url = f"https://clipsgamelab.github.io/#/clips/games/Just%20Chatting/{yesterday.strftime('%Y-%m-%d')}T00:00:00.000Z/{presentday.strftime('%Y-%m-%d')}T00:00:00.000Z"

    browser = webdriver.Chrome('/Users/aman/chromedriver-mac-x64/chromedriver')  # Optional argument, if not specified will search path.
    
    browser.get(url)

    doc = BeautifulSoup(browser.page_source,'html.parser')
    browser.close()

    all_links = doc.find(['div'], class_='card-deck pt-4')

    links_list = [a['href'] for a in all_links.find_all(['a'], string='twitch', href=True)]

    #links_list = {a['href']:a['title'] for a in all_links.find_all(['a'], string='twitch')}

    links_list = ['https://clips.twitch.tv' + link[link.find("/",23)+5:] for link in links_list]

    return links_list
 
def download(url):
    #PATH = '/Users/aman/Documents/mreal-time-video-automation-system/youtubefiles'
    ydl_opts = {
        'format': 'best[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': './youtubefiles/E'+'%(title)s'+'@'+'%(creator)s'+'.mp4',
        'nocheckcertificate': True,
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        return [filename, info['title'], info['creator']]

def write_log(links_list):
    print("Writing list to logs.txt")
    with open('logs.txt', 'w') as output:
        for link in links_list:
            output.write('%s\n' % link[24:])

def read_logs():
    old_links = open('logs.txt').read().splitlines()
    return old_links

def upload(new_links, old_links):
    for link in new_links:
        if link[24:] not in old_links:
            print('Downloading: ' + link)
            video_path = download(link)
            print(video_path)
            video_info = {
                'title': f"{video_path[1]}... ({video_path[2]})",
            }
            video_json = json.dumps(video_info)

            with open("metadata_path.json", "w") as outfile:
                outfile.write(video_json)

            json_path = './metadata_path.json'
            path = video_path[0]
            print(path)

            print('Uploading:' + link)
            uploader = YouTubeUploader(path, json_path)
            was_video_uploaded = uploader.upload()

            print("Writing list to logs.txt")
            with open('logs.txt', 'a') as output:
                output.write('%s\n' % link[24:])

            assert was_video_uploaded
        else:
            print('Already Downloaded: ' + link[24:])


def deletevids():
    for filename in os.listdir(path='/Users/aman/Documents/real-time-video-automation-system/exporter/youtubefiles'):
        if filename.endswith('.mp4') and filename[0] == 'E':
            try: 
                os.remove('/Users/aman/Documents/real-time-video-automation-system/exporter/youtubefiles/' + filename)
            except:
                pass
            


new_links = scrap()
old_links = read_logs()
upload(new_links, old_links)
print(new_links, old_links)
deletevids()
