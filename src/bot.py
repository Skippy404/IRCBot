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
    globals()['server'] = client.server()

    # Connect to serverIP and serverPort (TODO: Loop through channel list)
    server.connect(serverIP, serverPort, bot_name)

    server.join("#club45")
    server.notice("bruh", "#club45")
    dprint("Joined server")
    server.topic("This is test topic", "#club45")

def smsg(who, msg):
    dprint("\nSending: " + who + "\nMessage: " + msg)
    server.privmsg(who,msg)

startUp("irc.freenode.net", 6667, "#club45")

smsg("deavmi", "welcome to the krustykrab");
smsg("ohmyskippy", "welcome to the krustykrab");
smsg("#club45", "welcome to the krustykrab");

while True: pass

pass
