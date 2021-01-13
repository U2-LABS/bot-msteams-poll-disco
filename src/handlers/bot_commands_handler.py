from botbuilder.core import TurnContext

from src.handlers.commands import (
    handle_disco_command,
    handle_lightsoff_command,
    handle_top_command,
    handle_poptop_command,
    handle_poll_status_command,
    handle_settings_command
)
from src.models.poll import Poll


def _parse_text_with_command(text: str):
    """ Parse string that is passed when bot command is invoked. """
    if after_bot_name_text := text.split('</at>')[-1].rstrip().strip():
        return after_bot_name_text.split()
    else:
        return '', []


async def handle_bot_commands(turn_context: TurnContext, poll: Poll, text: str):
    """ Function that invokes bot commands. """

    command, *args = _parse_text_with_command(text)

    if command == 'disco':
        await handle_disco_command(turn_context, poll)
    elif command == 'lightsoff':
        await handle_lightsoff_command(turn_context, poll)
    elif command == 'top':
        await handle_top_command(turn_context, poll, args)
    elif command == 'poptop':
        await handle_poptop_command(turn_context, poll, args)
    elif command == 'settings':
        await handle_settings_command(turn_context, poll, args)
    elif command == 'poll_status':
        await handle_poll_status_command(turn_context, poll)