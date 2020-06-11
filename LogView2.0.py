from datetime import datetime
import os
import sys

Location = "C:\MyLog\\"
Passowrd_Location = Location+"Password.txt"
#PASSWORD CHECK TO ACCESS THE REST OF THE APPLICATION
if not os.path.exists(Location):
    os.makedirs(Location)

password_creation = False
while password_creation == False:
    if not os.path.exists(Passowrd_Location):
        password = input("Please enter the password that you want to use for log entry:   ")
        yes1_or_no1 = input("\nAre you sure you want your password to be "+password+"?\nType 'y' for YES\nType 'n' for NO\t")
        if((yes1_or_no1 == 'y') or (yes1_or_no1 == 'Y')):
            password_file = open(Passowrd_Location,encoding="utf8",mode='a+')
            password_file.write(password)
            password_creation = True
            password_file.close()
        else:
            password_creation = False
    else:
        password_creation=True
if os.path.exists(Passowrd_Location):    
    password_state = False
    while password_state != True:
        password = input("\nEnter Password: ")
        passcode_open = open(Passowrd_Location,encoding="utf8",mode='r')
        passcode = passcode_open.read()
        if password == passcode:
            password_state == True
            break

    #TOP MENU AND VARIABLE SETUP
    edit_or_read = input("\n1: Edit Today\n2: View Past\n3: Today's History\n[ENTER]: Exit\n")
    while(edit_or_read != ""):
        #general_path = r"C:\Users\ecoce\Important Folders\Documents\My_Log\\"
        date = datetime.now()
        year = date.strftime('%Y')
        day = date.strftime('%d')
        month = date.strftime('%B')
        today = Location+month+year+".txt"
        today_logged_state = False

        #EDIT TODAY SECTION
        if edit_or_read == '1':
            file_list = []
            today_valid = False
            for today_file in os.listdir(Location):
                if today_file.endswith(".txt"):
                    file_list.append(today_file)
            for item in file_list:
                if((month in item)and(year in item)):
                    today_valid = True
            if(today_valid==True):
                desired_file = open(today,encoding="utf8",mode='r+')
                #desired_file= desired_file.readlines()
                file_content = []
                for line_1 in desired_file:
                    file_content.append(line_1)
                desired_file.close()
                for line_2 in range(len(file_content)):
                    if ((str(day)+',' in file_content[line_2])and(month in file_content[line_2])and(year in file_content[line_2])):
                        today_logged_state = True
                if today_logged_state == False:
                    daily_entry = input("Enter your log entry for " + month + "/" + day + "/"+ year + "\n")
                    edit_today = open(today,'a+')
                    edit_today.write("\n"+ month + " " + day + ", " + year + "\n")
                    edit_today.write(daily_entry)    
                    edit_today.close()
                else:
                    print("\nYou have already logged an entry for " + month + "/" + day + "/"+ year + "\n")
                edit_or_read = input("\n1: Edit Today\n2: View Past\n3: Today's History\n[ENTER]: Exit\n")
            else:
                daily_entry = input("Enter your log entry for " + month + "/" + day + "/"+ year + "\n")
                edit_today = open(today,'a+')
                edit_today.write("\n"+ month + " " + day + ", " + year + "\n")
                edit_today.write(daily_entry)    
                edit_today.close()
                edit_or_read = input("\n1: Edit Today\n2: View Past\n3: Today's History\n[ENTER]: Exit\n")


        #VIEW PAST SECTION
        elif edit_or_read == '2':
            valid_day = False
            valid_month = False 
            valid_year = False
            keep_going_state = True
            keep_going = ""
            desired_year = ""
            desired_month = ""
            desired_day = ""

            fileList = []
            for filename in os.listdir(Location):
                if filename.endswith(".txt"):
                    fileList.append(filename)

            while keep_going_state == True:
                #YEAR CHECK
                invalid_year = False
                while valid_year == False:
                    desired_year = input("\nEnter the desired year ('2017' for example):\n")
                    for filename_1 in fileList:
                        if ((desired_year.isdigit())and(desired_year in filename_1)):
                            valid_year = True
                            invalid_year = False
                            break
                        else:
                            invalid_year = True
                    if(invalid_year == True):
                        print("\nYou do not have any logs for the year "+desired_year+"\n")       
                #MONTH CHECK
                invalid_month = False
                while valid_month == False:
                    desired_month = input("\nEnter the desired month ('January' for example):\n")
                    for filename_2 in fileList:
                        if desired_month in filename_2:
                            valid_month = True
                            invalid_month = False
                            break
                        else:
                            invalid_month = True
                    if(invalid_month == True):
                        print("\nYou do not have any logs for the month "+desired_month+"\n")                        
                #DAY CHECK
                while valid_day == False:
                    isdigit = False
                    while isdigit == False:
                        desired_day_str = input("\nEnter the desired day ('05' for example):\n")
                        if desired_day_str.isdigit():
                            desired_day = int(desired_day_str)
                            isdigit = True
                            break
                    #desired_day = int(input("Enter the desired day ('05' for example):\n"))

                    if(desired_month == "January")or(desired_month =="March")or(desired_month =="May")or(desired_month =="July")or(desired_month =="August")or(desired_month =="October")or(desired_month =="December"):
                        if (desired_day > 0) and (desired_day <= 31):
                            valid_day = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desired_month+"\n")
                            valid_day = False

                    if desired_month == "April"or"June"or"September"or"November":
                        if (desired_day > 0) and (desired_day <= 30):
                            valid_day = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desired_month+"\n")
                            valid_day = False

                    if desired_month == "February":
                        if (desired_day > 0) and (desired_day <= 28):
                            valid_day = True
                            break
                        else:
                            print("\nYou have entered an invalid day for the month of "+ desired_month+"\n")
                            valid_day = False

                #PRINTING THE DAY
                past_file = Location + desired_month + desired_year + ".txt"
                desired_file = open(past_file,encoding="utf8")
                desired_line = 0
                file_content = []
                ready_for_print = False
                for line_1 in desired_file:
                    file_content.append(line_1)
                for line_2 in range(len(file_content)):
                    if ((str(desired_day)+',' in file_content[line_2])and(desired_month.title() in file_content[line_2])and(desired_year in file_content[line_2])):
                        desired_line = line_2
                        ready_for_print = True
                        break
                if(ready_for_print == True):
                    print(file_content[desired_line+1])
                    valid_day = False
                    valid_month = False 
                    valid_year = False
                    keep_going = input("\nWould you like to read another day ('Y' or 'y' or 'N' or 'n')?")
                    if keep_going == "y" or keep_going == "Y":
                        keep_going_state = True
                    else:
                        keep_going_state = False
                else:
                    print("You don't have a log for "+desired_month+" "+str(desired_day)+", "+desired_year)
                    break
            edit_or_read = input("\n1: Edit Today\n2: View Past\n3: Today's History\n[ENTER]: Exit\n")

        #VIEW HISTORY SECTION
        elif edit_or_read == '3':
            line=0
            fileList = []
            SpecificMonthList = []
            desired_pages = []
            section = []
        
            for filename in os.listdir(Location):
                    if filename.endswith(".txt"):
                        fileList.append(filename)
            empty = False           
            for item_1 in fileList:
                if (month in item_1)and(year not in item_1 ):
                    empty= True
            if empty==False:
                print("\nThere are no past logs of today")
       
            for item_2 in fileList:
                if (month in item_2)and(year not in item_2 ):
                    SpecificMonthList.append(item_2)
    
            for desired_month in SpecificMonthList:        
                desired_file = open(Location+desired_month,encoding="utf8")
                contentList = []
                for line_1 in desired_file:
                    contentList.append(line_1)
                desired_pages.append(contentList)

            for page in range(len(desired_pages)):            
                for line_1 in range(len(desired_pages[page])):
                    if ((day+',' in desired_pages[page][line_1])and(month in desired_pages[page][line_1])):
                        print(desired_pages[page][line_1]+"\n"+desired_pages[page][line_1+1])
            edit_or_read = input("\n1: Edit Today\n2: View Past\n3: Today's History\n[ENTER]: Exit\n")

        #elif edit_or_read == '4':    
            #change_yes_or_no = input("Are you sure that you want to change your password?\nType 'y' for YES\nType 'n' for NO\t")
            #if ((change_yes_or_no == 'y')or(change_yes_or_no == 'Y')):
             #   newpass = False
              #  while newpass == False:
               #     new_password = input("Enter your new password:\t")
                #    yes2_or_no2 = input("\nAre you sure you want your password to be "+new_password+"?\nType 'y' for YES\nType 'n' for NO\t")
                 #   if((yes2_or_no2 == 'y') or (yes2_or_no2 == 'Y')):
                  #      password_file = open(Passowrd_Location,encoding="utf8",mode='w')
                   #     password_file.write(new_password)
                    #    password_file.close()
                     #   newpass = True





                


    


    


        
    
    