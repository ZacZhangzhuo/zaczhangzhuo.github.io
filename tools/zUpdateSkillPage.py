import numpy as np
from compas.data import json_dump
def ball_and_stick_model(names, links, sizes):
    """
    Generates a ball-and-stick model of a molecule based on the names, links and sizes of its elements.

    Args:
        names (list): List of names of the elements.
        links (list): List of tuples containing the indices of elements that are linked to each other.
        sizes (list): List of sizes of the elements.

    Returns:
        numpy.ndarray: Array of shape (n, 3) containing the locations of the elements.
    """
    n = len(names)
    locations = np.zeros((n, 3))

    # Compute the locations of the elements based on their sizes and links
    for i in range(n):
        locations[i][0] = sizes[i] * np.cos(i * 2 * np.pi / n)
        locations[i][1] = sizes[i] * np.sin(i * 2 * np.pi / n)
        locations[i][2] = 0

    for link in links:
        p1 = locations[link[0]]
        p2 = locations[link[1]]
        midpoint = (p1 + p2) / 2
        direction = p2 - p1
        length = np.linalg.norm(direction)
        direction /= length
        stick_length = 0.1 * min(sizes[link[0]], sizes[link[1]])
        locations[link[0]] += direction * (stick_length / 2)
        locations[link[1]] -= direction * (stick_length / 2)

    return locations


names = ["O", "H", "H", "H", "H","C","H"]
links = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),(5,6)]
sizes = [5.0, 0.8,0.8,0.8,0.8,3,0.8]

locations = ball_and_stick_model(names, links, sizes)
# print(locations)


data = {"names": names, "links": links, "sizes": sizes, "locations": locations.tolist()}
json_dump(data, "ball_and_stick.json")

