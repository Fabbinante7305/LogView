from datetime import datetime
import os
from colorama import Fore, Back, Style
from tkinter import *
import tkinter
import colorama
from pathlib import Path
import re
import sys
import subprocess

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
generalPath = r"C:\Users\ecoce\OneDrive\MyLog\\"

date = datetime.now()
year = date.strftime('%Y')
day = date.strftime('%d')
month = date.strftime('%B')
monthNum = date.month
today = generalPath+month+year+".txt"

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

#This is the function that will display the menu

#modeSelect here is set as a global variable so that its value can be read in modes 1-4
modeSelect = ""

def menu():
    print(Fore.LIGHTBLUE_EX)
    print("\n****************************************************************************************************")
    print("****************************************************************************************************")
    print(Fore.CYAN)
    print("**                                     [  1  ] Edit Today                                         **\n**                                     [  2  ] View Past                                          **\n**                                     [  3  ] Today's History                                    **\n**                                     [  4  ] Search                                             **\n**                                     [  5  ] Add Birthday                                       **\n**                                     [ENTER] Exit                                               **")
    print(Fore.LIGHTBLUE_EX)
    print("****************************************************************************************************")
    print("****************************************************************************************************")
    print(Fore.LIGHTWHITE_EX)
    global modeSelect 
    modeSelect = input()


modeSelect = ""
def mainMenu():
    f = open(generalPath+"\Birthdays\Birthdays.txt",'r')
    fileRead = f.readlines()
    f.close()
    prPurple("Birthdays...")
    nearestBirthMonth = []

    for i in fileRead:
        #Separates First Name, Last Name, Month, and Day
        i_split = i.split()
        
        value = 0
        if(i_split[2] == "January"):
            value = 1
        if(i_split[2] == "February"):
            value = 2
        if(i_split[2] == "March"):
            value = 3
        if(i_split[2] == "April"):
            value = 4
        if(i_split[2] == "May"):
            value = 5
        if(i_split[2] == "June"):
            value = 6
        if(i_split[2] == "July"):
            value = 7
        if(i_split[2] == "August"):
            value = 8
        if(i_split[2] == "September"):
            value = 9
        if(i_split[2] == "October"):
            value = 10
        if(i_split[2] == "November"):
            value = 11
        if(i_split[2] == "December"):
            value = 12
        
        #Since we are looking for upcoming birthdays, we forget about the past months and get the current and future months
        
        if(value>=monthNum):
                if(value==monthNum):
                    if(i_split[3]>day):
                        nearestBirthMonth.append(value)
                else:
                    nearestBirthMonth.append(value)        
        

        #If it finds a match for a birthday on the current day of the current month and finds the last name as well as the first name, it will print the first and last name
        if((i_split[2] == month)and(i_split[3]==day)and(i_split[1]!='X')):
            prPurple(i_split[0]+ " "+ i_split[1])
        #If it finfds a match for a birthday on the current day of the current month and only finds the first name, it will print the first name
        if((i_split[2] == month)and(i_split[3]==day)and(i_split[1]=='X')):
                prPurple(i_split[0])
    
    #Gets the soonest month from the current month
    closestMonth = min(nearestBirthMonth)

    closestMonthStr = ""
    if(str(closestMonth) == "1"):
        closestMonthStr = "January"
    if(str(closestMonth) == "2"):
        closestMonthStr = "February"
    if(str(closestMonth) == "3"):
        closestMonthStr = "March"
    if(str(closestMonth) == "4"):
        closestMonthStr = "April"
    if(str(closestMonth) == "5"):
        closestMonthStr = "May"
    if(str(closestMonth) == "6"):
        closestMonthStr = "June"
    if(str(closestMonth) == "7"):
        closestMonthStr = "July"
    if(str(closestMonth) == "8"):
        closestMonthStr = "August"
    if(str(closestMonth) == "9"):
        closestMonthStr = "September"
    if(str(closestMonth) == "10"):
        closestMonthStr = "October"
    if(str(closestMonth) == "11"):
        closestMonthStr = "November"
    if(str(closestMonth) == "12"):
        closestMonthStr = "December"
    
    nearestBirthDay = []
    for i in fileRead:
        #Separates First Name, Last Name, Month, and Day
        i_split = i.split()
        #Searching within the nearest upcoming birthday month
        if(i_split[2]==closestMonthStr):
            if(closestMonthStr == month):
                if(int(i_split[3])>int(day)):
                    nearestBirthDay.append(i_split[3])
            else:
                nearestBirthDay.append(i_split[3])

    #Gets the soonest day on the soonest month for upcoming birthdays
    closestDay = min(nearestBirthDay)

    for i in fileRead:
        #Separates First Name, Last Name, Month, and Day
        i_split = i.split()

        #If it finds a match for a birthday on the current day of the current month and finds the last name as well as the first name, it will print the first and last name
        if((i_split[2] == closestMonthStr)and(i_split[3]==closestDay)and(i_split[1]!='X')):
            prPurple("\n Upcoming Birthday...\n "+i_split[0]+ " "+ i_split[1] + " " + closestMonthStr+ " " + closestDay)

        #If it finfds a match for a birthday on the current day of the current month and only finds the first name, it will print the first name
        if((i_split[2] == closestMonthStr)and(i_split[3]==closestDay)and(i_split[1]=='X')):
                prPurple("\n Upcoming Birthday...\n "+i_split[0]+ " " + closestMonthStr+ " " + closestDay)


    print(Fore.LIGHTBLUE_EX)
    print("\n****************************************************************************************************")
    print("****************************************************************************************************")
    print(Fore.CYAN)
    print("**                                     [  1  ] Edit Today                                         **\n**                                     [  2  ] View Past                                          **\n**                                     [  3  ] Today's History                                    **\n**                                     [  4  ] Search                                             **\n**                                     [  5  ] Add Birthday                                       **\n**                                     [ENTER] Exit                                               **")
    print(Fore.LIGHTBLUE_EX)
    print("****************************************************************************************************")
    print("****************************************************************************************************")
    print(Fore.LIGHTWHITE_EX)
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

passwordLocation = generalPath+"Password.txt"

if not os.path.exists(generalPath):
    os.makedirs(generalPath)
    subprocess.check_call(["attrib","+H",generalPath])

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
        print(Fore.LIGHTWHITE_EX)
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

    date = datetime.now()
    year = date.strftime('%Y')
    day = date.strftime('%d')
    month = date.strftime('%B')
    today = generalPath+month+"_"+year+".txt"

###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
    #CATCH UP
    from pathlib import Path
    chk_file = Path(today)
    if (chk_file.is_file()==False):
        file = open(today, "w")
        file.close()

    intDay = int(day)
    todayFile = open(today,encoding="utf8",mode='r+')
    todayFileContent = []
    for k in todayFile:
        todayFileContent.append(k)
    todayFile.close()
            
    entryInputAppend = open(today,'a+')

    #This will update the current month's log with unrecorded days in the event that you don't start on time. 
    #Example if you start logging on June 05, 2022, this will create 4 entries in June 2022 with "Not Recorded." in them. 
    if(((len(todayFileContent))==0)and(intDay>1)):
        for i in range(1,intDay):
            if(i<10):
                entryInputAppend.write("\n"+month + " 0" + str(i) + ", " + year + "\nNot Recorded.")
            else:
                entryInputAppend.write("\n"+month + " " + str(i) + ", " + year + "\nNot Recorded.")
        entryInputAppend.close()
    #This will get the last logged day in an entry. 
    #It's always going to be the second line from the bottom anyway
        lastLoggedLine = todayFileContent[len(todayFileContent)-2]
        lastLoggedDay = ""
        commaMark = 0

        for i in range(0,len(lastLoggedLine)):
            if("," in lastLoggedLine[i]):
                commaMark = i
                break

        firstDigit = lastLoggedLine[commaMark-2]
        secondDigit = lastLoggedLine[commaMark-1]
        lastLoggedDay = firstDigit + secondDigit

        lastLoggedDayNum = int(lastLoggedDay)

        if(int(day)-1 !=lastLoggedDayNum):
            entryInputAppend = open(today,'a+')
    
            for i in range(lastLoggedDayNum+1,int(day)):
                if(i<10):
                    entryInputAppend.write("\n"+month+" 0"+str(i) + ", "+year+"\nNot Recorded.")
                else:
                    entryInputAppend.write("\n"+month+" "+str(i) + ", "+year+"\nNot Recorded.")

            entryInputAppend.close()


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
    
    
    mainMenu()
    while(modeSelect != ""):
        date = datetime.now()
        year = date.strftime('%Y')
        day = date.strftime('%d')
        month = date.strftime('%B')
        today = generalPath+month+"_"+year+".txt"
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
                    entryInputAppend.write(month + " " + day + ", " + year + "\n")
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
                    print(Fore.LIGHTWHITE_EX)
                    desiredYearInput = input()
                    for j in txtList:
                        if ((desiredYearInput.isdigit())and(int(desiredYearInput)>2000)and(desiredYearInput in j)):
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
                    print(Fore.LIGHTWHITE_EX)
                    desiredMonthInput = input()
                    for k in txtList:
                        if ((desiredMonthInput in k)and((desiredMonthInput=="January")or(desiredMonthInput=="February")or(desiredMonthInput=="March")or(desiredMonthInput=="April")or(desiredMonthInput=="May")or(desiredMonthInput=="June")or(desiredMonthInput=="July")or(desiredMonthInput=="August")or(desiredMonthInput=="September")or(desiredMonthInput=="October")or(desiredMonthInput=="November")or(desiredMonthInput=="December"))and(desiredMonthInput+"_"+desiredYearInput in k)):
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
                        print(Fore.LIGHTWHITE_EX)
                        desiredDayInput = input()
                        if desiredDayInput.isdigit():
                            desiredDayInput = int(desiredDayInput)
                            isdigit = True
                            break
                        else:
                            prRed("\nPlease enter a valid day")
                            isdigit = False


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
                pastFile = generalPath + desiredMonthInput + "_" + desiredYearInput + ".txt"
                pastFileRead = open(pastFile,encoding="utf8")
                desiredLine = 0
                pastFileContent = []
                foundState = False
                for l in pastFileRead:
                    pastFileContent.append(l)
                pastFileRead.close()
                for m in range(len(pastFileContent)):
                    if ((str(desiredDayInput)+',' in pastFileContent[m])and(desiredMonthInput.title() in pastFileContent[m])and(desiredYearInput in pastFileContent[m])):
                        desiredLine = m
                        foundState = True
                        break
                if(foundState == True):
                    print(Fore.LIGHTWHITE_EX)
                    print(pastFileContent[desiredLine] + "\n" +  pastFileContent[desiredLine+1])
                    validDay = False
                    validMonth = False 
                    validYear = False
                    print("Would you like to edit this entry?\t")
                    edit = input()
                    if(edit == 'y'):
                    
                        def move_window(event):
                            root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

                        root = Tk()
                        root.overrideredirect(True)
                        ws = root.winfo_screenwidth()
                        hs = root.winfo_screenheight()
                        x = (ws/2) - (1000/2)
                        y = (hs/2) - (300/2)
                        root.geometry('%dx%d+%d+%d' % (1000, 300, x, y))
                        root['bg']='#1e1e1e'
                        title_bar = Frame(root, bg='#03dac5', relief='raised', bd=2,height=8)
                        close_button = Button(title_bar, text='X', bg='red', command=root.destroy)
                        window = Canvas(root, bg='#1e1e1e',)


                        def saveExit():
                            pastFileRead = open(pastFile,'r',encoding='utf-8')
                            pastFileReadLines = pastFileRead.readlines()
                            replaced_content = ""


                            i=0

                            for line in pastFileReadLines:
                                
                                if ((i==desiredLine+1)):
                                   new_line = editEntryBox.get(1.0,"end-1c").strip()+"\n"
                                else:
                                   new_line = line
                            
                                replaced_content = replaced_content + new_line
                                i = i+1
                            
                            pastFileRead.close()
                            write_file = open(pastFile,'w',encoding='utf-8')
                            write_file.write(replaced_content)
                            write_file.close()                    
                            root.destroy()

                        editEntryBox = Text(window, height=4, width=104,bg="#2e2e2e",fg="#FFFFFF")                    
                        label = Label(window, text = pastFileContent[desiredLine],bg="#1e1e1e",fg='#FFFFFF')
                    
                        label.config(font=("Courier",14,'bold'),height = 2)

                        editEntryBox.insert(END,pastFileContent[desiredLine+1])
                        saveExitButton = tkinter.Button(root,text = "Save and Exit",bg="#03dac5", command = saveExit)                        
                        label.place(x=90,y=30)
                        saveExitButton.place(x=450,y=240)
                        title_bar.pack(side=TOP, fill=X)
                        close_button.pack(side=RIGHT)
                        editEntryBox.place(x=80,y=80)
                        window.pack(expand=1, fill=BOTH)

                        title_bar.bind('<B1-Motion>', move_window)
                        root.attributes('-topmost',1)

                        root.mainloop()
                    ##############################################                    
                    print(Fore.LIGHTYELLOW_EX + "Would you like to read another day ('Y' or 'y' or 'N' or 'n')?")
                    print(Fore.LIGHTWHITE_EX)
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
                        print(Fore.YELLOW)
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
            print(Fore.GREEN)
            print("1.) Single Search")
            print("2.) Multi Search")
            searchType = input("Enter which search method you want to use\t")
            if(searchType == "1"):

                print("Enter what you want to search for:")
                print(Fore.LIGHTWHITE_EX)
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
                searchCount = 0
                print("Enter all the things that you are searching for in a particular entry:")
                valueList = []
                print(Fore.LIGHTWHITE_EX)
                searchValues = input()

                valueList = searchValues.split(" ")  
                valueListLength = len(valueList)                  

                for j in txtList:
                    pastFileRead = open(j,encoding="utf8")
                    for k in pastFileRead:
                        pastContent.append(k)
                mergeList.append(pastContent)
                singleSearchtruths = []
                for l in range(len(mergeList)):
                    for m in range(len(mergeList[l])):
                        for x in valueList:
                            if((x in mergeList[l][m])or(x.title() in mergeList[l][m])or(x.upper() in mergeList[l][m])or(x.lower() in mergeList[l][m])):
                                singleSearchtruths.append("True")
                            else:
                                singleSearchtruths.append("False")
                        if(singleSearchtruths.count("True")==len(singleSearchtruths)):
                            searchCount = searchCount + 1
                        singleSearchtruths.clear()


                prLightPurple("\n************************************************************************************************************************************************************************************************************************************************\n")

                Llist = []
                Mlist = []
                multiSearchtruths = []
                for l in range(len(mergeList)):
                    for m in range(len(mergeList[l])):
                        for x in valueList:
                            if((x in mergeList[l][m])or(x.title() in mergeList[l][m])or(x.upper() in mergeList[l][m])or(x.lower() in mergeList[l][m])):      
                                multiSearchtruths.append("True")
                            else:
                                multiSearchtruths.append("False")
                        if((multiSearchtruths.count("True"))==len(multiSearchtruths)):
                            Llist.append(l)
                            Mlist.append(m)
                        multiSearchtruths.clear()

                for u in range(0,len(valueList)):
                    for y in range(0,len(Llist)):
                        mergeList[Llist[y]][Mlist[y]] =  mergeList[Llist[y]][Mlist[y]].replace(valueList[u],"\033[44;23m"+valueList[u]+"\033[m")
                        mergeList[Llist[y]][Mlist[y]] =  mergeList[Llist[y]][Mlist[y]].replace(valueList[u].lower(),"\033[44;23m"+valueList[u]+"\033[m")
                        mergeList[Llist[y]][Mlist[y]] =  mergeList[Llist[y]][Mlist[y]].replace(valueList[u].title(),"\033[44;23m"+valueList[u]+"\033[m")
                        mergeList[Llist[y]][Mlist[y]] =  mergeList[Llist[y]][Mlist[y]].replace(valueList[u].upper(),"\033[44;23m"+valueList[u]+"\033[m")

                    while(u + 1<len(valueList)):
                        u = u+1

                for y in range(0,len(Llist)):
                    print(mergeList[Llist[y]][Mlist[y]-1])
                    print(mergeList[Llist[y]][Mlist[y]])

                print(Fore.LIGHTCYAN_EX)
                print("You have " + str(searchCount) + " matches for ' " + searchValues + " '\n")
                prLightPurple("\n************************************************************************************************************************************************************************************************************************************************")
                menu()

        elif modeSelect == '5':
            print(Fore.LIGHTMAGENTA_EX)
            print("Is the birthday today?\nType 'y' for YES\nType 'n' for NO\nHit [ENTER] to return to menu\t")
            today_or_not = input()
            if ((today_or_not == 'y')or(today_or_not == 'Y')):
                print("Enter the Person's First Name")
                first_name = input()
                print("Enter the person's second name (if not needed, type 'X')")
                last_name = input()
                f = open(generalPath+"\Birthdays\Birthdays.txt",'a')
                f.write("\n" + first_name + " " + last_name + " "+ month+ " " + day)
                f.close()
                menu()
            elif((today_or_not == 'n')or(today_or_not == 'N')):
                print("Enter the person's first name")
                first_name = input()
                print("Enter the person's last name (if not needed, type 'X')")
                last_name = input()
                print("Enter "+ first_name + " " + last_name + "'s" + " birthday month")
                birthday_month = input()
                print("Enter "+ first_name + " " + last_name + "'s" + " birth day")
                birth_day = input()
                f = open(generalPath+"\Birthdays\Birthdays.txt",'a')
                f.write("\n" + first_name + " " + last_name + " "+ birthday_month+ " " + birth_day)
                f.close()
                menu()
            else:
                menu()


        elif modeSelect == '6':
            txtList = []
            print("\n")
            monthOrder = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            for i in os.listdir(generalPath):
                if i.endswith(".txt"):
                    txtList.append(i)

            pastYear = []
            for i in txtList:
                for j in range(1900,int(year)+1):
                    if((str(j) in i )and(j not in pastYear)):
                        pastYear.append(j)
            pastYear.sort()

            monthListSplit = []
            monthList = []

            for k in txtList:
                if (("January" in k)or("February" in k)or("March" in k)or("April" in k)or("May" in k)or("June" in k)or("July" in k)or("August" in k)or("September" in k)or("October" in k)or("November" in k)or("December" in k)):
                    monthListSplit.append(k)
                    monthList.append(k)


            monthListSplit.sort(key=lambda x: monthOrder.index(x.split('_')[0]))            

            for i in pastYear:
                print(str(i))
                for j in monthListSplit:
                    if(str(i)in j):
                        print("\t"+j)

                        count = 0
                        finalCount = 0
                        xf =0
                        iterator = -1
                        
                        pastFileRead = open(generalPath+j,encoding="utf8")
                        pastContentList = []
                        for m in pastFileRead:
                            iterator = iterator+1
                            xf=xf+len(m)
                            if(("Not Recorded." not in m)and(iterator%2!=0)and(len(m)<=1024)):
                                count = count + 1
                            if(len(m)>1014):
                                count = count+1
                                iterator = iterator + 2
                            else:
                                count = count + 0

                        finalCount = count
                        print("\t\t"+str(finalCount) + " Logged Entries")
                        print("\t\t\tSize of File --> "+str(xf))

                        count = 0
                        finalCount = 0
                        iterator=-1
            menu()
                
        else:
            menu()
        
