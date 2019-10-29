#!/usr/bin/python3
import http.server
import ssl
from argparse import ArgumentParser
import subprocess


parser = ArgumentParser()
parser.add_argument("-a", "--addr", dest="address",
                    help="Address host:port", metavar="ADDRESS")

parser.add_argument("-p", "--port", dest="port",
                    help="Address port on localhost", metavar="PORT")

parser.add_argument("-c", "--cert", dest="certfile",
                    help="SSL certfile", metavar="CERT")

parser.add_argument("-k", "--key", dest="keyfile",
                    help="SSL keyfile", metavar="KEY")

parser.add_argument("-s", "--default_secure", dest="default_secure", action="store_true",
                    help="If default secure => ./host.pem certfile, ./host-key.pem keyfile", default=False)

args = parser.parse_args()

if not args.address:
	if not args.port:
		args.address = "0.0.0.0:8000"
	else:
		args.address = "0.0.0.0:%s" % port

host, port = args.address.split(':')
Handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer((host, int(port)), http.server.SimpleHTTPRequestHandler)
if args.default_secure:
	args.certfile = './%s.pem' % host
	args.keyfile = './%s-key.pem' % host

if args.certfile and args.keyfile:
	try:
		httpd.socket = ssl.wrap_socket(httpd.socket, certfile=args.certfile, keyfile=args.keyfile, server_side=True)
		print('serving https on %s:%s...' % (host, port))
		httpd.serve_forever()
	except FileNotFoundError:
		if args.default_secure:
			code = subprocess.call(['mkcert', host])
			if code == 0:
				args.certfile = './%s.pem' % host
				args.keyfile = './%s-key.pem' % host
				httpd.socket = ssl.wrap_socket(httpd.socket, certfile=args.certfile, keyfile=args.keyfile, server_side=True)
				print('serving https on %s:%s...' % (host, port))
				httpd.serve_forever()
			else:
				print('Something wrong with mkcert...')
else:
	print('serving http on %s:%s...' % (host, port))
	httpd.serve_forever()