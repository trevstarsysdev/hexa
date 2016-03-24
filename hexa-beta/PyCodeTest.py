__author__ = 'karthi'
import binascii

img = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80,
               0x80, 0xC0, 0xC0, 0xE0, 0xE0, 0xF0, 0xF0, 0xF0, 0xF8, 0xF8, 0xF8, 0xF8, 0xF8, 0xF8, 0xFA, 0xFE,
               0xFA, 0xF4, 0xFC, 0xF0, 0xF0, 0xE0, 0xEC, 0xFC, 0xD8, 0xC8, 0x30, 0xE0, 0xE0, 0xC0, 0x80, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0xFC, 0xFE, 0xFF, 0xFF,
               0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x3F, 0x3F, 0x3F,
               0x7F, 0x7F, 0x7F, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF,
               0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3F,
               0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x0F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
               0xFE, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0xFF, 0xFF, 0xBF, 0x07, 0x20,
               0x20, 0x20, 0x20, 0xE0, 0xE0, 0xE0, 0xE0, 0xA0, 0x80, 0x40, 0x80, 0x00, 0x80, 0xC0, 0xC0, 0xC0,
               0xC0, 0xE0, 0xE0, 0xE0, 0xE0, 0x60, 0x60, 0x60, 0x60, 0x27, 0x3F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
               0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0xC0, 0xC0, 0xC0, 0x20, 0x10, 0x00, 0x00, 0x10, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x1F, 0x03, 0x01, 0x01,
               0x01, 0x01, 0x00, 0x03, 0x01, 0x01, 0x03, 0x03, 0x01, 0x0E, 0x03, 0x00, 0x01, 0x01, 0x0D, 0x05,
               0x23, 0x01, 0x01, 0x03, 0x03, 0x00, 0x03, 0x03, 0x02, 0x00, 0x06, 0x07, 0xFC, 0x1F, 0x01, 0x01,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x80, 0x00, 0x00,
               0xDE, 0x7B, 0x7B, 0xFF, 0x7B, 0xFA, 0x0B, 0x60, 0x04, 0x01, 0x75, 0xC8, 0x74, 0xFC, 0xFC, 0xFE,
               0x7C, 0xFC, 0x7C, 0xF8, 0xF8, 0xEC, 0xEC, 0x7E, 0x78, 0xFA, 0xFE, 0xBC, 0xBC, 0xB4, 0x20, 0x50,
               0x50, 0x94, 0x80, 0xC0, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x40, 0x44, 0x64, 0x20, 0x60, 0x70, 0x70, 0x68, 0x6C, 0x60,
               0x48, 0x00, 0x80, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02,
               0xDE, 0xFF, 0xFD, 0xFF, 0xFF, 0xFD, 0xFB, 0xFA, 0xFC, 0xF7, 0x79, 0xF8, 0xFC, 0xFF, 0xFF, 0xFB,
               0xFD, 0xF8, 0xFD, 0x3F, 0x7D, 0xFD, 0xFE, 0xAC, 0xFD, 0xFB, 0x39, 0x38, 0x79, 0xD9, 0xD3, 0xF9,
               0xCF, 0xFD, 0x1C, 0x1A, 0x1F, 0x0A, 0x8E, 0x18, 0x19, 0x18, 0x00, 0x20, 0x18, 0x00, 0x60, 0xEC,
               0x98, 0xB0, 0xC0, 0xC0, 0x01, 0x01, 0x03, 0x01, 0x00, 0x22, 0x22, 0x62, 0x62, 0x22, 0x22, 0x00,
               0x01, 0x03, 0x03, 0x03, 0x03, 0xC0, 0xF0, 0x60, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x00, 0x00,
               0x00, 0x00, 0x01, 0x00, 0x20, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0xC0, 0x50,
               0xAC, 0xEF, 0xDB, 0x1F, 0x3F, 0x9B, 0xFF, 0xF7, 0xF7, 0xCF, 0xFB, 0xFF, 0xED, 0x7D, 0xBC, 0x7C,
               0x3F, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xF6, 0xCC, 0x7D, 0xE3, 0xFE, 0x3B, 0x63, 0x6D, 0x84,
               0x00, 0x08, 0x00, 0x00, 0x04, 0x0C, 0x10, 0xF8, 0xE0, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x01, 0x07, 0x0E, 0x1F, 0x3F, 0x7E, 0xFE, 0xBE, 0xFE, 0xFC, 0xFC, 0xFE, 0xFE, 0xFE, 0xFC, 0xFC,
               0xFC, 0xFE, 0xFE, 0xFE, 0xDF, 0x27, 0x03, 0xF0, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
               0x00, 0x02, 0x02, 0x80, 0x80, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x02,
               0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x06, 0xE0, 0x00, 0x00, 0x00, 0x00, 0x01, 0x29]

font8x8= [
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  # <space> 32
0x00,0x00,0x00,0x00,0x5F,0x00,0x00,0x00,  # !
0x00,0x00,0x00,0x03,0x00,0x03,0x00,0x00,  # "
0x00,0x24,0x7E,0x24,0x24,0x7E,0x24,0x00,  # #
0x00,0x2E,0x2A,0x7F,0x2A,0x3A,0x00,0x00,  # $
0x00,0x46,0x26,0x10,0x08,0x64,0x62,0x00,  # %
0x00,0x20,0x54,0x4A,0x54,0x20,0x50,0x00,  # &
0x00,0x00,0x00,0x04,0x02,0x00,0x00,0x00,  # '
0x00,0x00,0x00,0x3C,0x42,0x00,0x00,0x00,  # (
0x00,0x00,0x00,0x42,0x3C,0x00,0x00,0x00,  # )
0x00,0x10,0x54,0x38,0x54,0x10,0x00,0x00,  # *
0x00,0x10,0x10,0x7C,0x10,0x10,0x00,0x00,  # +
0x00,0x00,0x00,0x80,0x60,0x00,0x00,0x00,  # ,
0x00,0x10,0x10,0x10,0x10,0x10,0x00,0x00,  # -
0x00,0x00,0x00,0x60,0x60,0x00,0x00,0x00,  # .
0x00,0x40,0x20,0x10,0x08,0x04,0x00,0x00,  # /

0x3C,0x62,0x52,0x4A,0x46,0x3C,0x00,0x00,  # 0
0x44,0x42,0x7E,0x40,0x40,0x00,0x00,0x00,  # 1
0x64,0x52,0x52,0x52,0x52,0x4C,0x00,0x00,  # 2
0x24,0x42,0x42,0x4A,0x4A,0x34,0x00,0x00,  # 3
0x30,0x28,0x24,0x7E,0x20,0x20,0x00,0x00,  # 4
0x2E,0x4A,0x4A,0x4A,0x4A,0x32,0x00,0x00,  # 5
0x3C,0x4A,0x4A,0x4A,0x4A,0x30,0x00,0x00,  # 6
0x02,0x02,0x62,0x12,0x0A,0x06,0x00,0x00,  # 7
0x34,0x4A,0x4A,0x4A,0x4A,0x34,0x00,0x00,  # 8
0x0C,0x52,0x52,0x52,0x52,0x3C,0x00,0x00,  # 9
0x00,0x00,0x00,0x48,0x00,0x00,0x00,0x00,  # :
0x00,0x00,0x80,0x64,0x00,0x00,0x00,0x00,  # ;
0x00,0x00,0x10,0x28,0x44,0x00,0x00,0x00,  # <
0x00,0x28,0x28,0x28,0x28,0x28,0x00,0x00,  # =
0x00,0x00,0x44,0x28,0x10,0x00,0x00,0x00,  # >
0x00,0x04,0x02,0x02,0x52,0x0A,0x04,0x00,  # ?

0x00,0x3C,0x42,0x5A,0x56,0x5A,0x1C,0x00,  # @
0x7C,0x12,0x12,0x12,0x12,0x7C,0x00,0x00,  # A
0x7E,0x4A,0x4A,0x4A,0x4A,0x34,0x00,0x00,  # B
0x3C,0x42,0x42,0x42,0x42,0x24,0x00,0x00,  # C
0x7E,0x42,0x42,0x42,0x24,0x18,0x00,0x00,  # D
0x7E,0x4A,0x4A,0x4A,0x4A,0x42,0x00,0x00,  # E
0x7E,0x0A,0x0A,0x0A,0x0A,0x02,0x00,0x00,  # F
0x3C,0x42,0x42,0x52,0x52,0x34,0x00,0x00,  # G
0x7E,0x08,0x08,0x08,0x08,0x7E,0x00,0x00,  # H
0x00,0x42,0x42,0x7E,0x42,0x42,0x00,0x00,  # I
0x30,0x40,0x40,0x40,0x40,0x3E,0x00,0x00,  # J
0x7E,0x08,0x08,0x14,0x22,0x40,0x00,0x00,  # K
0x7E,0x40,0x40,0x40,0x40,0x40,0x00,0x00,  # L
0x7E,0x04,0x08,0x08,0x04,0x7E,0x00,0x00,  # M
0x7E,0x04,0x08,0x10,0x20,0x7E,0x00,0x00,  # N
0x3C,0x42,0x42,0x42,0x42,0x3C,0x00,0x00,  # O

0x7E,0x12,0x12,0x12,0x12,0x0C,0x00,0x00,  # P
0x3C,0x42,0x52,0x62,0x42,0x3C,0x00,0x00,  # Q
0x7E,0x12,0x12,0x12,0x32,0x4C,0x00,0x00,  # R
0x24,0x4A,0x4A,0x4A,0x4A,0x30,0x00,0x00,  # S
0x02,0x02,0x02,0x7E,0x02,0x02,0x02,0x00,  # T
0x3E,0x40,0x40,0x40,0x40,0x3E,0x00,0x00,  # U
0x1E,0x20,0x40,0x40,0x20,0x1E,0x00,0x00,  # V
0x3E,0x40,0x20,0x20,0x40,0x3E,0x00,0x00,  # W
0x42,0x24,0x18,0x18,0x24,0x42,0x00,0x00,  # X
0x02,0x04,0x08,0x70,0x08,0x04,0x02,0x00,  # Y
0x42,0x62,0x52,0x4A,0x46,0x42,0x00,0x00,  # Z
0x00,0x00,0x7E,0x42,0x42,0x00,0x00,0x00,  # [
0x00,0x04,0x08,0x10,0x20,0x40,0x00,0x00,  # <backslash>
0x00,0x00,0x42,0x42,0x7E,0x00,0x00,0x00,  # ]
0x00,0x08,0x04,0x7E,0x04,0x08,0x00,0x00,  # ^
0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x00,  # _

0x3C,0x42,0x99,0xA5,0xA5,0x81,0x42,0x3C,  # `
0x00,0x20,0x54,0x54,0x54,0x78,0x00,0x00,  # a
0x00,0x7E,0x48,0x48,0x48,0x30,0x00,0x00,  # b
0x00,0x00,0x38,0x44,0x44,0x44,0x00,0x00,  # c
0x00,0x30,0x48,0x48,0x48,0x7E,0x00,0x00,  # d
0x00,0x38,0x54,0x54,0x54,0x48,0x00,0x00,  # e
0x00,0x00,0x00,0x7C,0x0A,0x02,0x00,0x00,  # f
0x00,0x18,0xA4,0xA4,0xA4,0xA4,0x7C,0x00,  # g
0x00,0x7E,0x08,0x08,0x08,0x70,0x00,0x00,  # h
0x00,0x00,0x00,0x48,0x7A,0x40,0x00,0x00,  # i
0x00,0x00,0x40,0x80,0x80,0x7A,0x00,0x00,  # j
0x00,0x7E,0x18,0x24,0x40,0x00,0x00,0x00,  # k
0x00,0x00,0x00,0x3E,0x40,0x40,0x00,0x00,  # l
0x00,0x7C,0x04,0x78,0x04,0x78,0x00,0x00,  # m
0x00,0x7C,0x04,0x04,0x04,0x78,0x00,0x00,  # n
0x00,0x38,0x44,0x44,0x44,0x38,0x00,0x00,  # o

0x00,0xFC,0x24,0x24,0x24,0x18,0x00,0x00,  # p
0x00,0x18,0x24,0x24,0x24,0xFC,0x80,0x00,  # q
0x00,0x00,0x78,0x04,0x04,0x04,0x00,0x00,  # r
0x00,0x48,0x54,0x54,0x54,0x20,0x00,0x00,  # s
0x00,0x00,0x04,0x3E,0x44,0x40,0x00,0x00,  # t
0x00,0x3C,0x40,0x40,0x40,0x3C,0x00,0x00,  # u
0x00,0x0C,0x30,0x40,0x30,0x0C,0x00,0x00,  # v
0x00,0x3C,0x40,0x38,0x40,0x3C,0x00,0x00,  # w
0x00,0x44,0x28,0x10,0x28,0x44,0x00,0x00,  # x
0x00,0x1C,0xA0,0xA0,0xA0,0x7C,0x00,0x00,  # y
0x00,0x44,0x64,0x54,0x4C,0x44,0x00,0x00,  # z
0x00,0x08,0x08,0x76,0x42,0x42,0x00,0x00,  # {
0x00,0x00,0x00,0x7E,0x00,0x00,0x00,0x00,  # |
0x00,0x42,0x42,0x76,0x08,0x08,0x00,0x00,  # }
0x00,0x00,0x04,0x02,0x04,0x02,0x00,0x00,  # ~
]

st = "hello"

def getHexCode(ch):
    for i in range(8):
        yield font8x8[(ord(ch)-32)*8+i]

mylist = range(3)
outval = [0x7C,0x12,0x12,0x12,0x12,0x7C,0x00,0x00]
for i in outval:
    print(i)
print (font8x8[12])

a=0x00
s="{:0>8}".format("{0:b}".format(a))
print(s)

#for x in st:
#    z = getHexCode(x)
#    for a in range(8):
#        #s="{:0>8}".format("{0:b}".format(a))
#        s="{:0>8}".format("{0:b}".format(z.next()))
#        print(s,"sss")

c= (x for x in getHexCode('A'))
print ("{:0>8}".format("{0:b}".format(0xff^((next(c)))))," >>> hexacode")

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = yrange(3)
print(y)
print(next(y))
next(y)
print(next(y))
#print(next(y))

x=9

con = "{:.^%d}" % x

#s= ("{:.^%d}" % x).format("hello")
#s = "005600000000000000000056".decode("hex")
s = binascii.unhexlify("005600000000000000000056")
#s = bytes.fromhex('005600000000000000000056').decode('utf-8')
#s = 0X005600000000000000000056 #4a4b4c
a = 0x40
#s = bin(10)
#s = s + "+9"
#str = s
#s = eval(str)
testvar1=binascii.hexlify(s).decode("utf-8")
#testvar = binascii.unhexlify(testvar1)
print ("\n\n***>>>",type(testvar1 ),">>>>>",testvar1)
print (">>>>",testvar1[0])

