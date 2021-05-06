from service import service

if __name__ == '__main__':
	# TODO: add config
    server = service.Server(port=8081, max_workers=10)
    exit(server.run())
