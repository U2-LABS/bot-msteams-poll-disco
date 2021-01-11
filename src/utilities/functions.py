from botbuilder.core import TurnContext, MessageFactory
from uuid import uuid4


def create_unique_id():
    """ Creates unique string ids. """
    return str(uuid4())

def create_message_activity(text: str):
    """ Convert str to Action object. """
    return MessageFactory.text(text=text)

def get_request_sender_id(turn_context: TurnContext):
    """ Return the id of the user, that send activity. """
    return turn_context.activity.from_property.id
