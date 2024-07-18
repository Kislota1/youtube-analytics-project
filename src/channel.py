import json
import os

from googleapiclient.discovery import build

import isodate
api_key: str = os.getenv("API_KEY")

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.info_channel = json.dumps(channel, indent=2)
        self.id = self.channel["items"][0]["id"]
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']


    @classmethod
    def get_service(cls):
        ''''возвращающий объект для работы с YouTube API'''
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube



    # def print_info(self) -> str:
    #     """Выводит в консоль информацию о канале."""
    #     channel_id = self.channel_id
    #     channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    #     print(json.dumps(channel, indent=2))


    def to_json(self, file):
        ''''сохраняющий в файл значения атрибутов экземпляра `Channel`'''
        moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
        chanel_info = json.loads(self.info_channel)
        with open(file, 'w', encoding="utf-8") as file:
            json.dump(f'{chanel_info}\n', file, ensure_ascii=False, indent=2)
            json.dump(f'Название канала: {moscowpython.title}\n', file, ensure_ascii=False, indent=2)
            json.dump(f'Количество просмотров: {moscowpython.video_count}\n', file, ensure_ascii=False)
            json.dump(f'URL адрес канала: {moscowpython.url}\n', file, ensure_ascii=False)



