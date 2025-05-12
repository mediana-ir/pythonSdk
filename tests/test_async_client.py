import pytest
from unittest.mock import AsyncMock
from mediana_sms.async_client import AsyncMedianaSMSClient

@pytest.mark.asyncio
async def test_async_send_sms():
    async with AsyncMedianaSMSClient("test_key") as client:
        with patch('aiohttp.ClientSession.post', new=AsyncMock()) as mock_post:
            mock_post.return_value.__aenter__.return_value.json = AsyncMock(return_value={"status": "success"})
            response = await client.send_sms("989982009183", ["09100000029"], "Test")
            assert response["status"] == "success"