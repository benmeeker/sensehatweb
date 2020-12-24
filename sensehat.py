from sense_hat import SenseHat
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

sense = SenseHat()

hostName = "localhost"
serverPort = 2000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        tempc = sense.get_temperature()
        tempf = ((sense.get_temperature()*9/5) + 32)
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://localhost:2000</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is information gathered from the SenseHat</p>", "utf-8"))
        self.wfile.write(bytes("<p>Temperature in F: %f</p>" % tempf, "utf-8"))
        self.wfile.write(bytes("<p>Temperature in C: %f</p>" % tempc, "utf-8"))
        self.wfile.write(bytes("<p>Pressure: %f</p>" % pressure, "utf-8"))
        self.wfile.write(bytes("<p>Humidity: %f</p>" % humidity, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__== "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started on port :2000")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")