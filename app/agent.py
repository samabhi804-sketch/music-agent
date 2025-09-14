from ytmusicapi import YTMusic
import webbrowser


class YouTubeMusicService:
    def __init__(self, auth_path="headers_auth.json"):
        self.ytmusic = YTMusic(auth_path)

    def search(self, query):
        # Returns a list of song dicts
        return self.ytmusic.search(query, filter="songs")

    def play(self, video_id):
        # Opens song in the browser/player
        url = f"https://music.youtube.com/watch?v={video_id}"
        webbrowser.open(url)


if __name__ == "__main__":
    yt_service = YouTubeMusicService()
    term = "Channa Mereya"
    results = yt_service.search(term)
    print(f"Results for '{term}':")
    for i, song in enumerate(results[:5]):
        print(
            f"{i+1}: {song['title']} - {song.get('artists',  [{'name': ''}])['name']}"  # noqa: E501
        )
    vid = results["videoId"]
    print("Opening:", vid)
    yt_service.play(vid)
