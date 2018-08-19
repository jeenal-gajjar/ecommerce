import logging
import os
from datetime import datetime
from slacker import Slacker
from django.conf import settings

slack = Slacker(settings.SLACK_SECRET_KEY)
slack_logger = logging.getLogger('django.request')
TEST_CHANNEL = os.environ.get('TEST_SLACK_CHANNEL', None)


channel_details = {
    "#general": {
        "username": 'Demo-' + settings.ENVIRON,
        "icon_url": None,
        "icon_emoji": ":email:"
    },
    "@Jeenal": {},
}


def bold(text):
    """bold markdown"""
    return "*%s*" % text


def blockquote(text):
    """block quote markdown
    :param text:
    """
    lines = text.splitlines()
    lines_blockquote = ['> ' + line for line in lines]
    new_text = '\n'.join(lines_blockquote)
    return new_text


def post_to_slack(message, channel, username=None, icon_url=None, icon_emoji=None):
    try:
        channel = TEST_CHANNEL or channel
        channel_info = channel_details.get(channel, dict())
        slack.chat.post_message(
            channel=channel,
            text=message,
            username=username or channel_info.get("username"),
            icon_url=icon_url or ((not icon_emoji) and channel_info.get("icon_url")) or None,
            icon_emoji=icon_emoji or ((not icon_url) and channel_info.get("icon_emoji")) or None,
            as_user=False
        )
    except Exception as e:
        slack_logger.error('Error post message to slack\n', exc_info=True)


def send_notification(message, channel):
    try:
        post_to_slack(message, channel)
    except Exception as e:
        slack_logger.error('Error send notification to slack\n', exc_info=True)


def send_registered_new_customer(first_name, last_name, email):
    try:
        message_template = "*New User Account Created*\n"\
                           ">*{first_name} {last_name}* \n" \
                           ">Email: {email}\n"\
                           ">Date: {timestamp}"

        message = message_template.format(
            first_name=first_name,
            last_name=last_name,
            email=email,
            timestamp=datetime.now(),
        )

        send_notification(message, channel='#general')
    except Exception as error:
        slack_logger.error('Error while send registered new user to slack\n', exc_info=True)
