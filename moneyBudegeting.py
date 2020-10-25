#!/home/baby/kivy_venv/bin/python3
import os,csv,datetime
class Budget:
    dictionary = {}
    def __init__(self,bank,money,spent=0):
        self.bank = bank
        self.money = money
        self.spent = spent
        self.directory = "/home/baby/Desktop/budget"
    #ask what the user wants to do
    def option(self):
        print("Welcome to the money budgeting program\n\tby:Claude Daigan\n")
        print("What do you want to do?\n(Please input a number)")

        choices = {
            1:"Read",
            2:"Write"
        }
        num = 0
        for c in choices:
            num += 1
            print(f"{num}.) {choices[c]}")
        print("\n")
        choice = input()
        self.listDir(choice)
        
    #print directory:
    def listDir(self,choice):
        menu = {}
        num = 0
        for files in os.listdir(self.directory):
            if files.endswith(".csv"):
                num += 1
                menu[num] = files
        print(f"There are {num} CSVs in '{self.directory}'")
        num = 0
        for c in menu:
            num += 1
            print(f"{num}.)  {menu[c]}")
        selected = input()
        chosen = menu[int(selected)]
        chosen_path = os.path.join(self.directory,chosen)
        if choice == "1":
            self.read(chosen_path)
        elif choice == "2":
            self.write(chosen_path)
        else:
            print("please input number")
        

    # option to read
    def read(self,choice):
        f = open(choice)
        reader = csv.reader(f)
        data = list(reader)
        for items in data:
            print(items)
        f.close()
            

    
        
    #option to write 
    def write(self,choice):
        f = open(choice,"w")
        writer = csv.writer(f)
        date = self.date()
        writer.writerow(["Date","bank","money","spent"])
        writer.writerow([date,self.bank,self.money,self.spent])
        f.close
        self.read(choice)




    #list directory

    #current standing of user for that day

    #date
    @staticmethod
    def date():
        today = datetime.datetime.now()
        date = today.strftime("%B %d,%Y")
        return date
         
        



    

def main():
    b = Budget(bank=3000,money=400,spent=300)
    b.option()
if __name__ == "__main__":
    main()