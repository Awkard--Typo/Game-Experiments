class Tile:
    def __init__(self, tile1, tile2, tile3, tag):
        self.tile1 = tile1
        self.tile2 = tile2
        self.tile3 = tile3
        self.piece = False
        self.tag = tag
        
    def __str__(self):
        t1 = ""
        t2 = ""
        t3 = ""
        
        if self.tile1 is not None:
            t1 = self.tile1.tag
        if self.tile2 is not None:
            t2 = self.tile2.tag
        if self.tile3 is not None:
            t3 = self.tile3.tag
            
        return self.tag + ": " + t1 + " " +  t2 + " " +  t3
        
    
      