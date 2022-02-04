log_file = open("um-server-01.txt") #This is the way we open a file in python


def sales_reports(log_file): #Making a function called sales_reports that takes in log_file as an argument
    for line in log_file: #For in loop
        line = line.rstrip() #rstrip() method removes any charactesrs at the end of a string
        day = line[0:3] #We want to get in every line index from 0-3 back
        if day == "Tue": #Then we check if the day equals to Tuesday, if yes 
            print(line) #We print the line


sales_reports(log_file) #Getting all lines back that start with a Tuesday


#Change the script to display sales info for Monday instead of Tuesday.

log_file = open("um-server-01.txt") 


def sales_reports(log_file): 
    for line in log_file: 
        line = line.rstrip() 
        day = line[0:3] 
        if day == "Mon": 
            print(line) 


sales_reports(log_file) 