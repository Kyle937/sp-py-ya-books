import csv
# comma separated values

with open("YA_Books.csv", mode = "r") as bookfile:
    # mode "r" = read
    # "as" renames the function to a simple name

    books = csv.reader(bookfile)
    next(books)

    #most_recent_published = 0 # minimum age
    Minumum_rating = 5.0 # max rate

    for book in books:
        title = book[0]
        Author = book[1]
        year = int(book[2])
        Publisher = book[3]
        Genre = book[4]
        NumberOfPages = int(book[5])
        GoodreadsStarRating = float(book[6])

        # print all authors that stary with M
        #if Author.startswith("M"):
        #    print(Author)

        # get most recently published book
        #if year > most_recent_published:
        #    most_recent_published = year
        #    most_recent_book = book

        # get lowest rating
        if GoodreadsStarRating < Minumum_rating:
            Minumum_rating = GoodreadsStarRating
            Lowest_Rated_Book = book


        
    #print(f"most recent book: {most_recent_book}")
    print(f"worst book: {Lowest_Rated_Book}")