from src.structures import BinaryHeap


def build_skyline(buildings):
    """
    Build the skyline from a set of buildings
    :param buildings: 2d boxes (x, x2, height)
    """

    heap = BinaryHeap(buildings)

    tree = []

    tree.append(0)

    skyline = []

    while not heap.is_empty():


        element = heap.pop()
        current_x = element[0]
        # Process event
        if len(element) == 3:

            x, x2, height = element
            tree.append(height)

            heap.insert((x2, height))

        else:
            x2, height = element
            tree.remove(height)

        if not heap.is_empty() and heap.peek()[0] == current_x:
            continue

        last_max = 0 if len(skyline) == 0 else skyline[-1][-1]
        current_max = max(tree)
        if current_max != last_max:
            skyline.append((element[0], last_max))
            skyline.append((element[0], current_max))



    return skyline

