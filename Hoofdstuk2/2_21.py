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
