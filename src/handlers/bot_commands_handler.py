from botbuilder.core import TurnContext
from botbuilder.schema import Activity

from src.handlers.commands import handle_disco_command
from src.models.poll import Poll


def _parse_text_with_command(text: str):
    """ Parse string that is passed when bot command is invoked. """
    return text.split('</at>')[-1].rstrip().strip().split()

async def handle_bot_commands(turn_context: TurnContext, text: str, poll: Poll):
    """ Function that invokes / commands. """
    command, *args = _parse_text_with_command(text)

    if command == 'disco':
        await handle_disco_command(turn_context, poll)
    elif command == 'lightsoff':
        pass
    elif command == 'top':
        pass
    elif command == 'poptop':
        pass
    elif command == 'settings':
        pass
    elif command == 'resume':
        pass
    elif command == 'drop':
        pass
    elif command == 'poll_status':
        pass