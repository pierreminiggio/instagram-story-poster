import os

def get_video_folder_path() -> str:
    video_folder_path = 'videos'

    if os.path.exists(video_folder_path) == False:
        os.makedirs(video_folder_path)

    return video_folder_path