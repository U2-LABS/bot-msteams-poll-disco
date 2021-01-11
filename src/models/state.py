import os
import json

from src.models.poll import Poll
from src.utilities.functions import create_unique_id


def load_state_from_json(path: str):
    """ Load poll state from json. """
    try:    
        with open(path) as f:
            data = json.load(f)    
        return (
            data.get('poll_id'),
            data.get('owner_id'),
            data.get('isStarted'),
            data.get('isSongUploaded')
        )
    except FileNotFoundError:
        return create_unique_id(), None, False, False

def save_state_into_json(poll: Poll, path: str):
    """ Save poll state in json. """
    data = {
        'poll_id': poll.id,
        'owner_id': poll.owner_id,
        'isStarted': poll.isStarted,
        'isSongUploaded': poll.isSongUploaded
    }
    with open(path, 'w') as f:
        f.write(json.dumps(data))

def clear_state(path: str):
    """ Delete state file. """
    os.remove(path)