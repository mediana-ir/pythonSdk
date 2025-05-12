import asyncio
from mediana_sms import AsyncMedianaSMSClient

async def main():
    async with AsyncMedianaSMSClient("your_api_key") as client:
        # Send SMS
        sms_response = await client.send_sms(
            sending_number="989982009183",
            recipients=["09100000000"],
            message_text="Async Hello"
        )
        print("Async SMS Sent:", sms_response)

        # Check status
        status = await client.get_status(sms_response["requestId"])
        print("Async Status:", status.status)

asyncio.run(main())