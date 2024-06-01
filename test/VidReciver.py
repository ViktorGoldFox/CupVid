from math import log
import socket
from logzero import logger, logfile

logfile("LogsClient.log")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 228

try:
    sock.connect((ip, port))
    logger.info(f"Успешно подключенно: {ip}:{port}")
except Exception as error_code:
    logger.error(msg=f"Ошибка при подключении: {error_code}")
    
data_vid = open("video.mp4", 'r')
sock.send((data_vid).encode("UTF-8"))
