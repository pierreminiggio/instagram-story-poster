from contextlib import redirect_stdout
from instagrapi import Client

def upload_story(username: str, password: str, video_path: str, proxy: str = None, instagram_code_beggar_api_url: str = None, instagram_code_beggar_api_token: str = None) -> int:
    client = Client({}, proxy)
    client.logger.disabled = True
    
    def challenge_code_handler(self, username: str, choice=None):
        raise Exception('code !!!')

    client.challenge_code_handler = challenge_code_handler
    client.login(username, password)

    with redirect_stdout(None):
        story = client.video_upload_to_story(video_path)

    return story.id
