#RUN FIRST:
#pip install -r requirements.txt

from pytube import YouTube
import os
import requests
import sys
from PIL import Image


os.system("cls")
print("   YouTube Video Downloaded by Robby ")
print("-----------------V1.1-------------------")

path=os.path.dirname(os.path.abspath(__file__))
link="https://www.youtube.com/watch?v="
ID = input("Enter Video ID or Link: ")

if ID.startswith("https"):
    ID = ID
else:
    ID = link + ID

total = f"   YouTube Video Downloaded by Robby \n-----------------V1.1-------------------\nEnter Video ID or Link: {str(ID)}"


try: 
    yt = YouTube(ID) 
except: 
    print("An error has occured, please try again. (Fetching Video from YouTube)")
    sys.exit(1)

try: 
    print("Downloading Thumbnail...")
    thumbnail = yt.thumbnail_url
    data = requests.get(thumbnail).content
    name = str(yt.title) + ".png"
    f = open(name,'wb')
    f.write(data)
    f.close()
except:
    print("Could not get thumbnail for video, please try again.")
    sys.exit(1)

try: 
    os.system("cls")
    print(total)
    print("Downloading Thumbnail...")
    print("Downloading Video...")

    yt = yt.streams.get_highest_resolution()
    filename=yt.title+".mp4"
    yt.download(output_path=path, filename=filename) 
    
except:
    print("An error has occured, please try again. (Video)") 
    sys.exit(1)

print(f'Video {yt.title} with ID {ID} has downloaded with it\'s thumbnail!') 