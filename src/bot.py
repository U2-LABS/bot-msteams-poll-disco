from botbuilder.core import TurnContext
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo

from src.models.poll import Poll
from src.handlers.bot_commands_handler import handle_bot_commands


class MusicBot(TeamsActivityHandler):
    """ Get all the requests from the chat and form the responses """
    def __init__(self):
        self.poll = Poll()

    async def on_message_activity(self, turn_context: TurnContext):
        if text := turn_context.activity.text:
            if '</at>' in text:
                await handle_bot_commands(turn_context, text[1:], self.poll)
