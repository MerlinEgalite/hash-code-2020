import pickle
import os
def configConstructor(file):
    result = {}
    with open(file) as data :
        books,libs,days = data.readline().strip().split(" ")
        result["days"]=int(days)
        result["books"]= [int(x) for x in data.readline().strip().split(" ")]
        libraries = []
        for lib in range(int(libs)):
            librarie={}
            num_books,signup,ship = data.readline().strip().split(" ")
            librarie["signup_time"]=int(signup)
            librarie["velocity"]=int(ship)
            librarie["books"]=[int(book) for book in data.readline().strip().split(" ")]
            libraries.append(librarie)
        result["libraries"]=libraries
    return result



#for dataPath in os.listdir('./datasets'):
#    with open("./pickle/%s.pickle"%dataPath[0],"wb") as dataFile: # On appelle les pickle juste a b c d e f
#        pickle.dump(configConstructor("./datasets/%s"%dataPath),dataFile)
#    break

#with open("prout.pickle","wb") as truc:
#    pickle.dump(configConstructor("./datasets/a_example.txt"), truc)
