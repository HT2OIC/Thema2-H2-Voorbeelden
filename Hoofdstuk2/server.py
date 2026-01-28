# Import libraries
import network
import socket
import json
from machine import Pin

# ------------------------
# Hardware setup
# ------------------------
# Onboard LED voor status
onboard_led = Pin("LED", Pin.OUT)
onboard_led.value(1) 

#  Actuator = led
led = Pin(15, Pin.OUT)

# Sensor = drukknop
sensor = Pin(16, Pin.IN)

# ------------------------
# Netwerk setup
# ------------------------
ssid = "WifiVervoort"
wachtwoord = "5martC1t1es"

def setup_AP():
    """
    Zet de Pico op als Access Point
    """
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=wachtwoord)
    ap.active(True)
    while not ap.active():
        pass
    print("Access Point actief!")
    print("IP-adres:", ap.ifconfig()[0])

setup_AP()

# ------------------------
# Help-functies
# ------------------------
def generate_json():
    """
    Genereert JSON met sensorwaarde.

    Returns: json
    """
    return json.dumps({
        "Sensorpin": 16,
        "Sensorwaarde": sensor.value()
    })

def ontvangen(conn):
    """
    Veilig ontvangen van HTTP requests:
    Lees totdat we de lege regel tussen headers en body zien (\r\n\r\n)

    argumenten: connectie tussen client en server
    Returns: request
    """
    request = b"" # Request als lege byte initialiseren.

    while True:
        deel = conn.recv(1024)
        if not deel:
            break
        request += deel
        if b"\r\n\r\n" in request:
            break
    return request.decode()

# ------------------------
# HTTP Server
# ------------------------
def start_server():
    """
    Start een eenvoudige HTTP-server op de Pico
    - GET /knop -> JSON sensor
    - PUT /led  -> LED aan/uitzetten
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)
    print("Server actief, wacht op verbindingen...")

    while True:
        print("Nieuwe connectie")
        connectie, adres = s.accept()
        print("Verbonden met", adres)

        # 1. Ontvang request
        request_string = ontvangen(connectie)
        print("Request ontvangen:\n", request_string)

        # 2. Parse HTTP request regel: methode, pad, versie
        try:
            request_regel = request_string.split('\n')[0]
            methode, pad, versie = request_regel.split()
            print(f"Methode: {methode}, Pad: {pad}, Versie: {versie}")
        except:
            methode, pad = "GET", "/"

        # ------------------------
        # GET /knop -> sensor uitlezen
        # ------------------------
        if pad.startswith("/knop") and methode == "GET":
            response_body = generate_json()

        # ------------------------
        # PUT /led -> LED aan/uit via JSON body
        # ------------------------
        elif pad.startswith("/led") and methode == "PUT":
            try:
                # HTTP scheidt headers van body met \r\n\r\n (lege regel)
                body_index = request_string.find("\r\n\r\n") + 4 # Naar karakter achter \r\n\r\n gaan
                body = request_string[body_index:] # Van eerste karakter body tot laatste karakter
                data = json.loads(body)

                # JSON key "Aanpassen" bepaalt LED aan of uit
                # Waarde van Aanpassen uitlezen, anders None geven.
                aanpassen = data.get("Aanpassen", None)
                if aanpassen is not None:
                    if aanpassen:
                        led.value(1)
                    else:
                        led.value(0)
                    print("LED status gewijzigd:", led.value())
            except Exception as e:
                print("Fout bij LED update:", e)
            response_body = json.dumps({"LED": led.value()})

        # ------------------------
        # Response sturen
        # ------------------------
        # HTTP Response bestaat uit:
        # 1. Statusregel: HTTP/1.1 200 OK
        # 2. Headers: Content-Type
        # 3. Lege regel (\r\n) scheidt headers van body
        # 4. Body: JSON
        response = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-Type: application/json\r\n"
            f"\r\n"
            f"{response_body}"
        )
        connectie.send(response.encode())
        connectie.close()

start_server()