from download_video import download_video_if_needed
import os
from upload_story import upload_story
import sys

args = sys.argv
print(args)

if len(args) != 5:
    print('Use like this : python main.py username password video_url caption')
    sys.exit()

username = args[1]
password = args[2]
video_url = args[3]
caption = args[4]

video_path = download_video_if_needed(video_url)

print(video_path)
story_id = upload_story(username, password, video_path, caption)
os.remove(video_path)

generated_thumbnail_path = video_path + '.jpg'
if os.path.isfile(generated_thumbnail_path):
    os.remove(generated_thumbnail_path)

print(story_id)