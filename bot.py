import discord
import asyncio
import sys
import time
import os
import random

motd = 'Bots!'
motdt = ''
client = discord.Client()
print('Connecting..')
token = ""
mode = "0"
tpass = ""

#Settings:
selfbot = True #Changing this to 'False' will break Discords ToS! Use at Your Own Risk. (This Allows other people to use your bot when it is in a user)
serrest = False #Enables Server Restrictions!
enablenewrepmsg = True
delaymsg = True

#stats
wordspersec = 10
msgperlev = 20


#msg:
noperm = "Sorry, No Permission To Do this"
newrep = "Hello [@men], Are you New. I don't think we have met before?"


cmds = ["test","help","sleep","reload","shutdown","badmin","bban"]
i = '-'
rmdelay = 10
#getting token from file
if os.path.isdir("config") == False:
    print("Config Folder NOT Found! Creating Dir '/config'")
    os.mkdir("config")
if os.path.exists("config/token.txt") == False:
    print("Token File NOT Found! Creating File 'token.txt'")
    file = open("config/token.txt", "w")
    file.close()
  
file = open("config/token.txt", "r")
token2 = file.read();
file.close()
token3 = token2.split('<%>')
if (str(token3[0]) == "0"):
    token = token3[1]
    mode = "1"
if str(token3[0]) == "1":
    token = token3[1]
    tpass = token3[2]
    mode = "2"
    
if token == "":
    print("Token Empty:")
    input1 = input("Press [1] to Enter Token or [2] To Enter User Account or [3] to exit Bot Program:  ")
    if input1 == "1":
        input2 = input("Enter Token: ")
        filecon = "0" + "<%>" + input2 + "<%>" + "null"
        os.remove("config/token.txt")
        file = open("config/token.txt", "w+")
        file.write(filecon)
        file.close()
        time.sleep(1)
        mode = "1"
        token = input2
        time.sleep(1)
        print("Setup Done!")
        print("Running Bot:")
        time.sleep(1)
        
    elif input1 == "2":
        input2 = input("Enter Email: ")
        input3 = input("Enter Password: ")
        filecon = "1" + "<%>" + input2 + "<%>" + input3
        os.remove("config/token.txt")
        file = open("config/token.txt", "w+")
        file.write(filecon)
        file.close()
        time.sleep(1)
        mode = "2"
        token = input2
        tpass = input3
        time.sleep(1)
        print("Setup Done!")
        print("Running Bot:")
        time.sleep(1)
    else:
        print("Exiting")
        time.sleep(1)
        sys.exit();
else:
    print("USING TOKEN:" + token)


 #cmdreader get
if os.path.exists("config/reader.txt") == False:
    print("Reader File NOT Found! Creating File 'reader.txt'")
    file = open("config/reader.txt", "w")
    file.write("!")
    file.close()
if serrest:
    if os.path.exists("config/servers.txt") == False:
        print("Reader File NOT Found! Creating File 'servers.txt'")
        file = open("config/servers.txt", "w")
        file.write("206116046325809152")
        file.close()
    file = open("config/servers.txt", "r")
    servi = file.read();
    file.close()
else:
    servi = "test"
serget = servi.split(";")

if os.path.exists("config/motd.txt") == False:
    print("MOTD File NOT Found! Creating File 'motd.txt'")
    file = open("config/motd.txt", "w")
    file.write("Bots!")
    file.close()
file = open("config/motd.txt", "r")
motd = file.read();
file.close()


    


  
file = open("config/reader.txt", "r")
i = file.read();
file.close() 




#command stuff
#cmdpath
if os.path.exists("config/cmdpath.txt") == False:
    cmde = ""
    for cmded in cmds:
        cmde = cmde + ";"+cmded
    cmde2 = cmde.replace(";","",1)
    print("CmdPath File NOT Found! Creating File 'cmdpath.txt'")
    file = open("config/cmdpath.txt", "w")
    file.write(cmde2)
    file.close()
cmds2 = ["test"]
cmds2.clear()
file = open("config/cmdpath.txt", "r+")
cmds2 = file.read().split(";")
file.close()


    
#Data:
if os.path.isdir("data") == False:
    print("Data Folder NOT Found! Creating Dir '/data'")
    os.mkdir("data")


#Commands:

#Role
#Role
def updaterepstore():
    global repl
    repl = {"":""}
    repl.clear()
    #print("Updating DataStore: RepL")
    repget1 = [""]
    repget1.clear()
    repget2 = {"":""}
    repget2.clear()
    if os.path.isdir("data") == False:
        print("Data Folder NOT Found! Creating Dir '/data'")
        os.mkdir("data")
    if os.path.isdir("data/rep") == False:
        print("Rep Folder NOT Found! Creating Dir '/rep'")
        os.mkdir("data/rep")
    if os.path.exists("data/rep/list.txt") == False:
        print("RepList File NOT Found! Creating File 'list.txt'")
        file = open("data/rep/list.txt", "w")
        file.write("TestID:0")
        file.close()
    file = open("data/rep/list.txt", "r+")
    filer = file.read();
    file.close()
    repget1 = filer.split(';')
    for repgets in repget1:
        repgets2 =  repgets.split(':')
        repget2[repgets2[0]] = str(repgets2[1])
    repl = repget2
def setrepstore():
    filecon = ""
    for key in repl:
        if filecon == "":
            filecon = filecon + "" + key + ":" + str(repl[key])
        else:
            filecon = filecon + ";" + key + ":" +str(repl[key])
    file = open("data/rep/list.txt", "w")
    file.truncate()
    file.write(filecon)
    file.close()
def repget(msg):
    endno = 0
    endmsg = msg
    for no in range(0,100):
        if "[#"+str(no)+"]" in msg:
            endno = no
            endmsg = msg.replace("[#"+str(no)+"]","",1)
    return endmsg,endno


#about
if os.path.isdir("data/roles") == False:
    print("roles Folder NOT Found! Creating Dir '/roles'")
    os.mkdir("data/roles")
if os.path.exists("data/roles/admin.txt") == False:
    cmde = ""
    for cmded in cmds:
        cmde = cmde + ";"+cmded
    cmde2 = cmde.replace(";","",1)
    print("AdminList File NOT Found! Creating File 'admin.txt'")
    file = open("data/roles/admin.txt", "w")
    file.write("")
    file.close()
admins = ["test"]
admins.clear()
file = open("data/roles/admin.txt", "r+")
admins = file.read().split(";")
file.close()
if os.path.exists("data/roles/ban.txt") == False:
    cmde = ""
    for cmded in cmds:
        cmde = cmde + ";"+cmded
    cmde2 = cmde.replace(";","",1)
    print("ban File NOT Found! Creating File 'ban.txt'")
    file = open("data/roles/ban.txt", "w")
    file.write("")
    file.close()
bans = ["test"]
bans.clear()
file = open("data/roles/ban.txt", "r+")
bans = file.read().split(";")
file.close()

#config
def getconfig(configloc):
    cget1 = [""]
    cget1.clear()
    cget2 = {"":""}
    cget2.clear()
    if os.path.isdir("data") == False:
        print("Data Folder NOT Found! Creating Dir '/config'")
    os.mkdir("data")
    if os.path.exists("config/"+ configloc) == False:
        print("ScammerNumber File NOT Found! Creating File 'nos.txt'")
        file = open("data/" + configloc, "w")
        file.close()
        file = open("config/token.txt", "r+")
        filer = file.read();
        file.close()
        cget1 = filer.split(';')
        for cgets in cget1:
            cgets2 = cgets.split(":")
            cget2.add(cgets2[0],cgets2[1])
        return cget2
    
def getconfigitem(config,configitem):
    return config[configitem]
        

print('PathedCmds')
for cmder in cmds2:
    print('---'+ "!"+cmder)

#AiGetMsg

def updateaistore():
    global airesp
    airesp = {"":""}
    airesp.clear()
    #print("Updating DataStore: AIRESP")
    aiget1 = [""]
    aiget1.clear()
    aiget2 = {"":""}
    aiget2.clear()
    if os.path.isdir("data") == False:
        print("Data Folder NOT Found! Creating Dir '/data'")
        os.mkdir("data")
    if os.path.isdir("data/ai") == False:
        print("airesp Folder NOT Found! Creating Dir '/ai'")
        os.mkdir("data/ai")
    if os.path.exists("data/ai/airesp.txt") == False:
        print("Ai-Response File NOT Found! Creating File 'airesp.txt'")
        file = open("data/ai/airesp.txt", "w")
        file.write("test:What are you testing [@men]?")
        file.close()
    file = open("data/ai/airesp.txt", "r+")
    filer = file.read();
    file.close()
    aiget1 = filer.split(';')
    for aigets in aiget1:
        aigets2 = aigets.split(":")
        if "/" in aigets2[0]:
            resp = aigets2[1]
            aigets3 = aigets2[0].split("/")
            for trig in aigets3:
                aiget2[trig] = resp

        else:
            aiget2[aigets2[0]] = aigets2[1]
    airesp = aiget2

updateaistore()
updaterepstore()

#print(airesp)

#Role Setup

def timezone():
    c = ""
    if (int(time.timezone / -(60*60) > -1)) :
        c = "+"
    return "GMT"+c+str(int(time.timezone / -(60*60)))



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=motd))
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('')
    print('')
    print('LOG:')
    print('------------------------------')
   
    
    #Role Setup
    rolecount = 1

@client.event
async def on_message(msg):
    if (msg.author.id in bans):
        print(msg.author.id + "  Attepted to Use Bot. Exception: 'Banned'")
        return



    #AI:
    if ((mode == "1")):
    
        acc = False
    else:
        if (selfbot):
            acc = True
        else:
            acc = False
    runai = False
    if (client.user.id == msg.author.id)==acc:
        runai = True
    else:
        runai = False
    if (serrest):
        print(str(msg.server.id))
        if (str(msg.server.id) in serget):
            runai = True
        else:
            print("MessageExeption: Server Bad")
            runai = False

    


    
                   

    
    if (msg.content.startswith(i) == False):
        if (runai):
            aimsg = msg.content
            aimsg = aimsg.replace(".","")
            aimsg = aimsg.replace("?","")
            aimsg = aimsg.replace("!","")
            aimsg = aimsg.replace("#","")
            aimsg1 = aimsg.split(' ')
            print("AI:")
            print("--Input: '" + msg.content.lower() +"'")
            keys = ["",""]
            keys.clear()
            x2keys = ["",""]
            x2keys.clear()
            for key in airesp:
                if "+" not in key:
                    keys.append(key)
                else:
                    x2keys.append(key)
            sub = True
            awn = ""
            
            for keyz in x2keys:
                
                keyy = keyz.split("+")
                
                count = 0
                for keyx in keyy:
                    
                    if (keyx in aimsg1):
                        
                        count = count +1

                if count == len(keyy):
                    awn = airesp[keyz]
                    sub = False
                        
 
            for word1 in aimsg1:
                if sub:
                    if word1 in keys:
                        awn = airesp[word1]  

            if (msg.author.id in repl) == False:
                if (enablenewrepmsg):
                    awn = newrep
                repl[msg.author.id] = 0
                setrepstore()
                
            repl[msg.author.id] = str(int(repl[msg.author.id]) + 1)
            setrepstore()

            awn , repno = repget(awn)
            awns = awn.split("~");
            awn1 = awns[0]
            if (int(int(repl[msg.author.id])/msgperlev)) < repno:
                awn1 = awns[1]



            awn1 = awn1.replace('[%3A]',":")
            awn1 = awn1.replace('[%3A]',":")
            awn1 = awn1.replace('[%3B]',";")
            awn1 = awn1.replace('[%2B]',"+")
            awn1 = awn1.replace('[%2F]',"/")
            legdis = awn1
            awn1 = awn1.replace('[@men]',msg.author.mention)
            awn1 = awn1.replace('[@tim]',time.strftime("%H:%M:%S"))
            awn1 = awn1.replace('[@dat]',time.strftime("%d/%m/%Y"))
            awn1 = awn1.replace('[@tiz]',timezone())
            awn1 = awn1.replace('[rep2]',timezone())
            
            if awn1 == "":
                print("--Output: " +"No AI Resp Found")

            else:
                print("--Output : '" + awn1+"'")
                awn1 = awn1.replace('[@n]',"\n")

                
                await client.send_typing(msg.channel)
                #typeholddis
                
                sleeptime = len(legdis)/wordspersec
                if (sleeptime > 5):
                    sleeptime = 5
                if (delaymsg == False):
                    sleeptime = 0
                print("--TDelay : " + str(sleeptime) + "s")
                print("--RepP  : " + repl[msg.author.id])
                

                await asyncio.sleep(sleeptime)
                
                
                
                await client.send_message(msg.channel,awn1)

    
 #Update MOTD
    await client.change_presence(game=discord.Game(name=motd))
##Commands
    if msg.content.startswith(i):
      if (serrest):
        print(str(msg.server.id))
        if (str(msg.server.id) in serget):
            runai = True
        else:
            print("MessageExeption: Server Bad")
            return
            
      args = msg.content.replace(i, '', 1) .split(' ')
      men = msg.author.mention + "\n"
      if args[0] in cmds2:
        print(i + args[0] + "----")
        for words in args:
          print("  -" + words)
        print("--------------")

        alen = len(args)
    
        if args[0] == "test":
          await client.send_message(msg.channel, 'Hello ' + msg.author.mention + '. I am Working Fine')
        if args[0] == "shutdown":
            if (msg.author.id in admins)== False:
                await client.send_message(msg.channel,noperm)
                return
            await client.send_message(msg.channel, 'GTG! ')
            time.sleep(1)
            await client.send_message(msg.channel, 'cya')
            #await asyncio.sleep(1)
            await client.delete_message(msg)
            print("Shuting-Down")
            time.sleep(1)
            print("Loging-Out")
            client.logout()
            time.sleep(1)
            print("Loged-Out")
            time.sleep(2)
            print("Exiting Bot")
            print("Session Ended! Goodbye!")
            os._exit(0)
        if args[0] == "reload":
            args.append("")
            args.append("")
            args.append("")
            sub = True
            if args[1] == "data":
                    if args[2] == "ai":
                        msgg1 = await client.send_message(msg.channel,men + "Reloading Data Store: AI")
                        updateaistore()
                        msgg2 = await client.send_message(msg.channel,men + "Task Compleate")
                        sub = False
                        await asyncio.sleep(rmdelay)
                        await client.delete_message(msg)
                        await client.delete_message(msgg1)
                        await client.delete_message(msgg2)

            if sub:
                test88989 = ""
                msgg = await client.send_message(msg.channel,men + "Use: !reload <data|config> <name>")
                test88989 = ""
                await asyncio.sleep(rmdelay)
                test88989 = ""
                await client.delete_message(msg)
                await client.delete_message(msgg)
                test88989 = ""

        if args[0] == "speak":
            argsl = ""
            for num in args:
                argsl = argsl +num + " "
            arsgl2 = argsl.replace("speak","",1)
            await client.send_message(msg.channel, arsgl2)
        if args[0] == "help":
          await client.send_message(msg.author, 'Yep You Need it ' + msg.author.mention + '!')

          
        if args[0] == "tell":
            if (msg.author.id in admins):
                argli = ""
                args.append("")
                args.append("")
                if args[1] == "":
                    await client.send_message(msg.channel,"Use:  " + i + "tell <person(Mention)> <msg>")
                if args[2] == "":
                    await client.send_message(msg.channel,"Use:  " + i + "tell <person(Mention)> <msg>")
                for argin in args:
                    argli = argli + argin + " "
                    argli = argli.replace(args[0],'',1)
                    argli = argli.replace(args[1],'',1)
                if (msg.mentions[0].id == client.user.id):
                    await client.send_message(msg.channel,"Erm. I cant send a Dm to my-self")
                else:
                    await client.send_message(msg.mentions[0],argli)
            else:
                await client.send_message(msg.channel,noperm)
                print(msg.author.id + "  Attepted to Use Bot. Exception: 'No Perm'")
        if args[0] == "badmin":
            if (msg.author.id in admins)== False:
                await client.send_message(msg.channel,noperm)
                print(msg.author.id + "  Attepted to Use Bot. Exception: 'No Perm'")
                return
            
            args.append("")
            args.append("")
            if args[1] == "":
                await client.send_message(msg.channel,"Use:  " + i + "badmin <ADD|RM|LIST> <person(Mention)>")
            if args[1] == "add":
                if msg.mentions[0].id in admins:
                    await client.send_message(msg.channel,"They are already an admin")
                    return
        
                admins.append(msg.mentions[0].id)
                filecon = ""
                for admin in admins:
                    if filecon == "":
                        filecon = filecon + "" + admin
                    else:
                        filecon = filecon + ";" + admin
                file = open("data/roles/admin.txt", "w")
                file.truncate()
                file.write(filecon)
                file.close()
                await client.send_message(msg.channel,"Added:" + "<@" +msg.mentions[0].id+">" + "   To Admins")
            if args[1] == "rm":
                if msg.mentions[0].id in admins:
                    admins.remove(msg.mentions[0].id)
                    filecon = ""
                    for admin in admins:
                        if filecon == "":
                            filecon = filecon + "" + admin
                        else:
                            filecon = filecon + ";" + admin
                    
                    file = open("data/roles/admin.txt", "w")
                    file.truncate()
                    file.write(filecon)
                    file.close()
                    await client.send_message(msg.channel,"Removed:" + "<@" +msg.mentions[0].id+">" + "   From Admins")
                else:
                    await client.send_message(msg.channel,"That person is not an admin")
            if args[1] == "list":
                msgcon = "Admins:"
                for admin in admins:
                    msgcon = msgcon + "\n" + msg.server.get_member(admin).name
                await client.send_message(msg.channel,msgcon)
                
        if args[0] == "bban":
            if (msg.author.id in admins)== False:
                await client.send_message(msg.channel,noperm)
                print(msg.author.id + "  Attepted to Use Bot. Exception: 'No Perm'")
                return
            
            args.append("")
            args.append("")
            if args[1] == "":
                await client.send_message(msg.channel,"Use:  " + i + "bban <ADD|RM|LIST> <person(Mention)>")
            if args[1] == "add":
                if msg.mentions[0].id in bans:
                    await client.send_message(msg.channel,"They are already Banned")
                    return
        
                bans.append(msg.mentions[0].id)
                filecon = ""
                for banee in bans:
                    if filecon == "":
                        filecon = filecon + "" + banee
                    else:
                        filecon = filecon + ";" + banee
                file = open("data/roles/ban.txt", "w")
                file.truncate()
                file.write(filecon)
                file.close()
                await client.send_message(msg.channel,"Added:" + "<@" +msg.mentions[0].id+">" + "   To banned")
            if args[1] == "rm":
                if msg.mentions[0].id in bans:
                    bans.remove(msg.mentions[0].id)
                    filecon = ""
                    for banee in bans:
                        if filecon == "":
                            filecon = filecon + "" + banee
                        else:
                            filecon = filecon + ";" + banee
                    
                    file = open("data/roles/ban.txt", "w")
                    file.truncate()
                    file.write(filecon)
                    file.close()
                    await client.send_message(msg.channel,"Removed:" + "<@" +msg.mentions[0].id+">" + "   From banned")
                else:
                    await client.send_message(msg.channel,"That person is not banned")        
            if args[1] == "list":
                msgcon = "Bans:"
                print(bans)
                for banee in bans:
                    print(msgcon)
                    print(banee)
                    msgcon = msgcon + "\n" + "-" + msg.server.get_member(banee).name
                await client.send_message(msg.channel,msgcon)    
                


        
       
      else:
        await client.send_message(msg.channel, men + "Sorry, I do not understand the command '!" + args[0] + "'   For Commands, Usage and Help do '!help'")
   

if mode == "1":
    client.run(token)
if mode == "2":
    client.run(token,tpass)

