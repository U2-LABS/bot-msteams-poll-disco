from botbuilder.core import TurnContext
from botbuilder.schema import Activity

from src.handlers.button_handlers import handle_vote_btn
from src.models.poll import Poll


async def handle_buttons_click(turn_context: TurnContext, poll: Poll, value: dict):

    if 'song_id' in value.keys():
        await handle_vote_btn(turn_context, poll, value)