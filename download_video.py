import base64
from get_file_name_from_video_url import get_file_name_from_video_url
from get_video_folder_path import get_video_folder_path
import os
import requests

def download_video_if_needed(video_url: str, proxy:str = None) -> str:

    video_folder_path = get_video_folder_path()

    video_path = video_folder_path + os.path.sep + get_file_name_from_video_url(video_url) + '.mp4'

    if os.path.isfile(video_path) == False:
        video_download_request = requests.get(
            video_url,
            allow_redirects=True,
            timeout=60,
            proxies={
                "http": proxy,
                "https": proxy
            } if proxy != None else None
        )

        if video_download_request.status_code != 200:
            raise Exception(
                'Failed to download video from ' + video_url
                + ' (status code ' + str(video_download_request.status_code) + ')'
            )

        if len(video_download_request.content) == 0:
            raise Exception('Downloaded video from ' + video_url + ' is empty')

        open(video_path, 'wb').write(video_download_request.content)

    return video_path