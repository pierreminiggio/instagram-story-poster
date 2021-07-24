import base64
import os
import requests

def download_video_if_needed(video_url: str) -> str:

    video_folder_path = 'videos'

    if os.path.exists(video_folder_path) == False:
        os.makedirs(video_folder_path)

    video_path = video_folder_path + os.path.sep + base64.urlsafe_b64encode(video_url.encode()).decode() + '.mp4'

    if os.path.isfile(video_path) == False:
        video_download_request = requests.get(video_url, allow_redirects=True)
        open(video_path, 'wb').write(video_download_request.content)

    return video_path