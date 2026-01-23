# ------------------------
# GET sensor
# ------------------------
if keuze == "1":
    # GET request: bedoeld om data op te halen
    request_message = (
        f"GET /knop HTTP/1.1\r\n"
        f"Host: {PICO_IP}\r\n"
        f"\r\n"
    )

# ------------------------
# PUT actuator
# ------------------------
elif keuze == "2":
    # PUT request: bedoeld om resource te updaten
    # Body is JSON
    request_body = json.dumps({"Aanpassen": not status_led})
    request_message = (
        f"PUT /led HTTP/1.1\r\n"
        f"Host: {PICO_IP}\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(request_body)}\r\n"
        f"\r\n"
        f"{request_body}"
    )
    # Pas lokale status led aan
    status_led = not status_led