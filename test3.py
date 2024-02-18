import librarian
import  time


exitStatue = False  # [EN] Variable to control the exit status of the program.
                     # [TR] Programın çıkış durumunu kontrol etmek için değişken.

while not exitStatue:
    lib = librarian.Librarian()     # [EN] Create an instance of the Library class.
                                    # [TR] Kütüphane sınıfından bir örnek oluştur.

    print('\n***MENU*** \n1)List Books\n2)Add Books\n3)Remove Book\n4)Exit\n')  # [EN] Print the menu options.
                                                                                  # [TR] Menü seçeneklerini yazdır.
    choose = input("Enter Your Choose:")  # [EN] Get the user's choice.
                                           # [TR] Kullanıcının seçimini alın.
    print('\n')
    
    match choose:
        case '1':
            itemType = input('enter item type:')
            items=lib.listItems(itemType)  # [EN] Call the method to list books.

            for item in items:
                print(item) 

                             # [TR] Kitapları listelemek için yöntemi çağırın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after listing books.
                             # [TR] Kitapları listeledikten sonra 0.5 saniye gecikme yap.
        case '2':
            itemType = input('item type:')
            addName = str(input('name:'))
            addPerson = str(input('person:'))
            addReleaseDate = input('release date:')
            addPageNumorDuration = input('pageNum  or duration:')
            addStockNumber = input('stock num:')
            addShelfNumber = input('shelf num:')
            print(lib.addLibraryItems(itemType,addName,addPerson,addReleaseDate,addPageNumorDuration,addStockNumber,addShelfNumber))  # [EN] Call the method to add a book.
                           # [TR] Bir kitap eklemek için yöntemi çağırın.
            time.sleep(0.5)  # [EN] Delay for 0.5 seconds after adding a book.
                             # [TR] Bir kitap ekledikten sonra 0.5 saniye gecikme yap.
        case '3':
            itemType = input('item type:')
            itemName = input('item name:')
            lib.removeLibraryItem(itemType,itemName)  # [EN] Call the method to remove a book.
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
