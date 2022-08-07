import time as t
import sys

def cas():
  password = input("Enter password")
  if password == 'cas58172':
    print('Central Autonomic System, made in Ukraine by Komandarm. Control system. All elements start!')
  else:
    print('Invalid password!')

def info():
    print("Central Autonomic System, enter help to see list of commands!")

def help():
    print("Commands list: \n info \n help \n bot \n get ")

def bot():
  print("https://discord.com/api/oauth2/authorize?client_id=1002217263199420426&permissions=8&scope=bot")

def get():
  print("https://github.com/Komandarm/C.A.SConsole")

print("Hello user, this is official C.A.S Console!")
t.sleep(1)
print("Please, enter command...")

while True:
  command = input(">")
  if command == 'cas':
    cas()
  if command == 'info':
      info()
  if command == 'help':
      help()
  if command == 'bot':
    bot()
  if command == 'get':
    get()
  elif command == 'exit':
    sys.exit()
  else:
    print('Wrong command!')