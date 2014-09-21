from tile import Tile

class Board:
    def __init__(self):
        self.middle = None                                            
        self.piece = None
        self.tiles = {}
        
    def getTileWithPiece(self):
        return self.piece
        
    def buildBasicBoard(self):
        #create middle Tile, load with piece, and link to piece pointer
        self.middle = Tile(None,None,None,"middle")
        self.middle.piece = True                                       #set middle tile to have piece
        self.piece = self.middle                                       #pointer to the tile that has the piece
        
        self.tiles['middle'] = self.middle
        
        home1 = Tile(None,None,None,"home1")
        home2 = Tile(None,None,None,"home2")
        home3 = Tile(None,None,None,"home3")
        
        self.tiles['home1'] = home1
        self.tiles['home2'] = home2
        self.tiles['home3'] = home3
        
        self.portal1 = Tile(None,None,None,"portal1")
        self.portal2 = Tile(None,None,None,"portal2")
        self.portal3 = Tile(None,None,None,"portal3")
        
        self.tiles['portal1'] = self.portal1
        self.tiles['portal2'] = self.portal2
        self.tiles['portal3'] = self.portal3
        
        joint1 = Tile(None,None,None,"joint1")
        joint2 = Tile(None,None,None,"joint2")
        joint3 = Tile(None,None,None,"joint3")
        
        self.tiles['joint1'] = joint1
        self.tiles['joint2'] = joint2
        self.tiles['joint3'] = joint3
        
        self.connectTiles(self.portal1,home1)
        self.connectTiles(self.portal2,home2)
        self.connectTiles(self.portal3,home3)
        
        self.connectTiles(self.middle,joint1)
        self.connectTiles(self.middle,joint2)
        self.connectTiles(self.middle,joint3)
        
        self.connectTiles(self.portal2,joint1)
        self.connectTiles(self.portal3,joint1)
                
        self.connectTiles(self.portal3,joint2)
        self.connectTiles(self.portal1,joint2)
                
        self.connectTiles(self.portal2,joint3)
        self.connectTiles(self.portal1,joint3)
        
        
    def connectTiles(self,t1,t2):
        self.connectTilesHelper(t1,t2)
        self.connectTilesHelper(t2,t1)
        
    def connectTilesHelper(self,t1,t2):
        if t1.tile1 is None:
            t1.tile1 = t2
        elif t1.tile2 is None:
            t1.tile2 = t2
        elif t1.tile3 is None:
            t1.tile3 = t2

        
    def getBoard(self):
        return self.middle #refer to board by pointing to it's middle  
      
    def __str__(self):
        rtn = ""
        for tag in self.tiles:
            rtn += str(self.tiles[tag]) + "\n"
        return rtn

