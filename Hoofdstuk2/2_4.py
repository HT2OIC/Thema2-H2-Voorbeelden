# Functie die Pico instelt als access point.
def setup_AP():
    # Wireless LAN in AP-modus aanmaken.
    ap = network.WLAN(network.AP_IF)
    # Ssid en wachtwoord van het netwerk instellen.
    ap.config(essid = ssid, password = wachtwoord)
    # Wifi activeren.
    ap.active(True)
    # Wachten tot AP actief is.
    while not ap.active():
        pass
    
    # IP-adres van Pico printen.
    print("Access Point actief!")
    print("IP-adres: ", ap.ifconfig()[0])

setup_AP()