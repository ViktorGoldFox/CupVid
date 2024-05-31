from os import wait
import socket 
from logzero import logger, logfile

logfile("logs.log")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

now_connected = []

ip = '127.0.0.1'
port = 228

try:
    server.bind((ip, port))
    logger.info(f"Сервер открыт: {ip}:{port}")
except Exception as error_code:
    logger.error(f"Ошибка в создании сокета: {error_code}")
    
async def applied_users():
    us_data = await server.accept()
    
    now_connected.append(us_data)
    logger.info(f"Applied user: {us_data}")

applied_users()
