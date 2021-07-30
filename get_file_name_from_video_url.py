import base64

def get_file_name_from_video_url(video_url: str) -> str:
    return base64.urlsafe_b64encode(video_url.encode()).decode()
    