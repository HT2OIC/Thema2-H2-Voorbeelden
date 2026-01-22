# Json genereren
json_response = generate_json()
# We sturen een response.
# Met \n zorgen we ervoor dat de tekst op de volgende regel komt.
# Zo zijn de regel, header en body gescheiden van elkaar.
response = "HTTP/1.1 200 OK\nContent-Type: application/json\n\n" + json_response
connectie.send(response)