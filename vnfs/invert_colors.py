from moviepy.editor import VideoFileClip, vfx

def invert_colors(source):
    inverted_clip = (VideoFileClip(source).fx(vfx.invert_colors))
    return inverted_clip