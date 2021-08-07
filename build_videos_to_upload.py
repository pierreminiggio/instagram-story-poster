from build_video import build_video
from get_video_duration import get_video_duration
from get_file_name_from_video_url import get_file_name_from_video_url
from get_video_folder_path import get_video_folder_path
import os
from typing import List

def build_videos_to_upload(video_url: str, video_path: str) -> List[str]:

    duration = get_video_duration(video_path)
    video_min_duration = 7
    video_max_duration = 15

    if duration < video_min_duration:
        return []

    if duration <= video_max_duration:
        return [video_path]

    videos_to_upload = []
    video_folder_path = get_video_folder_path()
    downloaded_video_file_name = get_file_name_from_video_url(video_url)

    number_of_videos_to_build = int(duration // video_max_duration) + 1
    for video_to_build_key in range(number_of_videos_to_build):
        start_time = video_to_build_key * video_max_duration
        end_time = start_time + video_max_duration

        if end_time > duration:
            end_time = duration

        clip_duration = end_time - start_time
        if clip_duration < video_min_duration:
            start_time = end_time - video_min_duration


        video_to_build_path = video_folder_path + os.path.sep + downloaded_video_file_name + '_' + str(start_time).replace('.', '-') + '_' + str(end_time).replace('.', '-') + '.mp4'
        build_video(video_path, video_to_build_path, start_time, video_max_duration)
        videos_to_upload.append(video_to_build_path)

    return videos_to_upload
