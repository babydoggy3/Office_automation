#!/home/baby/kivy_venv/bin/python
import csv,os,datetime
class Budget:
    def __init__(self,bank,money,spent=0):
        self.bank = bank
        self.money = money
        self.spent = spent
    
    #Total amount spent on that day
    def totalSpent(self):
        remaining = self.money - self.spent
        return f"Amount spent on {self.dateFunc()} is PHP{remaining}"
    #When did you withdraw and how much?
    def withdraw(self,cash):
        withdrawCash = self.bank -cash
        bankAmount = withdrawCash 
        return "remaining balance: {}\nWithdrawn: {}".format(bankAmount,cash)
    #returns the date
    def dateFunc(self):
        today = datetime.date.today()
        date = today.strftime("%B %d,%Y")
        return date


    def writeCSV(self,name):
        directory = "/home/baby/Desktop/budget"
        path = os.path.join(directory,str(name))
        f = open(path+".csv","w",newline="")
        writeFile = csv.writer(f)
        print(datetime.date.today())
        writeFile.writerow(["bank","money","spent"])
        writeFile.writerow([self.bank,self.money,self.spent])
        writeFile.writerow([self.totalSpent()])
        f.close()
        
    def listFiles(self):
        directory = "/home/baby/Desktop/budget" #input your own directory
        dictionary = {}
        num = 0
        for files in os.listdir(directory):
            num += 1
            dictionary[num] = files
        print(f"There are {num} files in '{directory}'")
        for i in range(1,num+1):
            print(f'{i}.)  {dictionary[i]}')
        choice = int(input("Which file would you want to update?"))
        chosen = dictionary[choice]
        path_chosen = os.path.join(directory,chosen)
        f = open(path_chosen)
        reader = csv.reader(f)
        for i in reader:
            print(i)



def main():
    # bank = input("how much money is in your bank account?\n")
    # money = input("how much money do you have right now?\n")
    # spent = input("how much money did you spend today?\n")
    b = Budget(bank=600,money=200,spent=20)
    b.writeCSV("budget")
    b.listFiles()
    
if __name__ == "__main__":
    main()