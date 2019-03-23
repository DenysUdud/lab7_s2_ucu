from task_5.book import Book

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone",
                 "J. K. Rowling", 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert (str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
            "1 page, currently on page 1>")

    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4)  # turning pages does not return
    assert (book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert (book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert (book1.getCurrentPage() == 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert (book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert (book2.getCurrentPage() == 1)

    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 1>")
    assert (book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark()  # does not return
    assert (book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert (book3.getBookmarkedPage() == 10)
    assert (book3.getCurrentPage() == 17)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert (book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert (book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert (book3.getCurrentPage() == 35)
    book3.turnToBookmark()  # if there's no bookmark, don't turn to a page
    assert (book3.getCurrentPage() == 35)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 35>")

    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert (book5 == book6)
    assert (book5 != book7)
    assert (book5 != book8)
    book5.turnPage(1)
    assert (book5 != book6)
    book5.turnPage(-1)
    assert (book5 == book6)
    book6.placeBookmark()
    assert (book5 != book6)
    print("Done!")

if __name__ == "__main__":
    testBookClass()