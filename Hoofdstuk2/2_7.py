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
    
    # De server blijft lopen zolang de Pico aanstaat.
    while True:
        connectie, adres = s.accept()
        print("Verbonden met", adres)
        # We ontvangen een request van max. 1024 bytes lang.
        request = connectie.recv(1024)
        print("Request ontvangen:", request)
        # We sturen een response.
        # Met \n zorgen we ervoor dat de tekst op de volgende regel komt.
        # Zo zijn de regel, header en body gescheiden van elkaar.
        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nServer actief!"
        connectie.send(response)
        # We sluiten de verbinding af, zodat een nieuwe verbinding kan gemaakt worden.
        connectie.close()

start_server()