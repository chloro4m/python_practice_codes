#binary search with recursion benchmarking:
# 1) with slice operator
# 2) without slice operator
#our lucky number is 954 to search for

import time
#usage: time.time()

#1000 item "listBSearch" hiding down here:
listBSearch = [-1000, -1000, -995, -995, -995, -990, -987, -986, -984, -984, -982, -977, -976, -976, -975, -973, -965, -964, -963, -962, -961, -960, -956, -955, -954, -954, -952, -951, -950, -948, -946, -946, -939, -934, -932, -931, -931, -931, -930, -927, -926, -926, -923, -921, -917, -906, -902, -901, -900, -900, -898, -895, -895, -893, -888, -884, -884, -883, -883, -877, -870, -865, -863, -859, -858, -857, -856, -852, -848, -848, -848, -848, -846, -845, -839, -836, -836, -831, -829, -826, -825, -824, -819, -816, -816, -813, -811, -810, -808, -807, -807, -806, -803, -803, -801, -797, -796, -794, -794, -792, -791, -783, -783, -782, -779, -774, -772, -770, -765, -764, -759, -754, -752, -748, -746, -736, -727, -725, -722, -720, -720, -719, -719, -717, -717, -716, -715, -712, -710, -701, -700, -699, -698, -696, -695, -695, -693, -686, -682, -681, -678, -671, -667, -666, -665, -665, -661, -659, -658, -657, -657, -652, -651, -649, -647, -646, -644, -638, -637, -637, -636, -635, -635, -632, -628, -626, -624, -621, -619, -618, -617, -613, -613, -611, -610, -609, -609, -603, -601, -598, -595, -592, -591, -585, -582, -580, -578, -577, -571, -570, -566, -564, -562, -560, -553, -551, -549, -548, -547, -546, -546, -544, -538, -537, -533, -532, -531, -528, -528, -523, -523, -521, -520, -519, -516, -515, -515, -514, -511, -511, -507, -506, -505, -502, -502, -500, -498, -496, -494, -492, -489, -487, -486, -485, -484, -481, -475, -474, -472, -472, -472, -468, -467, -467, -465, -461, -454, -452, -447, -441, -441, -438, -437, -436, -434, -434, -426, -415, -414, -412, -409, -408, -407, -406, -405, -402, -401, -400, -399, -399, -398, -393, -392, -392, -389, -388, -388, -388, -385, -382, -382, -373, -372, -371, -369, -366, -366, -364, -363, -361, -361, -360, -356, -356, -356, -354, -352, -352, -349, -348, -348, -348, -348, -345, -345, -340, -331, -331, -331, -326, -324, -324, -320, -320, -313, -313, -311, -309, -308, -308, -304, -304, -302, -300, -297, -295, -294, -294, -293, -290, -289, -288, -288, -287, -283, -283, -279, -276, -275, -275, -271, -271, -271, -268, -266, -259, -259, -251, -250, -249, -247, -245, -245, -244, -244, -242, -240, -239, -238, -236, -235, -230, -228, -219, -215, -213, -213, -213, -211, -209, -208, -198, -196, -194, -194, -194, -192, -188, -188, -187, -187, -186, -186, -185, -185, -179, -179, -178, -175, -174, -174, -167, -165, -160, -160, -154, -154, -154, -153, -150, -149, -148, -143, -141, -139, -138, -138, -136, -134, -134, -132, -129, -128, -126, -123, -121, -120, -119, -118, -117, -116, -113, -109, -109, -108, -108, -105, -104, -103, -103, -100, -98, -98, -98, -94, -90, -89, -89, -87, -86, -83, -82, -64, -60, -58, -56, -52, -51, -51, -50, -49, -48, -48, -45, -43, -42, -36, -33, -31, -31, -30, -30, -29, -28, -26, -23, -20, -18, -13, -11, -11, -10, -10, -8, -8, -8, -5, -5, -4, 2, 6, 7, 8, 8, 11, 11, 12, 12, 15, 20, 27, 30, 30, 30, 31, 32, 41, 44, 45, 53, 54, 56, 56, 59, 61, 61, 62, 62, 66, 67, 67, 73, 74, 74, 75, 76, 77, 81, 83, 86, 87, 89, 90, 94, 96, 105, 105, 107, 109, 110, 112, 114, 114, 115, 117, 119, 119, 119, 121, 121, 124, 128, 129, 129, 130, 135, 138, 140, 140, 145, 146, 149, 150, 150, 153, 160, 162, 162, 167, 168, 171, 172, 173, 173, 177, 178, 180, 183, 184, 189, 190, 194, 195, 198, 199, 200, 203, 204, 208, 208, 210, 210, 218, 220, 222, 225, 228, 230, 231, 232, 235, 236, 239, 240, 240, 240, 241, 241, 242, 243, 245, 247, 250, 253, 254, 255, 256, 260, 260, 260, 261, 262, 265, 267, 272, 273, 274, 281, 281, 283, 286, 286, 289, 290, 291, 295, 296, 297, 297, 300, 306, 307, 312, 313, 316, 321, 321, 327, 328, 329, 330, 332, 333, 333, 335, 341, 343, 345, 350, 351, 352, 353, 354, 356, 358, 361, 362, 365, 366, 366, 368, 374, 374, 377, 379, 379, 380, 383, 385, 388, 392, 393, 393, 398, 412, 414, 414, 414, 414, 414, 415, 417, 417, 420, 424, 429, 431, 436, 438, 438, 439, 441, 442, 445, 445, 446, 449, 450, 451, 453, 454, 461, 462, 464, 464, 465, 465, 470, 472, 474, 475, 476, 479, 481, 481, 485, 485, 486, 486, 487, 490, 491, 491, 491, 491, 494, 495, 496, 496, 496, 498, 499, 500, 503, 505, 506, 506, 508, 509, 509, 511, 512, 513, 516, 523, 524, 526, 526, 527, 527, 532, 532, 534, 535, 538, 543, 546, 547, 549, 549, 550, 550, 554, 555, 555, 560, 560, 563, 565, 565, 568, 571, 573, 574, 576, 578, 588, 589, 590, 592, 596, 605, 605, 605, 609, 610, 612, 613, 613, 615, 618, 626, 631, 640, 640, 641, 641, 643, 648, 651, 659, 660, 661, 664, 666, 667, 670, 671, 671, 673, 676, 676, 677, 681, 687, 688, 690, 692, 692, 692, 693, 697, 699, 699, 701, 702, 703, 704, 705, 707, 708, 708, 713, 714, 719, 724, 728, 732, 732, 733, 734, 735, 737, 738, 738, 739, 742, 743, 745, 746, 747, 747, 748, 749, 750, 751, 752, 758, 759, 761, 764, 767, 767, 769, 770, 771, 772, 778, 784, 788, 788, 788, 791, 793, 793, 794, 796, 796, 797, 801, 801, 803, 803, 804, 810, 814, 814, 816, 818, 818, 818, 819, 819, 821, 822, 823, 823, 824, 825, 825, 826, 831, 831, 832, 833, 834, 836, 837, 837, 837, 837, 838, 841, 844, 846, 846, 849, 852, 855, 856, 856, 858, 863, 864, 871, 871, 871, 874, 874, 875, 875, 879, 879, 883, 886, 888, 890, 890, 892, 892, 892, 893, 893, 894, 895, 897, 899, 900, 902, 907, 907, 908, 911, 916, 925, 933, 933, 935, 938, 938, 938, 939, 944, 946, 947, 948, 948, 954, 954, 956, 958, 959, 959, 961, 962, 964, 966, 966, 966, 967, 967, 970, 971, 972, 973, 975, 977, 979, 981, 982, 983, 985, 986, 988, 992, 993, 993, 995, 995, 999]
#1000 item list up here^:

def binSearch(listt, num):
    #base case:
    if len(listt) == 1:
        if listt[0] == num:
            return True
        else:
            return False
        
    mid = len(listt)//2
    if listt[mid] == num:
        return True
    elif num < listt[mid]:
        return binSearch(listt[:mid], num)
    elif num > listt[mid]:
        return binSearch(listt[mid+1:], num)

def binSearchNoSlice(listt, num, startIdx, endIdx):
    #base case
    if startIdx == endIdx:
        if listt[startIdx] == num:
            return True
        else:
            return False

    mid = (startIdx + endIdx) // 2
    if listt[mid] == num:
        return True
    else:
        if num < listt[mid]:
            return binSearchNoSlice(listt, num, startIdx, mid-1)
        if num > listt[mid]:
            return binSearchNoSlice(listt, num, mid+1, endIdx)

for i in range(10):
    #with slicing
    begin = time.time()
    for i in range(10000):
        binSearch(listBSearch, 954)
    end = time.time()
    print("Time (s) for 1000 item list bin-searched 10000 times with slicing is:")
    print(end-begin)

    #without slicing
    begin = time.time()
    for i in range(10000):
        binSearchNoSlice(listBSearch, 954, 0, (len(listBSearch)-1))
    end = time.time()
    print("Time (s) for 1000 item list bin-searched 10000 times with NO slicing is:")
    print(end-begin)