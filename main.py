import csv
# comma separated values

with open("YA_Books.csv", mode = "r") as bookfile:
    # mode "r" = read
    # "as" renames the function to a simple name

    books = csv.reader(bookfile)
    next(books)

    Max_rating = 0.0 # min rate
    page_count = 0 # min rate
    Max_rating2 = 0.0 # min rate

    for book in books:
        title = book[0]
        Author = book[1]
        year = int(book[2])
        Publisher = book[3]
        Genre = book[4]
        NumberOfPages = int(book[5])
        GoodreadsStarRating = float(book[6])

        # question 1
        # what is the highest rating for any book in the dataset?
        if GoodreadsStarRating > Max_rating:
            Max_rating = GoodreadsStarRating

        # question 2
        # what is the longest book published before the year 2000
        if year < 2000:
            if NumberOfPages > page_count:
                page_count = NumberOfPages
                longest_Book_Before_2000 = book

        # question 3
        # What is the highest-rated book that has more than 400 pages?
        if NumberOfPages > 400:
            if GoodreadsStarRating > Max_rating2:
                Max_rating2 = GoodreadsStarRating
                highest_Rated_Book = book
                
        


    print(f"highest rating: {Max_rating}")
    print(f"process: i just swapped around the values for worst rating\n")
    print(f"longest book before 2000: {longest_Book_Before_2000}")
    print(f"process: made sure books made after (or during) 2000 would get ignored and did the same thing as question 1\n")
    print(f"highest rating book with over 400 pages: {highest_Rated_Book}")
    print(f"process: copy/pasted question 1 and made sure books with under (or exactly) 400 pages would be ignored\n")