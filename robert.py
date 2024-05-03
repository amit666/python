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

    def __init__(self, path):
        self.board_path = mpath.Path(path)

    def place(piece):
        pass

    def show(self):
        patch = mpatches.PathPatch(self.board_path, facecolor='none', lw=2)

        fig, ax = plt.subplots()
        ax.add_patch(patch)

        # Set the limits of the plot
        b = self.board_path.get_extents().bounds
        ax.set_xlim(b[0], b[2])
        ax.set_ylim(b[1], b[3])
        
        # Render the plot
        plt.show()

def main():
    pieces = (
        Piece( (3,3), ( 0,1,0, 0,1,1, 1,1,0 )),
        Piece( (2,4), ( 1,0, 1,1, 1,0, 1,0  )), 
        Piece( (3,3), ( 1,1,1, 1,1,0, 0,1,0 )),
        Piece( (3,3), ( 0,1,1, 0,1,0, 1,1,0 ))
    )
    print(f"pieces is {pieces}")

    board = ( (0,0), (5,0), (5,4), (2.5,6), (0,4) ) 
    b = Board(board)
    b.show()

if __name__ == "__main__":
    main()
