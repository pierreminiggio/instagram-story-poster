from contextlib import redirect_stdout
from instagrapi import Client
import requests

def upload_story(
    username: str,
    password: str,
    video_path: str,
    proxy: str = None,
    instagram_code_beggar_api_url: str = None,
    instagram_code_beggar_api_token: str = None
) -> int:
    client = Client({}, proxy)
    client.logger.disabled = True
    
    def challenge_code_handler(self, username: str, choice=None):
        if instagram_code_beggar_api_url == None and instagram_code_beggar_api_token == None:
            raise Exception('No code beggar configuration')

        headers = {'Authorization': 'Bearer ' + instagram_code_beggar_api_token}
        beggar_request = requests.get(instagram_code_beggar_api_url + username, headers=headers)
        
        if beggar_request.status_code != 200:
            raise Exception('Beggar didn\'t return a 200')
            
        response_text = response.text
        
        if not response_text:
            raise Exception('Beggar returned an empty response')
            
        return response_text

    client.challenge_code_handler = challenge_code_handler
    client.login(username, password)

    with redirect_stdout(None):
        story = client.video_upload_to_story(video_path)

    return story.id
