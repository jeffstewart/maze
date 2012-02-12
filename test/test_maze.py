from cStringIO import StringIO

from nose.tools import assert_equal

import maze


def _test_maze_result(input, expected):
    _stdout = StringIO()
    maze.main(_stdin=StringIO(input), _stdout=_stdout)
    assert_equal(_stdout.getvalue(), expected)


def test_solvable_maze():

    input = """\
 XXXX
  XXX
X  XX
XX XX
X  XX
X XXX
X    """

    expected = """\
.XXXX
..XXX
X..XX
XX.XX
X..XX
X.XXX
X....
"""

    _test_maze_result(input, expected)


def test_unsolvable_full():

    # Tests a completely filled maze.
    input = """\
XXXXXXXXX
XXXXXXXXX
XXXXXXXXX
XXXXXXXXX
XXXXXXXXX
XXXXXXXXX
"""

    expected = "Not solvable\n"
    _test_maze_result(input, expected)


def test_unsolvable_start():

    # Test the origin is not available.
    input = """\
X



"""

    expected = "Not solvable\n"
    _test_maze_result(input, expected)


#def test_solvable_side():
#
#    # Test the end point not available.
#    input = """\
#
#XXXX
#XXXX
#XXXX
#"""
#
#    expected = """\
#....
#XXXX
#XXXX
#XXXX
#"""
#
#    _test_maze_result(input, expected)
#
#
#def test_solvable_bottom():
#
#    # Test the end point not available.
#    input = """\
# XXX
# XXX
# XXX
# XXX
#"""
#
#    expected = """\
#.XXX
#.XXX
#.XXX
#.XXX
#"""
#
#   _test_maze_result(input, expected)
#
