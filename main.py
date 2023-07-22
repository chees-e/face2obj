import mediapipe as mp

def generate_output(file_name, detection_result):
    faces = [(0, 11, 37), (0, 11, 267), (0, 37, 164), (0, 164, 267), (1, 4, 44), (1, 4, 274), (1, 19, 44), (1, 19, 274),
     (2, 94, 141), (2, 94, 370), (2, 97, 141), (2, 97, 167), (2, 164, 167), (2, 164, 393), (2, 326, 370), (2, 326, 393),
     (3, 51, 195), (3, 51, 236), (3, 195, 197), (3, 196, 197), (3, 196, 236), (4, 5, 51), (4, 5, 281), (4, 44, 45),
     (4, 45, 51), (4, 274, 275), (4, 275, 281), (5, 51, 195), (5, 195, 281), (6, 122, 168), (6, 122, 196),
     (6, 168, 351), (6, 196, 197), (6, 197, 419), (6, 351, 419), (7, 25, 33), (7, 25, 110), (7, 110, 163), (8, 9, 55),
     (8, 9, 285), (8, 55, 193), (8, 168, 193), (8, 168, 417), (8, 285, 417), (9, 55, 107), (9, 107, 108), (9, 108, 151),
     (9, 151, 337), (9, 285, 336), (9, 336, 337), (10, 109, 151), (10, 151, 338), (11, 12, 72), (11, 12, 302),
     (11, 37, 72), (11, 267, 302), (12, 13, 38), (12, 13, 268), (12, 38, 72), (12, 268, 302), (13, 38, 82),
     (13, 268, 312), (14, 15, 86), (14, 15, 316), (14, 86, 87), (14, 316, 317), (15, 16, 85), (15, 16, 315),
     (15, 85, 86), (15, 315, 316), (16, 17, 85), (16, 17, 315), (17, 18, 83), (17, 18, 313), (17, 83, 84), (17, 84, 85),
     (17, 313, 314), (17, 314, 315), (18, 83, 201), (18, 200, 201), (18, 200, 421), (18, 313, 421), (19, 44, 125),
     (19, 94, 141), (19, 94, 370), (19, 125, 141), (19, 274, 354), (19, 354, 370), (20, 60, 99), (20, 60, 166),
     (20, 79, 166), (20, 79, 238), (20, 99, 242), (20, 238, 242), (21, 54, 68), (21, 68, 71), (21, 71, 162),
     (22, 23, 145), (22, 23, 230), (22, 26, 154), (22, 26, 231), (22, 145, 153), (22, 153, 154), (22, 230, 231),
     (23, 24, 144), (23, 24, 229), (23, 144, 145), (23, 229, 230), (24, 110, 144), (24, 110, 228), (24, 228, 229),
     (25, 31, 226), (25, 31, 228), (25, 33, 130), (25, 110, 228), (25, 130, 226), (26, 112, 155), (26, 112, 232),
     (26, 154, 155), (26, 231, 232), (27, 28, 159), (27, 28, 222), (27, 29, 160), (27, 29, 223), (27, 159, 160),
     (27, 222, 223), (28, 56, 157), (28, 56, 221), (28, 157, 158), (28, 158, 159), (28, 221, 222), (29, 30, 160),
     (29, 30, 224), (29, 223, 224), (30, 160, 161), (30, 161, 247), (30, 224, 225), (30, 225, 247), (31, 111, 117),
     (31, 111, 226), (31, 117, 228), (32, 140, 171), (32, 140, 211), (32, 171, 208), (32, 194, 201), (32, 194, 211),
     (32, 201, 208), (33, 130, 247), (33, 246, 247), (34, 127, 139), (34, 127, 234), (34, 139, 156), (34, 143, 156),
     (34, 143, 227), (34, 227, 234), (35, 111, 143), (35, 111, 226), (35, 113, 124), (35, 113, 226), (35, 124, 143),
     (36, 100, 101), (36, 100, 142), (36, 101, 205), (36, 142, 203), (36, 203, 206), (36, 205, 206), (37, 39, 72),
     (37, 39, 167), (37, 164, 167), (38, 41, 72), (38, 41, 81), (38, 81, 82), (39, 40, 73), (39, 40, 92), (39, 72, 73),
     (39, 92, 165), (39, 165, 167), (40, 73, 74), (40, 74, 185), (40, 92, 186), (40, 185, 186), (41, 42, 74),
     (41, 42, 81), (41, 72, 73), (41, 73, 74), (42, 74, 184), (42, 80, 81), (42, 80, 183), (42, 183, 184), (43, 57, 61),
     (43, 57, 202), (43, 61, 146), (43, 91, 106), (43, 91, 146), (43, 106, 204), (43, 202, 204), (44, 45, 220),
     (44, 125, 237), (44, 220, 237), (45, 51, 134), (45, 134, 220), (46, 53, 63), (46, 53, 225), (46, 63, 70),
     (46, 70, 156), (46, 113, 124), (46, 113, 225), (46, 124, 156), (47, 100, 121), (47, 100, 126), (47, 114, 128),
     (47, 114, 217), (47, 121, 128), (47, 126, 217), (48, 49, 64), (48, 49, 131), (48, 64, 235), (48, 115, 131),
     (48, 115, 219), (48, 219, 235), (49, 64, 102), (49, 64, 129), (49, 102, 129), (49, 129, 209), (49, 131, 209),
     (50, 101, 118), (50, 101, 205), (50, 117, 118), (50, 117, 123), (50, 123, 187), (50, 187, 205), (51, 134, 236),
     (52, 53, 63), (52, 53, 223), (52, 63, 105), (52, 65, 66), (52, 65, 222), (52, 66, 105), (52, 222, 223),
     (53, 223, 224), (53, 224, 225), (54, 68, 104), (54, 103, 104), (55, 65, 107), (55, 65, 221), (55, 189, 193),
     (55, 189, 221), (56, 157, 173), (56, 173, 190), (56, 190, 221), (57, 61, 185), (57, 185, 186), (57, 186, 212),
     (57, 202, 212), (58, 132, 177), (58, 172, 215), (58, 177, 215), (59, 75, 166), (59, 75, 235), (59, 166, 219),
     (59, 219, 235), (60, 75, 166), (60, 75, 240), (60, 99, 240), (61, 76, 146), (61, 76, 184), (61, 184, 185),
     (62, 76, 77), (62, 76, 183), (62, 77, 96), (62, 78, 96), (62, 78, 191), (62, 183, 191), (63, 68, 71),
     (63, 68, 104), (63, 70, 71), (63, 104, 105), (64, 98, 129), (64, 98, 240), (64, 102, 129), (64, 235, 240),
     (65, 66, 107), (65, 221, 222), (66, 69, 105), (66, 69, 107), (67, 69, 104), (67, 69, 108), (67, 103, 104),
     (67, 108, 109), (69, 104, 105), (69, 107, 108), (70, 71, 139), (70, 139, 156), (71, 139, 162), (74, 184, 185),
     (75, 235, 240), (76, 77, 146), (76, 183, 184), (77, 90, 91), (77, 90, 96), (77, 91, 146), (78, 95, 96),
     (79, 166, 218), (79, 218, 237), (79, 237, 239), (79, 238, 239), (80, 183, 191), (83, 84, 181), (83, 181, 182),
     (83, 182, 201), (84, 85, 180), (84, 180, 181), (85, 86, 179), (85, 179, 180), (86, 87, 178), (86, 178, 179),
     (88, 89, 96), (88, 89, 179), (88, 95, 96), (88, 178, 179), (89, 90, 96), (89, 90, 180), (89, 179, 180),
     (90, 91, 181), (90, 180, 181), (91, 106, 182), (91, 181, 182), (92, 165, 206), (92, 186, 216), (92, 206, 216),
     (93, 132, 137), (93, 137, 227), (93, 227, 234), (97, 98, 99), (97, 98, 165), (97, 99, 242), (97, 141, 242),
     (97, 165, 167), (98, 99, 240), (98, 129, 203), (98, 165, 203), (100, 101, 120), (100, 120, 121), (100, 126, 142),
     (101, 118, 119), (101, 119, 120), (106, 182, 194), (106, 194, 204), (108, 109, 151), (110, 144, 163),
     (111, 116, 123), (111, 116, 143), (111, 117, 123), (112, 133, 155), (112, 133, 243), (112, 232, 233),
     (112, 233, 244), (112, 243, 244), (113, 225, 247), (113, 226, 247), (114, 128, 188), (114, 174, 188),
     (114, 174, 217), (115, 131, 220), (115, 218, 219), (115, 218, 220), (116, 123, 137), (116, 137, 227),
     (116, 143, 227), (117, 118, 229), (117, 228, 229), (118, 119, 230), (118, 229, 230), (119, 120, 230),
     (120, 121, 232), (120, 230, 231), (120, 231, 232), (121, 128, 232), (122, 168, 193), (122, 188, 196),
     (122, 188, 245), (122, 193, 245), (123, 137, 177), (123, 147, 177), (123, 147, 187), (124, 143, 156),
     (125, 141, 241), (125, 237, 241), (126, 129, 142), (126, 129, 209), (126, 209, 217), (127, 139, 162),
     (128, 188, 245), (128, 232, 233), (128, 233, 245), (129, 142, 203), (130, 226, 247), (131, 134, 198),
     (131, 134, 220), (131, 198, 209), (132, 137, 177), (133, 173, 190), (133, 190, 243), (134, 198, 236),
     (135, 136, 138), (135, 136, 150), (135, 138, 192), (135, 150, 169), (135, 169, 214), (135, 192, 214),
     (136, 138, 172), (138, 172, 215), (138, 192, 213), (138, 213, 215), (140, 148, 171), (140, 148, 176),
     (140, 170, 176), (140, 170, 211), (141, 241, 242), (147, 177, 215), (147, 187, 213), (147, 213, 215),
     (148, 152, 175), (148, 171, 175), (149, 150, 170), (149, 170, 176), (150, 169, 170), (151, 337, 338),
     (152, 175, 377), (161, 246, 247), (164, 267, 393), (165, 203, 206), (166, 218, 219), (168, 351, 417),
     (169, 170, 211), (169, 210, 211), (169, 210, 214), (171, 175, 199), (171, 199, 208), (174, 188, 196),
     (174, 196, 236), (174, 217, 236), (175, 199, 396), (175, 377, 396), (182, 194, 201), (186, 212, 216),
     (187, 192, 213), (187, 192, 214), (187, 205, 207), (187, 207, 214), (189, 190, 221), (189, 190, 243),
     (189, 193, 244), (189, 243, 244), (193, 244, 245), (194, 204, 211), (195, 197, 248), (195, 248, 281),
     (197, 248, 419), (198, 209, 217), (198, 217, 236), (199, 200, 208), (199, 200, 428), (199, 396, 428),
     (200, 201, 208), (200, 421, 428), (202, 204, 210), (202, 210, 214), (202, 212, 214), (204, 210, 211),
     (205, 206, 216), (205, 207, 216), (207, 212, 214), (207, 212, 216), (218, 220, 237), (233, 244, 245),
     (237, 239, 241), (238, 239, 241), (238, 241, 242), (248, 281, 456), (248, 419, 456), (249, 255, 263),
     (249, 255, 339), (249, 339, 390), (250, 290, 328), (250, 290, 392), (250, 309, 392), (250, 309, 459),
     (250, 328, 462), (250, 458, 459), (250, 458, 462), (251, 284, 298), (251, 298, 301), (251, 301, 389),
     (252, 253, 374), (252, 253, 450), (252, 256, 381), (252, 256, 451), (252, 374, 380), (252, 380, 381),
     (252, 450, 451), (253, 254, 373), (253, 254, 449), (253, 373, 374), (253, 449, 450), (254, 339, 373),
     (254, 339, 448), (254, 448, 449), (255, 261, 446), (255, 261, 448), (255, 263, 359), (255, 339, 448),
     (255, 359, 446), (256, 341, 382), (256, 341, 452), (256, 381, 382), (256, 451, 452), (257, 258, 386),
     (257, 258, 442), (257, 259, 387), (257, 259, 443), (257, 386, 387), (257, 442, 443), (258, 286, 384),
     (258, 286, 441), (258, 384, 385), (258, 385, 386), (258, 441, 442), (259, 260, 387), (259, 260, 444),
     (259, 443, 444), (260, 387, 388), (260, 388, 466), (260, 444, 445), (260, 445, 467), (260, 466, 467),
     (261, 340, 346), (261, 340, 446), (261, 346, 448), (262, 369, 396), (262, 369, 431), (262, 396, 428),
     (262, 418, 421), (262, 418, 431), (262, 421, 428), (263, 359, 467), (263, 466, 467), (264, 356, 368),
     (264, 356, 454), (264, 368, 383), (264, 372, 383), (264, 372, 447), (264, 447, 454), (265, 340, 372),
     (265, 340, 446), (265, 342, 353), (265, 342, 446), (265, 353, 372), (266, 329, 330), (266, 329, 371),
     (266, 330, 425), (266, 371, 423), (266, 423, 426), (266, 425, 426), (267, 269, 302), (267, 269, 393),
     (268, 271, 302), (268, 271, 311), (268, 311, 312), (269, 270, 303), (269, 270, 322), (269, 302, 303),
     (269, 322, 391), (269, 391, 393), (270, 303, 304), (270, 304, 409), (270, 322, 410), (270, 409, 410),
     (271, 272, 304), (271, 272, 311), (271, 302, 303), (271, 303, 304), (272, 304, 408), (272, 310, 311),
     (272, 310, 407), (272, 407, 408), (273, 287, 291), (273, 287, 422), (273, 291, 375), (273, 321, 335),
     (273, 321, 375), (273, 335, 424), (273, 422, 424), (274, 275, 440), (274, 354, 457), (274, 440, 457),
     (275, 281, 363), (275, 363, 440), (276, 283, 293), (276, 283, 445), (276, 293, 300), (276, 300, 383),
     (276, 342, 353), (276, 342, 445), (276, 353, 383), (277, 329, 350), (277, 329, 355), (277, 343, 357),
     (277, 343, 437), (277, 350, 357), (277, 355, 437), (278, 279, 294), (278, 279, 360), (278, 294, 455),
     (278, 344, 360), (278, 344, 439), (278, 439, 455), (279, 294, 331), (279, 294, 358), (279, 331, 358),
     (279, 358, 429), (279, 360, 429), (280, 330, 347), (280, 330, 425), (280, 346, 347), (280, 346, 352),
     (280, 352, 411), (280, 411, 425), (281, 363, 456), (282, 283, 293), (282, 283, 443), (282, 293, 334),
     (282, 295, 296), (282, 295, 442), (282, 296, 334), (282, 442, 443), (283, 443, 444), (283, 444, 445),
     (284, 298, 333), (284, 332, 333), (285, 295, 336), (285, 295, 441), (285, 413, 417), (285, 413, 441),
     (286, 384, 398), (286, 398, 414), (286, 414, 441), (287, 291, 409), (287, 409, 410), (287, 410, 432),
     (287, 422, 432), (288, 361, 401), (288, 397, 435), (288, 401, 435), (289, 290, 305), (289, 290, 392),
     (289, 305, 455), (289, 392, 439), (289, 439, 455), (290, 305, 460), (290, 328, 460), (291, 306, 375),
     (291, 306, 408), (291, 408, 409), (292, 306, 307), (292, 306, 407), (292, 307, 325), (292, 308, 325),
     (292, 308, 415), (292, 407, 415), (293, 298, 301), (293, 298, 333), (293, 300, 301), (293, 333, 334),
     (294, 327, 358), (294, 327, 460), (294, 331, 358), (294, 455, 460), (295, 296, 336), (295, 441, 442),
     (296, 299, 334), (296, 299, 336), (297, 299, 333), (297, 299, 337), (297, 332, 333), (297, 337, 338),
     (299, 333, 334), (299, 336, 337), (300, 301, 368), (300, 368, 383), (301, 368, 389), (304, 408, 409),
     (305, 455, 460), (306, 307, 375), (306, 407, 408), (307, 320, 321), (307, 320, 325), (307, 321, 375),
     (308, 324, 325), (309, 392, 438), (309, 438, 457), (309, 457, 459), (310, 407, 415), (313, 314, 405),
     (313, 405, 406), (313, 406, 421), (314, 315, 404), (314, 404, 405), (315, 316, 403), (315, 403, 404),
     (316, 317, 402), (316, 402, 403), (318, 319, 325), (318, 319, 403), (318, 324, 325), (318, 402, 403),
     (319, 320, 325), (319, 320, 404), (319, 403, 404), (320, 321, 405), (320, 404, 405), (321, 335, 406),
     (321, 405, 406), (322, 391, 426), (322, 410, 436), (322, 426, 436), (323, 361, 366), (323, 366, 447),
     (323, 447, 454), (326, 327, 328), (326, 327, 391), (326, 328, 462), (326, 370, 462), (326, 391, 393),
     (327, 328, 460), (327, 358, 423), (327, 391, 423), (329, 330, 349), (329, 349, 350), (329, 355, 371),
     (330, 347, 348), (330, 348, 349), (335, 406, 418), (335, 418, 424), (339, 373, 390), (340, 345, 352),
     (340, 345, 372), (340, 346, 352), (341, 362, 382), (341, 362, 463), (341, 452, 453), (341, 453, 464),
     (341, 463, 464), (342, 445, 467), (342, 446, 467), (343, 357, 412), (343, 399, 412), (343, 399, 437),
     (344, 360, 440), (344, 438, 439), (344, 438, 440), (345, 352, 366), (345, 366, 447), (345, 372, 447),
     (346, 347, 449), (346, 448, 449), (347, 348, 450), (347, 449, 450), (348, 349, 450), (349, 350, 452),
     (349, 450, 451), (349, 451, 452), (350, 357, 452), (351, 412, 419), (351, 412, 465), (351, 417, 465),
     (352, 366, 401), (352, 376, 401), (352, 376, 411), (353, 372, 383), (354, 370, 461), (354, 457, 461),
     (355, 358, 371), (355, 358, 429), (355, 429, 437), (356, 368, 389), (357, 412, 465), (357, 452, 453),
     (357, 453, 465), (358, 371, 423), (359, 446, 467), (360, 363, 420), (360, 363, 440), (360, 420, 429),
     (361, 366, 401), (362, 398, 414), (362, 414, 463), (363, 420, 456), (364, 365, 367), (364, 365, 379),
     (364, 367, 416), (364, 379, 394), (364, 394, 434), (364, 416, 434), (365, 367, 397), (367, 397, 435),
     (367, 416, 433), (367, 433, 435), (369, 377, 396), (369, 377, 400), (369, 395, 400), (369, 395, 431),
     (370, 461, 462), (376, 401, 435), (376, 411, 433), (376, 433, 435), (378, 379, 395), (378, 395, 400),
     (379, 394, 395), (391, 423, 426), (392, 438, 439), (394, 395, 431), (394, 430, 431), (394, 430, 434),
     (399, 412, 419), (399, 419, 456), (399, 437, 456), (406, 418, 421), (410, 432, 436), (411, 416, 433),
     (411, 416, 434), (411, 425, 427), (411, 427, 434), (413, 414, 441), (413, 414, 463), (413, 417, 464),
     (413, 463, 464), (417, 464, 465), (418, 424, 431), (420, 429, 437), (420, 437, 456), (422, 424, 430),
     (422, 430, 434), (422, 432, 434), (424, 430, 431), (425, 426, 436), (425, 427, 436), (427, 432, 434),
     (427, 432, 436), (438, 440, 457), (453, 464, 465), (457, 459, 461), (458, 459, 461), (458, 461, 462)]
    scale = 1
    with open(file_name, 'w') as f:
        f.write(f"o Face\n")
        for point in detection_result.face_landmarks[0]:
            f.write(f"v {point.x * scale} {-point.y * scale} {point.z * scale}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

model_path = "./model/face_landmarker.task"

print(f"Model Path: {model_path}")

infile_path = "./in/" + input("Please input image name (should be inside ./in/ directory) => ")
outfile_path = "./out/output.obj"
try:
    mp_image = mp.Image.create_from_file(infile_path)
except:
    print("ERR: Image not found!")
    quit()

# Initializing landmarker
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True,
    running_mode=VisionRunningMode.IMAGE,
    num_faces=1
)

with FaceLandmarker.create_from_options(options) as landmarker:
    face_landmarker_result = landmarker.detect(mp_image)

generate_output(outfile_path, face_landmarker_result)

print(f"OBJ generation finished: {outfile_path}")