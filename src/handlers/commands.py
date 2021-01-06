from botbuilder.core import TurnContext
from botbuilder.schema import Activity

from src.chat_functions import send_chat_message
from src.models.poll import Poll


async def handle_disco_command(turn_context: TurnContext, poll: Poll):
    """ Start poll in the chat """
    poll.start()
    poll.activity = Activity(text='Choose your favorite song', attachments=poll.view.cards)
    resp = await send_chat_message(poll.activity, turn_context)
    poll.activity.id = resp.id
