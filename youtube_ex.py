# from pytube import YouTube
# YouTube("https://www.youtube.com/watch?v=fyMj73zcn3Y&t=1s"
#     ).streams.filter(progressive=True, file_extension='mp4').first().download()



# from pytube import YouTube
# YouTube("https://www.youtube.com/watch?v=fyMj73zcn3Y&t=1s"
#     ).streams.filter(file_extension='mp4').get_by_resolution('720p').download()


# from pytube import YouTube
# YouTube("https://www.youtube.com/watch?v=fyMj73zcn3Y&t=1s"
#     ).streams.filter(file_extension='mp4').get_highest_resolution().download()

# from pytube import YouTube
# YouTube("https://www.youtube.com/watch?v=fyMj73zcn3Y&t=1s"
#     ).streams.filter(only_audio=True).first().download(filename="strell_cbr_650.mp3")

# from pytube import Playlist

# p = Playlist('https://www.youtube.com/watch?v=Li2y1-xwMfM&list=PL0dHyj2mC0eR67uR4mD8CUEzYhaMW-2ZK')

# for video in p.videos:
#     print(video.title)


from pytube import Playlist

p = Playlist('https://www.youtube.com/watch?v=Li2y1-xwMfM&list=PL0dHyj2mC0eR67uR4mD8CUEzYhaMW-2ZK')

for video in p.videos[:3]:
    video.streams.first().download()

