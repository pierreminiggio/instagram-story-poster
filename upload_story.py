from contextlib import redirect_stdout
from instagrapi import Client

def challenge_code_handler(self, username: str, choice=None):
    raise Exception('code !!!')

def upload_story(username: str, password: str, video_path: str, proxy: str = None) -> int:
    client = Client({}, proxy)
    client.logger.disabled = True
    client.challenge_code_handler = challenge_code_handler
    client.login(username, password)

    with redirect_stdout(None):
        story = client.video_upload_to_story(video_path)

    return story.id
