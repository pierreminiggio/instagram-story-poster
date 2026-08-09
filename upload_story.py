from contextlib import redirect_stdout
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired
from session_store import load_session, save_session
import requests

def upload_story(
    username: str,
    password: str,
    video_path: str,
    proxy: str = None,
    instagram_code_beggar_api_url: str = None,
    instagram_code_beggar_api_token: str = None,
    session_json: str = None,
    session_output_path: str = None
) -> int:
    client = Client({}, proxy)
    client.logger.disabled = True

    saved_session = load_session(session_json)

    if saved_session:
        client.set_settings(saved_session)
        client.set_proxy(proxy)

    def challenge_code_handler(username: str, choice=None):
        if instagram_code_beggar_api_url == None and instagram_code_beggar_api_token == None:
            raise Exception('No code beggar configuration')

        headers = {'Authorization': 'Bearer ' + instagram_code_beggar_api_token}
        beggar_request = requests.get(instagram_code_beggar_api_url + username, headers=headers)
        
        if beggar_request.status_code != 200:
            raise Exception('Beggar didn\'t return a 200')
            
        response_text = beggar_request.text
        
        if not response_text:
            raise Exception('Beggar returned an empty response')
            
        return response_text

    client.challenge_code_handler = challenge_code_handler
    logged_in = client.login(username, password)

    if not logged_in:
        raise Exception(
            'Login failed for ' + username
            + ' (instagrapi returned False without raising an exception - '
            + 'check the account status, proxy, or whether Instagram is requiring a challenge)'
        )

    try:
        client.account_info()
    except ChallengeRequired as e:
        raise Exception(
            'Instagram requires manual verification (checkpoint) for ' + username
            + ' before this account can be used: ' + str(e)
        ) from e

    # Save the session as soon as we know it's genuinely authenticated, so it's
    # persisted even if the upload itself fails for an unrelated reason below.
    save_session(client.get_settings(), session_output_path)

    with redirect_stdout(None):
        story = client.video_upload_to_story(video_path)

    return story.id
