import praw
import os 
import pprint
import requests 
from requests import get
import os, random
import ctypes

tags = ['<', '>', '/', '|', '\\','*'," "]
#Function to download the image 
def download(url, file_name):
    response = get(url)
    with open(file_name, "wb") as file:
        file.write(response.content)


DLFolder="D:\\WallpapersScraped"  #Change the folder where you want the images to be downloaded to
try:
    os.makedirs(DLFolder)
except:
    pass 
reddit = praw.Reddit(client_id='', #Fill in the details here
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')
print(reddit.user.me())

submissions=reddit.subreddit('wallpaper').hot(limit=15) #Change wallpaper to any walllpaper subreddit of choice 

for submission in submissions:
    if (".jpg" in submission.url): 
        durl=submission.url
        fname=submission.title
        for tag in tags:
            fname = fname.replace(tag, " ")
        fnamewithdir=DLFolder+"\\"+fname+".jpg" 
        download(durl, fnamewithdir)
    elif (".png" in submission.url):  
        durl=submission.url
        fname=submission.title
        for tag in tags:
            fname = fname.replace(tag, "")
        fnamewithdir=DLFolder+"\\"+fname+".png" 
        download(durl, fnamewithdir)		
    else:
	    continue	
#Randomly Select an image from the Directory 		
rand=random.choice(os.listdir(DLFolder))
image_path=DLFolder+"\\"+rand 
print(image_path)

#To change the wallpaper
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

	
