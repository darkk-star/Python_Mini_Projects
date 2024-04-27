pwd = input("Enter master password: ")


def view():
    file = open('pwds.txt','r')

    for line in file.readlines():
        data=line.rstrip()
        user,pss = data.split("|")
        print("user: ",user," password: ",pss)

def add():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open('pwds.txt','a')
    file.write(username + "|" + password + "\n")
    file.close()
    pass

while(True):
    mode = input("would you like to add new password or see existing ones(view/add) or q to quit: ")
    if(mode == "q"):
        break

    if(mode=="view"):
        view()

    elif(mode == "add"):
        add()

    else:
        print("Invalis mode")
        continue

