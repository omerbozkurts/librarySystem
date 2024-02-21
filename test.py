import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")
 
app = ctk.CTk() 
app.geometry("400x800") 
app.title("AB Bank")

librarianFrameAnasayfaAddBook = ctk.CTkFrame(app)
librarianFrameAnasayfaAddMagazine = ctk.CTkFrame(app)  
librarianFrameAnasayfaAddDvd = ctk.CTkFrame(app)

isBooksCategorySelected = False
isMagazineCategorySelected = False
isDvdCategorySelected = False
lastSelectedFrame = None

def selectedState(choice):
    global isBooksCategorySelected
    global isMagazineCategorySelected
    global isDvdCategorySelected
    global lastSelectedFrame
    
    selectedCategory = str(choice).lower()

    # Her kategori seçildiğinde, mevcut kategori öğelerini gizle
    if lastSelectedFrame:
        lastSelectedFrame.pack_forget()

    # Kitap kategorisi seçildiğinde
    if selectedCategory == 'books':
        if isBooksCategorySelected:
            # Eğer zaten kitap kategorisi seçilmişse, öğeleri göster
            librarianFrameAnasayfaAddBook.pack(pady=20,padx=40,fill='both',expand=True)
            lastSelectedFrame = librarianFrameAnasayfaAddBook
            return
        isBooksCategorySelected = True
        # Kitap kategorisi öğelerini göster
        librarianFrameAnasayfaAddBook.pack(pady=20,padx=40,fill='both',expand=True)   
        lastSelectedFrame = librarianFrameAnasayfaAddBook

        booksName= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Name") 
        booksName.pack(pady=12,padx=10) 

        booksAuthor= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Author") 
        booksAuthor.pack(pady=12,padx=10) 

        booksPublicationDate= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Publication Date") 
        booksPublicationDate.pack(pady=12,padx=10)

        booksPageNumber= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Publication Date") 
        booksPageNumber.pack(pady=12,padx=10)

        booksStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Stock Quantity") 
        booksStockQuantity.pack(pady=12,padx=10)

        booksShelfQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddBook,placeholder_text="Books Shelf Quantity") 
        booksShelfQuantity.pack(pady=12,padx=10)

        addBooksButton = ctk.CTkButton(librarianFrameAnasayfaAddBook,text='Add Book') 
        addBooksButton.pack(pady=12,padx=10)

    # DVD kategorisi seçildiğinde
    elif selectedCategory == 'dvd':
        if isDvdCategorySelected:
            # Eğer zaten DVD kategorisi seçilmişse, öğeleri göster
            librarianFrameAnasayfaAddDvd.pack(pady=20,padx=40,fill='both',expand=True)
            lastSelectedFrame = librarianFrameAnasayfaAddDvd
            return
        isDvdCategorySelected = True
        # DVD kategorisi öğelerini göster
        librarianFrameAnasayfaAddDvd.pack(pady=20,padx=40,fill='both',expand=True)
        lastSelectedFrame = librarianFrameAnasayfaAddDvd

        dvdName= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Name") 
        dvdName.pack(pady=12,padx=10) 

        dvdDirector= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Director") 
        dvdDirector.pack(pady=12,padx=10) 

        dvdReleaseDate= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Release Date") 
        dvdReleaseDate.pack(pady=12,padx=10)

        dvdStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddDvd,placeholder_text="DVD Stock Quantity") 
        dvdStockQuantity.pack(pady=12,padx=10)

        addDvdButton = ctk.CTkButton(librarianFrameAnasayfaAddDvd,text='Add DVD') 
        addDvdButton.pack(pady=12,padx=10)
        
    # Dergi kategorisi seçildiğinde
    elif selectedCategory == 'magazine':
        if isMagazineCategorySelected:
            # Eğer zaten dergi kategorisi seçilmişse, öğeleri göster
            librarianFrameAnasayfaAddMagazine.pack(pady=20,padx=40,fill='both',expand=True)
            lastSelectedFrame = librarianFrameAnasayfaAddMagazine
            return
        isMagazineCategorySelected = True
        # Dergi kategorisi öğelerini göster
        librarianFrameAnasayfaAddMagazine.pack(pady=20,padx=40,fill='both',expand=True)
        lastSelectedFrame = librarianFrameAnasayfaAddMagazine

        magazineName= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Name") 
        magazineName.pack(pady=12,padx=10) 

        magazineIssue= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Issue") 
        magazineIssue.pack(pady=12,padx=10) 

        magazinePublicationDate= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Publication Date") 
        magazinePublicationDate.pack(pady=12,padx=10)

        magazineStockQuantity= ctk.CTkEntry(librarianFrameAnasayfaAddMagazine,placeholder_text="Magazine Stock Quantity") 
        magazineStockQuantity.pack(pady=12,padx=10)

        addMagazineButton = ctk.CTkButton(librarianFrameAnasayfaAddMagazine,text='Add Magazine') 
        addMagazineButton.pack(pady=12,padx=10)


comboboxAddItem = ctk.CTkOptionMenu(app,values=["Books", "DVD", 'Magazine'],command=selectedState)
comboboxAddItem.pack(padx=20, pady=10)
comboboxAddItem.set("Choose Item")

app.mainloop()
