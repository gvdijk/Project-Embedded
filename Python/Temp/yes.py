from connection import Connector
import time

con = Connector('COM3')

time.sleep(2)
print("Placeholder command prompt \n")
while True:
	command = input("Give index: ")
	prefix = command.split(' ')[0]

	try:
		if int(prefix) <= 9:
			print(con.commands[prefix](), "\n")
		else:
			suffix = command.split(' ')[1]
			print(con.commands[prefix](suffix))
	except:
		pass
