import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'DM', help_command = None)

print('Please enter your username')
username = input()
if username == 'root':
    print('Welcome ' + username + ' Please enter your password')
    password = input()
    if password == 'root':
        print('WAIT')
    else:
        print('Incorrect Password') # wtf why you don't remember your password
        exit()
else:
    print('Username not found')
    exit()

colorama.init()
token = input("Input Token>>")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.RED} By Mr.Cuda
{Fore.LIGHTRED_EX} DM = 1
''')
 discord = input(f"{Fore.GREEN}Select : ")
 if discord == '1':
  input2 = input(f"{Fore.RED}What Should I Send? : ")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Successfully Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False)
