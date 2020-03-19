import irc
import irc.client

def startUp(serverIP, serverPort, channelList):
    # Create a client
    client = irc.client.Reactor()

    # Create a server connection
    server = client.server()

    # Connect to serverIP and serverPort (TODO: Loop through channel list)
    server.connect(serverIP, serverPort, "EMANCIPATED")

    server.join("#club45")
    server.notice("bruh", "#club45")
    server.topic("This is test topic", "#club45")
    server.privmsg("deavmi", "welcome to the krustykrab")
    server.privmsg("ohmyskippy", "welcome to the krustykrab")
    
    while True: pass
    
    pass

startUp("irc.freenode.net", 6667, "#club45")
