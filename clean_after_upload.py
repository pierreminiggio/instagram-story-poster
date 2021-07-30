import os

def clean_after_upload(video_path: str):
    is_file = os.path.isfile
    remove = os.remove

    if is_file(video_path):
        remove(video_path)

    generated_thumbnail_path = video_path + '.jpg'
    if is_file(generated_thumbnail_path):
        remove(generated_thumbnail_path)
