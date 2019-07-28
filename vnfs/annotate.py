#This VNF annotates video with text
# Import everything needed to edit video clips
from moviepy.editor import *


def annotate(source, text, duration):

    main_clip = VideoFileClip(source)

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip(text, fontsize=50, color='white')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(duration)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([main_clip, txt_clip])
    return video