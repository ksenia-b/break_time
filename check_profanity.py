import urllib


def read_text():
    quotes = open(
        "/Users/ione/Documents/movie_quotes.txt")  # quotes is an object of a file, function creates space ina a memory for object
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("This document do not have curse words.")
    else:
        print("Could not scan the document properly")





read_text()
