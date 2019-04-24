import pygame
import os

b_b = pygame.image.load(os.path.join("img", "B_B.png"))
b_bt = pygame.image.load(os.path.join("img", "B_BT.png"))
b_c = pygame.image.load(os.path.join("img", "B_C.png"))
b_de = pygame.image.load(os.path.join("img", "B_DE.png"))
b_dh = pygame.image.load(os.path.join("img", "B_DH.png"))
b_dk = pygame.image.load(os.path.join("img", "B_DK.png"))
b_fk = pygame.image.load(os.path.join("img", "B_FK.png"))
b_fl = pygame.image.load(os.path.join("img", "B_FL.png"))
b_g = pygame.image.load(os.path.join("img", "B_G.png"))
b_gb = pygame.image.load(os.path.join("img", "B_GB.png"))
b_k = pygame.image.load(os.path.join("img", "B_K.png"))
b_ky = pygame.image.load(os.path.join("img", "B_KY.png"))
b_l = pygame.image.load(os.path.join("img", "B_L.png"))
b_ln = pygame.image.load(os.path.join("img", "B_LN.png"))
b_p = pygame.image.load(os.path.join("img", "B_P.png"))
b_ph = pygame.image.load(os.path.join("img", "B_PH.png"))
b_r = pygame.image.load(os.path.join("img", "B_R.png"))
b_rc = pygame.image.load(os.path.join("img", "B_RC.png"))
b_s = pygame.image.load(os.path.join("img", "B_S.png"))
b_sm = pygame.image.load(os.path.join("img", "B_SM.png"))
b_vm = pygame.image.load(os.path.join("img", "B_VM.png"))

w_b = pygame.image.load(os.path.join("img", "W_B.png"))
w_bt = pygame.image.load(os.path.join("img", "W_BT.png"))
w_c = pygame.image.load(os.path.join("img", "W_C.png"))
w_de = pygame.image.load(os.path.join("img", "W_DE.png"))
w_dh = pygame.image.load(os.path.join("img", "W_DH.png"))
w_dk = pygame.image.load(os.path.join("img", "W_DK.png"))
w_fk = pygame.image.load(os.path.join("img", "W_FK.png"))
w_fl = pygame.image.load(os.path.join("img", "W_FL.png"))
w_g = pygame.image.load(os.path.join("img", "W_G.png"))
w_gb = pygame.image.load(os.path.join("img", "W_GB.png"))
w_k = pygame.image.load(os.path.join("img", "W_K.png"))
w_ky = pygame.image.load(os.path.join("img", "W_KY.png"))
w_l = pygame.image.load(os.path.join("img", "W_L.png"))
w_ln = pygame.image.load(os.path.join("img", "W_LN.png"))
w_p = pygame.image.load(os.path.join("img", "W_P.png"))
w_ph = pygame.image.load(os.path.join("img", "W_PH.png"))
w_r = pygame.image.load(os.path.join("img", "W_R.png"))
w_rc = pygame.image.load(os.path.join("img", "W_RC.png"))
w_s = pygame.image.load(os.path.join("img", "W_S.png"))
w_sm = pygame.image.load(os.path.join("img", "W_SM.png"))
w_vm = pygame.image.load(os.path.join("img", "W_VM.png"))


b_img_paths = [b_b, b_bt, b_c, b_de, b_dh, b_dk, b_fk, b_fl, b_g, b_gb, b_k, b_ky, b_l, b_ln, b_p, b_ph, b_r, b_rc, b_s, b_sm, b_vm]
w_img_paths = [w_b, w_bt, w_c, w_de, w_dh, w_dk, w_fk, w_fl, w_g, w_gb, w_k, w_ky, w_l, w_ln, w_p, w_ph, w_r, w_rc, w_s, w_sm, w_vm]

b_imgs = []
w_imgs = []

for img in b_img_paths:
    b_imgs.append(pygame.transform.scale(img, (50,50)))

for img in w_img_paths:
    w_imgs.append(pygame.transform.scale(img, (50,50)))

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
