import os

programPath = os.path.dirname(os.path.abspath(__file__))

os.chdir(programPath)
if not os.path.exists(programPath+'/battery-report.html'):
    os.system('powercfg /batteryreport')
else:
    if input("A battery-report.html file already exists, would you like to delete it?\n") in ["y","yes"]:
          os.system('del battery-report.html')
          os.system('powercfg /batteryreport')
    else:
        pass
os.system('cls')
    
HTMLFile = open(programPath+'/battery-report.html','r').read()

from bs4 import BeautifulSoup

contentsText = BeautifulSoup(HTMLFile, 'lxml')

def makeInt(scoopedSoup):
    scoopedInt = ""
    for words in scoopedSoup.find_next():
        for char in words:
                if char in ["0","1","2","3","4","5","6","7","8","9"]:
                    scoopedInt += char
    return int(scoopedInt)


maxDesignedCapacity = ""
maxChargeCapacity = ""

for text in contentsText.find_all(string=True):
    if text == "DESIGN CAPACITY":
        maxDesignedCapacity = makeInt(text)
    if text == "FULL CHARGE CAPACITY":
        maxChargeCapacity = makeInt(text)
            
print("your systems battery health is at:",round(maxChargeCapacity/maxDesignedCapacity*100,1),"%")
os.system('del battery-report.html')