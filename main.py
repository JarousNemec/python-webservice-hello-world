from app.server import server
from app.logging.galg_logger import init_logger

init_logger()

def start_server():
    server()


if __name__ == '__main__':
    start_server()
