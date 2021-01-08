from botbuilder.core import TurnContext

from src.models.poll import Poll


async def handle_vote_btn(turn_context: TurnContext, poll: Poll, value: dict):
    song_id = int(value.get('song_id'))
    voted_user_id = turn_context.activity.from_property.id
    
    poll.vote_for_song(song_id, voted_user_id)
    
