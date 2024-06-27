# webhook_receiver.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        
        # Überprüfe den Timestamp, um festzustellen, ob der Link noch gültig ist (30 Minuten)
        if 'timestamp' in params:
            timestamp = int(params['timestamp'][0])
            if timestamp > time():
                # Zeit noch nicht abgelaufen
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Daten erfolgreich erhalten und verarbeitet!')
                return
            else:
                # Zeit abgelaufen
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Fehler: Der Link ist abgelaufen.')
                return
        
        # Wenn kein gültiger Timestamp vorhanden ist
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Fehler: Ungültiger Link.')

def run(server_class=HTTPServer, handler_class=WebhookHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
