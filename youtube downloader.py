#youtube downloader with python

#ibrabries used in this project


from pytube import YouTube

link = "https://www.youtube.com/watch?v=PGwXZqviGyg"
youTube = YouTube(link)

print(youTube.title)
print(youTube.thumbnail_url)

#videos = youTube.streams.all()# all format
videos = youTube.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in (vid):
    print(i)
print()
strm = int(input("enter :  "))
videos[strm].download()
print("succesfully")

# downloading complete playlist
'''from pytube import Playlist

links = Playlist("https://www.youtube.com/watch?v=q_BzsPxwLOE&list=PLeo1K3hjS3uuZPwzACannnFSn9qHn8to8")
print(f"downaload : {links.title}")

for video in links.videos :
    video.streams.first().download()'''


