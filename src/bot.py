import irc
import irc.client
from debugging import dprint
import os
import subprocess

def startUp(serverIP, serverPort, channelList):
    # Create a client
    client = irc.client.Reactor()
    bot_name = subprocess.check_output("hostname")
    bot_name = str(str.rstrip(bot_name.decode("utf-8")))
    dprint("botname = " + bot_name)

    # Create a server connection
    server = client.server()

    # Connect to serverIP and serverPort (TODO: Loop through channel list)
    server.connect(serverIP, serverPort, bot_name)

    server.join("#club45")
    server.notice("bruh", "#club45")
    dprint("Joined server")

    while True: pass
    
    pass

startUp("irc.freenode.net", 6667, "#club45")
