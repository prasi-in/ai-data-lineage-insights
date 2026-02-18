import os
import json
from typing import List, Dict
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackIngestionService:
    """
    Service to ingest Slack messages either from:
    1. Slack Export JSON
    2. Live Slack API
    """

    def __init__(self, bot_token: str = None):
        self.bot_token = bot_token or os.getenv("SLACK_BOT_TOKEN")
        self.client = WebClient(token=self.bot_token) if self.bot_token else None

    # -----------------------------
    # Option 1: Read Slack Export
    # -----------------------------
    def read_export_folder(self, export_root: str) -> List[Dict]:
        messages = []

        for root, _, files in os.walk(export_root):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                            if isinstance(data, list):
                                for message in data:
                                    messages.append({
                                        "user": message.get("user"),
                                        "timestamp": message.get("ts"),
                                        "text": message.get("text")
                                    })

                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        return messages

    # -----------------------------
    # Option 2: Read Live Channel
    # -----------------------------
    def read_channel_messages(self, channel_id: str) -> List[Dict]:
        if not self.client:
            raise ValueError("Slack bot token not provided")

        messages = []

        try:
            response = self.client.conversations_history(
                channel=channel_id,
                limit=200
            )

            messages.extend(response["messages"])

            while response.get("response_metadata", {}).get("next_cursor"):
                cursor = response["response_metadata"]["next_cursor"]

                response = self.client.conversations_history(
                    channel=channel_id,
                    cursor=cursor
                )

                messages.extend(response["messages"])

        except SlackApiError as e:
            print(f"Slack API error: {e.response['error']}")

        return messages


if __name__ == "__main__":
    service = SlackIngestionService()

    # Example: export-based
    export_messages = service.read_export_folder("workspace_export")
    print(f"Export messages read: {len(export_messages)}")

    # Example: live API (requires SLACK_BOT_TOKEN)
    # live_messages = service.read_channel_messages("CXXXXXXX")
    # print(f"Live messages read: {len(live_messages)}")

