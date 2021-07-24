from instagrapi import Client

def upload_story(username: str, password: str, video_path: str) -> int:
    client = Client()
    client.login(username, password)

    story = client.video_upload_to_story(video_path)

    return story.id
