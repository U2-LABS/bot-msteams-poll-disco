from botbuilder.core import TurnContext

from src.models.poll import Poll
from src.utilities.functions import get_request_sender_id


async def handle_vote_btn(turn_context: TurnContext, poll: Poll, value: dict):
    """ Vote for the song functionality. Update db with voted user id. """
    song_id = int(value.get('song_id'))
    voted_user_id = get_request_sender_id(turn_context)
    
    poll.vote_for_song(song_id, voted_user_id)
    
