from moviepy.editor import *

def resize_video(source, width, height):
    resized_clip = (VideoFileClip(source).fx(vfx.resize, width=width, height=height))
    return resized_clip