import random


def generate_graph_edges(num_vertices, num_instances):
    """Generate graph edges

    Args:
        num_vertices: Number of vertices
        num_instances: Number of instances

    Returns:
        None

    Raises:
        None

    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    for p in range(len(num_vertices)):
        n_v = num_vertices[p]
        n_i = num_instances[p]

        for k in range(0, n_i):
            # Lista za cuvanje grana
            edges = []

            # Generisanje random grana izmedju cvorova
            for i in range(1, n_v+1):
                for j in range(1, n_v+1):
                    if i != j and random.random() < 0.5:
                        edges.append((i, j))

            # Upis informacija u fajl i cuvanje u odgovarajucem folderu u zavisnosti od dimenzije grafa
            with open('./instances/level0/instance_' + str(n_v) + "_" + str(len(edges)) + '.txt', 'w') as f:
                for e in edges:
                    f.write(f"{e[0]} {e[1]}\n")


if __name__ == '__main__':
    generate_graph_edges([5, 10, 15, 50], [3, 3, 2, 2])
    print("Completed")
