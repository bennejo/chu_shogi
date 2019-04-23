class Piece:
    def __init__(self):
        pass

class Bishop(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "B"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class BlindTiger(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "BT"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class CopperGeneral(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "C"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class CrownPrince(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+DE"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class DragonHorse(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "DH"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class DragonKing(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "DK"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class DrunkElephant(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "DE"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class FerociousLeopard(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "FL"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class FlyingOx(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+VM"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class FlyingStag(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+BT"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class FreeBoar(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+SM"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class FreeKing(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "FK"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class GoBetween(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "GB"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class GoldGeneral(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "G"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class HornedFalcon(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+DH"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class King(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "K"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Kylin(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "KY"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Lance(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "L"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Lion(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "LN"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Pawn(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "P"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Phoenix(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "PH"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class NullPiece(Piece):

    def __init__(self):
        pass

    def to_string(self):
        return "-"

class ReverseChariot(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "RC"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Rook(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "R"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class SideMover(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "SM"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class SilverGeneral(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "S"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class SoaringEagle(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+DK"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Tokin(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+P"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class VerticalMover(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "VM"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class Whale(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+RC"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()

class WhiteHorse(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position
        self.short_name = "+L"

    def to_string(self):
        return self.short_name if self.alliance == "Black" else self.short_name.lower()
