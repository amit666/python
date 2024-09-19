#!/home/amit/venv/bin/python

from dataclasses import dataclass
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

piece_index = 0

@dataclass
class Piece:
    size : tuple
    shape : tuple
    index : int

    def __init__(self, size, shape):
        global piece_index
        self.size = size
        self.shape = shape
        piece_index += 1
        self.index = piece_index

class Board:
    board_path: tuple
    pieces = []

    def __init__(self, path):
        self.board_path = mpath.Path(path)

    def place(self, piece, loc):
        self.pieces.append((piece, loc))


    def show(self):
        fig, ax = plt.subplots()

        ax.add_patch(mpatches.PathPatch(self.board_path, facecolor='none', lw=3))
        b = self.board_path.get_extents().bounds
        ax.set_xlim(b[0], b[2])
        ax.set_ylim(b[1], b[3])

        for p, loc in self.pieces:
            p_patch = mpatches.PathPatch(p, facecolor='none', lw=3)
            #ax.add_patch(p_patch)

        plt.show()

def main():
    pieces = (
        Piece( (3,3), ( 0,1,0,      0,1,1,      1,1,0           )),
        Piece( (2,4), ( 1,0,        1,1,        1,0,        1,0 )),
        Piece( (3,3), ( 1,1,1,      1,1,0,      0,1,0           )),
        Piece( (3,3), ( 0,1,1,      0,1,0,      1,1,0           ))
    )
    print(f"pieces is {pieces}")

    board = ( (0,0), (5,0), (5,4), (2.5,6), (0,4) )
    b = Board(board)
    b.place(pieces[0], (0,0))
    b.show()

if __name__ == "__main__":
    main()


import matplotlib.pyplot as plt

def plot_polygon(coords):
    """
    Plots a polygon given a list of coordinates.

    :param coords: List of tuples or arrays where each tuple/array is (x, y) coordinate of a vertex.
    """
    # Unzip the list of coordinates into x and y lists
    x, y = zip(*coords)

    # Append the first point to the end to close the polygon
    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the polygon
    ax.plot(x, y, marker='o', linestyle='-')

    # Fill the polygon for better visibility
    ax.fill(x, y, alpha=0.3)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Polygon Plot')

    # Set equal scaling and grid
    ax.set_aspect('equal')
    ax.grid(True)

    # Show the plot
    plt.show()

# Example coordinates for a polygon
polygon_coords = [
    (1, 1), (4, 1), (4, 4), (1, 4)
]

# Plot the polygon
plot_polygon(polygon_coords)

