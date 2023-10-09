from http.server import BaseHTTPRequestHandler, HTTPServer

from utils import render_html
from config import config
import os


class MyServer(BaseHTTPRequestHandler):
    def __get_index(self):
        return render_html(os.path.join(config.templates_folder, "index.html"))

    def do_GET(self):
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((config.hostName, config.serverPort), MyServer)
    print("Server started http://%s:%s" % (config.hostName, config.serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
