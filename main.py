# Import everything needed to edit video clips
from moviepy.editor import *
from skimage.filters import gaussian
from vnfs import annotate
from vnfs import crop
from vnfs import transcoder_mp4
from vnfs import transcoder_avi
from vnfs import transcoder_web
from vnfs import concatenate
from vnfs import invert_colors
from vnfs import resize_video
from vnfs import speed_up
from vnfs import split_merge

def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian(image.astype(float), sigma=2)

original_file = "small.mp4"
# # Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
# clip = VideoFileClip(original_file)
#
# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("My Holidays 2013", fontsize=70, color='white')
#
# # Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(3)
#
# # Overlay the text clip on the first video clip
# video = CompositeVideoClip([clip, txt_clip])
#
# # Write the result to a file (many options available !)
# video.write_videofile("myHolidays_edited.webm")
#
# clip_blurred = clip.fl_image( blur )
# clip_blurred.write_videofile("blurred_video.mp4")

if __name__ == '__main__':
    original_file = "small.mp4"
    annotated_clip = annotate.annotate(original_file, "Hola", 5)
    crop_clip = crop.crop(original_file, 2, 4)
    concatenate_clip = concatenate.concatenate(annotated_clip, crop_clip)
    inverted_clip = invert_colors.invert_colors(original_file)
    resized_clip = resize_video.resize_video(original_file, 300, 200)
    speed_clip = speed_up.speed_up_raw(original_file, 2)
    # split_clip = split_merge.split_merge(original_file, 3)

    transcoder_mp4.transcoder_mp4(annotated_clip, "annotated")
    transcoder_mp4.transcoder_mp4(crop_clip, "crop")
    transcoder_mp4.transcoder_mp4(concatenate_clip, "concatenated")
    transcoder_mp4.transcoder_mp4(inverted_clip, "inverted")
    transcoder_mp4.transcoder_mp4(resized_clip, "resized")
    transcoder_mp4.transcoder_mp4(speed_clip, "speed")
    # transcoder_avi.transcoder_avi(annotated_clip, "annotated")
    transcoder_web.transcoder_web(annotated_clip, "annotated")

    # transcoder_mp4.transcoder_mp4(split_clip, "split")
