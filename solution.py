import parser
import loader
import encoder
import test_hashcode as test

def new_score_book(config, book_id):

    return 1


def new_score_lib(config, library):

    velocity = library['velocity']
    signup_time = library['signup_time']
    books = library['books']

    return 1


def output(config):
    solution = {'libraries': {}, 'libraries_order': []}

    # Create sorted list of libraries
    solution['libraries_order'] = sorted(range(len(config['libraries'])), key=lambda library_id: new_score_lib(config, config['libraries'][library_id]))

    for (index, value) in enumerate(solution['libraries_order']):

        # Create sorted list of books within a libraries
        books_order = {}
        books_order['books_order'] = sorted(config['libraries'][value]['books'], key=lambda book_id: new_score_book(config, book_id))
        solution['libraries'][value] = books_order

    return solution

datasets = ["a", "b", "c", "d", "e", "f"]
for index, config in enumerate([loader.a, loader.b, loader.c, loader.d, loader.e, loader.f]):
    dataset = datasets[index]
    solution = output(config)
    if test.is_valid(config, solution):
        print("Score {}: {}".format(dataset, test.model(config, solution)))
        encoder.encoder("./solutions/{}.txt".format(dataset), solution)
    else: print("Solution not found!")