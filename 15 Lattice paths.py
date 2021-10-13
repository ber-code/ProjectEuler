def grid_lattice_paths(size):
    if size < 1:
        return None
    routes = 2
    for i in range(1, size):
        routes += routes * (i) // (i + 1)
        routes *= 2
    return routes


print(grid_lattice_paths(20))
