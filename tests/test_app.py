from unittest.mock import Mock, patch

from app import fetch_status_message


@patch("app.requests.get")
def test_fetch_status_message(mock_get):
    mock_get.return_value = Mock(status_code=200)

    result = fetch_status_message("https://example.com")

    assert result == "https://example.com responded with 200"
    mock_get.assert_called_once_with("https://example.com", timeout=5)
