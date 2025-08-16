import psutil,ctypes, random,math,time,threading,tkinter as tk

def AvoidSleep():
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def DisplayBlack():
    root=tk.Tk()
    root.attributes("-fullscreen",True)
    root.configure(bg="black")
    root.bind("<Escape>",lambda e: root.destroy())
    root.mainloop()

def isPrime(n):
    if (n<2):
        return False
    if n%2==0 and n!=2:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True

def primeGen():
    while True:
        num=random.randint(10**6,10**7)
        if isPrime(num):
            pass
        time.sleep(0.001)


if __name__=="__main__":
    AvoidSleep()
    starttime=time.time()
    startbattery=psutil.sensors_battery().percent if psutil.sensors_battery() else None
    threading.Thread(target=primeGen,daemon=True).start()
    DisplayBlack()
    endtime=time.time()
    endbattery=psutil.sensors_battery().percent if psutil.sensors_battery() else None
    timeWorkdone=int(endtime-starttime)
    hours,rem=divmod(timeWorkdone,3600)
    mins,secs=divmod(rem,60)

    print(f"Total time run : \n Hours: {hours} \t Mins:{mins} \t Secs:{secs}\n")
    if startbattery is not None and endbattery is not None:
        print(f"Battery Drained (%): {startbattery-endbattery}")
    else:
        print("Unable to fetch Battery info :(")
    

