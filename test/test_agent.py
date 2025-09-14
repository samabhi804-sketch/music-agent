from app.agent import YouTubeMusicService


def test_search():
    yt = YouTubeMusicService()
    results = yt.search("Channa Mereya")
    assert len(results) > 0
    assert "videoId" in results
