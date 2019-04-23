from pieces import NullPiece
from pieces import Bishop
from pieces import BlindTiger
from pieces import CopperGeneral
from pieces import DragonHorse
from pieces import DragonKing
from pieces import DrunkElephant
from pieces import FerociousLeopard
from pieces import FreeKing
from pieces import GoBetween
from pieces import GoldGeneral
from pieces import King
from pieces import Kylin
from pieces import Lance
from pieces import Lion
from pieces import Pawn
from pieces import Phoenix
from pieces import ReverseChariot
from pieces import Rook
from pieces import SideMover
from pieces import SilverGeneral
from pieces import VerticalMover


class Board:

    game_tiles = {}

    def __init__(self):
        pass

    def create_board(self):

        for tile in range(144):
            self.game_tiles[tile] = Tile(tile, NullPiece())

        self.game_tiles[0] = Tile(0, Lance("Black", 0))
        self.game_tiles[1] = Tile(1, FerociousLeopard("Black", 1))
        self.game_tiles[2] = Tile(2, CopperGeneral("Black", 2))
        self.game_tiles[3] = Tile(3, SilverGeneral("Black", 3))
        self.game_tiles[4] = Tile(4, GoldGeneral("Black", 4))
        self.game_tiles[5] = Tile(5, DrunkElephant("Black", 5))
        self.game_tiles[6] = Tile(6, King("Black", 6))
        self.game_tiles[7] = Tile(7, GoldGeneral("Black", 7))
        self.game_tiles[8] = Tile(8, SilverGeneral("Black", 8))
        self.game_tiles[9] = Tile(9, CopperGeneral("Black", 9))
        self.game_tiles[10] = Tile(10, FerociousLeopard("Black", 10))
        self.game_tiles[11] = Tile(11, Lance("Black", 11))
        self.game_tiles[12] = Tile(12, ReverseChariot("Black", 12))
        self.game_tiles[14] = Tile(14, Bishop("Black", 14))
        self.game_tiles[16] = Tile(16, BlindTiger("Black", 16))
        self.game_tiles[17] = Tile(17, Phoenix("Black", 17))
        self.game_tiles[18] = Tile(18, Kylin("Black", 18))
        self.game_tiles[19] = Tile(19, BlindTiger("Black", 19))
        self.game_tiles[21] = Tile(21, Bishop("Black", 21))
        self.game_tiles[23] = Tile(23, ReverseChariot("Black", 23))
        self.game_tiles[24] = Tile(24, SideMover("Black", 24))
        self.game_tiles[25] = Tile(25, VerticalMover("Black", 25))
        self.game_tiles[26] = Tile(26, Rook("Black", 26))
        self.game_tiles[27] = Tile(27, DragonHorse("Black", 27))
        self.game_tiles[28] = Tile(28, DragonKing("Black", 28))
        self.game_tiles[29] = Tile(29, FreeKing("Black", 29))
        self.game_tiles[30] = Tile(30, Lion("Black", 30))
        self.game_tiles[31] = Tile(31, DragonKing("Black", 31))
        self.game_tiles[32] = Tile(32, DragonHorse("Black", 32))
        self.game_tiles[33] = Tile(33, Rook("Black", 33))
        self.game_tiles[34] = Tile(34, VerticalMover("Black", 34))
        self.game_tiles[35] = Tile(35, SideMover("Black", 35))
        self.game_tiles[36] = Tile(36, Pawn("Black", 36))
        self.game_tiles[37] = Tile(37, Pawn("Black", 37))
        self.game_tiles[38] = Tile(38, Pawn("Black", 38))
        self.game_tiles[39] = Tile(39, Pawn("Black", 39))
        self.game_tiles[40] = Tile(40, Pawn("Black", 40))
        self.game_tiles[41] = Tile(41, Pawn("Black", 41))
        self.game_tiles[42] = Tile(42, Pawn("Black", 42))
        self.game_tiles[43] = Tile(43, Pawn("Black", 43))
        self.game_tiles[44] = Tile(44, Pawn("Black", 44))
        self.game_tiles[45] = Tile(45, Pawn("Black", 45))
        self.game_tiles[46] = Tile(46, Pawn("Black", 46))
        self.game_tiles[47] = Tile(47, Pawn("Black", 47))
        self.game_tiles[51] = Tile(51, GoBetween("Black", 51))
        self.game_tiles[56] = Tile(56, GoBetween("Black", 56))

        self.game_tiles[87] = Tile(87, GoBetween("White", 87))
        self.game_tiles[92] = Tile(92, GoBetween("White", 92))
        self.game_tiles[96] = Tile(96, Pawn("White", 96))
        self.game_tiles[97] = Tile(97, Pawn("White", 97))
        self.game_tiles[98] = Tile(9, Pawn("White", 98))
        self.game_tiles[99] = Tile(99, Pawn("White", 99))
        self.game_tiles[100] = Tile(100, Pawn("White", 100))
        self.game_tiles[101] = Tile(101, Pawn("White", 101))
        self.game_tiles[102] = Tile(102, Pawn("White", 102))
        self.game_tiles[103] = Tile(103, Pawn("White", 103))
        self.game_tiles[104] = Tile(104, Pawn("White", 104))
        self.game_tiles[105] = Tile(105, Pawn("White", 105))
        self.game_tiles[106] = Tile(106, Pawn("White", 106))
        self.game_tiles[107] = Tile(107, Pawn("White", 107))
        self.game_tiles[108] = Tile(108, SideMover("White", 108))
        self.game_tiles[109] = Tile(109, VerticalMover("White", 109))
        self.game_tiles[110] = Tile(110, Rook("White", 110))
        self.game_tiles[111] = Tile(111, DragonHorse("White", 111))
        self.game_tiles[112] = Tile(112, DragonKing("White", 112))
        self.game_tiles[113] = Tile(113, Lion("White", 113))
        self.game_tiles[114] = Tile(114, FreeKing("White", 114))
        self.game_tiles[115] = Tile(115, DragonKing("White", 115))
        self.game_tiles[116] = Tile(116, DragonHorse("White", 116))
        self.game_tiles[117] = Tile(117, Rook("White", 117))
        self.game_tiles[118] = Tile(118, VerticalMover("White", 118))
        self.game_tiles[119] = Tile(119, SideMover("White", 119))
        self.game_tiles[120] = Tile(120, ReverseChariot("White", 120))
        self.game_tiles[122] = Tile(122, Bishop("White", 122))
        self.game_tiles[124] = Tile(124, BlindTiger("White", 124))
        self.game_tiles[125] = Tile(125, Kylin("White", 125))
        self.game_tiles[126] = Tile(126, Phoenix("White", 126))
        self.game_tiles[127] = Tile(127, BlindTiger("White", 127))
        self.game_tiles[129] = Tile(129, Bishop("White", 129))
        self.game_tiles[131] = Tile(131, ReverseChariot("White", 131))
        self.game_tiles[132] = Tile(132, Lance("White", 132))
        self.game_tiles[133] = Tile(133, FerociousLeopard("White", 133))
        self.game_tiles[134] = Tile(134, CopperGeneral("White", 134))
        self.game_tiles[135] = Tile(135, SilverGeneral("White", 135))
        self.game_tiles[136] = Tile(136, GoldGeneral("White", 136))
        self.game_tiles[137] = Tile(137, King("White", 137))
        self.game_tiles[138] = Tile(138, DrunkElephant("White", 138))
        self.game_tiles[139] = Tile(139, GoldGeneral("White", 139))
        self.game_tiles[140] = Tile(140, SilverGeneral("White", 140))
        self.game_tiles[141] = Tile(141, CopperGeneral("White", 141))
        self.game_tiles[142] = Tile(142, FerociousLeopard("White", 142))
        self.game_tiles[143] = Tile(143, Lance("White", 143))

    def print_board(self):
        count = 0
        for tiles in range(144):
            print('|', end=self.game_tiles[tiles].piece_on_tile.to_string())
            count += 1
            if count == 12:
                print('|', end='\n')
                count = 0

class Tile:

    piece_on_tile = None
    tile_coodinate = None

    def __init__(self, coordinate, piece):
        self.tile_coodinate = coordinate
        self.piece_on_tile = piece

class Move:

    def __init__(self):
        pass
