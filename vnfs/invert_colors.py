from moviepy.editor import *

def invert_colors(source):
    inverted_clip = (VideoFileClip(source).fx(vfx.invert_colors))
    return inverted_clip