# book-record-using-tkinter
This is a window application to manage (Add, Update, view all, search book, listing) books using python and SQLite database.

frontend.py contains python gui code
backend.py conatins database connection code

# How to create Executable (.exe) file in Python
1. Install pyinstaller
2. execute this command 
    python --onefile --windowed frontend.py
    
  --onefile is use to create one executable file and create connection whichever file is imported in frontend.py
  --windowed , when you execute this file it will execute cmd in backgroud to prevent this and use only 
    window application we need to use windowed argument
    
   above command will create a build and dist folder..where dist folder will contain .exe file in the name of frontend.exe
   when you exxecute that file it will create a database file because we have called connection in backend.py
  
