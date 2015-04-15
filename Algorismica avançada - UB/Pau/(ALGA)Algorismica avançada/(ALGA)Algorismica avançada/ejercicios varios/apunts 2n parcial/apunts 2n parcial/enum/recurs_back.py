def recursiveBacktrack(board):
  if(checkEntireBoard(board)):
    return board
  else:
    for node in board:
      if(node.val == "."):
        for val in (1,2,3,4,5,6,7,8,9):
           if(checkNodeConstraintsOk(board, node, val)):
             node.val = val
             posNewBoard = recursiveBacktrack(board)
             if(posNewBoard != None):
               return posNewBoard
             else:
              node.val = "."
         return None

---------------------------------------------------------------------

def checkEntireBoard(board):
  for node in board:
    if(node.val == "."):
      return False
    if(not checkNodeConstraintsOk(board, node, node.val)):
      return False
  return True

def checkNodeConstraintsOk(board, inNode, posVal):
  val = posVal
  for node in board:
    if(node != inNode and node.val == val):
      if(node.x == inNode.x or node.y == inNode.y or node.sqr == inNode.sqr):
        return False
  return True
