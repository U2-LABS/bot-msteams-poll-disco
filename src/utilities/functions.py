from botbuilder.core import TurnContext, MessageFactory
from uuid import uuid4


def create_unique_id():
    return str(uuid4())

def create_message_activity(text: str):
    return MessageFactory.text(text=text)

def get_request_sender(turn_context: TurnContext):
    return turn_context.activity.from_property
