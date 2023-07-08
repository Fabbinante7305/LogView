
from datetime import datetime
import cmd
import os
from colorama import Fore, Back, Style
from tkinter import *
import tkinter
import colorama
from alive_progress import alive_bar
from playsound import playsound
import multiprocessing
from pathlib import Path
from fpdf import FPDF
import sys
import time
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
        empty_dictionary = {}
        content = {}
        #COMMENT: If you've been logging in the current month, you obviously already have the json file for the month created so just take the contents of the file and if there are any days we've missed since last log, we account for that here too
        if(os.path.exists(self.todays_file)):
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

        #COMMENT: This case is for when you start a new month and you start it on the first day of it as opposed to checking for days that you've missed in the new month                
        elif(not(os.path.exists(self.todays_file)) and (int(self.day) == 1)):
            f = open(self.todays_file,"w",encoding="utf-8")
            print("The month's log file has been created.")
            f.close()


        #COMMENT: This case is for when you start a new month and a couple days have already passed so we update the json file to fill in "Not Recorded." for those days
        else:
            for i in range(1,int(self.day)-1):
                empty_dictionary[str(i)] = "Not Recorded."
            f = open(self.todays_file,"w",encoding="utf-8")
            json.dump(empty_dictionary,f)
            f.close()
            
            f = open(self.todays_file,"r",encoding="utf-8")
            content = json.load(f)
            f.close()
            for total in range(1):
                with alive_bar(total,bar="smooth") as bar:
                    for _ in range(int(self.day)-1):
                        time.sleep(.3)
                        bar()
            print("\nThe month's log file has been created")
            print("You have "+ str(int(self.day)-1) + " days uncaccounted for and they have been stored in the log as 'Not Recorded.'\n")
        

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
                dictionary[str(self.day)] = log
                
                f = open(self.todays_file,"r",encoding="utf-8")
                content = json.loads(f.read())
                f.close()
                content.update(dictionary)

                f = open(self.todays_file,"w")
                f.write(json.dumps(content))
                f.close()

            else:
                log = input("\nLog your day\n")
                dictionary[str(self.day)] = log
                
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
        prYellow("\n\nPrints out the events that occured on today's date but in past years.\n\nScenario: It is June 01, 2023 currently and you run \n(LOG) >> history\n\nYou will see the logs of June 01, 2022 & June 01, 2021, & so on\n")

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