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
        "libraries": [
            {
                0: {
                    "books_order": [0, 1, 2, 3, 4]
                },
                1: {
                    "books_order": [5, 2, 3]
                }
            }
        ]
    }
"""

def model(config, solution):
    # Computing the score for this solution
    score = 0

    libraries_order = solution["libraries_order"] # the order in which librairies will sign up
    if len(libraries_order) > 0:
        libraries_signed = []
        library_index = 0 # index of the library signing up
        for t in range(config["days"]):
            for library_id in libraries_signed:
                velocity = config["libraries"][library_id]["velocity"]
                shipped_books = solution["libraries"]
    
    return score

def is_valid(solution):
    for library_id in solution["libraries"]:
        assert set(solution["libraries"][library_id]["books_order"]).issubset(config["books"]), "Library {} ships a book that doesn't exist!".format(library_id)
        assert set(solution["libraries"][library_id]["books_order"]).issubset(config["libraries"][library_id]["books"]), "Library {} ships a book that it doesn't own!".format(library_id)

def compute(config, solution):
    is_valid(config, solution)