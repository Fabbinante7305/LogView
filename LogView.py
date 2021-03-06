from datetime import datetime
import os
import colorama
from colorama import Fore, Back, Style
from pathlib import Path
import sys

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

# Colored print functions

colorama.init()

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#This is the function that will display the menu

#modeSelect here is set as a global variable so that its value can be read in modes 1-4

modeSelect = ""

def menu():
    print(Fore.LIGHTGREEN_EX)
    print("\n**************************************************")
    print("**************************************************")

    print("**             [  1  ] Edit Today               **\n**             [  2  ] View Past                **\n**             [  3  ] Today's History          **\n**             [  4  ] Search                   **\n**             [ENTER] Exit                     **")
    print("**************************************************")
    print("**************************************************")
    print(Fore.WHITE)
    global modeSelect 
    modeSelect = input()

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#This sections is responsible for storing the main path to the log files and creating a file to store your password.

#generalPath holds the path to the directory which will hold all of the log files and the password file

#passwordLocation is a file within the generalPath directory that holds your entry password

#passwordCreationState holds a boolean value for whether or not the password file has been created

#passwordInput is the user input when CREATING a NEW password

#passwordCheck is the user input to double check that the password they chose to create is their truly desired one

#passwordFile is the file that holds the password

#passwordState holds a boolean value for whether or not the user typed in the correct password on entry

#inputPassword is the user input when typing the EXISTING/RECORDED password on entry

#password = the actual password that is stored in passwordFile
generalPath = r"C:\Users\ecoce\OneDrive\MyLog\\"
passwordLocation = generalPath+"Password.txt"

if not os.path.exists(generalPath):
    os.makedirs(generalPath)

#created= os.stat('file.txt').st_ctime


passwordCreationState = False
while passwordCreationState == False:
    if not os.path.exists(passwordLocation):
        passwordInput = input("Please enter the password that you want to use for log entry:   ")
        passwordCheck = input("\nAre you sure you want your password to be "+passwordInput+"?\nType 'y' for YES\nType 'n' for NO\t")
        if((passwordCheck == 'y') or (passwordCheck == 'Y')):
            passwordFile = open(passwordLocation,encoding="utf8",mode='a+')
            passwordFile.write(passwordInput)
            passwordCreationState = True
            passwordFile.close()
        else:
            passwordCreationState = False
    else:
        passwordCreationState=True

if os.path.exists(passwordLocation):    
    passwordState = False
    while passwordState != True:
        print(Fore.WHITE)
        print("Enter Password: " + Fore.BLACK)
        inputPassword = input()
        passwordFile = open(passwordLocation,encoding="utf8",mode='r')
        password = passwordFile.read()
        if inputPassword == password:
            passwordState == True
            break
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#This section sets up the main menu prompt

#modeSelect is the user input for the desired mode shown in the main menu

#date holds the date object as "2020-10-11 12:45:21.784683"

#year holds the year value from the date object as "2020"

#day holds the day value from the date object as "11"

#month holds the month value from the date object as "October"

#today holds the file name of the current month-year log as "C:\Users\ecoce\OneDrive\MyLog\\October2020.txt"

#todayLoggedState holds a boolean value for if the user has already logged the current day's date
    
    
    menu()
    while(modeSelect != ""):
        date = datetime.now()
        year = date.strftime('%Y')
        day = date.strftime('%d')
        month = date.strftime('%B')
        today = generalPath+month+year+".txt"
        todayLoggedState = False

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#Mode 1 allows the user to log the current day's log entry

#txtList holds all of the .txt files in the generalPath directory

#todayFileState holds a boolean for if there is already a created text file for the current month-year

#todayFile is the file that holds the current month-year log

#todayFileContent holds the content within todayFile

#entryInput holds the user input for what they want logged on the current day

#entryInputAppend opens the current month-year file and appends entryInput along with the datestamp

        if modeSelect == '1':                                                                                                   
            txtList = []
            todayFileState = False

            for i in os.listdir(generalPath):
                if i.endswith(".txt"):
                    txtList.append(i)

            for j in txtList:
                if((month in j)and(year in j)):
                    todayFileState = True
            if(todayFileState==True):
                todayFile = open(today,encoding="utf8",mode='r+')
                todayFileContent = []
                for k in todayFile:
                    todayFileContent.append(k)
                todayFile.close()
                for l in range(len(todayFileContent)):
                    if ((str(day)+',' in todayFileContent[l])and(month in todayFileContent[l])and(year in todayFileContent[l])):
                        todayLoggedState = True
                if todayLoggedState == False:
                    print(Fore.LIGHTMAGENTA_EX + "\nEnter your log entry for " + month + "/" + day + "/"+ year)
                    print(Fore.LIGHTCYAN_EX)
                    entryInput = input()
                    entryInputAppend = open(today,'a+')
                    entryInputAppend.write("\n"+ month + " " + day + ", " + year + "\n")
                    entryInputAppend.write(entryInput)    
                    entryInputAppend.close()
                else:
                    prRed("\nYou have already logged an entry for " + month + "/" + day + "/"+ year)
                menu()
            else:
                print(Fore.LIGHTMAGENTA_EX + "\nEnter your log entry for " + month + "/" + day + "/"+ year)
                print(Fore.LIGHTCYAN_EX)
                entryInput = input()
                entryInputAppend = open(today,'a+')
                entryInputAppend.write("\n"+ month + " " + day + ", " + year + "\n")
                entryInputAppend.write(entryInput)    
                entryInputAppend.close()
                menu()
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#Mode 2 allows the user to search for a specific date (that has been obviously logged) and will display the corresponding entry

#txtList holds all of the .txt files in the generalPath directory

#validYear is a boolean that will be true if the user inputs a number AND if there is a file with that year in the generalPath

#invalidYear is another boolean that will essentially do the same thing as validYear however makes the nested loops less complicated 

#validMonth is a boolean that will be true if the user inputs a number AND if there is a file with that month in the generalPath

#invalidMonth is a boolean that will essentially do the same thing as validMonth however makes the nested loops less complicated 

#validDay is a boolean that will be true if the user inputs a number that makes sense according the month

#keepGoing holds the user input for whether the user wants to keep searching past dates or exit back to the menu

#desiredYearInput holds the user input for the desired year 

#desiredMonthInput holds the user input for the desired month

#desiredDayInput holds teh user input for the desired day

#isdigit is a boolean that will check to see if the user input for the day is a number

#pastFile holds a string that has the path and filename based off the user input for the desired month-year

#pastFileRead opens and reads pastFile into the buffer

#desiredLine holds the line number in pastFileRead where the desired day, month, and year is found

#pastFileContent stores what is read from pastFileRead

#foundState is a boolean that determines whether there is a log entry with the desired day

        elif modeSelect == '2':
            validDay = False
            validMonth = False 
            validYear = False
            keepGoingState = True
            keepGoing = ""
            desiredYearInput = ""
            desiredMonthInput = ""
            desiredDayInput = ""

            txtList = []
            for i in os.listdir(generalPath):
                if i.endswith(".txt"):
                    txtList.append(i)

            while keepGoingState == True:
                #YEAR CHECK
                invalidYear = False
                while validYear == False:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Enter the desired year ('2017' for example):")
                    print(Fore.WHITE)
                    desiredYearInput = input()
                    for j in txtList:
                        if ((desiredYearInput.isdigit())and(desiredYearInput in j)):
                            validYear = True
                            invalidYear = False
                            break
                        else:
                            invalidYear = True
                    if(invalidYear == True):
                        prRed("\nYou do not have any logs for the year "+desiredYearInput)       
                #MONTH CHECK
                invalidMonth = False
                while validMonth == False:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Enter the desired month ('January' for example):")
                    print(Fore.WHITE)
                    desiredMonthInput = input()
                    for k in txtList:
                        if ((desiredMonthInput in k)and(desiredYearInput in k)):
                            validMonth = True
                            invalidMonth = False
                            break
                        else:
                            invalidMonth = True
                    if(invalidMonth == True):
                        prRed("\nYou do not have any logs for the month "+desiredMonthInput)                        
                #DAY CHECK
                while validDay == False:
                    isdigit = False
                    while isdigit == False:
                        print(Fore.LIGHTYELLOW_EX)
                        print("Enter the desired day ('05' for example):")
                        print(Fore.WHITE)
                        desiredDayInput = input()
                        if desiredDayInput.isdigit():
                            desiredDayInput = int(desiredDayInput)
                            isdigit = True
                            break

                    if(desiredMonthInput == "January")or(desiredMonthInput =="March")or(desiredMonthInput =="May")or(desiredMonthInput =="July")or(desiredMonthInput =="August")or(desiredMonthInput =="October")or(desiredMonthInput =="December"):
                        if (desiredDayInput > 0) and (desiredDayInput <= 31):
                            validDay = True
                            break
                        else:
                            prRed("\nYou have entered an invalid day for the month of "+ desiredMonthInput)
                            validDay = False

                    if ((desiredMonthInput == "April")or(desiredMonthInput == "June")or(desiredMonthInput == "September")or(desiredMonthInput == "November")):
                        if (desiredDayInput > 0) and (desiredDayInput <= 30):
                            validDay = True
                            break
                        else:
                            prRed("\nYou have entered an invalid day for the month of "+ desiredMonthInput)
                            validDay = False

                    if desiredMonthInput == "February":
                        if (desiredDayInput > 0) and (desiredDayInput <= 28):
                            validDay = True
                            break
                        else:
                            prRed("\nYou have entered an invalid day for the month of "+ desiredMonthInput)
                            validDay = False

                #PRINTING THE DAY
                pastFile = generalPath + desiredMonthInput + desiredYearInput + ".txt"
                pastFileRead = open(pastFile,encoding="utf8")
                desiredLine = 0
                pastFileContent = []
                foundState = False
                for l in pastFileRead:
                    pastFileContent.append(l)
                for m in range(len(pastFileContent)):
                    if ((str(desiredDayInput)+',' in pastFileContent[m])and(desiredMonthInput.title() in pastFileContent[m])and(desiredYearInput in pastFileContent[m])):
                        desiredLine = m
                        foundState = True
                        break
                if(foundState == True):
                    print(Fore.WHITE)
                    print(pastFileContent[desiredLine] + "\n" +  pastFileContent[desiredLine+1])
                    validDay = False
                    validMonth = False 
                    validYear = False
                    print(Fore.LIGHTYELLOW_EX + "Would you like to read another day ('Y' or 'y' or 'N' or 'n')?")
                    print(Fore.WHITE)
                    keepGoing = input()
                    if keepGoing == "y" or keepGoing == "Y":
                        keepGoingState = True
                    else:
                        keepGoingState = False
                else:
                    prRed("You don't have a log for "+desiredMonthInput+" "+str(desiredDayInput)+", "+desiredYearInput)
                    break
            menu()
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

# Mode 3 will allow you to read the current day's past logs. For example, if the current day is January 03, 2020, you will be able to see your log entry for January 03, 2019/2018/etc.

#txtList holds all of the .txt files in the generalPath directory

#empty is a boolean that determines whether there are past entries of the current day

#pastMonthList is a list of all the files in the general path with the same month as the current month

#pastContentList will hold the content of each of the month files from pastMonthList

#pastFileRead is just the buffer that actually reads each month's file

#mergeList is just a big list that appends all the content in pastContentList
        elif modeSelect == '3':
            txtList = []
            pastMonthList = []
            mergeList = []
            
            print(Fore.LIGHTBLUE_EX + "\n************************************************************************************************************************************************************************************************************************************************")

            for i in os.listdir(generalPath):
                    if i.endswith(".txt"):
                        txtList.append(i)

            empty = False           
            for j in txtList:
                if (month in j)and(year not in j ):
                    empty= True
            if empty==False:
                print(Fore.LIGHTBLUE_EX + "\n************************************************************************************************************************************************************************************************************************************************\n")
                prRed("There are no past logs of today")
                print(Fore.LIGHTBLUE_EX + "\n************************************************************************************************************************************************************************************************************************************************\n")

       
            for k in txtList:
                if (month in k)and(year not in k ):
                    pastMonthList.append(k)
    
            for l in pastMonthList:        
                pastFileRead = open(generalPath+l,encoding="utf8")
                pastContentList = []
                for m in pastFileRead:
                    pastContentList.append(m)
                mergeList.append(pastContentList)

            for n in range(len(mergeList)):            
                for o in range(len(mergeList[n])):
                    if ((day+',' in mergeList[n][o])and(month in mergeList[n][o])):
                        print(Fore.WHITE)
                        print(mergeList[n][o]+"\n"+mergeList[n][o+1]+"\n")

            print(Fore.LIGHTBLUE_EX + "************************************************************************************************************************************************************************************************************************************************")

            menu()
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#txtList is a list with all the text files found in the generalPath directory

#searchValue holds the user input for the word or phrase they are wanting to scan for

#pastFileRead is the buffer that actually holds what is actually read from the the files

#pastContent stores what is being read from pastFileRead

#mergeList is just a big list that appends all the content in pastContentList
        elif modeSelect == '4':
            txtList = []
            mergeList = []
            pastContent = []
            searchCount = 0

            sortedDirectory = sorted(Path(generalPath).iterdir(), key = os.path.getctime)

            for i in sortedDirectory:
                if(i.suffix == ".txt"):
                    txtList.append(i)
            print(Fore.LIGHTYELLOW_EX)
            print("Enter what you want to search for:")
            print(Fore.WHITE)
            searchValue = input()
            for j in txtList:
                pastFileRead = open(j,encoding="utf8")
                for k in pastFileRead:
                    pastContent.append(k)
            mergeList.append(pastContent)

            for l in range(len(mergeList)):
                for m in range(len(mergeList[l])):
                    if((searchValue in mergeList[l][m])or(searchValue.title() in mergeList[l][m])or(searchValue.upper() in mergeList[l][m])or(searchValue.lower() in mergeList[l][m])):
                        searchCount = searchCount + 1

            prLightPurple("\n************************************************************************************************************************************************************************************************************************************************\n")
            
            for l in range(len(mergeList)):
                for m in range(len(mergeList[l])):
                    if((searchValue in mergeList[l][m])or(searchValue.title() in mergeList[l][m])or(searchValue.upper() in mergeList[l][m])or(searchValue.lower() in mergeList[l][m])):
                        date = mergeList[l][m-1]
                        entry = mergeList[l][m]
                        
                        # ex.) Hello World
                        if(searchValue.title() in mergeList[l][m]):
                            print(date+"\n"+entry.replace(searchValue.title(),"\033[44;23m"+searchValue+"\033[m"))
                        # ex.) [The exact way you typed it when prompted]
                        elif(searchValue in mergeList[l][m]):
                            print(date+"\n"+entry.replace(searchValue,"\033[44;23m"+searchValue+"\033[m"))
                        # ex.) HELLO WORLD
                        elif(searchValue.upper() in mergeList[l][m]):
                            print(date+"\n"+entry.replace(searchValue.upper(),"\033[44;23m"+searchValue+"\033[m"))
                        # ex.) hello world
                        elif(searchValue.lower() in mergeList[l][m]):
                            print(date+"\n"+entry.replace(searchValue.lower(),"\033[44;23m"+searchValue+"\033[m"))

            print(Fore.LIGHTCYAN_EX)
            print("You have " + str(searchCount) + " matches for " + searchValue + "\n")
            prLightPurple("\n************************************************************************************************************************************************************************************************************************************************")
            menu()
        else:
            menu()
