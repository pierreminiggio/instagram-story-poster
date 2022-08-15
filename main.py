from clean_after_upload import clean_after_upload
from build_videos_to_upload import build_videos_to_upload
from download_video import download_video_if_needed
import json
from upload_story import upload_story
import sys
import traceback

args = sys.argv

if len(args) != 4 and len(args) != 7:
    print('Use like this : python main.py <username> <password> <video_url> [proxy] [instagram_code_beggar_api_url] [instagram_code_beggar_api_token]')
    sys.exit()

username = args[1]
password = args[2]
video_url = args[3]
proxy = args[4] if 4 in args else None
instagram_code_beggar_api_url = args[5] if 5 in args else None
instagram_code_beggar_api_token = args[6] if 6 in args else None
print('testest')
print(instagram_code_beggar_api_url)
print(instagram_code_beggar_api_token)
print('testest')
sys.exit()

video_path = download_video_if_needed(video_url, proxy)

videos_to_upload = build_videos_to_upload(video_url, video_path)

story_ids = []

errors = []

for video_to_upload in videos_to_upload:
    story_id = None
    
    try:
        story_id = upload_story(username, password, video_to_upload, proxy, instagram_code_beggar_api_url, instagram_code_beggar_api_token)
    except Exception as e:
        exc_info = sys.exc_info()
        errors.append(''.join(traceback.format_exception(*exc_info)))

    clean_after_upload(video_to_upload)

    if story_id:
        story_ids.append(story_id)

clean_after_upload(video_path)

if len(story_ids) == 0 and len(errors) > 0:
    print(json.dumps(errors, separators=(',', ':')))
    raise Exception('Error :\'(')

print(json.dumps(story_ids, separators=(',', ':')))
