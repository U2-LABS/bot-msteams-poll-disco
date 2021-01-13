from botbuilder.core import TurnContext
from botbuilder.schema import ConversationParameters, Activity, TextFormatTypes
from botbuilder.core.teams import TeamsInfo


async def send_private_message(turn_context: TurnContext, user_id: str, activity: Activity):
    """ Send proactive message to the user (Does not broke the chat conversation) """
    conversation_reference = TurnContext.get_conversation_reference(
        turn_context.activity
    )

    conversation_parameters = ConversationParameters(
        is_group=False,
        bot=turn_context.activity.recipient,
        members=[await TeamsInfo.get_member(turn_context, user_id)],
        tenant_id=turn_context.activity.conversation.tenant_id,
    )

    async def get_reference(temp_turn_context_1: TurnContext):
        conversation_reference_inner = TurnContext.get_conversation_reference(
            temp_turn_context_1.activity
        )
        return await temp_turn_context_1.adapter.continue_conversation(
            conversation_reference_inner, send_message, temp_turn_context_1.adapter.settings.app_id
        )

    async def send_message(temp_turn_context_2: TurnContext):
        return await temp_turn_context_2.send_activity(activity)

    await turn_context.adapter.create_conversation(
        conversation_reference, get_reference, conversation_parameters
    )

async def send_chat_message(turn_context: TurnContext, activity: Activity):
    """ Send message to the hole chat/channel/user (if it is 1:1 chat) """
    return await turn_context.send_activity(activity)