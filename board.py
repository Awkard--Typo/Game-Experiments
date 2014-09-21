from tile import Tile

class Board:
    def __init__(self):
        self.middle = None                                            
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
        
        self.connectTiles(self.portal1,home1)
        
    def connectTiles(self,t1,t2):
        self.connectTilesHelper(t1,t2)
        self.connectTilesHelper(t2,t1)
        
    def connectTilesHelper(self,t1,t2):
        if t1.tile1 is None:
            t1.tile1 = t2
        elif t1.tile2 is None:
            t1.tile1 = t2
        elif t1.tile2 is None:
            t1.tile1 = t2

        
    def getBoard(self):
        return self.middle #refer to board by pointing to it's middle             

