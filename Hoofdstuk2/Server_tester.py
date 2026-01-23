import socket
import json
import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Standaard instellingen
# ----------------------------
DEFAULT_PICO_IP = "192.168.4.1"
PORT = 80
TIMEOUT = 2  # seconden

# ----------------------------
# Functie om request te maken en te versturen
# ----------------------------
def stuur_request(method, endpoint, body=None):
    """Verstuurt een GET of PUT request naar de Pico en retourneert de response"""
    pico_ip = pico_ip_entry.get()  # gebruik het IP uit de GUI
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(TIMEOUT)
        client.connect((pico_ip, PORT))

        if method == "GET":
            request = (
                f"GET {endpoint} HTTP/1.1\r\n"
                f"Host: {pico_ip}\r\n"
                f"\r\n"
            )
        elif method == "PUT":
            try:
                body_json = json.dumps(json.loads(body))  # controleer of JSON correct is
            except Exception as e:
                messagebox.showerror("Fout", f"Ongeldige JSON:\n{e}")
                return None

            request = (
                f"PUT {endpoint} HTTP/1.1\r\n"
                f"Host: {pico_ip}\r\n"
                f"Content-Type: application/json\r\n"
                f"Content-Length: {len(body_json)}\r\n"
                f"\r\n"
                f"{body_json}"
            )
        else:
            messagebox.showerror("Fout", "Alleen GET of PUT toegestaan")
            return None

        client.send(request.encode())
        response = client.recv(4096).decode()
        client.close()
        return response

    except Exception as e:
        messagebox.showerror("Fout", f"Kan geen verbinding maken:\n{e}")
        return None

# ----------------------------
# GUI functies
# ----------------------------
def verstuur_request():
    method = method_var.get()
    endpoint = endpoint_entry.get()
    body = body_text.get("1.0", tk.END).strip()

    response = stuur_request(method, endpoint, body if method=="PUT" else None)
    if response:
        # Scheid headers en body
        try:
            body_only = response.split("\r\n\r\n")[1]
        except IndexError:
            body_only = response
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, body_only)

def update_body_state(*args):
    """Schakelt body-veld aan of uit afhankelijk van methode"""
    if method_var.get() == "GET":
        body_text.config(state=tk.DISABLED, bg="#f0f0f0")
    else:
        body_text.config(state=tk.NORMAL, bg="white")

# ----------------------------
# Tkinter GUI
# ----------------------------
root = tk.Tk()
root.title("Server tester")

# Pico IP invoer
tk.Label(root, text="Pico IP:").pack(anchor=tk.W, padx=10)
pico_ip_entry = tk.Entry(root, width=20)
pico_ip_entry.pack(anchor=tk.W, padx=10)
pico_ip_entry.insert(0, DEFAULT_PICO_IP)

# Method selector
method_var = tk.StringVar(value="GET")
method_var.trace("w", update_body_state)
tk.Label(root, text="Methode:").pack(anchor=tk.W, padx=10)
tk.OptionMenu(root, method_var, "GET", "PUT").pack(anchor=tk.W, padx=10)

# Endpoint input
tk.Label(root, text="Endpoint (bijv. /knop of /led):").pack(anchor=tk.W, padx=10)
endpoint_entry = tk.Entry(root, width=30)
endpoint_entry.pack(anchor=tk.W, padx=10)
endpoint_entry.insert(0, "/knop")

# Body input (alleen relevant voor PUT)
tk.Label(root, text="Body (JSON, alleen voor PUT):").pack(anchor=tk.W, padx=10)
body_text = tk.Text(root, height=5, width=50)
body_text.pack(padx=10, pady=5)
body_text.insert(tk.END, '{"Aanpassen":true}')

# Verstuur knop
tk.Button(root, text="Verstuur request", command=verstuur_request).pack(pady=10)

# Response display
tk.Label(root, text="Response:").pack(anchor=tk.W, padx=10)
response_text = tk.Text(root, height=10, width=60)
response_text.pack(padx=10, pady=5)

# Zet body uit of aan bij start
update_body_state()

root.mainloop()