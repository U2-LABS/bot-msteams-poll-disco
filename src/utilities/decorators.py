from pprint import pprint

from src.utilities.functions import get_request_sender, create_message_activity
from src.chat_functions import send_chat_message


def poll_not_started(func):
    async def wrapped(*args):
        """ Check if the poll is started. Ignore disco command. """
        turn_context, poll = args

        if not poll.isStarted:
            notification_msg = create_message_activity(
                turn_context, 
                f'The poll is not started yet. Use disco command to rock it, baby!!!'
            )
            await send_chat_message(turn_context, notification_msg)
            return 
        return await func(*args)
    return wrapped

def poll_is_started(func):
    async def wrapped(*args):
        turn_context, poll = args

        if poll.isStarted:
            notification_msg = create_message_activity(turn_context, f'The poll is already started by { poll.owner.name }')
            await send_chat_message(turn_context, notification_msg)
            return 

        return await func(*args)
    return wrapped

