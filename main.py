from app.service import service

if __name__ == '__main__':
    server = service.Server()
    exit(server.run())
