import time
import datetime

class Library:
    
    def __init__(self):
        
        self.file=open('books.txt','a+',encoding='utf-8')


    def __del__(self):
        
        self.file.close()

    def listBooks(self):
        
        self.file.seek(0)

        for lines in self.file.readlines():
            
            lines = lines.split(',')
            
            bookName = lines[0].replace('*',' ')
            bookAuthor = lines[1].replace('*',' ')
            
            print(f'{bookName} {bookAuthor}')
    
    def addBook(self):
        
        isAdded = False
        isNumPageNumber = False
        isTimeFormatTrue = False

        while not isAdded:
            try:
                self.name = str(input("Book's Name:"))
                self.author = str(input("Book's Author:"))
                while not isTimeFormatTrue:
                    try:
                        relaseDate = str(input("Release Date (dd/mm/yyyy):"))
                        datetime.datetime.strptime(relaseDate,'%d/%m/%Y')
                        self.relaseDate = relaseDate 
                        isTimeFormatTrue = True
                    except:
                        print('Time Format is Not True')
                while not isNumPageNumber:
                    try:
                        self.numOfPages = int(input("Number Of Pages:"))
                        isNumPageNumber = True
                    except:
                        print('Number of Pages must be number')
                
                isAdded = True

            except:
                print('Something went wrong')

        self.file.write(f'{self.name},{self.author},{self.relaseDate},{self.numOfPages}\n')

    def removeBook(self):

        removedBooks = input('Enter the name of the book you want to delete:')

        self.file.seek(0)
        lines = self.file.readlines()
        
        if any(removedBooks in line for line in lines):
            
            newLines = [line for line in lines if not removedBooks in line]
        
            self.file = open('books.txt','w',encoding='utf-8')
        
            for line in newLines:   
                self.file.write('{}'.format(line))
        else:
            print(f'{removedBooks} is not in Library')


exitStatue = False

while not exitStatue:

    lib = Library()

    print('\n***MENU*** \n1)List Books\n2)Add Books\n3)Remove Book\n4)Exit\n')
    choose = input("Enter Your Choose:")
    print('\n')
    
    match choose:
        case '1':
            lib.listBooks()
            time.sleep(0.5)
        case '2':
            lib.addBook()
            time.sleep(0.5)
        case '3':
            lib.removeBook()
            time.sleep(0.5)
        case '4':
            exitStatue = True
            time.sleep(0.5)
        case _:
            print('invalid value directed to the menu')
            time.sleep(0.5)
            

    
