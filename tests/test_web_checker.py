from ..src.WebChecker import WebChecker


class TestWebChecker:
    def test_check_link_success(self):
        web = WebChecker()
        link = "https://google.com"
        result = web.checkLink(link)
        assert len(result) == 4
        assert result[1] == link
        assert result[2] >= 100 and result[2] <= 599
        assert result[3] > 0

