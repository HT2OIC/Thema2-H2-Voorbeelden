while True:
    try:
        # ------------------------
        # Maak een TCP socket = verbinding tussen client en server o.b.v IP-adres en poort
        # ------------------------
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(2)  # time-out als server niet reageert
        client.connect((PICO_IP, PORT))

    except Exception as e:
        print("Fout:", e)