from pytube import YouTube
link = input("ENTER THE LINK")
yt = YouTube(link)

print("title: ", yt.title)
print("number of views: ",yt.views)
ys = yt.streams.get_highest_resolution()

print("downloading....")
ys.download()
print("Download complete")