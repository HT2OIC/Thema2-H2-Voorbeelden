# Functie om de HTTP-server te starten.
def start_server():
    # We maken een socket aan. 
    # Deze socket bevat informatie over het IP-adres van de client en de poort waarlangs de verbinding gebeurt.
    # Met AF_INET stellen we IPv4 in, met SOCK_STREAM stellen we TCP in als protocol.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # We willen alle inkomende IP-adressen toelaten via poort 80.
    s.bind(('', 80))
    s.listen(1)
    print("Server actief, wacht op verbindingen...")