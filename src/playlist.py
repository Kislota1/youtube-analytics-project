import isodate
from googleapiclient.discovery import build
from datetime import timedelta
import os

api_key: str = os.getenv("API_KEY")


def parse_duration(iso_duration: str) -> int:
    duration = isodate.parse_duration(iso_duration)
    return int(duration.total_seconds())


class PlayList:

    def __init__(self, playlist_id: str):
        self.url = None
        self.title = None
        self.playlist_id = playlist_id
        self.youtube = youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist_data = self.get_playlist_data()
        self.videos = self.get_videos_from_playlist()

    def get_playlist_data(self):
        # Получаем данные о плейлисте (название и ссылка)
        response = self.youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()

        playlist = response['items'][0]['snippet']
        self.title = playlist['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def get_videos_from_playlist(self):
        videos = []
        next_page_token = None

        while True:
            response = self.youtube.playlistItems().list(
                part='contentDetails',
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            for item in response['items']:
                video_id = item['contentDetails']['videoId']
                videos.append(video_id)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        return videos

    @property
    def total_duration(self) -> timedelta:
        total_seconds = 0

        for video_id in self.videos:
            response = self.youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()

            duration = response['items'][0]['contentDetails']['duration']
            total_seconds += parse_duration(duration)

        return timedelta(seconds=total_seconds)

    def show_best_video(self) -> str:
        best_video = None
        max_likes = 0

        for video_id in self.videos:
            response = self.youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            likes = int(response['items'][0]['statistics'].get('likeCount', 0))
            if likes > max_likes:
                max_likes = likes
                best_video = video_id

        if best_video:
            return f"https://youtu.be/{best_video}"
