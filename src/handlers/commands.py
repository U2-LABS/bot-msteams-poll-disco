from botbuilder.core import TurnContext
from botbuilder.schema import Activity

from src.chat_functions import send_chat_message
from src.models.poll import Poll

from src.utilities.functions import get_request_sender
from src.utilities.decorators import poll_not_started, poll_is_started


@poll_is_started
async def handle_disco_command(turn_context: TurnContext, poll: Poll):
    """ Start poll in the chat """
    poll.start()
    poll.owner = get_request_sender(turn_context)
    poll.activity = Activity(text='Choose your favorite song', attachments=poll.view.cards)
    resp = await send_chat_message(turn_context, poll.activity)
    poll.activity.id = resp.id
    