import parser
import loader
import encoder

def new_score_book(config, book):




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
        books_order['books_order'] = sorted(config['libraries'][value]['books'], key=lambda book: new_score_book(config, book))
        solution['libraries'][value] = books_order

    return solution

encoder.encoder("./solutions/a.txt", output(loader.a))