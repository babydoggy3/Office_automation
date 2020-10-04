import PyPDF2,os,re


class TextWriter:

    def __init__(self,destination,directory):
        self.destination = destination
        self.directory = directory

    def menu(self):
        file_list = []
        number = 0
        dictionary = {

        }
        for files in os.listdir(self.directory):
            if files.endswith(".pdf"):
                file_list.append(files)
                number += 1
                dictionary[number] = files
                print(f"{number}.) {dictionary[number]}")
        answer  = input("which pdf would you like to convert to text file?\n\t type the number:")
        self.open_file(dictionary[int(answer)])

    def open_file(self,pdf):
        location = self.directory + "/"+ pdf
        f = open(location,"rb")
        file_reader = PyPDF2.PdfFileReader(f)
        string = ""
        for num in range(1,file_reader.numPages):
            get_page = file_reader.getPage(num)
            text = get_page.extractText()
            string += text
        file = open(self.destination,"w+")
        file.write(string)
        file.close()
        f.close()


if __name__ == "__main__":
    destination = input("Where do you want to write the file?\n")
    directory  = input("Where is the location of the pdf?\n")
    t = TextWriter(destination,directory)
    t.menu()


