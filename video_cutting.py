

from moviepy.editor import VideoFileClip
video = VideoFileClip("strell_cbr_650.mp4").subclip(180, 200)
video.write_videofile("cropped.mp4")
