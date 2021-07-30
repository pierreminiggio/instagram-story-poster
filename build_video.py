import datetime
import os

def build_video(video_path: str, video_to_build_path: str, start_time: float, duration: float):
    if os.path.isfile(video_to_build_path) == False:
        os.system(
            'ffmpeg -ss '
            + str(datetime.timedelta(seconds=start_time))
            + ' -i '
            + video_path
            + ' -to '
            + str(datetime.timedelta(seconds=duration))
            + ' -c copy '
            + video_to_build_path
        )