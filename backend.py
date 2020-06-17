import sqlite3

#create database and tables
def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title VARCHAR(200), author VARCHAR(200), year VARCHAR(4), isbn VARCHAR(10))")
    conn.commit()
    conn.close()

#add book details
def addBook(title, author, year, isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("insert into book(title,author,year,isbn) values(?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

#show all books info
def viewAll():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("select * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

#show searched books info
def viewSearched(title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

#delete book details
def deleteBook(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

#update book details
def updateBook(title, author, year, isbn, id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()



#CALL connect
connect()
#addBook("The Book", "Nitish", "2010", "0000-0001")
#addBook("The Book V2", "Nitish", "2011", "0000-0002")
#print(viewAll())