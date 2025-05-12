import pytest
from unittest.mock import Mock, patch
from mediana_sms.client import MedianaSMSClient
from mediana_sms.exceptions import AuthenticationError

@patch('requests.Session')
def test_send_sms_success(mock_session):
    mock_response = Mock()
    mock_response.json.return_value = {"status": "success"}
    mock_session.return_value.post.return_value = mock_response

    client = MedianaSMSClient("test_key")
    response = client.send_sms("989982009183", ["09100040029"], "Test")
    assert response["status"] == "success"