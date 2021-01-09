from botbuilder.core import TurnContext
from botbuilder.schema import Activity

from src.chat_functions import send_chat_message, send_private_message
from src.models.poll import Poll

from src.utilities.functions import get_request_sender, create_message_activity
from src.utilities.decorators import poll_not_started, poll_is_started, only_owner

from src.config import DEFAULT_TOP_COMMAND_SONGS, DEFAULT_POPTOP_COMMAND_SONGS


def _parse_song_number_arg(args: list, default_value: int):
    for arg in args:
        try:
            return int(arg)
        except ValueError:
            continue
    return default_value

def _parse_settings_args(args: list):
    if not args:
        return 'common', []  # 'common' is the option, when user does not use any option.
    else:
        try:
            option, signal, *_ = args
        except ValueError:
            return args[0], ''
    return option, signal

@poll_not_started
async def handle_disco_command(turn_context: TurnContext, poll: Poll):
    """ Start poll in the chat """
    poll.start()
    poll.owner = get_request_sender(turn_context)
    poll.activity = Activity(text='Choose your favorite song', attachments=[poll.view.card])
    await send_chat_message(turn_context, poll.activity)

    # This command is not working in MS Team
    # It needs to get id of the poll activity to update/delete it in the future
    # resp = await send_chat_message(turn_context, poll.activity)
    # poll.activity.id = resp.id if resp.id else create_unique_id()

@poll_is_started 
@only_owner
async def handle_lightsoff_command(turn_context: TurnContext, poll: Poll):
    """ Finish the poll. Send results """
    winner = poll.finish()

    winner_msgs = [f"The winner is {winner.title} with {winner.mark} votes!!!"]

    if poll.isSongUploaded:
        winner_msgs.append(f"Download link: {winner.link}")

    winner_msg = create_message_activity(
        '\n\n'.join(winner_msgs)
    )
    await send_chat_message(turn_context, winner_msg)


@poll_is_started
async def handle_top_command(turn_context: TurnContext, poll: Poll, args: list):
    number_of_songs = _parse_song_number_arg(args, DEFAULT_TOP_COMMAND_SONGS)

    top_songs = list(poll.storage.sort_songs())[:number_of_songs]

    song_msgs = [f'Top {number_of_songs}:']
    for song in top_songs:
        song_msgs.append(f'{song.title} --- {song.author} --- {song.mark} votes')

    msg = create_message_activity('\n\n'.join(song_msgs))

    sender_id = get_request_sender(turn_context).id
    await send_private_message(turn_context, sender_id, msg)

@poll_is_started
@only_owner
async def handle_poptop_command(turn_context: TurnContext, poll: Poll, args: list):
    song_number = _parse_song_number_arg(args, DEFAULT_POPTOP_COMMAND_SONGS)

    poptop_song = list(poll.storage.sort_songs())[song_number-1]

    poptop_msgs = [
        f'Poptop song #{song_number}',
        f'{poptop_song.title} --- {poptop_song.author} --- {poptop_song.mark} votes'
    ]

    if poll.isSongUploaded:
        poptop_msgs.append(f"Download link: {poptop_song.link}")

    msg = create_message_activity('\n\n'.join(poptop_msgs))

    poll.storage.nullify_song_votes(poptop_song)

    await send_chat_message(turn_context, msg)

async def handle_poll_status_command(turn_context: TurnContext, poll: Poll):
    status_msgs = [
        'Poll status:',
        f"Poll is started: {poll.isStarted}",
        f"Uploading files enabled: {poll.isSongUploaded}"
    ]

    msg = create_message_activity('\n\n'.join(status_msgs))
    sender_id = get_request_sender(turn_context).id
    await send_private_message(turn_context, sender_id, msg)

@poll_is_started
@only_owner
async def handle_settings_command(turn_context: TurnContext, poll: Poll, args: list):
    option, signal = _parse_settings_args(args)

    sender_id = get_request_sender(turn_context).id

    if option == 'common':
        commands_msgs = [
            'List of valid commands:',
            '1. settings mp3 <on/off>'
        ]
        await send_private_message(
            turn_context,
            sender_id,
            create_message_activity('\n\n'.join(commands_msgs))
        )
    elif option == 'mp3':
        if signal == 'on' or signal == 'off':
            if signal == 'on':
                poll.isSongUploaded = True
                await send_private_message(
                    turn_context,
                    sender_id,
                    create_message_activity('Uploading music: ON')
                )
            else:
                poll.isSongUploaded = False
                await send_private_message(
                    turn_context,
                    sender_id,
                    create_message_activity('Uploading music: OFF')
                )
        else:
            await send_private_message(
                turn_context,
                sender_id,
                create_message_activity('mp3 <on/off> - it will on/off uploading music to chat functionality.')
            )
