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