from moviepy.editor import VideoFileClip, vfx

def speed_up_raw(source, factor):
    inverted_clip = (VideoFileClip(source).fx(vfx.speedx, factor=factor))
    return inverted_clip

def speed_up(source, factor):
    inverted_clip = source.fx(vfx.speedx, factor=factor)
    return inverted_clip