class library:
    def __init__(self):
        self.file = open('books.txt', 'a+') 
        self.file.seek(0)  
    
    def __del__(self):
        # Destructor method to close the file
        self.file.close()
        print("File closed.")

    def listBooks(self):
        self.file.seek(0)
        bookList=self.file.read().splitlines()
        flag=1
        for book in bookList:
           line = book.split(",")   
           print(f"{flag}. book: "+line[0]+", author: "+line[1]+"\n")
           flag= flag+1
        
        self.file.flush()
        
    
    def addBook(self,line):
        self.file.seek(0)
        self.file.write(line+"\n")
        self.file.flush()
    
    
    def removeBook(self,title):
        self.file.seek(0)
        bookList=self.file.read().splitlines()
        
        with open("books.txt", "w") as file:
            for book in bookList:
                line = book.split(",")   
                if line[0] != title:
                    file.write(book+"\n")
        self.file.flush()
