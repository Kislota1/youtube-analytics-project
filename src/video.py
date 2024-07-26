import os
from googleapiclient.discovery import build
import isodate

class Video:
    api_key: str = os.getenv("API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    def __init__(self, channel_id: str) -> None:
        video_response = Video.youtube.videos().list(part='snippet,statistics',
                                                     id=channel_id
                                                     ).execute()

        self.id = channel_id
        self.title = video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={channel_id}"
        self.count_views = video_response['items'][0]['statistics']['viewCount']
        self.count_likes = video_response['items'][0]['statistics']['likeCount']

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

