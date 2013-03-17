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
    for i in range(len(maze[row])-1):
	    if maze[row][i] == " ":
		return (row, i)


def solve_maze(maze, start):
    """Solve the maze.

    Return a solution to the maze.  If no solution is possible, return None.

    """
    row, col = start
    end = find_maze_endpoint(maze)
    if end == None:
	    return None

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
    if start == end:
         return maze

    # Recursive case
    # Use A* algorithm to select which direction to try first
    col_diff = (col - end[1])
    row_diff = (end[0] - row)
    if ((col_diff <= 0) and (abs(col_diff) <= row_diff)):
        return (solve_maze(maze, (row + 1, col)) or
                solve_maze(maze, (row, col + 1)) or
                solve_maze(maze, (row, col - 1)) or
                solve_maze(maze, (row - 1, col)))
    elif ((col_diff > 0) and (abs(col_diff) <= row_diff)):
        return (solve_maze(maze, (row + 1, col)) or
                solve_maze(maze, (row, col - 1)) or
                solve_maze(maze, (row, col + 1)) or
                solve_maze(maze, (row - 1, col)))
                
    elif ((col_diff <= 0) and (abs(col_diff) > row_diff)):
        return (solve_maze(maze, (row, col + 1)) or
                solve_maze(maze, (row + 1, col)) or
                solve_maze(maze, (row - 1, col)) or
                solve_maze(maze, (row, col - 1)))
    elif ((col_diff > 0) and (abs(col_diff) > row_diff)):
        return (solve_maze(maze, (row, col - 1)) or
                solve_maze(maze, (row + 1, col)) or
                solve_maze(maze, (row, col + 1)) or
                solve_maze(maze, (row - 1, col)))
                



def find_start(maze):
	"""

	Return the starting point of the maze somewhere along the top row.

	"""
	for i in range(len(maze[0])-1):
	    if maze[0][i] == " ":
		return (0, i)


def main(_stdin=sys.stdin, _stdout=sys.stdout):
    maze = read_maze(_stdin=_stdin)
    start = find_start(maze)
    if start == None:
	print >> _stdout, "No start point"
    else:
	maze = solve_maze(maze, start)
        if maze is None:
	    print >> _stdout, "Not solvable"
        else:
	    write_maze(maze, _stdout=_stdout)


if __name__ == '__main__':
    main()



