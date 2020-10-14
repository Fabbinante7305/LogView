from datetime import datetime
import os
import colorama
import sys
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
        inputPassword = input("\nEnter Password: ")
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

    modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")
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
                    entryInput = input("Enter your log entry for " + month + "/" + day + "/"+ year + "\n")
                    entryInputAppend = open(today,'a+')
                    entryInputAppend.write("\n"+ month + " " + day + ", " + year + "\n")
                    entryInputAppend.write(entryInput)    
                    entryInputAppend.close()
                else:
                    print("\nYou have already logged an entry for " + month + "/" + day + "/"+ year + "\n")
                modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")
            else:
                entryInput = input("Enter your log entry for " + month + "/" + day + "/"+ year + "\n")
                entryInputAppend = open(today,'a+')
                entryInputAppend.write("\n"+ month + " " + day + ", " + year + "\n")
                entryInputAppend.write(entryInput)    
                entryInputAppend.close()
                modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")
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
                    desiredYearInput = input("\nEnter the desired year ('2017' for example):\n")
                    for j in txtList:
                        if ((desiredYearInput.isdigit())and(desiredYearInput in j)):
                            validYear = True
                            invalidYear = False
                            break
                        else:
                            invalidYear = True
                    if(invalidYear == True):
                        print("\nYou do not have any logs for the year "+desiredYearInput+"\n")       
                #MONTH CHECK
                invalidMonth = False
                while validMonth == False:
                    desiredMonthInput = input("\nEnter the desired month ('January' for example):\n")
                    for k in txtList:
                        if desiredMonthInput in k:
                            validMonth = True
                            invalidMonth = False
                            break
                        else:
                            invalidMonth = True
                    if(invalidMonth == True):
                        print("\nYou do not have any logs for the month "+desiredMonthInput+"\n")                        
                #DAY CHECK
                while validDay == False:
                    isdigit = False
                    while isdigit == False:
                        desiredDayInput = input("\nEnter the desired day ('05' for example):\n")
                        if desiredDayInput.isdigit():
                            desiredDayInput = int(desiredDayInput)
                            isdigit = True
                            break

                    if(desiredMonthInput == "January")or(desiredMonthInput =="March")or(desiredMonthInput =="May")or(desiredMonthInput =="July")or(desiredMonthInput =="August")or(desiredMonthInput =="October")or(desiredMonthInput =="December"):
                        if (desiredDayInput > 0) and (desiredDayInput <= 31):
                            validDay = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desiredMonthInput+"\n")
                            validDay = False

                    if desiredMonthInput == "April"or"June"or"September"or"November":
                        if (desiredDayInput > 0) and (desiredDayInput <= 30):
                            validDay = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desiredMonthInput+"\n")
                            validDay = False

                    if desiredMonthInput == "February":
                        if (desiredDayInput > 0) and (desiredDayInput <= 28):
                            validDay = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desiredMonthInput+"\n")
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
                    print(pastFileContent[desiredLine+1])
                    validDay = False
                    validMonth = False 
                    validYear = False
                    keepGoing = input("\nWould you like to read another day ('Y' or 'y' or 'N' or 'n')?")
                    if keepGoing == "y" or keepGoing == "Y":
                        keepGoingState = True
                    else:
                        keepGoingState = False
                else:
                    print("You don't have a log for "+desiredMonthInput+" "+str(desiredDayInput)+", "+desiredYearInput)
                    break
            modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")
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
        
            for i in os.listdir(generalPath):
                    if i.endswith(".txt"):
                        txtList.append(i)

            empty = False           
            for j in txtList:
                if (month in j)and(year not in j ):
                    empty= True
            if empty==False:
                print("\nThere are no past logs of today")
       
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
                        print(mergeList[n][o]+"\n"+mergeList[n][o+1])
            modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")
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
            count = 0

            for i in os.listdir(generalPath):
                if(i.endswith('.txt')):
                    txtList.append(i)
            
            searchValue = input("Enter what you want to search for: \n")
            for j in txtList:
                pastFileRead = open(generalPath+j,encoding="utf8")
                for k in pastFileRead:
                    pastContent.append(k)
            mergeList.append(pastContent)

            for l in range(len(mergeList)):
                for m in range(len(mergeList[l])):
                    if(searchValue in mergeList[l][m]):
                        #print(mergeList[l][m-1]+"\n"+mergeList[l][m])
                        date = mergeList[l][m-1]
                        entry = mergeList[l][m]
                        colorama.init()
                        print(date+"\n"+entry.replace(searchValue,"\033[44;23m"+searchValue+"\033[m"))
            modeSelect = input("\n1: Edit Today\n2: View Past\n3: Today's History\n4: Search\n[ENTER]: Exit\n")




                


    


    


        
    
    
