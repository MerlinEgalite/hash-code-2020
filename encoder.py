
solTest= {
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


def encoder(pathToSave,solution):
    with open(pathToSave,"w") as savedFile:
        savedFile.writelines(str(len(solution["libraries_order"])))
        savedFile.writelines("\n")
        libraries=solution["libraries"]
        for lib_id in solution["libraries_order"] :
            librarie = libraries[lib_id]
            savedFile.writelines("%s %s"%(lib_id,len(librarie["books_order"])))
            savedFile.writelines("\n")
            savedFile.writelines(" ".join(map(str,librarie["books_order"])))
            savedFile.writelines("\n")

encoder("./test.txt",solTest)