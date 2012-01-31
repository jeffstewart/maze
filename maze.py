import copy
import sys


def read_maze(_stdin=sys.stdin):
    maze = _stdin.readlines()
    maze = [list(line.strip("\n")) for line in maze]
    return maze


def write_maze(maze, _stdout=sys.stdout):
    for row in maze:
        print >> _stdout, "".join(row)


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

    # Base case solvable
    if start == find_maze_endpoint(maze):
         return maze

    # Recursive case
    return (solve_maze(maze, (row + 1, col)) or
            solve_maze(maze, (row - 1, col)) or
            solve_maze(maze, (row, col + 1)) or
            solve_maze(maze, (row, col - 1)))


def main(_stdin=sys.stdin, _stdout=sys.stdout):
    maze = read_maze(_stdin=_stdin)
    maze = solve_maze(maze, (0, 0))
    if maze is None:
        print >> _stdout, "Not solvable"
    else:
        write_maze(maze, _stdout=_stdout)


if __name__ == '__main__':
    main()



