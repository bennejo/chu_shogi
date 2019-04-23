class Tile:

    piece_on_tile = None
    tile_coodinate = None

    def __init__(self, coordinate, piece):
        self.tile_coodinate = coordinate
        self.piece_on_tile = piece
