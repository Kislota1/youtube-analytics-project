import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import isodate

class Video:
    api_key: str = os.getenv("API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    def __init__(self, video_id: str) -> None:

        self.id = video_id
        self.title = None
        self.url = None
        self.count_views = None
        self.like_count = None

        try:
            # Запрашиваем данные о видео с помощью API
            video_response = Video.youtube.videos().list(
                part='snippet,statistics',
                id=video_id
            ).execute()

            # Проверяем, что видео найдено
            if video_response['items']:
                self.title = video_response['items'][0]['snippet']['title']
                self.url = f"https://www.youtube.com/watch?v={video_id}"
                self.count_views = video_response['items'][0]['statistics']['viewCount']
                self.like_count = video_response['items'][0]['statistics']['likeCount']
            else:
                # Если видео не найдено, оставляем атрибуты в значении None
                pass
        except Exception as e:
            # Ловим любые исключения и оставляем атрибуты в значении None
            print(f"Ошибка при запросе данных о видео: {e}")

    def __str__(self):
        return f'{self.title}'

class PLVideo(Video):
    def __init__(self, channel_id, play_list_id):
        super().__init__(channel_id)
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.play_list_id = youtube.playlistItems().list(playlistId=play_list_id,
                                                         part='contentDetails',
                                                         maxResults=50,
                                                         ).execute()

