try:
    request_regel = request_string.split('\n')[0]
    methode, pad, versie = request_regel.split()
    print(f"Methode: {methode}, Pad: {pad}, Versie: {versie}")
except:
    methode, pad = "GET", "/"