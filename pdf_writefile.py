import PyPDF2,os,re


class TextWriter:

    def __init__(self,destination,pdf):
        self.destination = destination
        self.pdf = pdf

    def open_file(self):
        f = open(self.pdf,"rb")
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

    def select_pdf(self):
        directory = input("Please input the directory you wish to open a pdf")
        list_dir = []
        number = 0
        for files in os.listdir(directory):
            number +=1
            list_dir.append(files)


if __name__ == "__main__":
    destination = input("Where do you want to write the file?\n")
    pdf = input("")


