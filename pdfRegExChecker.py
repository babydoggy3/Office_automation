import re,os,PyPDF2


class KeywordChecker:

    def __init__(self,directory,keyword):

        self.directory = directory
        self.keyword = keyword

    def list_directory(self):
        directory_list = []
        for items in os.listdir(self.directory):
            directory_list.append(items)
        selected_file = list(filter(lambda x:x.endswith(".pdf"),directory_list))
        print(f"Here are the following pdf files in '{self.directory}'")
        num = 0
        self.dictionary  ={

        }
        for pdfs in selected_file:
            num += 1
            self.dictionary[num] = pdfs
            print(str(num)+".)  "+str(self.dictionary[num])+"\n")
        print("Which pdf file would you like to scan?")
        print("please input number")
        self.pdf = int(input())
        print("You have selected "+self.dictionary[pdf])
        self.open_file(self.dictionary[pdf])


    def open_file(self,file_name):
        pdf = self.directory +"/" + file_name
        f = open(pdf,"rb")
        file_reader =  PyPDF2.PdfFileReader(f)
        string = ""
        for num in range(1,file_reader.numPages):
            get_page = file_reader.getPage(num)
            text = get_page.extractText()
            string +=text


        searching = re.search(self.keyword,string)
        if searching == None:
            print(f"The keyword: '{self.keyword}' cannot be found in the pdf")
        elif searching != None:
            print(f"{self.keyword} is found")

    def scan_directory(self):
        file_list = []
        for files in os.listdir(self.directory):
            file_list.append(files)

        selected_files = list(filter(lambda x: x.endswith(".pdf"),file_list))
        for files in selected_files:
            self.open_file(files)

options = {
    1:"Scan the whole directory",
    2:"Scan one file"
}

if __name__ == "__main__":
    directory = input("Please input directory:  ")
    keyword = input("Please input keyword:  ")
    print("Do you want to scan the whole directory or only 1 file?")

    for numbers in range(1,3):
        choices = (str(numbers)+".)  " +options[numbers])
        print(choices)

    choice = int(input())
    if choice == 1:
        of = KeywordChecker(directory,keyword)
        of.scan_directory()
    elif choice  == 2:
        sf = KeywordChecker(directory,keyword)
        sf.list_directory()
    else:
        print("that is not a valid answer")
