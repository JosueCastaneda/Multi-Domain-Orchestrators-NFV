from moviepy.editor import VideoFileClip

def crop(source, initial_time, end_time):
    clip = VideoFileClip(source)
    clip_cropped = clip.subclip(initial_time, end_time)
    return clip_cropped
