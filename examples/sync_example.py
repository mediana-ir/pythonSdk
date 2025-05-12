from mediana_sms import MedianaSMSClient

client = MedianaSMSClient("your_api_key")

# Send SMS
sms_response = client.send_sms(
    sending_number="989982009183",
    recipients=["09100000000"],
    message_text="Hello from SDK"
)
print("SMS Sent:", sms_response)

# Check status
status = client.get_status(sms_response["requestId"])
print("Status:", status.status)