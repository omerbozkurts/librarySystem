import time  # [EN] Import the time module to use time-related functions.
             # [TR] Zamanla ilgili işlevleri kullanmak için zaman modülünü içe aktar.

import datetime  # [EN] Import the datetime module to work with dates and times.
                 # [TR] Tarih ve zamanla çalışmak için datetime modülünü içe aktar.

class Library:
    
    def __init__(self):
        # [EN] Constructor method for initializing the Library class.
        # [TR] Kütüphane sınıfını başlatmak için yapıcı yöntem.
        self.file = open('books.txt', 'a+', encoding='utf-8')  
        # [EN] Open the 'books.txt' file in append mode with utf-8 encoding.
        # [TR] 'books.txt' dosyasını utf-8 kodlamasıyla ekleme modunda aç.

    def __del__(self):
        # [EN] Destructor method for closing the file when the object is destroyed.
        # [TR] Nesne yok edildiğinde dosyayı kapatmak için yok edici yöntem.
        self.file.close()

    def listBooks(self):
        # [EN] Method to list all the books in the library.
        # [TR] Kütüphanedeki tüm kitapları listelemek için yöntem.
        self.file.seek(0)  # [EN] Move the file cursor to the beginning of the file.
                           # [TR] Dosya imlecinin dosyanın başına gitmesi.
        for lines in self.file.readlines():
            lines = lines.split(',')
            bookName = lines[0].replace('*', ' ')  # [EN] Replace '*' with space in book name.
                                                   # [TR] Kitap adında '*' karakterini boşlukla değiştir.
            bookAuthor = lines[1].replace('*', ' ')  # [EN] Replace '*' with space in book author.
                                                      # [TR] Kitap yazarında '*' karakterini boşlukla değiştir.
            print(f'{bookName} {bookAuthor}')  # [EN] Print the formatted book name and author.
                                                 # [TR] Biçimlendirilmiş kitap adı ve yazarını yazdır.

    def addBook(self):
        # [EN] Method to add a book to the library.
        # [TR] Kütüphaneye kitap eklemek için yöntem.
        isAdded = False
        isNumPageNumber = False
        isTimeFormatTrue = False

        while not isAdded:
            try:
                self.name = str(input("Book's Name:"))  # [EN] Get the name of the book from the user.
                                                          # [TR] Kullanıcıdan kitap adını al.
                self.author = str(input("Book's Author:"))  # [EN] Get the author of the book from the user.
                                                              # [TR] Kullanıcıdan kitabın yazarını al.
                while not isTimeFormatTrue:
                    try:
                        relaseDate = str(input("Release Date (dd/mm/yyyy):"))  # [EN] Get the release date of the book from the user.
                                                                                # [TR] Kullanıcıdan kitabın yayın tarihini al.
                        datetime.datetime.strptime(relaseDate, '%d/%m/%Y')  # [EN] Check if the entered date is in the correct format.
                                                                              # [TR] Girilen tarihin doğru formatta olup olmadığını kontrol edin.
                        self.relaseDate = relaseDate  # [EN] If it is correct, assign it to the release date attribute.
                                                      # [TR] Doğru ise, bunu yayın tarihi özniteliğine atayın.
                        isTimeFormatTrue = True  # [EN] Set the flag to True indicating that the date format is correct.
                                                 # [TR] Tarih formatının doğru olduğunu belirten bayrağı True olarak ayarlayın.
                    except:
                        print('Time Format is Not True')  # [EN] If the date format is incorrect, print an error message.
                                                           # [TR] Tarih formatı yanlışsa, bir hata mesajı yazdır.
                while not isNumPageNumber:
                    try:
                        self.numOfPages = int(input("Number Of Pages:"))  # [EN] Get the number of pages of the book from the user.
                                                                            # [TR] Kullanıcıdan kitabın sayfa sayısını alın.
                        isNumPageNumber = True  # [EN] If it is a number, set the flag to True.
                                                 # [TR] Sayı ise, bayrağı True olarak ayarlayın.
                    except:
                        print('Number of Pages must be number')  # [EN] If it is not a number, print an error message.
                                                                  # [TR] Sayı değilse, bir hata mesajı yazdır.
                
                isAdded = True  # [EN] Set the flag to True indicating that the book details are added.
                                # [TR] Kitap detaylarının eklendiğini belirten bayrağı True olarak ayarlayın.

            except:
                print('Something went wrong')  # [EN] If something goes wrong, print an error message.
                                                # [TR] Bir şeyler ters giderse, bir hata mesajı yazdır.

        self.file.write(f'{self.name},{self.author},{self.relaseDate},{self.numOfPages}\n')  # [EN] Write the book details to the file.
                                                                                                # [TR] Kitap detaylarını dosyaya yazın.

    def removeBook(self):
        # [EN] Method to remove a book from the library.
        # [TR] Kütüphaneden kitap kaldırmak için yöntem.
        removedBooks = input('Enter the name of the book you want to delete:')  # [EN] Get the name of the book to be removed from the user.
                                                                                 # [TR] Kaldırılacak kitabın adını kullanıcıdan alın.
        self.file.seek(0)  # [EN] Move the file cursor to the beginning of the file.
                            # [TR] Dosya imlecinin dosyanın başına gitmesi.
        lines = self.file.readlines()  # [EN] Read all lines from the file.
                                        # [TR] Dosyadan tüm satırları oku.
        
        if any(removedBooks in line for line in lines):  # [EN] Check if the book to be removed exists in the library.
                                                         # [TR] Kaldırılacak kitabın kütüphanede olup olmadığını kontrol edin.
            newLines = [line for line in lines if not removedBooks in line]  # [EN] Create a new list excluding the book to be removed.
                                                                             # [TR] Kaldırılacak kitap hariç yeni bir liste oluştur.
            self.file = open('books.txt', 'w', encoding='utf-8')  # [EN] Open the file in write mode to overwrite it.
                                                                   # [TR] Üzerine yazmak için dosyayı yazma modunda aç.
            for line in newLines:   # [EN] Write the updated list of books to the file.
                                    # [TR] Güncellenmiş kitap listesini dosyaya yaz.
                self.file.write('{}'.format(line))
        else:
            print(f'{removedBooks} is not in Library')  # [EN] If the book is not found, print an error message.
                                                         # [TR] Kitap bulunamazsa, bir hata mesajı yazdır.


exitStatue = False  # [EN] Variable to control the exit status of the program.
                     # [TR] Programın çıkış durumunu kontrol etmek için değişken.

while not exitStatue:
    lib = Library()  # [EN] Create an instance of the Library class.
                     # [TR] Kütüphane sınıfından bir örnek oluştur.

    print('\n***MENU*** \n1)List Books\n2)Add Books\n3)Remove Book\n4)Exit\n')  # [EN] Print the menu options.
                                                                                  # [TR] Menü seçeneklerini yazdır.
    choose = input("Enter Your Choose:")  # [EN] Get the user's choice.
                                           # [TR] Kullanıcının seçimini alın.
    print('\n')
    
    match choose:
        case '1':
            lib.listBooks()  # [EN] Call the method to list books.
                             # [TR] Kitapları listelemek için yöntemi çağırın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after listing books.
                             # [TR] Kitapları listeledikten sonra 0.5 saniye gecikme yap.
        case '2':
            lib.addBook()  # [EN] Call the method to add a book.
                           # [TR] Bir kitap eklemek için yöntemi çağırın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after adding a book.
                             # [TR] Bir kitap ekledikten sonra 0.5 saniye gecikme yap.
        case '3':
            lib.removeBook()  # [EN] Call the method to remove a book.
                              # [TR] Bir kitap kaldırmak için yöntemi çağırın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after removing a book.
                             # [TR] Bir kitap kaldırdıktan sonra 0.5 saniye gecikme yap.
        case '4':
            exitStatue = True  # [EN] Set the exit status variable to True to exit the loop.
                                # [TR] Döngüden çıkmak için çıkış durumu değişkenini True olarak ayarlayın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds before exiting.
                             # [TR] Çıkış yapmadan önce 0.5 saniye gecikme yap.
        case _:
            print('invalid value directed to the menu')  # [EN] Print an error message for an invalid input.
                                                          # [TR] Geçersiz bir giriş için bir hata mesajı yazdır.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after an invalid input.
                             # [TR] Geçersiz bir giriş yaptıktan sonra 0.5 saniye gecikme yap.
