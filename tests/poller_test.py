import requests
import pytest
from unittest.mock import Mock

from src.auto_dclone.poller import Poller


@pytest.fixture
def mock_requests():
    requests.get = Mock()
    return requests

def test_poll_api(mock_requests):
    # Define the return value of the mocked function
    mock_requests.get.return_value.json.return_value = [
        {
            "region": "1",
            "ladder": "1",
            "hc": "1",
            "progress": "5",
        },
    ]

    # Test the function
    poller = Poller("1", "1", "1")
    data = poller.poll_api()

    # Assert that the data we get corresponds to the data we mocked
    assert data[0]["region"] == "1"
    assert data[0]["ladder"] == "1"
    assert data[0]["hc"] == "1"
    assert data[0]["progress"] == "5"

    mock_requests.get.assert_called_once_with(
        "https://diablo2.io/dclone_api.php",
        params={
            "region": "1",
            "ladder": "1",
            "hc": "1",
        },
    )
