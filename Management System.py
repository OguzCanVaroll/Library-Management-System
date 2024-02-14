import Library

if __name__ == "__main__":
    lib= Library.library()

    while(True):
        
        print("*** MENU***")
        inpt = int(input("1) List Books"+"\n"+"2) Add Book"+"\n"+"3) Remove Book"+"\n"+"4) End the program \n"+"Select: "))

        if inpt == 1:
            lib.listBooks()

        elif inpt == 2:
            questions = ["book title","book author","first release year","number of pages"]
            answers=[]
            for question in questions:
                answer = input(question +": \n")
                answers.append(answer)
            
            line= ", ".join(answers)
            lib.addBook(line)
            
        elif inpt == 3:
            book_delete = input("Book title:")
            lib.removeBook(book_delete)
        
        elif inpt == 4:
            break
        