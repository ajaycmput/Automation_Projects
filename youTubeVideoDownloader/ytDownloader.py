# To download from youtube, run from command line,
# enter python3 youtubeDownloader.py "<youtubeLink>"

# import Youtube class from pytube library
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link) #create youube object from YouTube class

# download video
yd = yt.streams.get_highest_resolution().download('C:/Users/ajayd/OneDrive/Desktop/PythonAutomation')

file = open("Out.txt", "w")
file.write(str(yt.title))
file.write("\n")
file.write(str(yt.views))

file.close()

