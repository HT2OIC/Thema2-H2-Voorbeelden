# ------------------------
# GET /knop -> sensor uitlezen
# ------------------------
if pad.startswith("/knop") and methode == "GET":
    response_body = generate_json()
