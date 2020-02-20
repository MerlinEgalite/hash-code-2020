
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
    return order
