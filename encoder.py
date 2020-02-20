def encoder(pathToSave,solution): # le path puis le dict
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

