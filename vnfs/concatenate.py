# Import everything needed to edit video clips
from moviepy.editor import *

def concatenate_raw(first, second):
    first_clip = VideoClip(first)
    second_clip = VideoClip(second)
    final_clip = concatenate_videoclips([first_clip, second_clip])
    return final_clip

def concatenate(first, second):
    final_clip = concatenate_videoclips([first, second])
    return final_clip