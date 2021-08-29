##############################################
# Run this script locally to add bot commands
##############################################
import requests
import os
from dotenv import load_dotenv

load_dotenv()

bot_id = os.getenv('bot_id')
bot_key = os.getenv('bot_key')


json = {
    "name": "saturn",
    "description": "A Helpful Bot!",
    "options": [
        {
            "name": "configure",
                    "description": "Manage Callback URLS for other commands.",
                    "type": 2,
                    "options": [
                        {
                            "name": "schedule",
                            "description": "Add or Remove Callback URLS for the schedule message.",
                            "type": 1,
                            "options": [
                                {
                                    "name": "add_callback_url",
                                    "description": "Format as comma seperated: Alias,URL.",
                                    "type": 3
                                },
                                {
                                    "name": "remove_callback",
                                    "description": "Remove URLs by alias.",
                                    "type": 3
                                },
                                {
                                    "name": "add_allowed_roles",
                                    "description": "Add Roles to use this feature.",
                                    "type": 4
                                },
                                {
                                    "name": "remove_allowed_roles",
                                    "description": "Remove previously added roles.",
                                    "type": 4
                                }
                            ]
                        },
                        {
                            "name": "reminder",
                            "description": "Add or Remove Callback URLS for reminders.",
                            "type": 1,
                            "options": [
                                {
                                    "name": "add_callback_url",
                                    "description": "Format as comma seperated: Alias,URL.",
                                    "type": 3
                                },
                                {
                                    "name": "remove_callback",
                                    "description": "Remove URLs by alias.",
                                    "type": 3
                                },
                                {
                                    "name": "add_allowed_roles",
                                    "description": "Add Roles to use this feature.",
                                    "type": 4
                                },
                                {
                                    "name": "remove_allowed_roles",
                                    "description": "Remove previously added roles.",
                                    "type": 4
                                }
                            ]
                        }
                    ]
        },
        {
            "name": "schedule",
            "description": "schedules messages to be sent at a future time!",
            "type": 2,
            "options": [
                {
                    "name": "Alias",
                    "description": "Alias for the channel you want the message to appear in.",
                    "type": 3,
                    "required": True
                },
                {
                    "name": "Message",
                    "description": "Message you want to send.",
                    "type": 3,
                    "required": True
                },
                {
                    "name": "Time",
                    "description": "Time you want message to appear. Formatted YYYY-MM-DD HH:MM:SS AM/PM",
                    "type": 3,
                    "required": True
                },
                {
                    "name": "Timezone",
                    "description": "Message you want to send.",
                    "type": 3,
                    "required": True,
                    "choices": [
                        {
                            "name": "PST",
                            "value": "PST"
                        },
                        {
                            "name": "MST",
                            "value": "MST"
                        },
                        {
                            "name": "CST",
                            "value": "CST"
                        },
                        {
                            "name": "EST",
                            "value": "EST"
                        }
                    ]
                },
            ]

        }
    ]
}


headers = {
    "Authorization": f"Bot {bot_key}"
}


def update_commands(url):
    r = requests.post(url, headers=headers, json=json)

    print(r.content)


def get_commands(url):
    r = requests.get(url, headers=headers)

    print(r.content)


def delete_commands(url):
    r = requests.delete(url, headers=headers)

    print(r.content)


update_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# get_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# delete_commands(
#     f"https://discord.com/api/v8/applications/{bot_id}/commands/795912485793431583")
