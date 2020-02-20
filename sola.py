
def computeLibsMultilist(weights, velocities, signups):
    """
    Compute the libraries order for multilib
    """
    first_list = []
    second_list = []
    order = []
    for lib_index in range(len(weights)):
        libs = [weights[lib_index], velocities[lib_index], signups[lib_index]]
        for lib in libs:
            if lib in first_list:
                if lib in second_list:
                    order.append(lib)
                else:
                    second_list.append(lib)
            else:
                first_list.append(lib)
    for lib in second_list:
        if not lib in order:
            order.append(lib)
    for lib in first_list:
        if not lib in order:
            order.append(lib)
    return order

def dumbMultilist(config):
    """
    Compute a dumb solution
    """
    weights={}
    seen=[]
    velocities={}
    signups={}
    sol={}
    # Compute dump weihts
    for lib in range(len(config["libraries"])):
        velocities[lib]=config["libraries"][lib]["velocity"]
        signups[lib]=config["libraries"][lib]["signup_time"]
        ever_seen=0
        for book in config["libraries"][lib]["books"]:
            if not book in seen:
                seen.append(book)
                ever_seen+=1
        weights[lib]=ever_seen
    order = computeLibsMultilist(list({k: v for k, v in sorted(weights.items(), key=lambda item: item[1])}.keys()), list({k: v for k, v in sorted(velocities.items(), key=lambda item: item[1])}.keys()), list({k: v for k, v in sorted(signups.items(), key=lambda item: item[1])}.keys()))
    print(weights,velocities,signups,order)
    sol["libraries_order"]=order
    sol["libraries"]={}
    for lib in order:
        sol["libraries"][lib]={}
        sol["libraries"][lib]["books_order"]=config["libraries"][lib]["books"]
    return sol

import loader
print(loader.a)
print(dumbMultilist(loader.a))
