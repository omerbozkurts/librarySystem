import customtkinter as ctk

ctk.set_appearance_mode("dark") 

        # Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue")
 
app = ctk.CTk() 
app.geometry("400x800") 
app.title("AB Bank")

tabview = ctk.CTkTabview(app,fg_color='transparent',width=360,height=700)
tabview.pack(pady=10,padx=10,expand=True,fill='both')
tabview.add("Librarian") 
tabview.add("Member")

print(tabview._current_name)

app.mainloop()