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