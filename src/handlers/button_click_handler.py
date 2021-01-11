from botbuilder.core import TurnContext

from src.chat_functions import send_private_message
from src.handlers.button_handlers import handle_vote_btn
from src.models.poll import Poll
from src.utilities.functions import create_message_activity


async def _is_current_poll(turn_context: TurnContext, poll: Poll, value: dict):
    """ Check if the poll, user is been voting is the valid one. """
    current_poll_id = value.get('poll_id')
    if poll.id != current_poll_id:
        msg_activity = create_message_activity(
            f"Selected song is in the finished poll. Please start new poll, if it is not started yet."
        )
        await send_private_message(turn_context, turn_context.activity.from_property.id, msg_activity)
        return False
    return True


async def handle_buttons_click(turn_context: TurnContext, poll: Poll, value: dict):
    """ Handle different buttons click events. """
    # Check if user use current poll, not previous once
    if not await _is_current_poll(turn_context, poll, value):
        return

    if 'song_id' in value.keys():
        await handle_vote_btn(turn_context, poll, value)