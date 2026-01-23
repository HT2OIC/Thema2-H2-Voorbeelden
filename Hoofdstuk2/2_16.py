# ------------------------
# Verstuur request
# ------------------------
client.send(request_message.encode())

# Ontvang response
data = client.recv(1024)
print("Data ontvangen:", data.decode())

# Sluit socket
client.close()