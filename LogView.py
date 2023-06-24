
from datetime import datetime
import cmd
import os
from colorama import Fore, Back, Style
from tkinter import *
import tkinter
import colorama
from playsound import playsound
import multiprocessing
from pathlib import Path
from fpdf import FPDF
import re
import sys
import subprocess
import json
import glob
import atexit

colorama.init()
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))





def birthdayMenu():
    print(Fore.LIGHTCYAN_EX)
    print(r"""
           (        (
             ( )      ( )          (
      (       Y        Y          ( )
     ( )     |"|      |"|          Y
      Y      | |      | |         |"|                   BIRTHDAYS
     |"|     | |.-----| |---.___  | |                         
     | |  .--| |,~~~~~| |~~~,,,,'-| |                       [1] Add Birthday   
     | |-,,~~'-'___   '-'       ~~| |._                     [2] View Birthdays
    .| |~       // ___            '-',,'.  
   /,'-'     <_// // _  __             ~,\
  / ;     ,-,     \\_> <<_______________;_)
  | ;    {(_)} _,      . |================|
  | '-._ ~~,,,           | ,,             |
  |     '-.__ ~~~~~~~~~~~|________________|   
  |\         `'----------|
  | '=._                 |                       
  :     '=.__            |          
   \         `'==========|
    '-._                 |
        '-.__            |
             `'----------|""")

##################################################################################################################################



class Commands(cmd.Cmd):

    prompt = "(LOG) >> "
    generalPath = r"C:\Users\ecoce\OneDrive\MyLog\\"
    json_file_list = glob.glob(generalPath+"*.json")
    valid_months_list = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
    date = datetime.now()
    year = date.strftime('%Y')
    day = date.strftime('%d')
    month = date.strftime('%B')
    monthNum = date.month
    today = generalPath + month + "_" + year + ".txt"
    desiredDay = ""
    desiredMonth = ""
    desiredYear = ""
    modeSelect = ""
    todays_file = generalPath + month + "_" + year + ".json"

    def __init__(self):
        os.system('cls')
        print(Fore.LIGHTBLUE_EX)
        print(r"""

                              __
                            .d$$b
                          .' TO$;\
                         /  : TP._;                
                        / _.;  :Tb|                
                       /   /   ;j$j                
                   _.-"       d$$$$                  Welcome Francesco
                 .' ..       d$$$$;                
                /  /P'      d$$$$P. |\             
               /   "      .d$$$P' |\^"l
             .'           `T$P^'''''  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :\
                           ; 
    """)
        print(Fore.LIGHTWHITE_EX)
        super(Commands,self).__init__()
        f = open(self.todays_file,"r",encoding="utf-8")
        content = json.load(f)
        f.close()
        dictionary = {}
        content_int_list = []
        for k in content.keys():
            content_int_list.append(int(k))

        if(len(content.keys()) != (int(self.day) - 1)):

            for j in range(1,int(self.day)):
                if j not in content_int_list:
                    dictionary[str(j)] = "Not Recorded."

                    f = open(self.todays_file,"r",encoding="utf-8")
                    content = json.loads(f.read())
                    f.close()
                    content.update(dictionary)

                    f = open(self.todays_file,"w")
                    f.write(json.dumps(content))
                    f.close()

    def check_today_logged(self):
        f = open(self.todays_file,"r",encoding="utf-8")
        content = json.load(f)
        f.close()
        if(self.day in content):
            return True
        else:
            return False
        
    def do_get(self,line):
        line_split = line.split(" ")
        if(len(line_split)!=3):
            prRed("\nINCORRECT FORMATTING: 'get' takes exactly 3 parameters.\nSee help for more details\n")
        else:
            if(line_split[0] not in self.valid_months_list):
                prRed("\nINCORRECT FORMATTING: The month you provided was not valid\n")

            elif((line_split[1].isnumeric() == False)or(line_split[2].isnumeric() == False)):
                prRed("\nINCORRECT FORMATTING: The [Day] and [Month] fields must be numeric\n")

            else:

                desired_month = line_split[0]
                desired_day   = line_split[1]
                desired_year  = line_split[2]
                if os.path.exists(self.generalPath + desired_month + "_" + desired_year + ".json"):
                    f = open(self.generalPath+desired_month + "_"+desired_year+".json","r",encoding="utf-8")
                    content = json.load(f)
                    if(desired_day in content.keys()):
                        print("\n"+content[desired_day] +"\n")
                    else:
                        prRed("\nINVALID DAY\n")
                else:
                    prRed("\nYou do not have a file for the month of " + desired_month + " in the year " + desired_year+"\n")

        
    def help_get(self):
        prYellow("\nGets the log entry attributed to the [Month] [Day] [Year] that you specify")
        prYellow("\nEx.) (LOG) >> get June 05 2023\n")
        

    def do_journal(self,line):
        dictionary = {}
        if(os.path.exists(self.todays_file)):
            if(self.check_today_logged()):
                print("\nYou've already logged today but feel free to log again\n")
                print("BEFORE")
                f = open(self.todays_file,"r",encoding="utf-8")
                content = json.load(f)
                print(content[str(self.day)])
                print("\n\n")
                f.close()

                log = input("\nLog your day\n")
                dictionary[str(day)] = log
                
                f = open(self.todays_file,"r",encoding="utf-8")
                content = json.loads(f.read())
                f.close()
                content.update(dictionary)

                f = open(self.todays_file,"w")
                f.write(json.dumps(content))
                f.close()

            else:
                log = input("\nLog your day\n")
                dictionary[str(day)] = log
                
                f = open(self.todays_file,"r",encoding="utf-8")
                content = json.loads(f.read())
                f.close()
                content.update(dictionary)

                f = open(self.todays_file,"w")
                f.write(json.dumps(content))
                f.close()


    def help_journal(self):
        prYellow("\nLog today's entry\n")

    def do_history(self,line):
        print("\n")
        current_month_file_history = []
        for i in self.json_file_list:
            if ((i.__contains__(self.month))and not(i.__contains__(self.year))):
                current_month_file_history.append(i)
        
        for i in current_month_file_history:
            get_year_from_name = i.split("_")
            get_year_from_name = get_year_from_name[1].split(".")
            get_year_from_name = str(get_year_from_name[0])
            prPurple(get_year_from_name + "\n")
            f = open(i,"r",encoding="utf-8")
            content = json.load(f)
            f.close()
            print("  *\t"+content[self.day]+"\n")


    def help_history(self):
        prYellow("\n\nPrints out the events that occured on today's date but in past years.\n\nEx.)It is June 01, 2023\n\nYou run >> history\n\nYou will see the logs of the first of June for 2022, 2021, 2020, etc.\help n")

    def do_quit(self,line):
        sys.exit()

    def help_quit(self):
        prYellow("\nExit program\n")

    def do_exit(self,line):
        sys.exit()

    def help_exit(self):
        prYellow("\nExit program\n")

    def do_clear(self,line):
        os.system('cls')

    def help_clear(self):
        prYellow("\nClears the console\n")
""" 




modeSelect = ""
#mainMenu differs from menu becuase this is the very firt menu that performs the birthday check
def startup():
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


def ONE():
    txtList = []
    modeSelect_log = ""
    todayFileState = False
    todayLoggedState = False

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
            logMenuY()
            entryInput = input(":  ")
            entryInputAppend = open(today,'a+')
            entryInputAppend.write("\n" + month + " " + day + ", " + year + "\n")
            entryInputAppend.write(entryInput)    
            entryInputAppend.close()
            flag = True
            while(flag):
                print(Fore.LIGHTWHITE_EX)
                modeSelect_log = input("\n(LOG TODAY) >>  ")
                if((modeSelect_log == "back")or(modeSelect_log == "menu")):
                    menu()
                    flag = False
                elif(modeSelect_log == "help"):
                    print("\nYou are in the LOG TODAY menu\nValid Commands:\n\n[clear , back/menu]")
                elif(modeSelect_log == "clear"):
                    os.system('cls')
                    logMenuN()
                else:
                    print("\nInvalid Command\nType 'help' for valid commands")


        else:
            logMenuN()
            flag = True
            while(flag):
                print(Fore.LIGHTWHITE_EX)
                modeSelect_log = input("\n(LOG TODAY) >>  ")

                if((modeSelect_log == "back")or(modeSelect_log == "menu")):
                    menu()
                    flag = False
                elif(modeSelect_log == "help"):
                    print("\nYou are in the LOG TODAY menu\nValid Commands:\n\n[clear , back/menu]")
                elif(modeSelect_log == "clear"):
                    os.system('cls')
                    logMenuN()
                else:
                    print("\nInvalid Command\nType 'help' for valid commands")
    else:
        logMenuY()
        entryInput = input(":  ")
        entryInputAppend = open(today,'a+')
        entryInputAppend.write("\n"+ month + " " + day + ", " + year + "\n")
        entryInputAppend.write(entryInput)    
        entryInputAppend.close()
        logMenuN()
        flag = True
        while(flag):
            print(Fore.LIGHTWHITE_EX)
            modeSelect_log = input("\n(LOG TODAY) >>  ")
            if((modeSelect_log == "back")or(modeSelect_log == "menu")):
                menu()
                flag = False
            elif(modeSelect_log == "help"):
                print("\nYou are in the LOG TODAY menu\nValid Commands:\n\n[clear , back/menu]")
            elif(modeSelect_log == "clear"):
                os.system('cls')
                logMenuN()
            else:
                print("\nInvalid Command\nType 'help' for valid commands")


def TWO():
    pastEntryMenu()

    txtList = []
    for i in os.listdir(generalPath):
        if i.endswith(".txt"):
            txtList.append(i)

    def year():
        global desiredYear
        invalidYear = False
        validYear = False
        while(validYear == False):
            print(Fore.LIGHTYELLOW_EX)
            print("Enter the desired year ('2017' for example):")
            print(Fore.LIGHTWHITE_EX)
            input2 = input(">>  ")

            if(input2 == "back"):
                menu()
                desiredYear = ""
                desiredMonth = ""
                desiredDay = ""
                #validYear = True
                break

            elif(input2 == "exit"):
                sys.exit()

            else:
                desiredYear = input2
                for j in txtList:
                    if ((desiredYear.isdigit())and(int(desiredYear)>2000)and(desiredYear in j)):
                        validYear = True
                        invalidYear = False
                        #return True
                        month()
                    else:
                        invalidYear = True

                if(invalidYear == True):
                    prRed("\nYou do not have any logs for the year "+desiredYear)



    def month():
        global desiredMonth
        invalidMonth = False
        validMonth = False
        while validMonth == False:
            print(Fore.LIGHTYELLOW_EX)
            print("Enter the desired month ('January' for example):")
            print(Fore.LIGHTWHITE_EX)
            input2 = input(">>  ")

            if(input2 == "back"):
                year()
                validMonth = True
                keepGoingState = False
                break

            elif(input2 == "exit"):
                sys.exit()
            else:
                desiredMonth = input2
                for k in txtList:
                    if ((desiredMonth in k)and((desiredMonth=="January")or(desiredMonth=="February")or(desiredMonth=="March")or(desiredMonth=="April")or(desiredMonth=="May")or(desiredMonth=="June")or(desiredMonth=="July")or(desiredMonth=="August")or(desiredMonth=="September")or(desiredMonth=="October")or(desiredMonth=="November")or(desiredMonth=="December"))and(desiredMonth+"_"+desiredYear in k)):
                        validMonth = True
                        invalidMonth = False
                        #return True
                        day()
                    else:
                        invalidMonth = True
                if(invalidMonth == True):
                    prRed("\nYou do not have any logs for the month "+desiredMonth)

    def processing():

        #PRINTING THE DAY
        pastFile = generalPath + desiredMonth + "_" + desiredYear + ".txt"
        pastFileRead = open(pastFile,encoding="utf8")
        desiredLine = 0
        pastFileContent = []
        foundState = False
        for l in pastFileRead:
            pastFileContent.append(l)
        pastFileRead.close()
        for m in range(len(pastFileContent)):
            if ((str(desiredDay)+',' in pastFileContent[m])and(desiredMonth.title() in pastFileContent[m])and(desiredYear in pastFileContent[m])):
                desiredLine = m
                foundState = True
                break
        if(foundState == True):
            print(Fore.LIGHTWHITE_EX)
            print(pastFileContent[desiredLine] + "\n" +  pastFileContent[desiredLine+1])
            #validDay = False
            #validMonth = False 
            #validYear = False
            print("Would you like to edit this entry?\n")
            edit = input(">>  ")
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

            else:
                year()
        else:
            prRed("You don't have a log for " + desiredMonth+" "+str(desiredDay)+", "+desiredYear)





    def day():
        global desiredDay
        global desiredMonth
        global desiredYear
        validDay = False
        isdigit = False
        while validDay == False:
            while isdigit == False:
                print(Fore.LIGHTYELLOW_EX)
                print("Enter the desired day ('05' for example):")
                print(Fore.LIGHTWHITE_EX)
                input3 = input(">>  ")
                if(input3 == "back"):
                    month()
                    isdigit = True
                    validDay = True

                elif(input3 == "exit"):
                    sys.exit()

                else:
                    desiredDay = input3
                    if(desiredDay.isdigit()):
                        desiredDay = int(desiredDay)
                        isdigit = True
                        validDay = True
                        
                        
                    else:
                        prRed("\nPlease enter a valid day")
                        isdigit = False

        if(desiredMonth == "January")or(desiredMonth =="March")or(desiredMonth =="May")or(desiredMonth =="July")or(desiredMonth =="August")or(desiredMonth =="October")or(desiredMonth =="December"):
            if (desiredDay > 0) and (desiredDay <= 31):
                processing()
                validDay = True
                
            else:
                prRed("\nYou have entered an invalid day for the month of "+ desiredMonth)
                validDay = False

        if ((desiredMonth == "April")or(desiredMonth == "June")or(desiredMonth == "September")or(desiredMonth == "November")):
            if (desiredDay > 0) and (desiredDay <= 30):
                processing()
                validDay = True
                
            else:
                prRed("\nYou have entered an invalid day for the month of "+ desiredMonth)
                validDay = False

        if desiredMonth == "February":
            if (desiredDay > 0) and (desiredDay <= 28):
                processing()
                validDay = True
                
            else:
                prRed("\nYou have entered an invalid day for the month of "+ desiredMonth)
                validDay = False

        return desiredDay
    
    year()


def THREE():

    print()


    


    
	modeSelect_past = ""
	pastMenu()
	global month
	global day
	txtList = []
	pastMonthList = []
	mergeList = []
	output = ""
    
    
	for i in os.listdir(generalPath):
		if i.endswith(".txt"):
			txtList.append(i)

	empty = False           
	for j in txtList:
		if (month in j)and(year not in j ):
			empty= True
	if empty==False:
		prRed("There are no past logs of today")

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
				output = output + mergeList[n][o]+mergeList[n][o+1]+"\n\n"
				print(mergeList[n][o]+"\n"+mergeList[n][o+1]+"\n")
	flag = True
	while(flag):
		print(Fore.LIGHTWHITE_EX)
		modeSelect_past = input("\n(History) >>  ")

		if((modeSelect_past == "back")or(modeSelect_past == "menu")):
			menu()
			flag = False
		elif(modeSelect_past == "clear"):
			os.system('cls')
			pastMenu()
			for n in range(len(mergeList)):
				for o in range(len(mergeList[n])):
					if ((day+',' in mergeList[n][o])and(month in mergeList[n][o])):
						print(Fore.YELLOW)
						print(mergeList[n][o]+"\n"+mergeList[n][o+1]+"\n")
		elif(modeSelect_past == "pdf"):
			pdf = FPDF()
			pdf.add_page()
			pdf.set_font("Arial",size = 12)
			#pdf.cell(0,100,txt=bytes(output,'utf-32').decode('latin1','ignore'),align='C',border=1,ln=1)
			pdf.multi_cell(0,10,txt=bytes(output,'ansi').decode('utf8','ignore'),align='C',border=1)

			pdf.output(str(month) + "_" + str(day) + "_history.pdf")
			print("Today's history has been succesfully saved as a pdf")

		elif(modeSelect_past == "help"):
			print("\nYou are in the HISTORY menu\nValid Commands:\n\n[clear , menu/back , pdf]")
		else:
			print("\nInvalid Command\nType 'help' for valid commands")
               

        



def FOUR():
    modeSelect_search = ""
    modeSelect_search_com = ""
    flag = True
    searchMenu()
    while(modeSelect_search != "back"):
        print(Fore.LIGHTWHITE_EX)
        modeSelect_search = input("\n(Search) >> ")
        if(modeSelect_search == "::"):
            while(flag):
                modeSelect_search_com = input("\n(Search COM) >> ")
                if(modeSelect_search_com == "clear"):
                    flag=False
                    os.system('cls')
                    searchMenu()
                if(modeSelect_search_com=="search"):
                    FOUR()
                elif((modeSelect_search_com == "back")or(modeSelect_search_com == "menu")):
                    flag = False
                    menu()
                elif(modeSelect_search_com == "help"):
                    print("You are in the SEARCH menu\nValid Commands:\n\n[clear , menu/back , search]")
                    flag = False
                    FOUR()
                else:
                    print("Invalid Command\nType 'help' for valid commands")

        

        txtList = []
        mergeList = []
        pastContent = []
        searchCount = 0

        sortedDirectory = sorted(Path(generalPath).iterdir(), key = os.path.getctime)

        for i in sortedDirectory:
            if(i.suffix == ".txt"):
                txtList.append(i)

        print(Fore.GREEN)

        searchCount = 0
        valueList = []

        valueList = modeSelect_search.split(" ")  
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
        print("You have " + str(searchCount) + " matches for ' " + modeSelect_search + " '\n")
        prLightPurple("\n************************************************************************************************************************************************************************************************************************************************")
        FOUR()


def FIVE():
    birthdayMenu()
    modeSelect_birth = ""
    flag = True
    while(flag):
        print(Fore.YELLOW)
        modeSelect_birth = input("\n(BIRTHDAY) >>  ")

        if(modeSelect_birth == "1"):
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

        elif(modeSelect_birth == "2"):

            f = open(generalPath+"\Birthdays\Birthdays.txt",'r')
            content = f.readlines()
            MONTHS = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            Janlist = []
            Feblist = []
            Marlist = []
            Aprlist = []
            Maylist = []
            Junlist = []
            Jullist = []
            Auglist = []
            Seplist = []
            Octlist = []
            Novlist = []
            Declist = []
            for i in content:
                i = i.split(" ")

                if(i[2]=="January"):
                    Janlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="February"):
                    Feblist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="March"):
                    Marlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="April"):
                    Aprlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="May"):
                    Maylist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="June"):
                    Junlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="July"):
                    Jullist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="August"):
                    Auglist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="September"):
                    Seplist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="October"):
                    Octlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="November"):
                    Novlist.append(i[0]+" "+i[1] + " " + i[3].strip())
                if(i[2]=="December"):
                    Declist.append(i[0]+" "+i[1] + " " + i[3].strip())

            def displayBirthdays(LIST):
                if(LIST):
                    for i in LIST:
                        print("* " + i)
                else:
                    print("NONE")

            print("\n\t\t\t\t[ January ]\n")
            displayBirthdays(Janlist)
            print("\n\t\t\t\t[ February ]\n")
            displayBirthdays(Feblist)
            print("\n\t\t\t\t[ March ]\n")
            displayBirthdays(Marlist)
            print("\n\t\t\t\t[ April ]\n")
            displayBirthdays(Aprlist)
            print("\n\t\t\t\t[ May ]\n")
            displayBirthdays(Maylist)
            print("\n\t\t\t\t[ June ]\n")
            displayBirthdays(Junlist)
            print("\n\t\t\t\t[ July ]\n")
            displayBirthdays(Jullist)
            print("\n\t\t\t\t[ August ]\n")
            displayBirthdays(Auglist)
            print("\n\t\t\t\t[ September ]\n")
            displayBirthdays(Seplist)
            print("\n\t\t\t\t[ October ]\n")
            displayBirthdays(Octlist)
            print("\n\t\t\t\t[ November ]\n")
            displayBirthdays(Novlist)
            print("\n\t\t\t\t[ December ]\n")
            displayBirthdays(Declist)

        elif(modeSelect_birth =="help"):
             print("\nYou are in the BIRTHDAY menu\nValid Commands:\n\n[clear , menu/back ]")
        elif((modeSelect_birth == "back")or(modeSelect_birth == "menu")):
            flag = False
            menu()
        elif(modeSelect_birth == "clear"):
            os.system('cls')
            birthdayMenu()
        else:
            print("\nInvalid Command\nType 'help' for valid commands")



def SIX():
    global year
    modeSelect_stat = ""
    txtList = []
    monthOrder = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #Gets every .txt file
    for i in os.listdir(generalPath):
        if i.endswith(".txt"):
            txtList.append(i)

    pastYear = []
    for i in txtList:
        for j in range(1900,int(year)+1):
            if((str(j) in i )and(j not in pastYear)):
                pastYear.append(j)
    pastYear.sort()
    #pastYear stores a list of the years you have logged

    monthListSplit = []
    monthList = []

    for k in txtList:
        if (("January" in k)or("February" in k)or("March" in k)or("April" in k)or("May" in k)or("June" in k)or("July" in k)or("August" in k)or("September" in k)or("October" in k)or("November" in k)or("December" in k)):
            monthListSplit.append(k)
            monthList.append(k)

    monthListSplit.sort(key=lambda x: monthOrder.index(x.split('_')[0]))            

    statisticsMenu()
    flag2 = True
    while(flag2):
        print(Fore.LIGHTWHITE_EX)
        modeSelect = input("\n>>  ")
        if(modeSelect == "1"):
        
            count = 0
            for i in pastYear:
                for j in monthListSplit:
                    if(str(i)in j):

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

            print("YEARS LOGGED: " + str(len(pastYear)))

            print("Logged Entry Count: " + str(count))

            
      

        #THIS WILL SHOW A TREE VIEW OF THE HIERARCHY OF ENTRIES (WITH SEVERAL DIFFERENT WAYS TO SORT AND ORGANIZE)
        elif(modeSelect == "2"):
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

      
        
        #SUMMARIZE A MONTH TO GET THE HIGHLIGHTS
        elif(modeSelect == "3"):
            print("Available Years")
            for i in pastYear:
                print(i)
            year = input("Select the year:\n")
            yearmonthlist = []
            for k in txtList:
                if(year in k):
                    yearmonthlist.append(k)
            yearmonthlist.sort(key=lambda x: monthOrder.index(x.split('_')[0]))
            print("\n")
            for k in yearmonthlist:
                print(k.split('_')[0])

            month = input("Select the month:\n")

            # specify file path
            file_path = generalPath + month + "_" + year + ".txt"

            # open the file and read its contents
            with open(file_path, "r") as file:
                text = file.read()

            # tokenize the text into sentences
            sentences = sent_tokenize(text)

            # print the number of sentences
            num_of_sentences = (len(sentences))

            # create plain text parser object
            parser = PlaintextParser.from_file(file_path, Tokenizer("english"))

            # create LSA summarizer object
            summarizer = LsaSummarizer()

            # summarize the file and print the result
            summary = summarizer(parser.document, num_of_sentences/6) # 3 is the number of sentences to summarize
            for sentence in summary:
                print(sentence)

        elif(modeSelect == "back"):
            menu()
            flag2 = False
        elif(modeSelect == "exit"):
            sys.exit()
        elif(modeSelect == "clear"):
            os.system('cls')
            statisticsMenu()
        else:
            print("\n'" + modeSelect + "' is not a valid command")



def menu():
    os.system('cls')
    print(Fore.LIGHTBLUE_EX)
    print(r

                              __
                            .d$$b
                          .' TO$;\
                         /  : TP._;                [1] Daily Log
                        / _.;  :Tb|                [2] View/Edit Past Entry
                       /   /   ;j$j                [3] Today's History
                   _.-"       d$$$$                [4] Search  
                 .' ..       d$$$$;                [5] Birthdays
                /  /P'      d$$$$P. |\             [6] Statistics
               /   "      .d$$$P' |\^"l
             .'           `T$P^'''''  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :\
                           ; 
    )
    flag = True
    while(flag):
	    global modeSelect
	    print(Fore.LIGHTWHITE_EX)
	    modeSelect = input("(MENU) >>  ")
	    if(modeSelect == "1"):
	    	flag = False
	    	ONE()
	    elif(modeSelect == "2"):
	    	flag = False
	    	TWO()
	    elif(modeSelect == "3"):
	    	flag = False
	    	THREE()
	    elif(modeSelect == "4"):
	    	flag = False
	    	FOUR()
	    elif(modeSelect == "5"):
	    	flag = False
	    	FIVE()
	    elif(modeSelect == "6"):
	    	flag = False
	    	SIX()
	    elif(modeSelect == "exit"):
	    	flag = False
	    	sys.exit()
	    elif(modeSelect == "clear"):
	    	flag=False
	    	menu()
	    elif(modeSelect == "help"):
	    	print("\nYou are in the MAIN menu\nValid Commands:\n\n[clear , 1 , 2 , 3 , 4 , 5 , 6 , exit ]")

	    else:
	    	print("\nInvalid Command\nType 'help' for valid commands")


"""

class sound():
    p = multiprocessing.Process(target=playsound, args=("LoFi.mp3",))
    @staticmethod
    def __init__():
        sound.p.start()
    @staticmethod
    def close():
        sound.p.terminate()
        



if __name__ == "__main__":
    sound()
    atexit.register(sound.close)
    Commands().cmdloop()