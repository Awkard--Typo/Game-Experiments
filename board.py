from tile import Tile

class Board:
    def __init__(self):
        self.board = None
        self.piece = None
        
    def getTileWithPiece(self):
        return self.piece
        
    def buildBasicBoard(self):
        #create middle Tile, load with piece, and link to piece pointer
        self.middle = Tile(None,None,None,"middle")
        self.middle.piece = True                                       #set middle tile to have piece
        self.piece = self.middle                                       #pointer to the tile that has the piece
        
        home1 = Tile(None,None,None,"home1")
        home2 = Tile(None,None,None,"home2")
        home3 = Tile(None,None,None,"home3")
        
        self.portal1 = Tile(None,None,None,"portal")
        self.portal2 = Tile(None,None,None,"portal2")
        self.portal3 = Tile(None,None,None,"portal")
        
        joint1 = Tile(None,None,None,"joint1")
        joint2 = Tile(None,None,None,"joint2")
        joint3 = Tile(None,None,None,"joint3")
        
        
        
    def getBoard(self):
        return self.board

