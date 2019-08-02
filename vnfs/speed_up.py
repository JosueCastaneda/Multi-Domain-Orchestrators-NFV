from moviepy.editor import VideoFileClip, vfx

def speed_up_raw(source, factor):
    speed_clip = (VideoFileClip(source).fx(vfx.speedx, factor=factor))
    return speed_clip

def speed_up(source, factor):
    speed_clip = source.fx(vfx.speedx, factor=factor)
    return speed_clip