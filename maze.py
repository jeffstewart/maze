import copy
import sys


def read_maze():
    maze = sys.stdin.readlines()
    maze = [list(line.strip("\n")) for line in maze]
    return maze


def write_maze(maze):
    for row in maze:
        print "".join(row)


def find_maze_endpoint(maze):
    """Find the endpoint to the maze.

    Return (row, col).

    """
    row = len(maze) - 1
    col = len(maze[0]) - 1
    return (row, col)


def solve_maze(maze, start):
    """Solve the maze.

    Return a solution to the maze.  If no solution is possible, return None.

    """
    row, col = start

    # Base case not solvable
    try:
        curr = maze[row][col]
    except IndexError:
        return None
    if curr != " ":
        return None

    maze = copy.deepcopy(maze)
    maze[row][col] = "."
    write_maze(maze)    #TODO remove
    print

    # Base case solvable
    if start == find_maze_endpoint(maze):
         return maze

    # Recursive case
    return (solve_maze(maze, (row + 1, col)) or
            solve_maze(maze, (row - 1, col)) or
            solve_maze(maze, (row, col + 1)) or
            solve_maze(maze, (row, col - 1)))






maze = read_maze()
maze = solve_maze(maze, (0, 0))
if maze is None:
    print "Not solvable"
else:
    write_maze(maze)



