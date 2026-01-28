import socket
import json

PICO_IP = "192.168.4.1"
PORT = 80

status_led = False  # Lokale LED status bijhouden

while True:
    # ------------------------
    # Menu voor interactie
    # ------------------------
    print("\nKeuzemenu:")
    print("1. Waarde knop uitlezen")
    print("2. Led aan- / uitzetten")
    print("3. Programma stoppen")

    keuze = input("Maak een keuze: ")

    if keuze == "3":
        print("Programma stoppen...")
        exit()

    try:
        # ------------------------
        # Maak een TCP socket = verbinding tussen client en server o.b.v IP-adres en poort
        # ------------------------
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)  # time-out als server niet reageert
        client.connect((PICO_IP, PORT))

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
            # Pas lokale status pas aan
            status_led = not status_led

        # ------------------------
        # Verstuur request
        # ------------------------
        client.send(request_message.encode())

        # Ontvang response
        data = client.recv(1024)
        print("Data ontvangen:", data.decode())

        # Sluit socket
        client.close()

    except Exception as e:
        print("Fout:", e)
