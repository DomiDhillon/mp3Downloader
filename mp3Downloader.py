# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:31:02 2023

@author: DomiDhillon
"""

from pytube import YouTube
import argparse
import os

def mp3Downloader(url, filename=None, directory=None):
    url = url
    
    try:
        # create a youtube object
        video = YouTube(url)
        
        #filter out streams we don't need & select the first stream available
        stream = video.streams.filter(only_audio=True).first()
        
        #filename.. annoying if special characters
        if not filename:
            filename=f"{video.title}.mp3"
            
            #remove any special characters (and white space) if they are in it:
            filename=''.join([ c  for c in filename if (c.isalnum()) | (c=="_") | (c==".")])
                
        else:
            filename=filename+'.mp3'
        
        #if directory specified, add it to the path
        if directory:
            filename=os.path.join(directory, filename)
        
        #dwn audio
        stream.download(filename=filename)
        if directory:
            print(f"The MP3 is downloaded in {os.path.split(filename)[0]}")
        else:
            print(f"The MP3 is downloaded in {os.getcwd()}")
    
    #excpet the url is wrong
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")



if __name__=='__main__':
    #create arguments to parse
    parser = argparse.ArgumentParser(usage="Gimme youtube link, and select where to store the music.")
    parser.add_argument("url", type=str, help="Youtube link")
    parser.add_argument("--filename", type=str)
    #add option to select WHERE (pop up)
    parser.add_argument("--directory", type=str, default=None)   
    
    #parse the arguments
    args=parser.parse_args()
    
    #run code
    mp3Downloader(url=args.url,
                  filename=args.filename,
                  directory=args.directory)
    
    ##old version
    # url = "https://www.youtube.com/watch?v=gEQHhMNxr3Q"
    # mp3Downloader(url, filename=None)
    
    
    
