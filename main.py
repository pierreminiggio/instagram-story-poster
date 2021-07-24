from download_video import download_video_if_needed
import os
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

story_id = upload_story(username, password, video_path, proxy)
os.remove(video_path)

generated_thumbnail_path = video_path + '.jpg'
if os.path.isfile(generated_thumbnail_path):
    os.remove(generated_thumbnail_path)

print(story_id)