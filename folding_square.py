"""
Visual depiction
Folding a square from each corner
For each iteration:
    1.  Fold each convex corner in in a way that the resulting polyhedron has all edges of equal length after each iteration
    2.  Fold each concave corner out
    3.  Visualize

    Example:

    Initial:
            +--------+
            |        |
            |        |
            |        |
            |        |
            +--------+

    After 1 iteration:
               +--+ 
            +--+  +--+
            |        |
            |        |
            +--+   +-+
               +--+ 

"""


from matplotlib import pyplot
import math
import sys
import numpy

ITERATIONS = 5

def iterate(coords, fold_ratio):
    """
        coords come in this shape:  
                [ [0, 0], [4, 0], [4, 4], [0, 4] ]
        where each of the tuples represents a vertex
        This method will fold each vertex, thus replacing each of the vertices with 3 others

    """
    result = []
    
    x_coords, y_coords = zip(*coords)

    mean_x = numpy.average(x_coords) 
    mean_y = numpy.average(y_coords) 
    center = (mean_x, mean_y)

    for i,curr_vertex in enumerate(coords):
        current_x = curr_vertex[0]
        current_y = curr_vertex[1]

        prev_vertex = coords[(i - 1) % len(coords)]
        previous_x = prev_vertex[0]
        previous_y = prev_vertex[1]

        next_vertex = coords[(i + 1) % len(coords)]
        next_x = next_vertex[0]
        next_y = next_vertex[1]

        #print(f"curr_vertex is {curr_vertex}")
        #print(f"prev_vertex is {prev_vertex}")
        #print(f"next_vertex is {next_vertex}")

        prev_length_sqr = (current_x-previous_x)**2 + (current_y-previous_y)**2  
        next_length_sqr = (current_x-next_x)**2 + (current_y-next_y)**2  

        span = min(prev_length_sqr, next_length_sqr)
        span = math.sqrt(span)/fold_ratio

        # Compute the 3 new vertices v1, v2 and v3
        if previous_x == current_x:
            v1x = current_x
        elif previous_x < current_x:
            v1x = current_x - span
            v2x = current_x - span
        else:
            v1x = current_x + span
            v2x = current_x + span

        if previous_y == current_y:
            v1y = current_y
        elif previous_y < current_y:
            v1y = current_y - span
            v2y = current_y - span
        else:
            v1y = current_y + span
            v2y = current_y + span

        if next_x == current_x:
            v3x = current_x
        elif next_x < current_x:
            v3x = current_x - span
            v2x = current_x - span
        else:
            v3x = current_x + span
            v2x = current_x + span

        if next_y == current_y:
            v3y = current_y
        elif next_y < current_y:
            v3y = current_y - span
            v2y = current_y - span
        else:
            v3y = current_y + span
            v2y = current_y + span

        v1 = [v1x, v1y]
        v2 = [v2x, v2y]
        v3 = [v3x, v3y]

        result.extend([v1, v2, v3])

        #print(f"result is {result}")

    return result

def plot_polygon(coords):
    x, y = zip(*coords)

    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    fig, ax = pyplot.subplots()

    ax.plot(x, y)
    #ax.fill(x, y)
    ax.set_aspect('equal')
    pyplot.show()

for fold_ratio in range(3, 10):
    poly = [ [0, 0], [4, 0], [4, 4], [0, 4] ]

    for f in range(ITERATIONS):
        poly = iterate(poly, fold_ratio)

    plot_polygon(poly)

