from cStringIO import StringIO

from nose.tools import assert_equal

import maze


def test_true():
    assert_equal(1, 1)


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
    