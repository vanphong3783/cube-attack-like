'''
Created on Dec 13, 2010
'''

__author__ = 'Bo Zhu, bo.zhu@uwaterloo.ca'
__copyright__ = 'Copyright 2010, University of Waterloo'
__license__ = 'GPL, http://www.gnu.org/licenses/gpl.txt'

cube_attack_table1 = (
    ((0, 9, 50),    (2, 13, 20, 24, 37, 42, 43, 46, 53, 55, 57, 67),    675), 
    ((0, 24),       (2, 12, 17, 25, 37, 39, 46, 48, 54, 56, 65, 78),    673),
    ((1, 10, 51),   (3, 14, 21, 25, 38, 43, 44, 47, 54, 56, 58, 68),    674),
    ((1, 25),       (3, 13, 18, 26, 38, 40, 47, 49, 55, 57, 66, 79),    672),
    ((2, 34, 62),   (0, 5, 7, 18, 21, 32, 38, 43, 59, 67, 73, 78),      678),
    ((3, 35, 63),   (1, 6, 8, 19, 22, 33, 39, 44, 60, 68, 74, 79),      677),
    ((4,),          (11, 18, 20, 33, 45, 47, 53, 60, 61, 63, 69, 78),   675),
    ((5,),          (5, 14, 16, 18, 27, 31, 37, 43, 48, 55, 63, 78),    677),
    ((7,),          (1, 3, 6, 7, 12, 18, 22, 38, 47, 58, 67, 74),       675),
    ((8, 49, 68),   (1, 12, 19, 23, 36, 41, 42, 45, 52, 54, 56, 66),    676),
    ((11,),         (0, 4, 9, 11, 22, 24, 27, 29, 44, 46, 51, 76),      684),
    ((12,),         (0, 5, 8, 11, 13, 21, 22, 26, 36, 38, 53, 79),      673),
    ((13,),         (0, 5, 8, 11, 13, 22, 26, 36, 37, 38, 53, 79),      673),
    ((14,),         (2, 5, 7, 10, 14, 24, 27, 39, 49, 56, 57, 61),      672), 
    ((15,),         (0, 2, 9, 11, 13, 37, 44, 47, 49, 68, 74, 78),      685),
    ((16,),         (1, 6, 7, 12, 18, 21, 29, 33, 34, 45, 49, 70),      675),
    ((17,),         (8, 11, 15, 17, 26, 23, 32, 42, 51, 62, 64, 79),    677),
    ((18,),         (0, 10, 16, 19, 28, 31, 43, 50, 53, 66, 69, 79),    676),
    ((19,),         (4, 9, 10, 15, 21, 24, 32, 36, 37, 48, 52, 73),     672),
    ((20,),         (7, 10, 18, 20, 23, 25, 31, 45, 53, 63, 71, 78),    675),
    ((20, 50),      (11, 16, 20, 22, 35, 43, 46, 51, 55, 58, 62, 63),   675),
    ((21, 66),      (10, 13, 15, 17, 30, 37, 39, 42, 47, 57, 73, 79),   673),
    ((22,),         (2, 4, 21, 23, 25, 41, 44, 54, 58, 66, 73, 78),     673),
    ((23,),         (3, 6, 14, 21, 23, 27, 32, 40, 54, 57, 70, 71),     672),
    ((24,),         (3, 5, 14, 16, 18, 20, 33, 56, 57, 65, 73, 75),     672),
    ((28,),         (6, 11, 14, 19, 33, 39, 44, 52, 58, 60, 74, 79),    676),
    ((29,),         (1, 7, 12, 18, 21, 25, 29, 45, 46, 61, 68, 70),     675),
    ((30,),         (2, 8, 13, 19, 22, 26, 30, 46, 47, 62, 69, 71),     674),
    ((31,),         (3, 9, 14, 20, 23, 27, 31, 47, 48, 63, 70, 72),     673),
    ((32,),         (4, 10, 15, 21, 24, 28, 32, 48, 49, 64, 71, 73),    672),
    ((33,),         (2, 4, 6, 12, 23, 29, 32, 37, 46, 49, 52, 76),      680),
    ((34, 62),      (0, 5, 7, 13, 18, 21, 32, 38, 43, 59, 73, 78),      678),
    ((35, 63),      (1, 6, 8, 14, 19, 22, 33, 39, 44, 60, 74, 79),      677),
    ((36,),         (2, 4, 5, 8, 15, 19, 27, 32, 35, 57, 71, 78),       677),
    ((38, 56),      (0, 3, 4, 9, 20, 28, 33, 41, 54, 58, 72, 79),       678),
    ((39, 57, 66),  (8, 11, 13, 17, 23, 25, 35, 45, 47, 54, 70, 79),    674), 
    ((40, 58, 64),  (0, 6, 10, 16, 19, 31, 43, 50, 66, 69, 77, 79),     676),
    ((41,),         (2, 15, 17, 20, 21, 37, 39, 44, 46, 56, 67, 73),    674),
    ((42, 60),      (1, 16, 20, 22, 34, 37, 38, 53, 58, 69, 71, 78),    674),
    ((43,),         (2, 7, 14, 22, 41, 45, 48, 58, 68, 70, 72, 76),     673),
    ((44, 62),      (3, 14, 16, 18, 20, 23, 32, 46, 56, 57, 65, 73),    672),
    ((45, 64),      (0, 6, 10, 16, 18, 28, 31, 43, 53, 69, 77, 79),     676),
    ((46, 55),      (2, 8, 11, 13, 28, 31, 35, 37, 49, 51, 68, 78),     684),
    ((47,),         (5, 8, 20, 32, 36, 39, 45, 51, 65, 69, 76, 78),     676),
    ((48,),         (2, 4, 10, 14, 16, 22, 25, 44, 49, 51, 57, 78),     678),
    ((49, 62),      (1, 12, 19, 23, 36, 41, 42, 45, 52, 56, 69, 75),    676),
    ((51, 62),      (1, 7, 8, 13, 21, 23, 28, 30, 47, 68, 71, 75),      674),
    ((52,),         (5, 8, 9, 12, 16, 18, 23, 40, 44, 63, 66, 70),      674),
    ((53,),         (2, 11, 21, 24, 32, 55, 57, 60, 63, 66, 70, 77),    675),
    ((54, 60),      (4, 7, 10, 18, 20, 25, 50, 53, 61, 63, 71, 78),     675),
    ((55, 64),      (5, 12, 16, 19, 22, 36, 47, 55, 63, 71, 77, 79),    674),
    ((56,),         (4, 9, 18, 21, 23, 27, 32, 38, 43, 58, 67, 69),     677),
    ((57,),         (1, 7, 9, 14, 18, 21, 33, 40, 45, 49, 59, 68),      675),
    ((58,),         (2, 6, 12, 13, 19, 23, 30, 48, 55, 59, 69, 79),     673),
    ((60,),         (5, 7, 10, 13, 15, 17, 28, 40, 47, 73, 76, 79),     681),
    ((61,),         (13, 21, 24, 39, 42, 46, 48, 51, 55, 61, 72, 78),   673),
    ((62,),         (2, 4, 10, 11, 19, 34, 47, 55, 56, 58, 69, 77),     674),
    ((63,),         (5, 7, 10, 15, 17, 35, 40, 47, 52, 57, 76, 79),     674),
    ((64,),         (8, 11, 13, 17, 23, 25, 35, 47, 62, 64, 68, 79),    673),
    ((65,),         (2, 3, 13, 15, 19, 29, 32, 37, 39, 51, 76, 79),     682),
    ((66,),         (5, 7, 10, 13, 15, 17, 35, 40, 52, 70, 76, 79),     678),
    ((67,),         (5, 20, 24, 29, 33, 35, 37, 39, 63, 65, 74, 78),    677),
    ((68,),         (1, 12, 19, 23, 36, 41, 52, 54, 56, 66, 69, 75),    676), 
)

cube_attack_table2 = (
    ((0,),     (1, 3, 4, 7, 9, 10, 12, 16, 19, 21, 25, 27, 29, 30, 32, 34, 35, 37, 40, 47, 50, 51, 60, 61, 64, 67, 72, 73, 79),        769,    ()),
    ((3,),     (0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 32, 37, 40, 43, 44, 48, 50, 53, 57, 59, 61, 63, 64, 66, 68, 71, 73, 77, 79),   773,    (11,)),
    ((20,),    (1, 3, 5, 7, 10, 14, 18, 20, 22, 23, 26, 30, 36, 38, 42, 43, 44, 45, 47, 49, 52, 54, 60, 63, 69, 71, 72, 73, 78),       770,    (53,)),
    ((22,),    (1, 3, 5, 7, 10, 12, 14, 16, 18, 20, 23, 26, 30, 39, 41, 42, 43, 47, 50, 52, 53, 55, 58, 60, 61, 64, 69, 71, 78),       769,    ()),
    ((23,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 21, 23, 26, 30, 34, 35, 36, 43, 45, 46, 48, 49, 54, 59, 64, 67, 72, 73, 74, 75, 79),    767,    ()),
    ((29,),    (1, 3, 5, 7, 10, 12, 14, 17, 20, 22, 24, 30, 32, 34, 37, 38, 40, 41, 48, 50, 54, 56, 58, 59, 65, 66, 68, 70, 78),       774,    ()),
    ((30,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 21, 23, 26, 30, 33, 34, 35, 36, 43, 45, 46, 49, 54, 57, 59, 62, 64, 72, 73, 75, 79),    773,    (67,)),
    ((31,),    (0, 2, 4, 6, 8, 10, 13, 14, 17, 19, 21, 23, 26, 30, 31, 34, 35, 36, 37, 42, 53, 60, 61, 64, 66, 69, 72, 73, 77, 79),    773,    ()),
    ((32,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 21, 23, 25, 26, 27, 30, 32, 34, 43, 44, 53, 58, 63, 68, 70, 71, 72, 75, 78, 79),        772,    (33, 37, 38)),
    ((33, 60, 66, 68),     (1, 3, 5, 7, 10, 14, 18, 20, 23, 26, 30, 35, 37, 39, 40, 41, 44, 48, 49, 51, 54, 58, 59, 60, 61, 64, 70, 75, 77, 78), 772, ()),
    ((34,),    (1, 3, 5, 7, 10, 12, 14, 16, 17, 20, 24, 28, 30, 33, 34, 36, 40, 42, 45, 46, 51, 52, 54, 56, 62, 66, 70, 77, 78),       770,    (76,)),
    ((35,),    (1, 3, 4, 6, 7, 8, 9, 12, 14, 16, 19, 21, 25, 27, 30, 38, 41, 44, 45, 48, 50, 55, 57, 60, 63, 65, 71, 73, 79),          769,    ()),
    ((36,),    (0, 2, 4, 5, 6, 8, 10, 14, 17, 19, 21, 23, 26, 27, 30, 37, 39, 40, 47, 48, 55, 62, 65, 70, 73, 75, 77, 78, 79),         768,    (54,)),
    ((37,),    (1, 3, 5, 7, 10, 12, 14, 16, 17, 20, 24, 26, 30, 32, 35, 37, 41, 45, 46, 54, 58, 60, 64, 67, 68, 69, 70, 72, 78),       770,    ()),
    ((38,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 23, 25, 26, 30, 34, 36, 38, 40, 42, 44, 53, 56, 57, 60, 63, 69, 72, 73, 75, 79),        768,    (39,)),
    ((41,),    (0, 1, 3, 4, 7, 10, 12, 15, 17, 19, 22, 24, 25, 28, 30, 34, 39, 42, 44, 52, 56, 58, 59, 62, 64, 68, 70, 72, 79),        773,    (71,)),
    ((45,),    (1, 3, 5, 7, 10, 12, 14, 16, 18, 20, 22, 23, 26, 30, 33, 39, 42, 43, 47, 50, 52, 53, 55, 58, 60, 64, 71, 77, 78),       769,    ()),
    ((46,),    (1, 3, 5, 8, 11, 14, 16, 17, 19, 21, 23, 26, 27, 29, 30, 32, 36, 38, 42, 44, 45, 49, 51, 53, 59, 60, 63, 64, 75, 76, 78), 771,  ()),
    ((51,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 23, 26, 30, 33, 38, 39, 41, 43, 46, 47, 50, 54, 58, 59, 60, 62, 63, 64, 71, 72, 77, 79), 773,   ()),
    ((53, 57), (1, 3, 5, 7, 10, 14, 16, 18, 20, 23, 26, 30, 35, 37, 39, 41, 44, 48, 49, 51, 54, 58, 60, 64, 68, 70, 75, 77, 78),       773,    (40, 61)),
    ((54,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 23, 26, 30, 33, 38, 39, 41, 43, 46, 50, 54, 59, 60, 61, 62, 63, 64, 70, 74, 77, 79),    767,    ()),
    ((55,),    (1, 3, 5, 7, 10, 12, 14, 17, 18, 20, 24, 27, 30, 33, 36, 38, 40, 41, 44, 53, 56, 59, 61, 66, 68, 72, 75, 76, 78),       771,    ()),
    ((56,),    (1, 3, 5, 7, 9, 12, 14, 16, 19, 21, 23, 25, 27, 30, 35, 37, 40, 51, 56, 62, 63, 64, 67, 69, 71, 74, 75, 76, 79),        769,    ()),
    ((57,),    (1, 3, 5, 7, 10, 12, 14, 17, 20, 24, 30, 32, 34, 37, 38, 40, 48, 50, 52, 54, 56, 57, 58, 59, 63, 66, 68, 70, 78),       774,    ()),
    ((58,),    (0, 2, 4, 6, 8, 10, 14, 17, 19, 21, 23, 26, 30, 33, 36, 43, 45, 48, 49, 54, 57, 59, 62, 64, 67, 72, 74, 75, 79),        767,    ()),
    ((59, 65), (1, 3, 5, 7, 10, 12, 14, 17, 20, 22, 24, 26, 28, 30, 35, 40, 41, 42, 44, 52, 54, 60, 65, 67, 68, 73, 74, 75, 78),       773,    ()),
    ((60,),    (2, 4, 10, 13, 15, 19, 23, 25, 27, 31, 33, 34, 37, 40, 41, 45, 48, 50, 51, 54, 56, 60, 61, 62, 67, 69, 71, 73, 76),     770,    ()),
    ((60, 66), (1, 3, 4, 5, 7, 9, 12, 16, 19, 21, 25, 27, 30, 32, 33, 35, 38, 40, 43, 45, 47, 51, 55, 57, 59, 60, 62, 75, 79),         774,    ()),
    ((61,),    (3, 5, 11, 14, 16, 20, 24, 26, 28, 32, 34, 35, 38, 41, 42, 46, 49, 51, 52, 55, 57, 61, 62, 63, 68, 70, 72, 74, 77),     769,    ()),
    ((62,),    (1, 3, 5, 7, 10, 12, 14, 17, 20, 22, 24, 26, 28, 30, 35, 40, 41, 42, 44, 47, 52, 54, 65, 66, 67, 68, 73, 75, 78),       772,    ()),
    ((62, 68), (1, 3, 5, 7, 10, 12, 14, 17, 20, 22, 24, 26, 28, 30, 35, 40, 41, 42, 44, 47, 52, 59, 60, 67, 68, 73, 75, 77, 78),       773,    ()),
    ((63,),    (2, 4, 8, 10, 13, 15, 19, 23, 27, 31, 33, 37, 40, 41, 45, 48, 50, 54, 56, 60, 61, 62, 67, 69, 71, 73, 76, 78),          770,    ()),
    ((64,),    (3, 5, 9, 11, 14, 16, 20, 24, 28, 32, 34, 38, 41, 42, 46, 49, 51, 55, 57, 61, 62, 63, 68, 70, 72, 74, 77, 79),          769,    ()),
    ((65,),    (0, 2, 4, 6, 7, 8, 10, 14, 17, 19, 21, 23, 26, 30, 32, 34, 36, 37, 39, 41, 43, 45, 55, 56, 61, 66, 74, 76, 79),         767,    ()),
    ((67,),    (2, 4, 6, 8, 11, 13, 15, 17, 19, 21, 23, 24, 27, 31, 34, 40, 42, 43, 44, 48, 51, 56, 59, 61, 65, 70, 72, 78, 79),       768,    ())
)


one_fivium_table = (
    ((0,),      (3, 6, 11, 14, 1, 55),      596),
    ((1, 64),   (3, 6, 11, 14, 7, 32),      579),
    ((2, 65),   (3, 6, 11, 14, 13, 31),     579),
    ((3,),      (3, 6, 11, 14, 5, 46),      578),
    ((4,),      (6, 11, 14, 0, 78),         576),
    ((5,),      (3, 6, 11, 14, 40, 50),     610),
    ((7,),      (3, 6, 11, 14, 22, 53),     588),
    ((8,),      (3, 6, 11, 14, 35, 62),     588),
    ((10,),     (3, 6, 11, 14, 23, 40),     594),
    ((13,),     (3, 6, 11, 14, 20, 31),     603),
    ((15,),     (3, 6, 11, 14, 76, 78),     577),
    ((16,),     (3, 6, 11, 14, 19, 78),     587),
    ((18,),     (3, 6, 11, 14, 22, 39),     586),
    ((24,),     (3, 11, 14, 22, 48),        579),
    ((25,),     (3, 11, 14, 21, 48),        579),
    ((26,),     (3, 6, 11, 22, 47),         578),
    ((35,),     (3, 6, 11, 33, 43),         582),
    ((37,),     (6, 11, 14, 48, 54),        579),
    ((38,),     (6, 11, 14, 51, 78),        577),
    ((54,),     (3, 6, 11, 14, 50, 57),     597),
    ((55,),     (3, 6, 11, 14, 25, 49),     577),
    ((56, 62),  (3, 6, 11, 13, 23),         587),
    ((58, 64),  (3, 6, 11, 14, 9, 40),      611),
    ((59, 65),  (3, 11, 14, 37, 47),        588),
    ((60,),     (3, 6, 11, 14, 39, 73),     586),
    ((61,),     (3, 6, 11, 14, 22, 74),     603),
    ((62,),     (3, 6, 11, 14, 22, 73),     603),
    ((63,),     (3, 6, 11, 14, 2, 29),      596),
    ((64,),     (3, 6, 11, 14, 1, 32),      579),
    ((65,),     (3, 6, 11, 14, 15, 33),     579),
    ((66,),     (3, 6, 11, 14, 39, 64),     595),
    ((67,),     (3, 6, 11, 14, 39, 63),     595),
    ((14,),     (3, 27, 30, 78, 2, 46),     580),
    ((17,),     (3, 27, 30, 78, 0, 68),     599),
    ((19,),     (3, 27, 30, 78, 2, 49),     597),
    ((22,),     (3, 27, 30, 78, 7, 11),     624),
    ((29,),     (3, 27, 30, 78, 11, 45),    605),
    ((31,),     (3, 27, 30, 78, 0, 16),     605),
    ((32,),     (27, 30, 78, 1, 36),        590),
    ((34,),     (3, 27, 30, 78, 13, 50),    588),
    ((57,),     (3, 27, 30, 78, 34, 37),    587),
    ((20,),     (1, 6, 7, 11, 18, 44),      582),
    ((21,),     (1, 6, 7, 11, 19, 55),      582),
    ((9,),      (1, 7, 79, 18, 42),         582),
    ((11,),     (1, 7, 11, 79, 18, 43),     581),
    ((57,),     (1, 7, 11, 79, 18, 70),     606),
    ((68,),     (1, 7, 11, 79, 13, 48),     578),
)

quad_table1 = (
    ((14,), (6, 8, 9, 13, 22, 24, 28, 30, 32, 36, 39, 40, 43, 45, 47, 48, 60, 63, 67, 68, 73, 76, 79,), 709),
    ((15,), (2, 9, 15, 17, 27, 28, 32, 40, 44, 46, 52, 54, 59, 64, 68, 70, 71, 72, 73, 74, 76, 78, 79), 709),
    ((16,), (1, 3, 9, 10, 13, 14, 16, 28, 34, 37, 42, 51, 52, 56, 59, 60, 62, 68, 69, 72, 74, 79), 709),
    ((17,), (4, 5, 6, 10, 11, 12, 17, 19, 21, 26, 32, 40, 44, 49, 54, 58, 60, 61, 67, 72, 74, 77, 78), 709),
    ((18,), (5, 9, 15, 16, 20, 21, 32, 33, 35, 38, 41, 43, 46, 52, 56, 58, 60, 61, 62, 69, 77, 78, 79), 709),
    ((19,), (6, 8, 13, 17, 23, 27, 28, 33, 44, 45, 46, 53, 54, 56, 60, 61, 67, 68, 72, 74, 75, 77, 79), 709),
    ((20,), (1, 2, 7, 13, 15, 18, 19, 23, 29, 34, 35, 36, 38, 47, 49, 54, 57, 62, 64, 65, 66, 68, 74), 709),
    ((21,), (4, 7, 10, 11, 19, 20, 22, 23, 24, 30, 32, 33, 38, 41, 49, 52, 54, 59, 66, 67, 69, 74, 77), 709),
    ((22,), (8, 16, 18, 22, 24, 26, 29, 31, 34, 36, 40, 41, 45, 46, 47, 48, 50, 59, 63, 69, 72, 76, 78), 709),
    ((23,), (6, 10, 13, 16, 19, 25, 28, 35, 39, 42, 44, 48, 57, 61, 62, 63, 64, 65, 67, 68, 73, 77, 78), 709),
    ((24,), (2, 4, 7, 15, 17, 18, 20, 23, 24, 27, 29, 35, 45, 47, 48, 51, 57, 59, 63, 65, 67, 74, 77), 709),
    ((25,), (3, 5, 8, 16, 18, 19, 21, 24, 25, 28, 30, 36, 46, 48, 49, 52, 58, 60, 64, 66, 68, 75, 78), 710),
    ((33,), (5, 10, 13, 14, 15, 22, 26, 27, 32, 35, 36, 45, 46, 50, 51, 56, 59, 60, 63, 64, 77, 78, 79), 709),
    ((35,), (2, 6, 8, 9, 19, 23, 24, 29, 32, 33, 34, 42, 47, 49, 51, 52, 53, 57, 61, 64, 73, 77), 710),
    ((39,), (0, 3, 6, 8, 11, 17, 28, 34, 38, 39, 41, 43, 46, 51, 52, 53, 54, 56, 64, 65, 70, 72, 78), 709),
    ((40,), (5, 6, 11, 19, 27, 31, 32, 39, 40, 44, 47, 49, 51, 52, 56, 58, 59, 63, 65, 66, 69, 71, 79), 709),
    ((41,), (7, 9, 10, 15, 17, 24, 25, 26, 33, 36, 43, 45, 52, 56, 59, 60, 61, 63, 68, 71, 74, 77), 709),
    ((42,), (8, 10, 11, 16, 18, 25, 26, 27, 34, 37, 44, 46, 53, 57, 60, 61, 62, 64, 69, 72, 75, 78), 710),
    ((43,), (9, 11, 12, 17, 19, 26, 27, 28, 35, 38, 45, 47, 54, 58, 61, 62, 63, 65, 70, 73, 76, 79), 711),
    ((47,), (4, 5, 7, 13, 15, 18, 27, 30, 33, 34, 36, 39, 42, 44, 45, 46, 51, 53, 57, 63, 75, 77, 78), 709),
    ((48,), (6, 7, 15, 19, 27, 30, 35, 37, 44, 45, 46, 47, 49, 50, 56, 59, 60, 67, 70, 71, 72, 75, 79), 709),
    ((49,), (0, 8, 14, 18, 25, 28, 31, 35, 38, 42, 44, 45, 51, 52, 58, 60, 66, 67, 70, 73, 76, 77), 709),
    ((50,), (0, 2, 8, 11, 14, 15, 17, 21, 22, 28, 31, 32, 39, 41, 52, 53, 59, 60, 65, 67, 74, 77, 78), 709),
    ((51,), (1, 8, 10, 15, 18, 26, 28, 29, 33, 35, 37, 38, 42, 51, 53, 55, 57, 60, 61, 65, 66, 67, 75), 709),
    ((21, 52,), (7, 10, 11, 12, 15, 21, 29, 32, 37, 39, 41, 44, 47, 53, 56, 57, 59, 62, 63, 66, 70, 76), 710),
    ((53,), (1, 4, 8, 10, 11, 12, 14, 15, 19, 22, 24, 29, 31, 33, 39, 42, 50, 52, 55, 58, 60, 61, 65), 710),
    ((23, 54,), (9, 12, 13, 14, 17, 23, 31, 34, 39, 41, 43, 46, 49, 55, 58, 59, 61, 64, 65, 68, 72, 78), 712),
    ((24, 55,), (10, 13, 14, 15, 18, 24, 32, 35, 40, 42, 44, 47, 50, 56, 59, 60, 62, 65, 66, 69, 73, 79), 713),
    ((57,), (1, 3, 6, 10, 11, 14, 15, 16, 23, 25, 28, 35, 40, 41, 42, 44, 46, 52, 58, 66, 68, 69, 75), 709),
    ((21, 49, 58,), (8, 12, 14, 19, 26, 28, 30, 40, 41, 42, 43, 48, 50, 53, 59, 62, 63, 67, 71, 72, 74, 79), 709),
    ((59,), (6, 14, 16, 31, 37, 40, 43, 48, 50, 53, 54, 55, 57, 58, 60, 61, 62, 68, 72, 73, 74, 76), 709),
    ((60,), (3, 4, 14, 16, 26, 29, 30, 38, 40, 43, 47, 54, 56, 58, 60, 64, 65, 67, 69, 70, 75, 76, 77), 709),
    ((61,), (3, 8, 11, 14, 16, 17, 18, 20, 22, 24, 27, 33, 35, 38, 44, 48, 52, 53, 59, 66, 73, 77), 711),
    ((62,), (4, 9, 12, 15, 17, 18, 19, 21, 23, 25, 28, 34, 36, 39, 45, 49, 53, 54, 60, 67, 74, 78), 712),
    ((19, 63,), (2, 5, 9, 17, 21, 27, 28, 30, 35, 37, 46, 48, 50, 53, 54, 60, 61, 63, 65, 69, 71, 73, 79), 709),
    ((67,), (1, 7, 12, 15, 18, 27, 30, 41, 44, 46, 47, 48, 49, 52, 53, 54, 56, 59, 62, 63, 66, 69, 79), 709),
    ((72,), (6, 11, 16, 19, 26, 34, 36, 39, 41, 42, 47, 49, 52, 54, 57, 59, 66, 67, 71, 72, 76, 79), 709),
    ((73,), (1, 3, 4, 6, 12, 14, 15, 19, 25, 26, 28, 29, 35, 40, 49, 52, 57, 64, 66, 67, 68, 72, 75), 709),
    ((74,), (2, 4, 5, 7, 13, 15, 16, 20, 26, 27, 29, 30, 36, 41, 50, 53, 58, 65, 67, 68, 69, 73, 76), 710),
    ((75,), (3, 5, 6, 8, 14, 16, 17, 21, 27, 28, 30, 31, 37, 42, 51, 54, 59, 66, 68, 69, 70, 74, 77), 711),
    ((76,), (4, 6, 7, 9, 15, 17, 18, 22, 28, 29, 31, 32, 38, 43, 52, 55, 60, 67, 69, 70, 71, 75, 78), 712), 
)

#Bedi_Pillai_table3 = (
#    ((68,), (3, 20, 28, 36, 42, 55, 77, 78), 579),
#    ((-77, -64, 67,), (18, 26, 36, 45, 61, 73, 78, 79), 579),
#    ((-78, 66,), (11, 18, 34, 37, 45, 51, 70, 79), 588),
#    ((65,), (1, 3, 28, 34, 51, 61, 67), 581),
#    ((64,), (3, 12, 19, 29, 37, 62, 77), 578),
#    ((63,), (8, 13, 21, 39, 53, 73, 74), 577),
#    ((62,), (6, 7, 12, 13, 15, 16, 36, 73), 576),
#    ((61,), (0, 10, 35, 45, 55, 58, 72, 77), 584),
##    ((-72, -9, -8, 60,), (6, 7, 10, 27, 35, 36, 67), 581),
#    ((59,), (1, 20, 29, 36, 48, 55, 73), 587),
#    ((58,), (8, 16, 19, 28, 52, 62, 69, 72), 586),
#    ((57,), (0, 10, 11, 23, 25, 26, 29, 57, 68, 71), 593),
#    ((56,), (5, 6, 11, 27, 44, 55, 60, 67), 578),
#    ((55,), (0, 3, 7, 20, 21, 31, 66), 578),
#    ((54,), (5, 6, 11, 44, 60, 65, 67), 577),
##    ((-65, -64, -50, 53,), (17, 25, 27, 35, 54, 62, 63, 79), 581),
##    ((-64, -63, -49, -7, 52,), (1, 2, 8, 39, 61, 62, 69, 70), 579),
#    ((51,), (15, 23, 32, 47, 49, 58, 76), 584),
#    ((50,), (0, 5, 14, 23, 38, 48, 67), 584),
#    ((49,), (14, 22, 30, 45, 48, 50, 59, 75), 585),
#    ((48,), (4, 29, 38, 43, 46, 47, 57, 66, 73), 586),
#    ((47,), (18, 28, 38, 39, 42, 45, 46, 65, 79), 587),
##    ((-25, 46,), (1, 17, 19, 21, 24, 27, 59, 60, 71), 614),
#    ((45,), (9, 18, 25, 28, 43, 45, 55, 69), 590),
##    ((-20, 44,), (2, 21, 29, 40, 57, 66, 73), 577),
##    ((-40, 43,), (1, 7, 8, 32, 39, 42, 67, 74), 591),
##    ((-39, 42,), (7, 15, 29, 38, 41, 42, 50, 75), 592),
##    ((-51, -38, 41,), (3, 9, 12, 22, 30, 49, 52, 53), 589),
#    ((40,), (19, 30, 36, 38, 43, 46, 58, 63, 79), 595),
##    ((-36, 39,), (4, 5, 21, 22, 37, 38, 39, 72), 595),
##    ((-48, -35, 38,), (3, 7, 11, 23, 44, 49, 50), 580),
##    ((-49, -48, -34, 37,), (1, 7, 9, 15, 46, 47, 59, 68), 582),
##    ((-48, -47, -33, 36,), (7, 21, 23, 45, 46, 58, 74, 76), 584),
##    ((-47, -46, -32, 35,), (22, 25, 41, 44, 45, 51, 55, 58, 67), 581),
##    ((-44, -31, 34,), (1, 15, 45, 46, 50, 57, 68, 69), 583),
##    ((-45, -44, -30, -27, 33,), (5, 22, 28, 31, 42, 43, 51, 75), 582),
##    ((-44, -43, -29, 32,), (0, 3, 32, 39, 41, 42, 47, 48, 61), 585),
##    ((-41, -28, 31,), (4, 20, 37, 42, 43, 54, 64), 587),
##    ((-42, -41, -27, 30,), (10, 11, 25, 26, 39, 40, 47, 56, 70), 588),
##    ((-39, -26, 29,), (0, 2, 11, 30, 40, 41, 53, 54), 589),
##    ((-40, -39, -25, 28,), (18, 28, 37, 38, 42, 45, 46, 65, 79), 588),
#    ((3,), (5, 9, 10, 11, 12, 42, 68, 77), 579),
##    ((-68, -29, 2,), (5, 8, 12, 28, 31, 67, 74), 576),
##    ((-67, 1,), (9, 10, 19, 33, 41, 68, 77), 590),
##    ((-66, 0,), (3, 12, 37, 63, 65, 71, 74), 578), 
#)

if __name__ == '__main__':
       pass