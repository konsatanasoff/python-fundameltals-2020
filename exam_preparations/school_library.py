def add(book_list, book):
    if book not in book_list:
        book_list.insert(0, book)
    return book_list


def take(book_list, book):
    if book in book_list:
        book_list.remove(book)
    return book_list


def swap(book_list, book_1, book_2):
    if book_1 in book_list and book_2 in book_list:
        b_1, b_2 = book_list.index(book_1), book_list.index(book_2)
        book_list[b_1], book_list[b_2] = book_list[b_2], book_list[b_1]
    return book_list


def insert(book_list, book):
    book_list.append(book)
    return book_list


def check(book_list, index):
    if index < len(book_list):
        print(book_list[index])


books = input().split("&")
command = input()

while not command == "Done":
    action = command.split(" | ")[0]

    if action == "Add Book":
        book = command.split(" | ")[1]
        books = add(books, book)

    elif action == "Take Book":
        book = command.split(" | ")[1]
        books = take(books, book)

    elif action == "Swap Books":
        book_1 = command.split(" | ")[1]
        book_2 = command.split(" | ")[2]
        books = swap(books, book_1, book_2)

    elif action == "Insert Book":
        book = command.split(" | ")[1]
        book_list = insert(books, book)

    elif action == "Check Book":
        index = int(command.split(" | ")[1])
        check(books, index)

    command = input()

print(", ".join(books))
