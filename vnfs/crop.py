# Import everything needed to edit video clips
from moviepy.editor import *

def crop(source, initial_time, end_time):
    clip = VideoFileClip(source)
    clip_cropped = clip.subclip(initial_time, end_time)
    return clip_cropped
