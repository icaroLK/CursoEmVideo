#include <stdio.h>
#include <locale.h>
#include <math.h>



int menu(void){
    while (1){
        int opc;
        printf("\n===============================================================================================================================");
        printf("\n                                                           MENU PRINCIPAL");
        printf("\n===============================================================================================================================");
        printf("\n 1. Vari�ncia de jovens adultos de 25 a 39 anos de idade");
        printf("\n 2. Desvio padr�o de adultos de 40 a 59 anos de idade");
        printf("\n 3. O menor n�mero de pessoas por munic�pio dentro da faixa de idosos acima de 60 anos");
        printf("\n 4. A m�dia da quantidade de pessoas dos 5 munic�pios com os maiores n�meros de pessoas dentro da faixa de crian�as at� 9 anos");
        printf("\n 5. Encerrar o programa");
        printf("\n===============================================================================================================================\n");
        printf("\nSua op��o: ");
        scanf("%i", &opc);
        fflush(stdin);
        if(opc==1 || opc==2 || opc==3 || opc==4 || opc==5){
            return opc;
        }
        else{
            system("cls");
            printf("\nDados inv�lidos!\nTente novamente");
        }
    }
}

int idades[][18] = {{82,387,511,687,749,593,537,530,548,592,555,500,387,337,271,223,143,132},
{83,394,590,702,624,416,434,372,385,392,385,351,330,246,228,185,126,133},
{118,473,642,859,807,614,619,587,586,577,568,474,366,324,260,200,92,104},
{1743,7093,8894,10792,10090,9240,9046,8537,8211,7391,6048,5014,3874,2719,1861,1232,753,666},
{56,217,362,427,426,314,296,299,274,335,291,221,229,168,134,107,75,75},
{30,177,262,288,274,251,222,250,248,230,218,196,143,120,117,87,47,46},
{203,700,994,1140,1225,1118,1056,1026,1005,1052,901,854,672,513,426,326,204,248},
{152,520,694,872,967,834,798,711,712,756,681,565,450,419,354,294,197,203},
{252,1078,1413,1665,1708,1622,1565,1442,1390,1493,1357,1257,1101,975,724,639,427,408},
{138,545,708,809,910,877,789,690,698,732,726,654,581,444,348,286,152,196},
{82,347,457,528,547,525,403,404,374,404,366,287,227,121,106,112,76,77},
{264,941,1326,1651,1657,1516,1358,1250,1229,1218,1192,962,763,633,502,394,244,208},
{40,148,193,268,253,197,194,231,182,216,172,179,156,127,117,73,56,72},
{246,1041,1387,1597,1667,1611,1594,1585,1515,1539,1458,1193,1170,948,765,541,370,383},
{34,148,201,235,245,242,215,205,221,214,210,176,129,113,100,72,43,56},
{270,1086,1575,1919,1697,1341,1274,1287,1223,1264,1313,1050,936,778,666,512,356,344},
{77,380,560,694,672,508,460,522,515,564,524,436,426,325,237,220,128,103},
{1562,6408,8300,9733,10481,10565,10073,9661,8732,9198,8056,7149,6018,4811,3698,2778,1843,1853},
{1433,5345,6972,8221,8433,9304,9190,8794,8169,7983,7152,5964,4896,3864,3012,2294,1568,1556},
{401,1645,2199,2562,2549,2101,2138,2043,1936,1831,1688,1300,1014,824,596,435,311,282},
{38,171,248,331,347,235,226,235,228,289,232,214,171,170,153,114,76,83},
{149,678,906,1147,1232,1103,954,1038,1041,1082,938,754,678,523,416,326,229,225},
{1841,7170,9708,11342,11259,11247,11118,10468,9628,8586,7357,5995,4702,3212,2142,1439,1005,904},
{47,102,173,189,213,172,169,156,180,189,169,145,140,128,105,72,55,49},
{224,870,1131,1332,1412,1305,1263,1128,1203,1116,1058,929,882,761,637,478,314,311},
{379,1538,2217,2597,2811,2412,2264,2424,2550,2713,2339,1982,1782,1495,1330,986,601,605},
{317,1233,1536,1859,2109,2020,1877,1846,1795,1909,1724,1551,1347,1093,846,660,466,510},
{50,144,233,321,322,268,285,274,305,347,285,242,221,200,154,101,78,83},
{169,646,802,1028,1028,1006,978,936,901,838,711,648,489,385,280,229,109,117},
{419,1672,2258,2702,2824,2753,2480,2251,2239,2357,2224,1972,1681,1413,1026,762,573,578},
{140,629,868,1115,1131,946,837,786,871,931,911,739,691,585,488,408,278,302},
{28,110,162,192,240,201,191,195,183,202,213,183,170,146,122,78,56,55},
{113,493,743,977,935,799,788,699,686,648,688,568,454,375,290,223,125,131},
{49,192,326,397,356,246,226,210,236,307,315,278,227,198,146,97,75,64},
{185,726,974,1227,1276,1197,1117,1051,1019,1099,1069,955,780,715,545,465,337,342},
{243,1094,1493,1766,1525,1288,1218,1232,1135,1053,938,764,691,484,350,262,195,149},
{47,200,313,342,363,344,332,313,348,394,384,296,218,198,179,137,77,83},
{25,140,249,275,251,194,216,183,227,220,168,177,139,96,73,54,49,28},
{103,383,579,726,682,532,503,515,504,417,413,311,291,197,165,105,68,60},
{126,436,691,806,690,481,533,549,597,527,463,449,420,352,325,202,148,116},
{178,719,980,1213,1017,890,885,816,803,681,623,553,465,390,276,222,128,148},
{56,186,279,394,385,223,213,256,252,258,223,235,229,190,152,116,73,76},
{101,345,485,592,601,545,507,473,439,510,450,356,284,266,203,183,111,110},
{44,147,209,264,321,253,201,222,233,263,254,209,190,163,130,73,54,63},
{95,324,450,622,689,546,498,501,620,564,624,516,485,381,326,266,182,189},
{69,299,469,490,507,448,394,395,413,456,415,339,263,215,224,139,97,103},
{40,149,216,253,309,240,197,228,218,273,248,168,172,132,133,109,53,71},
{30,128,198,214,250,227,204,189,204,229,190,147,119,105,101,75,32,53},
{217,849,1064,1311,1292,1378,1360,1265,1268,1199,964,718,563,395,316,224,148,131},
{57,185,269,346,362,306,288,290,333,343,305,248,257,196,145,154,101,105},
{95,450,564,679,718,683,607,547,536,660,527,487,389,348,271,215,137,156},
{278,1246,1663,1886,1991,1971,1817,1782,1702,1745,1699,1444,1216,1070,775,651,474,476},
{1251,4983,6835,8201,8058,8304,7996,7922,7576,7560,6455,5607,4667,3707,2738,2035,1467,1371},
{75,368,475,551,615,640,569,523,509,511,531,478,397,301,245,178,147,123},
{232,806,1156,1426,1420,1090,983,1115,1122,1161,1040,910,777,684,512,383,269,308},
{53,265,401,464,374,293,286,278,304,293,275,227,188,131,104,65,39,36},
{660,2538,3189,3952,3664,3538,3526,3233,2987,2772,2288,1999,1489,1029,744,517,340,304},
{38,245,371,473,479,315,271,329,325,347,283,210,201,174,108,105,73,60},
{128,471,634,804,710,615,546,582,498,501,408,329,268,206,153,116,86,70},
{1656,6166,8305,10119,10222,9710,9811,9850,8967,8548,7470,6058,4921,3718,2665,1905,1186,1100},
{389,1550,2010,2545,2451,2171,2109,2079,1987,1816,1484,1262,991,740,521,343,210,185},
{1163,4414,6131,7455,8000,7720,7238,6656,6610,6579,6135,5182,4118,3192,2418,1750,1197,1236},
{220,1026,1400,1776,1621,1153,1182,1170,1139,1109,1052,966,817,686,530,365,237,206},
{210,982,1387,1646,1534,1160,1123,1129,1092,1082,945,783,603,464,340,226,146,131},
{190,863,1189,1453,1286,970,894,949,939,876,760,681,599,436,338,220,159,150},
{219,857,1294,1554,1666,1341,1362,1283,1325,1375,1336,1217,1011,891,683,506,294,312},
{205,794,1130,1423,1366,1191,1154,1093,1114,1045,983,831,755,601,515,324,228,218},
{343,1433,1755,1878,1857,1707,1808,1679,1455,1254,1099,875,615,497,351,246,167,144},
{162,707,1035,1231,1174,1085,1074,922,933,915,990,874,749,604,430,348,256,217},
{4190,15789,20419,24649,26917,27735,26234,24004,22541,21318,18899,15451,12344,9025,6269,4557,2987,2877},
{1176,4578,6041,6913,6345,5596,5441,5355,4915,4468,3898,3234,2676,2120,1685,1200,746,697},
{150,604,827,1062,1031,843,752,783,763,700,574,526,445,366,302,224,136,114},
{117,517,756,956,1016,874,851,815,808,866,786,671,575,460,385,317,199,221},
{217,1079,1657,1978,1611,1264,1316,1219,1135,1060,992,805,762,589,478,348,224,204},
{138,539,777,924,944,885,844,868,895,827,732,615,566,486,374,261,173,184},
{263,1062,1490,1800,1871,1649,1462,1299,1441,1477,1375,1116,960,793,576,461,288,296},
{906,3631,4427,5519,6168,6441,6059,5646,5533,5481,4799,3912,3272,2603,1916,1512,1043,1090},
{176,592,860,1006,1011,942,910,923,838,815,708,572,470,364,287,249,166,173},
{267,1042,1429,1796,1654,1253,1213,1121,1151,1193,1208,977,776,640,520,446,285,269},
{3474,13425,17935,21010,20048,19433,19473,18534,17127,15282,12941,10635,8146,5776,3948,2646,1618,1516},
{229,991,1417,1713,1799,1873,1783,1793,1742,1755,1665,1448,1157,897,710,590,385,398},
{105,455,623,746,806,627,556,557,554,595,580,477,399,355,269,236,151,188},
{41,190,250,346,356,290,249,240,270,236,229,217,201,164,117,104,69,67},
{245,906,1336,1538,1364,1367,1240,1352,1186,1151,982,806,718,618,406,295,177,204},
{220,862,1130,1423,1524,1415,1280,1096,1180,1294,1140,967,777,597,492,383,269,263},
{514,2216,2947,3477,3850,3911,3730,3545,3323,3508,3342,3076,2693,2165,1548,1235,876,972},
{139,519,661,851,772,615,561,510,523,497,404,334,257,225,145,111,53,61},
{275,1114,1565,1932,2103,1716,1596,1494,1433,1570,1449,1367,1158,906,720,563,391,397},
{46,177,316,347,384,257,266,292,260,282,297,240,216,195,157,132,66,72},
{233,1006,1713,1947,1655,1459,1378,1362,1296,1210,1170,939,739,587,503,374,257,212},
{52,234,361,405,428,353,301,262,292,299,296,252,216,151,127,108,77,64},
{249,998,1336,1683,1720,1541,1530,1640,1583,1488,1391,1235,1004,884,701,600,396,437},
{60,233,307,362,402,389,361,308,353,356,322,292,246,157,147,99,82,87},
{44,141,196,260,294,196,236,241,240,245,226,211,173,129,115,97,60,58},
{22241,85678,112048,129993,139512,158554,165750,155230,138003,130381,122687,106731,87010,65793,45960,34456,24636,27244},
{179,859,1115,1362,1306,1142,1085,1010,981,934,874,788,607,510,452,318,191,210},
{75,248,374,472,484,413,367,379,431,418,390,329,276,258,218,166,132,86},
{42,217,322,440,364,223,238,260,260,234,237,132,148,131,85,74,51,52},
{88,305,396,518,551,416,315,306,321,330,352,233,237,213,174,113,74,85},
{500,1967,2650,3109,3367,3354,3094,2848,2723,2672,2501,2056,1655,1206,861,721,440,455},
{93,409,501,591,609,623,632,591,574,559,517,427,349,279,214,196,137,144},
{56,223,337,417,498,422,393,355,397,478,487,396,321,295,257,215,119,162},
{86,358,601,680,626,431,386,415,416,342,315,253,228,199,146,108,67,70},
{85,286,469,563,565,423,399,389,436,470,469,438,322,268,196,140,90,95},
{162,691,989,1165,1193,1134,1075,991,1027,1088,1003,830,731,591,420,353,222,241},
{53,195,267,309,321,321,305,311,307,317,282,216,214,180,139,85,53,51},
{27,72,128,155,148,118,129,127,158,164,150,105,114,107,96,71,52,49},
{61,311,440,476,442,308,292,277,338,296,284,265,230,208,165,116,95,73},
{52,183,262,326,344,227,232,259,262,268,253,203,159,123,114,77,71,57},
{265,886,1226,1479,1521,1335,1242,1115,1149,1170,1054,864,770,682,559,415,290,292},
{1437,5570,7499,8701,7921,7327,7274,7015,6388,5796,4939,3927,2890,1901,1314,844,491,441},
{56,205,332,408,477,347,323,305,359,390,341,289,240,216,163,141,98,112},
{99,341,521,624,616,487,419,426,446,414,383,298,270,200,136,99,81,72},
{109,439,608,781,776,598,550,583,642,560,562,465,420,367,303,243,140,147},
{69,225,393,473,484,311,301,317,348,384,333,281,231,182,142,120,77,55},
{42,192,237,350,440,399,345,340,370,408,374,309,335,251,242,161,123,132},
{82,283,388,439,503,538,502,471,413,433,429,391,294,228,195,138,110,94},
{134,597,801,1010,1006,954,896,852,882,854,807,657,491,372,325,250,176,158},
{28,141,175,201,201,200,178,196,181,215,186,156,119,108,91,74,45,48},
{78,266,411,542,620,538,495,477,514,617,641,533,460,369,323,276,188,193},
{4010,15780,20870,24514,24681,22726,21697,21425,20281,19141,16629,13656,10328,7428,5190,3551,2195,1986},
{100,336,560,616,575,401,397,377,380,330,321,268,226,180,146,95,59,53},
{85,348,476,516,621,417,383,367,415,495,420,392,369,349,271,218,128,148},
{1176,4250,5446,6655,7240,7548,7009,6152,5699,5854,5527,4500,3623,2838,2014,1452,965,995},
{227,887,1407,1628,1381,1138,971,1008,980,894,787,632,497,405,323,217,152,135},
{42,151,237,280,292,170,186,209,254,262,260,241,181,193,133,106,79,61},
{351,1427,2096,2474,2487,2379,2246,2065,2133,2174,2109,1703,1468,1176,931,779,537,483},
{137,468,775,898,776,539,587,486,463,510,472,394,322,223,208,114,81,50},
{82,347,453,652,660,514,431,458,469,483,471,376,343,268,222,154,117,125},
{447,1900,2388,2706,2666,2581,2424,2299,2348,2182,1958,1658,1438,1180,890,726,453,460},
{95,357,442,522,588,534,482,457,426,437,450,344,283,217,196,158,114,95},
{118,466,590,801,826,663,621,536,581,580,540,423,332,278,198,154,97,96},
{48,233,250,361,377,330,272,271,261,322,272,209,205,155,122,79,65,59},
{27,105,130,210,226,182,165,156,152,161,156,122,113,88,58,62,52,54},
{72,256,353,455,501,422,367,353,387,406,331,295,237,247,180,162,96,107},
{204,731,1139,1380,1467,985,1031,982,990,1061,984,870,771,623,535,387,219,223},
{2476,9988,13748,16332,16030,14389,13629,13260,12357,12052,10996,8950,7213,5481,4058,2815,1798,1756},
{114,488,723,889,767,598,602,613,524,494,414,417,311,287,232,175,111,112},
{511,1966,2672,3116,2978,2329,2315,2374,2233,2165,2127,1877,1740,1340,986,643,381,342},
{97,352,535,667,591,411,425,451,449,402,379,336,284,205,134,123,65,49},
{405,1702,2252,2556,2542,2306,2331,2223,1969,1974,1931,1575,1400,1110,885,676,463,451},
{88,334,526,614,660,490,402,462,450,433,367,302,245,230,182,138,72,71},
{642,2544,3474,3964,4062,3970,3935,4002,3506,3536,3232,2970,2463,1890,1402,1118,762,726},
{99,433,611,804,771,669,580,573,648,667,565,539,465,421,356,272,201,165},
{54,199,247,331,387,359,291,314,311,308,246,220,215,170,123,106,58,43},
{27,111,153,212,185,168,167,159,157,166,150,137,96,108,84,74,48,32},
{192,781,1025,1225,1061,871,842,877,872,689,624,544,471,383,307,218,158,134},
{432,1732,2640,2777,2722,2398,2408,2340,2105,1974,1746,1430,1131,873,665,494,289,299},
{212,763,1102,1264,1160,804,750,850,808,707,599,521,431,294,270,183,127,98},
{39,149,202,287,296,213,198,236,232,238,190,159,134,115,113,87,52,48},
{46,225,274,341,346,333,277,288,320,329,306,262,272,200,151,135,90,104},
{228,889,1223,1481,1392,1216,1185,1129,1022,941,834,690,579,433,341,257,157,153},
{177,726,1000,1261,1314,1150,1014,1023,980,1106,1030,965,809,666,527,479,376,378},
{23,116,178,210,218,188,159,168,207,228,220,141,103,112,112,83,62,50},
{790,3075,4041,4807,5030,4725,4604,4443,4205,4183,3829,3180,2774,2060,1629,1255,801,776},
{114,554,869,1056,987,692,748,707,745,771,751,580,538,440,388,299,177,206},
{73,257,323,428,440,370,345,275,343,317,319,287,198,161,138,123,94,77},
{122,472,680,838,858,790,745,695,726,659,590,452,387,354,249,175,118,116},
{84,353,475,602,568,503,484,514,461,492,461,414,380,262,233,191,135,147},
{93,278,394,443,546,459,497,451,452,476,396,350,314,259,212,148,105,106},
{125,534,740,912,962,816,761,728,733,781,778,651,575,444,348,272,186,185},
{425,1678,2380,2606,2481,2265,2105,2063,1811,1630,1219,924,727,559,423,256,163,172},
{48,215,282,325,338,274,257,234,256,230,223,185,164,144,147,114,76,71},
{226,795,1148,1301,1155,1064,1079,988,958,819,752,641,501,445,338,264,169,172},
{418,1553,2169,2509,2836,2267,2425,2234,2271,2375,2273,1994,1750,1415,1166,906,626,629},
{98,426,535,601,638,639,604,599,566,585,519,419,347,256,224,198,141,119},
{19,117,153,272,530,284,177,173,180,203,192,161,166,112,81,83,53,54},
{61,233,374,448,405,306,370,393,399,359,342,310,235,213,141,132,94,87},
{545,2138,2871,3352,3521,3454,3155,2911,2830,2710,2644,2289,1886,1570,1123,893,578,651},
{176,607,835,1011,1036,1071,1020,940,897,934,846,724,547,458,345,279,251,248},
{522,2157,2728,3180,3064,2777,2822,2681,2467,2198,2047,1701,1354,990,716,531,353,318},
{251,892,1323,1562,1761,1583,1503,1489,1455,1574,1447,1246,1086,913,734,605,391,454},
{67,298,442,555,604,473,426,388,475,460,486,418,379,324,265,196,132,144},
{73,263,412,441,414,367,349,342,327,325,332,312,253,226,168,123,83,93},
{97,380,522,650,694,672,615,615,619,673,660,566,481,397,306,245,182,175},
{142,606,914,1040,1133,852,802,820,876,926,843,782,675,580,465,389,251,228},
{14,85,89,133,143,98,99,104,105,127,110,71,59,42,42,36,25,27},
{173,696,975,1127,1095,968,984,869,811,819,761,650,545,447,358,273,150,174},
{98,439,533,683,723,566,582,585,703,715,677,568,510,470,393,337,204,215},
{149,556,746,876,913,949,860,816,733,733,731,609,548,502,343,259,205,208},
{37,178,278,321,297,239,192,223,221,275,243,238,183,157,116,88,73,74},
{77,326,600,672,658,581,586,581,594,621,592,464,360,279,221,195,119,115},
{85,347,503,528,598,537,500,510,512,523,453,370,272,273,210,171,109,109},
{43,194,241,325,386,315,278,287,317,359,344,290,266,228,203,164,130,136},
{607,2530,3579,4119,3918,3753,3725,3575,3393,3194,2963,2515,2101,1628,1241,897,624,570},
{92,435,700,798,724,488,463,452,401,367,385,270,244,177,157,101,51,55},
{402,1762,2555,3022,3067,2522,2377,2264,2158,2140,1907,1700,1406,1101,811,699,460,424},
{47,194,275,347,354,329,313,302,266,289,278,273,266,211,133,94,76,98},
{46,183,252,280,359,253,237,240,282,357,276,262,236,208,189,124,95,94},
{71,273,403,532,527,353,315,351,391,400,360,317,306,257,205,121,98,81},
{323,1084,1493,1776,1857,1832,1733,1595,1671,1582,1411,1223,952,795,637,506,360,371},
{52,214,295,370,363,336,372,353,353,347,363,268,206,137,127,113,68,64},
{6585,25553,33578,39559,41665,45226,44244,41246,36355,36973,34964,30532,25745,20479,15489,11803,8137,8568},
{128,428,602,682,685,634,571,533,520,527,489,385,314,256,214,152,95,100},
{61,247,367,456,421,348,331,328,362,402,394,355,269,241,221,151,114,92},
{67,197,340,385,398,352,313,318,322,404,331,234,221,193,170,143,105,99},
{171,640,984,1090,1228,1047,1041,974,907,930,908,772,633,509,378,290,247,224},
{185,743,992,1245,1224,1155,1015,996,1003,1055,1019,866,734,561,424,299,217,228},
{249,1022,1417,1674,1789,1730,1566,1535,1496,1524,1397,1125,872,741,554,475,293,322},
{388,1510,2124,2633,2696,2729,2591,2456,2443,2449,2330,2101,1656,1376,1094,823,632,627},
{327,1389,1936,2246,2043,1819,1650,1642,1588,1623,1379,1222,995,811,586,442,271,251},
{58,155,270,329,323,207,220,209,211,207,230,160,174,114,105,75,55,25},
{270,1114,1451,1844,1797,1417,1288,1281,1196,1138,1049,818,714,576,451,295,180,169},
{218,809,1121,1252,1221,1104,1015,946,943,868,797,712,580,531,406,258,179,209},
{540,2175,3072,3726,4125,4156,3878,3608,3621,3591,3375,2674,2290,1929,1455,1181,773,650},
{41,265,384,517,529,449,419,447,437,514,401,356,295,248,203,199,118,134},
{418,1559,2153,2492,2660,2792,2673,2417,2458,2445,2104,1935,1723,1405,1000,728,488,509},
{124,456,688,783,785,721,687,661,617,671,603,514,417,312,289,232,153,150},
{82,358,484,649,664,517,517,475,479,507,471,364,311,304,247,188,123,118},
{155,558,871,977,993,814,725,706,745,747,661,493,424,380,334,275,191,175},
{4232,16502,20975,24827,29473,35601,32162,28831,26858,27728,25820,22185,18510,14429,10526,7725,5158,5535},
{76,327,449,526,613,496,470,374,418,454,477,427,348,266,222,119,115,91},
{61,226,353,445,453,463,379,412,436,451,422,355,280,304,231,186,121,106},
{197,699,1062,1353,1297,1110,1023,895,938,1034,960,829,715,588,444,331,220,205},
{73,303,471,556,503,358,311,348,367,344,304,273,240,183,145,96,55,51},
{49,214,293,380,437,409,341,335,290,317,328,316,228,192,162,140,81,91},
{234,924,1220,1458,1490,1337,1294,1240,1184,1165,1077,880,761,575,455,358,215,211},
{403,1716,2293,2852,2583,2120,2068,2142,2100,2174,1934,1857,1633,1256,977,634,350,336},
{41,211,290,358,408,260,262,272,276,260,270,257,198,137,105,81,70,62},
{161,583,734,898,875,731,755,716,618,614,481,368,306,216,204,129,87,79},
{560,2220,2912,3487,3891,3946,3527,3244,3209,3279,2961,2343,1903,1384,1081,853,540,477},
{78,253,333,434,427,354,370,359,417,419,334,285,249,211,185,139,106,93},
{31,141,179,188,260,193,155,168,144,193,157,116,97,84,79,62,36,44},
{16,76,120,139,154,137,162,120,127,140,97,127,119,108,85,54,38,43},
{112,498,675,853,938,756,666,720,774,849,751,673,594,539,467,293,178,138},
{133,651,878,1119,1065,944,801,799,850,965,972,808,693,463,454,400,308,303},
{226,939,1265,1532,1445,1174,1072,1197,1135,1060,945,875,801,673,502,369,242,266},
{26,174,238,311,343,293,230,209,269,290,286,189,197,191,148,117,80,81},
{44,160,251,341,359,309,271,271,272,294,342,236,196,140,116,87,74,73},
{24,85,96,123,158,118,116,110,110,107,94,81,53,46,37,38,14,21},
{34,202,269,307,311,288,259,260,244,265,241,200,161,136,111,88,45,57},
{115,567,807,931,1077,888,829,865,900,956,838,722,665,530,418,345,238,175},
{101,387,555,760,788,475,470,449,549,552,547,459,362,316,242,188,105,120},
{312,1307,1847,2185,2252,2161,1969,1994,2030,2073,1899,1595,1341,1037,906,655,497,555},
{71,259,390,513,515,352,347,313,363,391,363,315,265,210,169,125,89,48},
{104,446,552,759,719,617,566,625,598,560,552,486,431,359,271,208,160,134},
{181,802,1093,1278,1180,815,758,684,697,754,669,588,539,392,303,225,140,143},
{172,683,945,1173,1235,1086,995,972,988,978,882,728,604,473,407,309,220,217},
{76,255,352,415,468,409,402,448,411,406,352,330,289,234,217,166,142,131},
{114,514,793,960,977,850,771,714,799,773,695,580,474,457,355,235,162,154},
{52,196,297,353,395,270,270,222,267,326,261,195,190,170,157,125,79,83},
{90,367,481,617,647,603,546,537,554,601,525,476,378,355,286,243,182,138},
{87,379,551,771,719,495,438,510,503,521,502,437,429,307,280,191,157,121},
{28,112,177,229,257,206,196,191,200,220,229,190,142,119,111,90,66,64},
{333,1468,2040,2406,2215,1721,1750,1740,1650,1483,1427,1200,1092,953,748,509,332,313},
{54,136,217,245,297,282,262,221,236,249,258,198,199,157,126,108,72,63},
{80,299,410,497,548,452,445,421,445,403,379,318,261,223,183,149,93,86},
{557,1875,2629,3107,3306,3224,3157,2907,2947,2680,2385,1911,1610,1238,917,656,408,422},
{804,3199,4310,4775,4260,3717,3613,3378,3105,2745,2348,1836,1544,1083,840,564,374,393},
{437,1877,2523,2991,3003,2716,2731,2437,2367,2322,2121,1780,1389,1103,819,658,448,401},
{232,909,1480,1590,1468,1094,1068,1019,1093,938,875,750,664,556,407,286,204,232},
{423,1431,1987,2254,2614,2520,2382,2221,2176,2151,1995,1583,1434,1165,920,618,421,388},
{167,635,825,942,1087,1065,985,877,932,907,754,649,533,419,313,283,202,197},
{173,648,774,925,907,887,880,789,755,794,672,505,392,324,284,242,145,154},
{2162,8926,12285,13927,13029,11753,11934,11163,10627,10095,9141,7169,5708,4271,3031,2366,1510,1372},
{46,166,207,247,292,240,233,217,208,212,189,151,104,87,75,47,30,40},
{1041,4178,5520,6588,6995,6749,6445,6008,6036,6282,5844,4970,3941,3302,2621,2093,1444,1533},
{63,254,330,386,395,401,382,352,371,357,333,278,227,211,191,140,72,79},
{981,3960,5102,6141,6751,6809,6404,5633,5293,5319,4947,4351,3382,2465,1777,1270,918,867},
{67,307,432,453,495,415,396,431,399,419,350,301,253,241,164,137,87,87},
{91,334,515,601,629,548,556,536,485,490,442,415,385,293,226,160,110,97},
{183,667,1014,1206,1254,1077,1050,967,1022,988,918,856,637,556,459,345,218,207},
{78,268,413,456,491,445,419,395,449,468,387,338,247,238,188,151,116,106},
{136,447,626,701,835,858,835,762,724,720,668,692,534,467,364,341,258,240},
{76,288,484,631,597,474,434,374,433,501,573,493,397,318,251,187,118,132},
{156,684,943,1101,1030,912,1035,994,873,789,639,582,517,368,253,139,114,107},
{1769,6667,9159,10336,10364,10434,10685,10715,9812,8714,7463,6241,4913,3721,2395,1632,1066,922},
{39,144,251,271,256,165,177,143,190,176,200,179,130,100,87,53,34,30},
{86,289,480,539,543,508,482,433,415,435,436,406,321,259,215,154,109,105},
{513,1982,3057,3743,3160,2398,2239,2161,2116,1904,1749,1425,1230,896,630,463,303,239},
{360,1501,2038,2178,2134,1950,1833,1775,1709,1547,1468,1163,1021,834,662,517,370,364},
{1549,6343,8309,9284,8696,8570,9049,8458,7537,6671,5359,4221,3115,2221,1546,1030,641,608},
{450,1821,2629,3209,3192,2512,2512,2492,2409,2368,2157,1744,1492,1214,930,651,436,420},
{29,152,215,269,245,221,201,219,219,225,182,167,128,118,89,59,38,38},
{54,211,317,342,387,367,279,272,296,311,289,207,185,162,119,117,93,87},
{156,621,901,1087,1270,973,933,891,969,1031,1085,852,792,697,469,417,269,241},
{4569,18638,24868,28473,28470,27261,26311,25609,22798,21304,19847,17148,13995,10857,7682,5714,3958,4109},
{302,1176,1604,1916,1700,1480,1489,1485,1464,1454,1502,1373,1225,1032,710,490,297,221},
{172,622,950,1196,1262,1109,1003,1039,1086,1115,962,857,750,689,522,375,241,239},
{62,243,392,434,438,372,374,354,319,316,293,231,199,151,110,82,61,83},
{54,198,300,360,389,282,258,261,224,255,237,267,164,166,91,75,44,38},
{37,128,171,241,248,214,164,207,201,179,167,162,111,86,64,66,42,42},
{54,245,333,391,364,282,315,300,298,256,236,234,199,158,134,94,61,66},
{35,190,235,307,301,291,237,280,265,244,234,181,172,162,122,77,56,45},
{78,239,372,473,474,458,369,388,414,450,406,362,317,261,199,160,101,107},
{66,255,370,432,456,394,372,401,393,361,322,230,214,167,124,94,71,62},
{111,469,697,836,891,838,842,707,742,838,798,714,652,476,423,335,223,240},
{685,2744,4030,4644,4415,3741,3914,3722,3581,3360,3154,2654,2366,1921,1454,1095,650,662},
{58,240,351,398,482,428,323,305,378,442,346,273,209,171,138,135,94,85},
{85,324,411,542,599,575,526,508,538,549,527,471,355,323,259,192,130,131},
{336,1213,1576,1825,1914,1798,1787,1708,1491,1431,1300,1041,778,582,427,276,176,192},
{37,151,237,313,331,296,241,255,283,308,302,251,183,164,139,122,100,90},
{466,1952,2799,3270,3016,2396,2302,2264,2240,2035,1813,1596,1309,1131,780,552,343,341},
{176,682,855,1130,1187,914,896,872,855,833,820,642,499,402,385,230,196,155},
{78,259,339,457,499,403,354,362,326,419,361,257,260,213,177,125,105,94},
{239,951,1371,1610,1620,1346,1325,1311,1213,1199,1035,980,821,683,556,361,247,221},
{63,228,362,456,419,299,301,281,310,288,263,209,178,176,116,83,59,43},
{48,165,249,344,332,262,284,265,267,303,300,221,226,215,168,121,81,104},
{31,142,203,251,263,237,197,188,231,228,203,162,148,85,91,75,51,61},
{209,823,1107,1385,1563,1340,1269,1129,1133,1206,1181,961,833,696,536,451,263,253},
{205,797,1183,1360,1363,1138,1078,933,995,1062,928,775,690,541,439,271,206,212},
{81,413,522,659,640,523,472,426,482,521,493,430,352,270,191,146,96,95},
{408,1663,2453,2781,2360,2098,2016,1870,1767,1568,1365,1134,988,933,674,496,297,301},
{108,495,771,976,811,555,512,553,518,479,421,332,260,193,114,98,57,54},
{140,502,740,872,916,810,824,776,753,786,708,662,567,464,409,300,199,250},
{177,724,977,1329,1277,952,936,892,916,926,951,745,686,595,453,415,277,296},
{235,776,1154,1330,1353,1205,1135,1075,992,1023,883,744,637,486,403,248,194,220},
{35,151,218,269,265,261,213,188,207,272,266,222,170,154,138,106,94,105},
{184,879,1352,1635,1432,925,925,938,990,982,878,697,601,439,321,210,148,125},
{52,240,344,433,415,316,291,293,263,244,227,192,165,117,98,83,70,55},
{493,1998,2732,3218,3029,2697,2736,2487,2323,2106,1744,1396,1211,872,643,425,280,260},
{425,1877,2430,2890,2763,2634,2567,2570,2417,2147,2003,1710,1439,1131,800,625,395,451},
{794,3004,3935,4516,4834,5188,4899,4728,4384,4477,3799,3423,2733,2312,1767,1281,927,861},
{137,591,969,1022,1022,881,872,786,899,830,806,628,590,472,383,275,199,175},
{132,459,689,748,806,728,679,711,655,740,637,487,410,318,285,199,146,167},
{78,278,398,543,579,356,359,367,364,408,399,296,266,271,217,165,129,115},
{63,297,398,503,575,489,471,487,461,468,409,349,361,239,182,139,100,105},
{56,197,349,481,417,292,309,307,303,328,288,258,218,171,143,127,78,81},
{57,242,355,423,468,360,342,338,365,341,368,346,343,255,192,155,117,111},
{194,712,1029,1233,1412,1190,1031,938,956,985,945,794,638,545,386,315,204,182},
{39,213,261,386,366,253,229,260,234,276,280,237,217,169,137,84,80,82},
{43,202,237,343,336,277,227,221,245,289,270,206,187,173,145,112,78,55},
{103,405,551,648,740,672,617,573,541,586,580,505,369,342,290,223,160,187},
{117,503,665,807,876,905,844,773,738,816,778,633,555,407,322,281,206,206},
{288,1134,1599,2035,2226,1800,1845,1723,1752,1766,1628,1335,1196,1049,807,564,332,334},
{20,84,121,155,166,138,137,119,132,142,155,108,85,90,57,47,33,29},
{102,392,570,684,723,638,644,567,628,653,675,541,481,399,348,296,192,227},
{181,640,964,1209,1309,1161,962,803,896,909,946,819,633,481,445,370,212,192},
{64,213,304,334,342,261,261,273,267,296,236,212,223,203,148,140,82,66},
{160,687,1006,1258,1256,876,785,837,777,721,679,604,556,451,335,247,138,127},
{132,561,785,998,1097,908,817,810,887,883,919,790,716,670,488,387,283,304},
{44,216,280,358,320,306,278,272,261,244,252,172,140,131,107,91,46,53},
{190,599,780,1038,1073,917,864,788,781,743,649,514,394,326,242,203,121,110},
{278,1175,1532,1966,2077,1754,1662,1622,1682,1628,1349,1116,870,712,563,380,265,210},
{59,265,403,521,442,346,368,377,369,373,397,318,284,228,177,129,90,103},
{605,2450,3248,3748,3635,3523,3427,3118,3031,3050,2899,2406,2152,1727,1249,1002,658,779},
{27,129,190,240,247,198,178,201,189,237,193,162,132,104,95,77,64,64},
{38,121,183,215,190,187,165,159,168,172,169,171,128,112,91,58,34,47},
{285,1099,1575,1993,1818,1481,1336,1223,1207,1260,1254,1100,910,721,579,436,341,275},
{69,262,341,412,463,457,428,393,397,394,414,290,256,194,172,136,92,99},
{89,335,441,548,631,540,508,454,482,497,439,335,280,208,193,147,111,116},
{158,652,951,1164,1063,885,779,823,782,741,697,623,541,451,359,298,194,176},
{143,497,725,880,977,800,754,652,680,761,785,738,649,490,363,295,196,214},
{78,299,456,551,563,441,445,451,413,418,399,335,283,210,192,173,94,110},
{112,527,795,911,977,869,780,756,806,895,806,725,711,560,445,349,249,252},
{210,909,1122,1389,1399,1209,1127,1052,970,924,823,705,551,460,319,224,170,141},
{65,255,336,432,416,394,376,385,395,476,429,345,302,268,237,176,108,122},
{66,261,347,453,568,467,393,408,426,462,433,388,356,306,235,194,132,146},
{112,415,592,744,839,744,654,574,639,719,671,598,516,364,337,245,161,161},
{73,332,468,674,574,439,469,405,424,488,442,403,371,314,202,174,140,119},
{44,177,299,340,359,309,285,259,279,280,246,207,211,181,160,88,51,55},
{4435,16467,21319,24285,23300,23755,25367,24463,21868,19560,16346,13203,10290,7357,4763,3323,2053,2056},
{17,98,141,175,161,169,145,152,140,167,160,131,117,101,76,59,49,40},
{580,2451,3344,3887,3769,3476,3513,3435,3258,2914,2682,2153,1732,1315,981,804,522,441},
{371,1377,1940,2350,2542,2226,1961,1953,1852,1902,1808,1399,1159,916,754,524,364,371},
{70,320,468,589,621,472,470,433,462,461,392,409,351,316,270,162,120,105},
{151,588,676,833,879,911,850,801,734,727,714,586,484,379,292,227,165,170},
{19,113,189,220,228,170,160,178,198,209,168,144,127,110,101,68,38,51},
{114,423,616,815,850,710,641,581,594,655,560,501,410,352,301,227,123,153},
{86,262,347,464,488,493,391,393,396,403,406,315,266,193,146,99,96,105},
{98,360,543,745,647,520,483,552,481,425,388,340,330,285,187,167,102,83},
{1246,4833,6237,7613,7523,7529,7110,6692,6543,6322,5270,4401,3644,2833,2031,1331,879,810},
{83,305,426,508,524,417,391,350,307,322,308,280,244,172,150,102,74,65},
{261,1217,1740,1968,1779,1507,1584,1424,1324,1245,1076,913,736,542,402,308,195,193},
{40,223,262,356,389,333,295,295,337,369,345,286,262,218,248,157,89,64},
{60,255,362,486,461,416,376,403,422,442,421,390,365,280,232,189,122,135},
{170,764,1020,1266,1352,1237,1217,1171,1126,1211,1130,972,852,650,520,401,278,301},
{249,901,1247,1645,1546,1509,1451,1491,1367,1360,1227,1144,914,732,597,478,338,258},
{45,162,252,283,252,243,209,194,253,270,259,211,193,165,158,129,63,53},
{203,821,1068,1260,1183,977,927,965,857,842,722,607,517,412,325,249,161,166},
{57,224,277,369,399,413,389,318,332,356,344,292,219,198,150,118,106,103},
{217,799,1036,1331,1332,1242,1253,1194,1136,1107,960,779,585,466,399,303,234,225},
{69,279,389,466,491,425,386,366,401,435,431,395,293,278,234,208,135,155},
{145,610,942,1071,1002,839,819,764,718,732,663,549,374,337,254,220,124,120},
{1119,4550,5712,6570,5949,5951,6049,5670,5112,4849,4469,3784,3004,2310,1807,1340,864,763},
{181,762,1035,1288,1414,1359,1328,1130,1174,1246,1093,867,702,615,538,469,289,286},
{237,871,1076,1241,1368,1232,1174,1093,1166,1103,1041,828,701,614,500,403,263,310},
{214,817,1153,1370,1473,1287,1263,1189,1255,1318,1209,982,827,704,577,487,329,305},
{331,1322,1828,2105,1884,1509,1440,1435,1325,1254,1182,973,771,629,506,362,249,239},
{178,944,1196,1503,1365,1122,1086,1096,1053,1051,873,745,625,540,451,307,209,193},
{1624,5873,8156,9931,10850,11492,10746,9712,9207,9216,8737,6674,5120,3814,2903,2175,1592,1491},
{106,439,594,706,720,683,647,570,595,653,667,595,480,433,311,225,174,193},
{160,690,995,1215,1130,875,870,832,852,861,759,614,554,456,361,282,156,162},
{126,502,715,755,625,567,575,496,401,364,286,236,197,146,94,70,52,49},
{127,450,620,773,803,675,649,655,669,667,622,461,401,317,275,216,163,152},
{88,419,587,626,595,585,506,614,617,619,528,486,470,395,322,228,162,150},
{219,805,1268,1449,1493,1152,1018,992,920,938,863,689,602,471,348,261,140,183},
{257,1014,1507,1711,1898,1667,1496,1580,1591,1725,1640,1368,1066,870,668,621,447,432},
{1253,4983,6457,7602,8696,9373,8493,8036,7738,7676,6947,5976,4875,3939,2971,2393,1645,1623},
{727,3097,4234,4996,4878,4391,4189,3964,3850,3701,3504,2842,2398,1841,1424,1186,763,750},
{24,128,166,220,236,191,184,204,180,204,163,105,124,104,83,57,56,37},
{114,537,764,932,980,870,771,734,832,858,790,711,652,553,418,374,275,307},
{150,633,903,1024,988,863,864,805,713,603,576,476,389,354,242,169,112,93},
{118,436,604,855,827,665,660,582,635,636,624,537,461,366,361,263,160,183},
{80,387,498,655,736,559,558,503,549,644,608,506,461,377,287,199,135,136},
{58,221,324,360,362,281,300,270,295,270,280,220,226,157,122,93,58,53},
{95,355,477,590,626,452,499,447,464,483,467,365,309,290,206,160,114,114},
{267,1054,1488,1807,1682,1478,1451,1392,1265,1352,1302,1188,1009,780,600,495,312,376},
{62,282,452,456,471,466,417,380,400,450,436,340,331,297,275,198,150,149}
};

float mediatop5(void){

    int verif = 0, maiorcol, dado, maiorfaixa;
    int qtdmaiorpessoas[399] = {};
    int faixaEtariadoMaior[399] = {};

    int topfivemuni[6] = {};
    int QtdPessoasAteNove[399] = {};

    int top1,top2,top3,top4,top5,atual;
    int muni1, muni2, muni3, muni4, muni5, muniatual;



    for(int lin=0; lin<399; lin++){         //passa por todas as linhas (municipios)
        for(int col=0; col < 3; col++){     //passa por todas as colunas (faixa etaria, no caso at� 9 anos (3�coluna))
            dado = idades[lin][col];        //analisa o dado atual
            QtdPessoasAteNove[lin] += dado; //soma os dados pra obter a quantidade de pessoas at� 9 anos daquele municipio)
        }

    };

    for(int pos=0; pos < 399; pos++){
        atual = QtdPessoasAteNove[pos];
        muniatual = pos;
        if(pos==0){
            top1 = top2 = top3 = top4 = top5 = atual;
            muni1 = muni2 = muni3 = muni4 = muni5 = muniatual;
        }else{
            if(atual>top1){
                top5 = top4;
                top4 = top3;
                top3 = top2;
                top2 = top1;
                top1 = atual;

                muni5 = muni4;
                muni4 = muni3;
                muni3 = muni2;
                muni2 = muni1;
                muni1 = muniatual;

            }else if (atual > top2) {
                top5 = top4;
                top4 = top3;
                top3 = top2;
                top2 = atual;

                muni5 = muni4;
                muni4 = muni3;
                muni3 = muni2;
                muni2 = muniatual;

            } else if (atual > top3) {
                top5 = top4;
                top4 = top3;
                top3 = atual;

                muni5 = muni4;
                muni4 = muni3;
                muni3 = muniatual;

            } else if (atual > top4) {
                top5 = top4;
                top4 = atual;

                muni5 = muni4;
                muni4 = muniatual;

            } else if (atual > top5) {
                top5 = atual;

                muni5 = muniatual;
            }
        }
    }
    int poptot = 0;

    for(int lin=0; lin<399; lin++){
        if(lin==muni1 || lin==muni2 || lin==muni3 || lin==muni4 || lin==muni5){ //se tiver na linha de um dos 5 municipios com mais pessoas ate 9 anos entra no for
            for(int col=0; col < 18; col++){
            poptot += idades[lin][col];
            }
        }
    };

    float mediafinal;
    mediafinal = (float) poptot/5;
    return mediafinal;

}





int main(){
    setlocale(LC_ALL, "Portuguese");



    printf("%f", mediatop5());

printf("\n\n\n");
return 0;
}
