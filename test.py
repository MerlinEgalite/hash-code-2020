import copy

"""
    @config: {
        "books": [1, 2, 3, 6, 5, 4],
        "libraries": [
            {
                "books": [0, 1, 2, 3, 4],
                "signup_time": 2,
                "velocity": 2
            },
            {
                "books": [3, 2, 5, 0],
                "signup_time": 3,
                "velocity": 1
            }
        ],
        "days": 7
    }
    @solution: {
        "libraries_order": [1, 0],
        "libraries": {
            0: {
                "books_order": [0, 1, 2, 3, 4]
            },
            1: {
                "books_order": [5, 2, 3]
            }
        }
    }
"""

def model(config, solution):
    # Computing the score for this solution
    score = 0

    shipped_books = [] # already shipped books
    states = copy.deepcopy(solution["libraries"]) # current state of libraries (books remaining to be shipped)
    libraries_order = solution["libraries_order"] # the order in which librairies will sign up
    if len(libraries_order) > 0:
        libraries_signed = [] # libraries currently signed up, that can ship books
        library_index = 0 # index (in libraries_order) of the library currently signing up
        library_signup_delay = config["libraries"][library_index]["signup_time"] # delay of library signing up (counter)
        for t in range(config["days"]):
            if library_index is not None:
                library_signup_delay -= 1

                if library_signup_delay <= 0:
                    libraries_signed.append(libraries_order[library_index])
                    if len(libraries_order) > library_index + 1:
                        library_index += 1
                        library_signup_delay = config["libraries"][library_index]["signup_time"]
                    else:
                        library_index = None

            for library_id in libraries_signed:
                velocity = config["libraries"][library_id]["velocity"]
                remaining_books_order = states[library_id]["books_order"]
                for i in range(velocity):
                    if len(remaining_books_order) > 0:
                        shipped_book_id = remaining_books_order.pop(0)
                        if shipped_book_id not in shipped_books:
                            score += config["books"][shipped_book_id]
                            shipped_books.append(shipped_book_id)
    
    return score

def is_valid(config, solution):
    books = set(range(len(config["books"])))
    for library_id in solution["libraries_order"]:
        if library_id >= len(config["libraries"]): return False
        books_order = set(solution["libraries"][library_id]["books_order"])
        books_owned = set(config["libraries"][library_id]["books"])
        if not books_order.issubset(books): return False
        if not books_order.issubset(books_owned): return False
    return True

def compute(config, solution):
    is_valid(config, solution)
    return model(config, solution)

model({
        "books": [1, 2, 3, 6, 5, 4],
        "libraries": [
            {
                "books": [0, 1, 2, 3, 4],
                "signup_time": 2,
                "velocity": 2
            },
            {
                "books": [3, 2, 5, 0],
                "signup_time": 3,
                "velocity": 1
            }
        ],
        "days": 7
    }, {
        "libraries_order": [1, 0],
        "libraries": {
            0: {
                "books_order": [0, 1, 2, 3, 4]
            },
            1: {
                "books_order": [5, 2, 3]
            }
        }
    })