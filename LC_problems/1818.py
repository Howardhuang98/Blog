#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1818.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/11 16:43  
------------      
"""
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        a = sorted(nums1)
        diff = []
        for i in range(len(nums1)):
            diff.append(abs(nums2[i] - nums1[i]))
        current = 0
        if len(nums1) == 1:
            return sum(diff)
        for i in range(len(nums1)):
            l = 0
            r = len(a)
            while 2 < r - l:
                mid = (l + r) // 2
                if a[mid] > nums2[i]:
                    r = mid+1
                else:
                    l = mid
            new = min(abs(a[l] - nums2[i]), abs(a[l + 1] - nums2[i]))
            if new - diff[i] < current:
                current = new - diff[i]

        return int((sum(diff) + current) % (1e9 + 7))


if __name__ == '__main__':
    s = Solution()
    print(s.minAbsoluteSumDiff([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]))
    print(s.minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]))
    print(s.minAbsoluteSumDiff(
        [951, 1550, 1589, 50, 1452, 1374, 1163, 1715, 318, 867, 1290, 901, 296, 460, 1441, 1322, 1500, 113, 1300, 11,
         1933, 682, 568, 1746, 421, 182, 1176, 192, 415, 725, 979, 1288, 1422, 206, 780, 1810, 1765, 1290, 665, 1882,
         1133, 503, 1845, 31, 146, 502, 1182, 1892, 1254, 126, 1064, 1457, 1724, 391, 1672, 435, 1502, 735, 1961, 456,
         1928, 904, 1658, 1092, 555, 151, 750, 1023, 1147, 87, 1978, 549, 65, 1764, 1131, 341, 1994, 1793, 350, 1682,
         1606, 547, 1382, 180, 394, 1699, 1386, 1432, 1918, 1696, 1300, 1388, 1295, 714, 611, 52, 1551, 488, 1145, 665,
         848, 1763, 334, 1124, 412, 1081, 123, 1671, 1648, 428, 1200, 1428, 1949, 1136, 863, 580, 918, 1264, 1134, 1265,
         1156, 1689, 1129, 1021, 53, 1677, 285, 1865, 1992, 1633, 767, 1326, 1267, 1168, 1043, 1096, 1086, 503, 485,
         1941, 837, 118, 1444, 251, 57, 805, 1729, 1439, 352, 1661, 1189, 1919, 1857, 186, 1768, 1465, 1353, 928, 587,
         1074, 1080, 1459, 31, 752, 884, 1837, 1339, 639, 149, 156, 1194, 992, 1672, 194, 106, 885, 1788, 1315, 590,
         1927, 1368, 1546, 670, 225, 1971, 1044, 1154, 1986, 1962, 755, 1498, 1838, 398, 1613, 969, 1998, 564, 1851,
         533, 11, 515, 1626, 1913, 743, 1113, 1133, 1667, 1685, 1686, 1273, 902, 827, 1791, 1495, 1385, 1399, 604, 1734,
         374, 695, 1803, 1831, 1388, 240, 1147, 1199, 1997, 1576, 1089, 1976, 1857, 620, 247, 576, 386, 1034, 504, 265,
         381, 152, 373, 1207, 39, 540, 1060, 1701, 1222, 737, 11, 112, 132, 89, 409, 139, 1472, 437, 910, 1401, 1916,
         78, 557, 1830, 1392, 1952, 1489, 1519, 741, 1786, 38, 68, 1195, 639, 859, 1261, 1459, 616, 1463, 1203, 454,
         224, 1297, 419, 1212, 582, 166, 1119, 1654, 975, 118, 556, 373, 1713, 216, 1412, 1600, 1417, 306, 1653, 1490,
         70, 593, 1105, 666, 651, 71, 1196, 1769, 1457, 1976, 961, 968, 691, 1180, 510, 1087, 1136, 1377, 291, 1150,
         781, 1126, 1847, 168, 1072, 1696, 338, 563, 806, 1608, 260, 762, 574, 1131, 621, 971, 539, 1482, 387, 1194,
         1846, 120, 1248, 1036, 586, 1534, 1857, 76, 166, 1194, 791, 1097, 1167, 363, 1610, 950, 1899, 1015, 1841, 1977,
         1991, 693, 1003, 300, 370, 228, 1946, 1903, 271, 18, 594, 340, 183, 870, 254, 82, 741, 1846, 316, 115, 1401,
         385, 908, 710, 293, 183, 1797, 1517, 19, 268, 1072, 1456, 1228, 1241, 1931, 536, 146, 1610, 23, 1173, 504,
         1153, 1194, 1433, 21, 514, 1325, 843, 373, 453, 127, 1524, 487, 103, 545, 1125, 1472, 1017, 1976, 1519, 1174,
         1471, 495, 1930, 694, 546, 706, 1679, 207, 623, 1716, 1806, 437, 1814, 1481, 1080, 1759, 492, 349, 1510, 1545,
         1609, 379, 240, 1154, 651, 1222, 327, 1631, 449, 1332, 524, 1190, 1488, 1262, 1014, 644, 1522, 610, 624, 776,
         994, 1969, 1976, 1190, 1009, 65, 738, 181, 629, 1900, 51, 241, 420, 1311, 1350, 1817, 1181, 844, 682, 546, 911,
         968, 178, 1810, 336, 1838, 1636, 950, 232, 842, 1883, 1389, 1299, 1647, 1013, 267, 1363, 1473, 1013, 455, 1595,
         1404, 658, 1757, 373, 779, 790, 1437, 1693, 930, 944, 681, 1524, 1301, 515, 1627, 878, 1374, 1413, 173, 820,
         1914, 1584, 735, 1267, 1693, 1092, 21, 651, 1082, 131, 1366, 1217, 1436, 1604, 78, 1805, 256, 881, 1660, 876,
         152, 712, 1045, 719, 1433, 718, 848, 362, 334, 39, 184, 1351, 259, 240, 653, 1473, 203, 1237, 418, 265, 651,
         1467, 1312, 164, 1420, 8, 1267, 1738, 364, 325, 1752, 1497, 1262, 739, 101, 1312, 1782, 51, 832, 421, 1102,
         364, 1239, 1504, 1924, 1977, 1063, 413, 1657, 1929, 116, 1213, 323, 477, 1080, 261, 1164, 910, 540, 1742, 1809,
         676, 1824, 1476, 932, 1392, 1625, 1272, 1451, 930, 558, 302, 1679, 1316, 746, 1807, 1805, 541, 1805, 1431, 616,
         1423, 1083, 888, 1861, 1002, 1835, 949, 861, 198, 729, 72, 1215, 637, 1141, 814, 683, 654, 545, 1413, 1624,
         156, 615, 869, 1679, 509, 1729, 1940, 718, 1596, 799, 720, 1559, 663, 1669, 297, 638, 33, 362, 515, 1550, 913,
         1051, 1833, 1284, 529, 1813, 197, 1650, 896, 174, 1705, 638, 144, 1213, 138, 1105, 409, 829, 1199, 328, 884,
         350, 390, 582, 977, 612, 1600, 416, 1410, 1830, 1936, 1423, 173, 1568, 511, 1410, 1054, 1874, 395, 890, 867,
         671, 964, 1676, 926, 1711, 205, 1570, 327, 1069, 497, 1146, 535, 681, 1403, 629, 1006, 1799, 1805, 106, 125,
         1486, 1498, 289, 1789, 731, 444, 1064, 1766, 1435, 559, 1537, 169, 580, 388, 1074, 919, 1853, 1855, 1075, 727,
         321, 1897, 372, 292, 96, 1103, 565, 76, 1198, 1537, 1932, 787, 35, 643, 338, 1646, 905, 655, 566, 1368, 993,
         226, 1881, 321, 366, 331, 16, 154, 695, 1951, 1237, 458, 378, 311, 54, 1819, 1284, 448, 1333, 1133, 1930, 1338,
         806, 83, 1491, 426, 612, 1250, 1771, 1481, 1693, 181, 1426, 546, 289, 155, 1035, 456, 71, 1046, 1982, 973, 55,
         1982, 1878, 1036, 1089, 93, 548, 1552, 1797, 433, 1962, 1066, 489, 1389, 1024, 288, 71, 23, 162, 408, 763, 139,
         768, 1057, 585, 423, 285, 1115, 725, 398, 305, 1322, 1146, 613, 1847, 1751, 1524, 777, 1344, 1374, 133, 454,
         1182, 1265, 1124, 1697, 649, 51, 985, 704, 1293, 1774, 786, 332, 362, 910, 1138, 262, 1427, 1508, 12, 1855,
         640, 1476, 508, 1583, 157, 984, 1023, 847, 1976, 1258, 1206, 222, 326, 557, 935, 80, 1534, 389, 316, 1482,
         1229, 603, 850, 695, 1473, 874, 234, 887, 1854, 452, 652, 219, 348, 1837, 1759, 970, 598, 415, 1634, 1199,
         1900, 933, 1495, 680, 1747, 720, 1602, 761, 464, 1125, 1103, 1095, 1952, 1229, 425, 1549, 211, 1636, 1779,
         1434, 1644, 1914, 211, 1137, 867, 117, 130, 1240, 1812, 108, 1022, 345, 1421, 206, 1560, 1621, 947, 1145, 118,
         1116, 606, 932, 306, 965, 1528, 1142, 137, 829, 1378, 1195, 1293, 1888, 191, 1478, 643, 1409, 327, 714, 774,
         472, 54, 208, 1234, 414, 1994, 341, 1881, 1987, 1512, 73, 1858, 1369, 744, 400, 197, 599, 404, 1444, 1457,
         1622, 317, 1474, 678, 615, 342, 1577, 1515, 220, 935, 1646, 921, 1130, 1964],
        [1767, 1572, 1734, 1348, 852, 637, 758, 1613, 513, 1278, 1997, 1145, 248, 1908, 1214, 1790, 24, 156, 98, 613,
         690, 731, 69, 155, 108, 1143, 1800, 1473, 673, 59, 1053, 1357, 1631, 151, 398, 1559, 1256, 173, 1399, 669,
         1826, 469, 1591, 1840, 456, 10, 99, 85, 1942, 1323, 339, 1125, 577, 955, 1683, 1949, 1484, 434, 195, 318, 4,
         1545, 1095, 750, 5, 1490, 1704, 1286, 1602, 1421, 705, 290, 897, 564, 355, 1715, 45, 1568, 1329, 400, 1794,
         1890, 1589, 449, 677, 1803, 793, 723, 202, 276, 287, 1111, 75, 1639, 634, 1587, 1751, 1347, 402, 1599, 1377,
         1149, 820, 1017, 1837, 1802, 288, 1554, 215, 597, 1689, 1294, 940, 1807, 328, 616, 1438, 698, 1737, 1212, 1796,
         1565, 733, 1595, 1048, 244, 950, 315, 1655, 1869, 1630, 1956, 1989, 1739, 737, 83, 374, 38, 238, 523, 1318,
         1194, 186, 640, 818, 948, 1117, 1274, 157, 984, 162, 840, 956, 1886, 1803, 1898, 698, 1184, 1708, 1302, 1348,
         1117, 907, 964, 926, 1961, 1830, 1265, 1389, 1051, 1437, 1712, 555, 1837, 1140, 1764, 22, 1264, 1666, 1688,
         1281, 853, 405, 343, 449, 901, 1691, 996, 1185, 363, 650, 1764, 847, 468, 602, 1311, 829, 198, 325, 1794, 1841,
         1926, 1966, 1520, 1045, 624, 1255, 540, 1991, 1859, 1769, 737, 874, 882, 112, 842, 963, 964, 1437, 1786, 286,
         837, 210, 69, 551, 1219, 233, 837, 416, 450, 1598, 215, 609, 441, 592, 267, 756, 802, 388, 295, 1317, 1917,
         1905, 1221, 616, 1262, 389, 608, 35, 203, 1695, 1707, 927, 511, 899, 666, 475, 745, 938, 999, 330, 1870, 639,
         222, 1424, 451, 627, 354, 1272, 1235, 1242, 902, 1441, 1311, 1867, 20, 1340, 1337, 115, 761, 1120, 1736, 275,
         423, 886, 1672, 382, 1922, 254, 1111, 236, 868, 1592, 456, 826, 1897, 1163, 964, 71, 867, 562, 868, 137, 919,
         954, 1992, 134, 398, 1957, 67, 1627, 1574, 986, 1693, 1064, 142, 1555, 1760, 402, 1821, 669, 459, 1728, 1436,
         539, 1362, 1150, 167, 20, 604, 1773, 208, 1745, 100, 1313, 1756, 1296, 1064, 498, 772, 67, 493, 107, 1397, 321,
         425, 1102, 993, 1476, 295, 623, 428, 1354, 551, 1700, 1007, 964, 1356, 987, 1113, 410, 844, 964, 1928, 1253,
         643, 1858, 1204, 1827, 480, 1903, 405, 583, 1574, 1589, 504, 1430, 364, 582, 1951, 43, 1486, 325, 494, 324,
         298, 522, 1038, 1970, 820, 562, 429, 525, 1843, 492, 1964, 206, 593, 1709, 672, 1219, 575, 445, 946, 1567, 654,
         24, 15, 1464, 791, 543, 1144, 567, 84, 1172, 851, 1979, 997, 1713, 136, 1814, 1756, 1249, 661, 478, 1073, 1590,
         635, 1341, 1199, 721, 414, 65, 837, 1069, 889, 237, 1925, 213, 200, 727, 905, 873, 316, 440, 1529, 909, 1483,
         1567, 22, 1641, 989, 366, 1315, 42, 272, 299, 1158, 1104, 341, 705, 1324, 1599, 144, 572, 1602, 334, 1420,
         1120, 1964, 1338, 181, 1907, 290, 1380, 60, 1438, 878, 1199, 1990, 257, 1439, 595, 1438, 1884, 1497, 317, 574,
         1798, 1107, 268, 634, 570, 680, 1429, 117, 565, 822, 1952, 1034, 1433, 962, 969, 229, 1309, 1842, 721, 1655,
         490, 33, 1322, 357, 1296, 623, 942, 937, 239, 1455, 1064, 496, 238, 1543, 697, 218, 1752, 131, 453, 510, 250,
         1602, 1716, 147, 470, 263, 753, 696, 1315, 1146, 702, 925, 603, 1284, 174, 1415, 1084, 103, 1434, 1328, 1687,
         1955, 1661, 885, 964, 706, 88, 1110, 220, 157, 1454, 345, 1453, 1893, 1337, 1256, 681, 1291, 259, 1854, 1768,
         632, 1981, 1614, 1937, 1302, 1036, 381, 1637, 1557, 1975, 66, 101, 615, 331, 669, 471, 1220, 823, 13, 325, 391,
         1440, 1800, 381, 799, 910, 8, 1362, 1391, 1438, 1592, 1817, 1118, 1598, 619, 1805, 1912, 35, 1621, 1356, 1979,
         550, 992, 504, 971, 1218, 1160, 1639, 1326, 600, 479, 35, 1776, 732, 1898, 1626, 1041, 1846, 1203, 495, 1522,
         321, 645, 999, 268, 207, 147, 830, 249, 1987, 353, 1488, 1048, 1062, 792, 1232, 637, 1779, 55, 660, 415, 1802,
         1677, 1702, 1945, 801, 48, 629, 953, 238, 953, 1842, 1492, 863, 901, 771, 896, 1618, 326, 1556, 601, 253, 944,
         433, 1292, 263, 76, 77, 383, 925, 665, 1182, 727, 1662, 1158, 1295, 608, 1967, 41, 1212, 489, 1032, 59, 1386,
         261, 1861, 1865, 668, 972, 486, 900, 911, 1176, 111, 1842, 975, 856, 1289, 1532, 144, 128, 112, 1454, 934, 119,
         1491, 90, 397, 1399, 1702, 52, 353, 1521, 787, 631, 1655, 1638, 1733, 1423, 611, 1007, 1851, 1230, 1903, 726,
         1995, 648, 1979, 267, 893, 998, 919, 336, 252, 966, 1259, 1597, 56, 793, 1744, 29, 1095, 1108, 1108, 1231,
         1215, 239, 1865, 1350, 45, 313, 134, 969, 1138, 291, 693, 1460, 1649, 1344, 228, 437, 978, 700, 1812, 928, 33,
         1666, 1421, 1787, 1440, 1203, 920, 1362, 849, 614, 451, 1493, 1645, 227, 1313, 1205, 1216, 1959, 695, 907, 618,
         979, 1056, 897, 1967, 300, 122, 1894, 1528, 941, 311, 1902, 368, 864, 1997, 1696, 1640, 1337, 662, 1879, 820,
         1596, 208, 1490, 1483, 161, 446, 163, 1579, 1559, 293, 1252, 483, 1502, 688, 1709, 999, 1196, 909, 783, 447,
         1945, 286, 412, 248, 1490, 249, 1181, 738, 1898, 1784, 443, 944, 996, 1818, 1094, 1595, 155, 1328, 33, 1552,
         539, 1153, 820, 1005, 1989, 1830, 952, 1640, 1166, 990, 399, 1720, 1552, 1995, 458, 1513, 1624, 1523, 1248,
         1965, 438, 1793, 766, 1846, 1841, 1873, 257, 157, 240, 407, 542, 1933, 1634, 41, 43, 841, 183, 641, 531, 402,
         1428, 380, 118, 18, 1219, 1309, 1190, 692, 192, 314, 523, 937, 126, 1502, 480, 692, 1536, 1814, 1316, 495, 64,
         212, 730, 677, 1964, 1647, 969, 565, 1444, 433, 1501, 181, 813, 711, 4, 1325, 785, 1252, 610, 856, 44, 735,
         1245, 118, 512, 417, 66, 109, 1875, 1000, 990, 787, 892, 726, 1093, 1045, 1801, 1506, 1567, 1299, 1516, 598,
         1766, 1026, 73, 1535, 1434, 777, 938, 161, 1101, 1301, 107, 513, 39, 1125, 1534, 584, 851, 798, 1497, 103, 383,
         1896, 1139, 477, 672, 1759, 1034, 1538, 1116, 1619, 992, 912, 1151, 1832, 1273, 949, 1703, 1127, 1518, 1059,
         199, 1867, 1694]))
