import sys

sys.path.insert(0, '/home/action/workspace/game/')

from board import Board

t1 = Board()
t1.buildBasicBoard()
print t1.portal1