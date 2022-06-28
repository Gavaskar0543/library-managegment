#libary managment project
class Library():
    #variables
      def __init__(self,list):
        self.book_list=list
        self.available_book_list=list[:]#[:]-->this will create same list in another memory location
        self.books_lent={}  # key-->book,val-->user_name
      def display_available_book_list(self):
         for book in self.available_book_list:
             print(book)
      def display_all_books(self):
         for book in self.book_list:
             print(book)
      def lend_book(self,name,book):
         if book not in self.book_list:
             print("Incorrect book name . please check the book list")
             return
         if book in self.available_book_list:
             self.books_lent.update({book:name})
             #Removing a book from the list
             self.available_book_list.remove(book)
             print("you are taken the book....")
         else:
             print("The book is already taken by.."+self.book.lend(book))
      def return_book(self,book):
            del self.books_lent[book]
            print("you are returned the book"+" "+book)
            #after user return the book,it will added to the available book list
            self.available_book_list.append(book)


if __name__=="__main__":
    #creating object for the class
        lib = Library(["The Life Divine", "Da Vinci Code", "The Alchemist", "Educated", "Harry Potter"])
while True:
        print("welcome to libary,enter an optin")
        print("1.Display availabe books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.quit")
        #To get user input
        user_choice=int(input("enter here:"))
        if user_choice==1:
            lib.display_available_book_list()
        elif user_choice==2:
            lib.display_all_books()
        elif user_choice==3:
            name=input("enter user name:")
            book=input("enter book name:")
            lib.lend_book(name,book)
        elif user_choice==4:
            lib.return_book(book)
        elif user_choice==5:
            #to exit from loop
              break
        else:
            print("Invalid input")

