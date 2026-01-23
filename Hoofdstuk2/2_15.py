# ------------------------
# GET sensor
# ------------------------

# GET request: bedoeld om data op te halen
request_message = (
    f"GET /knop HTTP/1.1\r\n"
    f"Host: {PICO_IP}\r\n"
    f"\r\n"
)