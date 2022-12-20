#!/bin/python

from pytube import YouTube
import sys # another way (from sys import argv) 


link = sys.argv[1]

yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('../Downloads')

print("Download completed")
