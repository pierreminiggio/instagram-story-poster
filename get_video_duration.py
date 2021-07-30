import os

def get_video_duration(video_path: str) -> float:
    duration_command_stream = os.popen(
        'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 ' + video_path
    )
    duration_command_output = duration_command_stream.read()

    return float(duration_command_output)
