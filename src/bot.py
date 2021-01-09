from botbuilder.core import TurnContext
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo

from src.models.poll import Poll
from src.handlers.bot_commands_handler import handle_bot_commands
from src.handlers.button_click_handler import handle_buttons_click

from pprint import pprint

class MusicBot(TeamsActivityHandler):
    """ Get all the requests from the chat and form the responses """
    def __init__(self):
        self.poll = Poll()

    async def on_message_activity(self, turn_context: TurnContext):
        if value := turn_context.activity.value:
            if 'song_id' in value.keys():
                await handle_buttons_click(turn_context, self.poll, value)

        if text := turn_context.activity.text:
            if '</at>' in text:
                await handle_bot_commands(turn_context, self.poll, text[1:])