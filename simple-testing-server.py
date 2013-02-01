#!/usr/bin/env python
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler


PORT = 8003

if __name__ == "__main__":
    try:
        import argparse

        parser = argparse.ArgumentParser(description='A simple fake server for testing your API client.')
        parser.add_argument('-p', '--port', type=int, dest="PORT",
                           help='the port to run the server on; defaults to 8003')

        args = parser.parse_args()

        if args.PORT:
            PORT = args.PORT
    except Exception:
        # Could not successfully import argparse or something
        pass


class JSONRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type:", "application/json")
        # send a blank line to end headers:
        self.wfile.write("\n")

        try:
            output = open(self.path[1:] + ".json", 'r').read()
        except Exception:
            output = "{'error': 'Could not find file " + self.path[1:] + ".json'" + "}"
        self.wfile.write(output)

    def do_POST(self):
        if self.path == "/success":
            self.send_response(200)
        elif self.path == "/error":
            self.send_response(500)
        else:
            try:
                response_code = int(self.path[1:])
            except Exception:
                    response_code = 500
            self.send_response(response_code)


server = HTTPServer(("localhost", PORT), JSONRequestHandler)
server.serve_forever()
