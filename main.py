from clean_after_upload import clean_after_upload
from build_videos_to_upload import build_videos_to_upload
from download_video import download_video_if_needed
import json
from upload_story import upload_story
import sys

args = sys.argv

if len(args) != 4 and len(args) != 5:
    print('Use like this : python main.py <username> <password> <video_url> [proxy]')
    sys.exit()

username = args[1]
password = args[2]
video_url = args[3]
proxy = args[4] if 4 in args else None

video_path = download_video_if_needed(video_url, proxy)

videos_to_upload = build_videos_to_upload(video_url, video_path)

story_ids = []

for video_to_upload in videos_to_upload:

    story_id = upload_story(username, password, video_to_upload, proxy)
    clean_after_upload(video_to_upload)

    story_ids.append(story_id)

clean_after_upload(video_path)

print(json.dumps(story_ids, separators=(',', ':')))
