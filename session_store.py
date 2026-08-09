import json
from typing import Optional


def load_session(session_json: str = None) -> Optional[dict]:
    if not session_json:
        return None

    return json.loads(session_json)


def save_session(settings: dict, session_output_path: str = None) -> None:
    if session_output_path is None:
        return

    with open(session_output_path, 'w') as fp:
        json.dump(settings, fp)
