from win32api import GetSystemMetrics

# level_map = [
# '                                                                                  ',
# 'X                                XXXXX                                             ',
# 'X     P                    XX           XXXXXX                                        ',
# 'XXX                                                                                ',
# 'XX       XXX      XXX                                                               ',
# 'XX                                   XXXXX XXXXXXXX                                      ',
# '      XXX   XXX           XXXXX      XXXXX   XXXXXX            XX                          ',
# '      XXX   XXX      XX   XXXXX   XXXXXX    XXX           XX   XX                        ',
# '    XXXXX   XXXXXX   XX   XXXXX   XXXXX          XXXXX    XX   XX                         ',
# 'XXXXXXXXX   XXXXXX   XX   XXXXX   XXXXXXXXXXXXXXXXXXXX    XX   XX                               ',
# ]

level_map = [
'                                                                                                               ',
'                                                                                                                  ',
'                                                                                           XXXXXXXXXXXXXXX               ',
'                                                                               XXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'         X           X           XXXX                                   XXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                             ',
'                                                            XXX     X          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXX                     ',
'                XXX                                                            XXXXXXXXXXXXXXXXXXXX                                  ',
'                                        XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXXXX     XXXX            XX                 ',
'P                                       XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX       XXXX                               ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX     XXXXXX                                ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX      XXXXXX                             ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXX                          ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXX                                   ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
]

tile_size = 64
screen_width = GetSystemMetrics (0)
screen_height = GetSystemMetrics (1)

