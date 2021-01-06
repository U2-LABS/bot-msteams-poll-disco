from botbuilder.core import TurnContext, MessageFactory


def create_message_activity(turn_context: TurnContext, text: str):
    return MessageFactory.text(text)

def get_request_sender(turn_context: TurnContext):
    return turn_context.activity.from_property