from pprint import pprint

from src.utilities.functions import get_request_sender_id, create_message_activity
from src.chat_functions import send_chat_message


def poll_is_started(func):
    """ Check if the poll is started. """
    async def wrapped(*args):
        turn_context, poll, *_ = args

        if not poll.isStarted:
            notification_msg = create_message_activity(
                f'The poll is not started yet. Use disco command to rock it, baby!!!'
            )
            await send_chat_message(turn_context, notification_msg)
            return 
        return await func(*args)
    return wrapped

def poll_not_started(func):
    """ Check if the poll is not started yet. """
    async def wrapped(*args):
        turn_context, poll, *_ = args

        if poll.isStarted:
            notification_msg = create_message_activity(
                f'The poll is already started'
            )
            await send_chat_message(turn_context, notification_msg)
            return 

        return await func(*args)
    return wrapped

def only_owner(func):
    """ Check if the command invoked by owner of the poll. """
    async def wrapped(*args):
        turn_context, poll, *_ = args
        sender_id = get_request_sender_id(turn_context)

        if poll.owner_id != sender_id:
            notification_msg = create_message_activity(
                f"You can not use this command. You are not the owner of the poll."
            )
            await send_chat_message(turn_context, notification_msg)
            return

        return await func(*args)
    return wrapped