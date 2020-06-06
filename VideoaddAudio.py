from moviepy.editor import VideoFileClip


fg_video_path = "Audio.mp4"

def from_video_get_mp3():
    video = VideoFileClip(fg_video_path)
    audio = video.audio
    name = fg_video_path.split('.', 1)[0] + ".mp3"
    audio.write_audiofile(name)
    return name


def add_mp3(video_have_zm):
    fg_video = VideoFileClip(fg_video_path)
    video = VideoFileClip(video_have_zm)
    audio = fg_video.audio
    videoclip2 = video.set_audio(audio)
    name1 = video_have_zm.split('.', 1)[0] + "_out.mp4"
    videoclip2.write_videofile(name1)


if __name__ == '__main__':
    add_mp3('demo.mp4')
