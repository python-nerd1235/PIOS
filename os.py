ver="dv_1.2"
num=0
try:
    command='SetupFail'
    def help():print('commands:\nhelp:\tshow help\nnew:\tnew file\nexec:\trun python file\nread:\tshow file contents\ninfo:\tshow info\nQ:\tQuit')
    def new(file,text):
        try:
            filet=open(file,"x")
            filet.write(text)
        except:print('err 04')
    def execy(file):
        try:
            e=open(file,"r")
            exec(e.read())
        except:print('err 03')   
    def read(file):
        o=open(file,"r")
        print(o.read())
    def info(file):
        t=open(file,"r")
        print(t)
    print('checking for log file...')
    try:
        log=open("commandLog","w")
        logTrue="log file alredy on disk."
    except:
        log=open("commandLog","x")
        logTrue="log file made."
    print(logTrue)
    print('welcome to pios!\nver: '+ver)
    
    while True:
        command=input("usr~$")
        if command=='help':
            help()
        elif command == 'new':
            new(input('file: '),input("text: "))
        elif command == 'read':
            try:read(input('file: '))
            except:print('err 01')
        elif command == 'exec':
            execy(input('file: '))
        elif command == 'info':
            try:info(input('file: '))
            except:print('err 01')
        elif command == 'Q':
            break
        else:
            print("err02")
        cl=command
        command="logFail"
        try:
            log=open("commandLog","x")
            log.write("log start\n<logEntry#"+str(num)+"command:"+cl+'ver:'+ver+'>' )
        except:
            log=open('commandLog',"a")
            log.write("<logEntry#"+str(num)+"command:"+cl+'>\n' )
        num+=1
except typeError:yy=input('pios has run in to a cratical error. send error report to dev on gethub.\n'+'-'*20+"\ncommandFail: "+command+' ver: '+ver)

