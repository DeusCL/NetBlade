# RUN THIS IN PYTHON 3.10 OR ABOVE

import socket
import threading
import pickle
import time
import logging

LOGGING_FORMAT = '[%(asctime)s] [%(levelname)s] >> %(message)s'
HEADER = 8
FULL_HEADER = 512
PORT = 49500
SERVER_IP = "0.0.0.0"
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
TPS = 30


class Server:
	def __init__(self, addr):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(addr)

		self.clients = {}
		self.current_map = "Ragnar_M2"
		self.max_players = 2
		self.compact_info = 1


	def handle_client(self, sock, addr):
		str_addr = f'{addr[0]}:{addr[1]}'

		logging.info(f"{str_addr} is joining.")

		try:
			first_data = eval(sock.recv(FULL_HEADER))
		except socket.error:
			logging.error(f"{str_addr} recv failed.")
			self.remove_client(str_addr, sock)
			return
		except Exception:
			logging.error("Invalid data received.")
			self.remove_client(str_addr, sock)
			return

		if not 'msg' in first_data.keys():
			return

		msg = first_data['msg']

		if msg == 'REQ':
			if len(self.clients) >= self.max_players:
				logging.warning(f"Access denied to {str_addr}. Server is full!")
				#time.sleep(0.1)

				self.send_data(str_addr, sock, {'msg':'denied', 'content':'server.full'})
				self.remove_client(str_addr, sock)

				return

			logging.info(f"Access granted to {str_addr}.")

			self.send_data(str_addr, sock, {'msg':'granted', 'content':self.current_map})
			self.remove_client(str_addr, sock)

			return


		if msg != 'JOIN':
			return


		while True:
			try:
				data = sock.recv(FULL_HEADER)
			except socket.error:
				logging.error(f"{str_addr} recv failed.")
				break

			try:
				eval_data = eval(data)
			except Exception:
				logging.error(f"Error convirtiendo el dato recibido a diccionario.\n{data}")
				continue

			# Handle the data received
			self.process_data(str_addr, sock, eval_data)

		self.remove_client(str_addr, sock)


	def process_data(self, str_addr, sock, data):
		if not 'msg' in data.keys(): return

		msg_type = data.pop('msg')

		if msg_type == 'MSG':
			# Simple message sent by this player
			logging.info(data.pop('content'))
			return

		if msg_type == 'DIS':
			# Message for when another player left the game
			logging.info(f"{str_addr} decided to leave the server.")
			self.remove_client(str_addr, sock)
			return

		if msg_type == 'IPD':
			# Message for when this player connected for the first time
			logging.info(f"{data['nick']} joined the game.")


		if not str_addr in self.clients.keys():
			self.clients[str_addr] = {}

		client_data = self.clients[str_addr]
		client_data['sock'] = sock

		if not 'player_data' in client_data.keys():
			client_data['player_data'] = {}

		client_data['player_data'].update(data)



	def send_data_to_clients(self):
		if len(self.clients) <= 1: return

		for str_addr, client_data in self.clients.items():
			sock = client_data['sock']

			players = {}

			for str_addr_2, client_data_2 in self.clients.items():
				if str_addr == str_addr_2: continue
				
				player_data_2 = client_data_2['player_data'].copy()
				nick_2 = player_data_2.pop('nick')

				players[nick_2] = player_data_2

			# Send data of all clients
			self.send_data(str_addr, sock, players, self.compact_info)


	def send_data(self, str_addr, sock, data, compact=0):
		str_data = str(data)
		if compact: str_data = str_data.replace(' ', '')
		self.send_msg(str_addr, sock, str_data)


	def send_msg(self, str_addr, sock, msg):
		msg = msg + ' '*(FULL_HEADER - len(msg))

		try:
			sock.send(msg.encode(FORMAT))
		except socket.error:
			logging.error(f"Error sending msg to {str_addr}.")
			self.remove_client(str_addr, sock)


	def remove_client(self, str_addr, sock):
		sock.close()

		if not str_addr in self.clients.keys(): return
		logging.info(f"Removing {str_addr} from the list of clients.")


		# Remover este cliente de la lista y obliterar el objeto sock
		try:
			disconnected_client = self.clients.pop(str_addr)
		except KeyError:
			logging.error("Error deleting this client, it was obliterated by another task.")
			return

		nick = disconnected_client['player_data']['nick']

		# Avisar al resto de clientes que este gil se fue
		if len(self.clients) == 0: return

		for str_addr_2, client_data in self.clients.items():
			client_sock = client_data['sock']
			disconnection_data = {'msg':'disconnection', 'content':nick}
			self.send_data(str_addr_2, client_sock, disconnection_data)



	def start_server(self):
		self.sock.listen()

		logging.info(f"Server is listening on {SERVER_IP}")
		logging.info(f"Current map: {self.current_map}")
		logging.info(f"The next player that tries to join the game will be joined to \"{self.current_map}\"")

		while True:
			sock, addr = self.sock.accept()
			threading.Thread(target=self.handle_client, args=(sock, addr)).start()


	def init(self):
		# Start the Listener
		threading.Thread(target=self.start_server).start()

		while True:
			self.send_data_to_clients()
			time.sleep(1/TPS)


def main():

	#game_map = input("Enter the map: ")

	server = Server(ADDR)
	#server.current_map = game_map
	server.init()


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)

	logging.info("Initializing Server...")

	main()
