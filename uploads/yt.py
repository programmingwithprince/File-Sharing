from pytube import YouTube
import os
path="/storage/emulated/0/Documents/Pydroid3/instatube/"
tax= '''#℅{}\<>*?/$!'":@+`|='''
sample ='this is a text message | text message / hggf #going'
for i in range(len(tax)):
	sample=sample.replace(tax[i],'')
print(sample)	
def main(link):
    yt = YouTube(link)
    video= yt.streams.filter(only_audio=False).first()
    print(video.title)
    title=video.title
    for i in range(len(tax)):
    	title=title.replace(tax[i],'')
    print("starting download!")
    video.download(path)
    os.rename(f"{path}{title}.mp4",f"{path}{title}.mp3")    
   
link=input("link:  ")
main(link)
print("Downloaded sucessfully!")