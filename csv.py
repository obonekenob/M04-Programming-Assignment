""" SDEV220 M04 Programming Assignment
    Paul R Thompson
    Chapter 16 Problem 2
"""

with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(bbok)
        
