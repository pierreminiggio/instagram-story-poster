import base64
from get_file_name_from_video_url import get_file_name_from_video_url
from get_video_folder_path import get_video_folder_path
import os
import requests

def download_video_if_needed(video_url: str, proxy:str = None) -> str:

    video_folder_path = get_video_folder_path()

    video_path = video_folder_path + os.path.sep + get_file_name_from_video_url(video_url) + '.mp4'

    if os.path.isfile(video_path) == False:
        video_download_request = requests.get(video_url, allow_redirects=True, proxies={
            "http": proxy,
            "https": proxy
        } if proxy != None else None)
        open(video_path, 'wb').write(video_download_request.content)

    return video_path