# Import everything needed to edit video clips
from moviepy.editor import *

def add_audio(source, audio_track):
    source.set_audio(audio_track)
    return source