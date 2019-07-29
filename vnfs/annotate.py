from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


def annotate(source, text, duration=2, font_size=50, color="white"):

    main_clip = VideoFileClip(source)

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip(text, fontsize=font_size, color=color)

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(duration)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([main_clip, txt_clip])
    return video