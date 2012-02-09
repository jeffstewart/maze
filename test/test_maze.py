from cStringIO import StringIO

from nose.tools import assert_equal

import maze


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

    _stdout = StringIO()
    maze.main(_stdin=StringIO(input), _stdout=_stdout)
    assert_equal(_stdout.getvalue(), expected)


def test_unsolvable1():

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

    _stdout = StringIO()
    maze.main(_stdin=StringIO(input), _stdout=_stdout)
    assert_equal(_stdout.getvalue(), expected)


def test_unsolvable2():

    # Test the origin is not available.
    input = """\
X



"""

    expected = "Not solvable\n"

    _stdout = StringIO()
    maze.main(_stdin=StringIO(input), _stdout=_stdout)
    assert_equal(_stdout.getvalue(), expected)


def test_unsolvable3():

    # Test the end point not available.
    input = """\



   X
"""

    expected = "Not solvable\n"

    _stdout = StringIO()
    maze.main(_stdin=StringIO(input), _stdout=_stdout)
    assert_equal(_stdout.getvalue(), expected)
