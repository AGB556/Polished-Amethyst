
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)
keyboard.row_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()

#Encoder
encoder_handler.pins = ((board.GP21,board.GP22,board.GP28),)

keyboard.keymap = [
	    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9,
	    KC.F10, KC.F11, KC.F12, KC.PGDN, KC.LNUM, KC.PSCR, KC.SLCK, KC.PAUSE, KC.GRAVE, KC.N1,
      KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS,
	    KC.EQUAL, KC.BSPACE, KC.DEL, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS, KC.TAB, KC.Q, KC.W, KC.E,
      KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH,
      KC.P7, KC.P8, KC.P9, KC.NO, KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G,
      KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.P4, KC.P5, KC.P6,
      KC.KP_PLUS, KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA,
      KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.P1, KC.P2, KC.P3, KC.KP_ENTER, KC.LCTRL, KC.LGUI, 
      KC.LALT, KC.SPACE, KC.RALT, KC.RGUI, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.P0, KC.PDOT]
]
encoder_handler.map = [  
            ((KC.VOLD, KC.VOLU),),        
            ((KC.MW_UP, KC.MW_DN),),       
            ]

if __name__ == '__main__':
    keyboard.go()
