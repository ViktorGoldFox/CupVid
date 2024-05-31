from math import log
import socket
from logzero import logger, logfile

logfile("LogsClient.log")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 228

try:
    sock.connect((ip, port))
    logger.log(f"Успешно подключенно: {ip}:{port}")
except Exception as error_code:
    logger.error(f"Ошибка при подключении: {error_code}")
    

