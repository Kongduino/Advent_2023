import threading

# Most of the input file has been converted (in code, via regexes) to code
# Same as D5P2_v1.py, but calculations have been pre-computed (see converter.py)
def seed2soil(num):
  if num in range(1203272644, 1255408890): # eg 1203272644+52136246
    return num - 707003613
  if num in range(496269031, 953364929):
    return num + 52136246
  if num in range(953364929, 1203272644):
    return num + 52136246
  return num

def soil2fertilizer(num):
  if num in range(2086205436, 2111259135):
    return num - 1868797115
  if num in range(1670861921, 1701865702):
    return num + 933346535
  if num in range(0, 258383552):
    return num + 1631572552
  if num in range(3768288787, 3804481455):
    return num - 3639063233
  if num in range(2905533654, 3032200416):
    return num - 484328266
  if num in range(3399542287, 3756947172):
    return num - 3157080267
  if num in range(3032200416, 3286160975):
    return num - 2166047913
  if num in range(2262442546, 2643726153):
    return num - 222520765
  if num in range(2714844607, 2905533654):
    return num - 79632370
  if num in range(1753855801, 1777831915):
    return num + 1859152777
  if num in range(1503365158, 1670861921):
    return num + 2133619534
  if num in range(2111259135, 2111534091):
    return num - 770587274
  if num in range(806620565, 956586242):
    return num + 1083335539
  if num in range(3286160975, 3399542287):
    return num - 3286160975
  if num in range(956586242, 1503365158):
    return num + 2030503018
  if num in range(3756947172, 3768288787):
    return num - 1209075022
  if num in range(3807789063, 3851066913):
    return num + 39130584
  if num in range(258383552, 337523954):
    return num + 3275484624
  if num in range(1701865702, 1753855801):
    return num - 1536447480
  if num in range(586061766, 806620565):
    return num + 534051296
  if num in range(2217447855, 2262442546):
    return num + 341765910
  if num in range(4255836712, 4294967296):
    return num - 448047649
  if num in range(3851066913, 4255836712):
    return num + 39130584
  if num in range(1777831915, 1819919838):
    return num - 436885098
  if num in range(2111534091, 2217447855):
    return num + 769641405
  if num in range(2643726153, 2659570395):
    return num - 2530344841
  if num in range(337523954, 586061766):
    return num + 1045510786
  if num in range(2659570395, 2714844607):
    return num + 166330889
  if num in range(1819919838, 2086205436):
    return num - 1220052933
  return num

def fertilizer2water(num):
  if num in range(1751042330, 1890693964):
    return num + 2199477950
  if num in range(3912173308, 3954570380):
    return num - 2975594513
  if num in range(1722281506, 1751042330):
    return num + 1831399494
  if num in range(651809140, 741998534):
    return num + 46144177
  if num in range(876081661, 1244160117):
    return num + 2706360163
  if num in range(2358439651, 2610695344):
    return num - 1379463784
  if num in range(2678320518, 2878095651):
    return num - 1182440986
  if num in range(3308279888, 3430619104):
    return num - 1397899250
  if num in range(1561901004, 1653531622):
    return num + 1793191095
  if num in range(2033753243, 2104045316):
    return num + 1153914266
  if num in range(3816184128, 3857752165):
    return num - 1063981255
  if num in range(479585511, 528938542):
    return num + 169014775
  if num in range(2356473769, 2358439651):
    return num + 793126862
  if num in range(2629130810, 2678320518):
    return num - 933476145
  if num in range(385568770, 479585511):
    return num - 183667627
  if num in range(741998534, 745180691):
    return num - 205622530
  if num in range(3954570380, 4234470162):
    return num - 1482267289
  if num in range(257732262, 273037139):
    return num + 281825899
  if num in range(2610695344, 2629130810):
    return num + 520469821
  if num in range(1890693964, 1997652247):
    return num + 1556028753
  if num in range(1653531622, 1694355556):
    return num + 1140239288
  if num in range(65680232, 257732262):
    return num - 55831119
  if num in range(2104045316, 2356473769):
    return num + 774691396
  if num in range(2878095651, 2995639597):
    return num - 1085258959
  if num in range(1244160117, 1517759136):
    return num + 928425203
  if num in range(3884012463, 3912173308):
    return num - 1823366659
  if num in range(3719051611, 3816184128):
    return num - 461092029
  if num in range(745180691, 873107180):
    return num - 336731176
  if num in range(4234470162, 4294967296):
    return num - 3358388501
  if num in range(3043631916, 3308279888):
    return num - 1812400356
  if num in range(1997652247, 2033753243):
    return num + 1153914266
  if num in range(3430619104, 3456737856):
    return num - 984434765
  if num in range(582518586, 651809140):
    return num + 221298040
  if num in range(9849113, 50006317):
    return num + 545013925
  if num in range(3857752165, 3884012463):
    return num - 1711427143
  if num in range(50006317, 65680232):
    return num + 738136394
  if num in range(273037139, 385568770):
    return num + 22880745
  if num in range(1517759136, 1561901004):
    return num + 1316835708
  if num in range(3456737856, 3661533238):
    return num + 633434058
  if num in range(3661533238, 3719051611):
    return num - 1572726589
  if num in range(2995639597, 3043631916):
    return num - 1250795224
  if num in range(1694355556, 1722281506):
    return num + 338364298
  if num in range(528938542, 582518586):
    return num + 66081700
  return num

def water2light(num):
  if num in range(840812947, 855739064):
    return num - 284002841
  if num in range(2184905392, 2298950584):
    return num + 413508292
  if num in range(1600958027, 1849185560):
    return num + 529106010
  if num in range(1253957270, 1293495377):
    return num + 17070940
  if num in range(4262821917, 4294967296):
    return num - 741535005
  if num in range(1944404618, 2009337610):
    return num - 13841678
  if num in range(3302720391, 3345314333):
    return num + 949652963
  if num in range(279496091, 441497558):
    return num + 829530652
  if num in range(2565853410, 2569823274):
    return num - 1840075856
  if num in range(1330352326, 1516067791):
    return num + 1382106550
  if num in range(3173278185, 3302720391):
    return num + 866464076
  if num in range(2064417497, 2184905392):
    return num - 2064417497
  if num in range(855739064, 1113238133):
    return num - 556428027
  if num in range(1849185560, 1944404618):
    return num - 1119438142
  if num in range(767226476, 833457772):
    return num + 605774903
  if num in range(688212171, 767226476):
    return num - 116475948
  if num in range(2890412515, 2942298927):
    return num - 1011735987
  if num in range(682278717, 688212171):
    return num + 2215895624
  if num in range(441497558, 538937587):
    return num + 1339738941
  if num in range(3673052565, 3723191813):
    return num - 582963267
  if num in range(833457772, 840812947):
    return num + 532188432
  if num in range(2412172480, 2454933272):
    return num - 673696773
  if num in range(2569823274, 2704391379):
    return num - 574327342
  if num in range(3476912261, 3673052565):
    return num - 283363581
  if num in range(538937587, 682278717):
    return num + 286028889
  if num in range(3723191813, 4209501783):
    return num - 169759522
  if num in range(4209501783, 4262821917):
    return num - 1069273237
  if num in range(1113238133, 1253957270):
    return num - 144930527
  if num in range(3090089298, 3173278185):
    return num + 1079095169
  if num in range(204469065, 279496091):
    return num + 446281463
  if num in range(2704391379, 2890412515):
    return num - 1265158704
  if num in range(1516067791, 1600958027):
    return num + 995767234
  if num in range(2298950584, 2412172480):
    return num - 673696773
  if num in range(3345314333, 3476912261):
    return num + 44374651
  if num in range(0, 22623317):
    return num + 2378291570
  if num in range(2942298927, 2943987350):
    return num - 345573666
  if num in range(2009337610, 2064417497):
    return num - 698771293
  if num in range(201446459, 204469065):
    return num + 2739518285
  if num in range(22623317, 201446459):
    return num + 97864578
  if num in range(1293495377, 1330352326):
    return num + 1610612418
  if num in range(2454933272, 2565853410):
    return num - 54018385
  return num

def light2temperature(num):
  if num in range(624435822, 704880597):
    return num + 620023191
  if num in range(3309263777, 3482255287):
    return num - 700671514
  if num in range(2278806547, 2613904452):
    return num + 886596320
  if num in range(1643978777, 1749392529):
    return num - 1351159396
  if num in range(462426854, 477826347):
    return num + 242048413
  if num in range(2678497330, 3024337577):
    return num + 1018086831
  if num in range(3613542439, 3647705313):
    return num - 722287866
  if num in range(281665589, 462426854):
    return num + 1612858281
  if num in range(1456352798, 1643978777):
    return num + 250545093
  if num in range(1877125477, 2075285135):
    return num - 1478892344
  if num in range(3482255287, 3586796911):
    return num + 693845759
  if num in range(3662029939, 3991815655):
    return num - 1383223392
  if num in range(4098883907, 4294967296):
    return num - 598383135
  if num in range(3647705313, 3662029939):
    return num + 632937357
  if num in range(3024337577, 3035541099):
    return num + 1125155083
  if num in range(0, 207034864):
    return num + 85784517
  if num in range(3231118601, 3309263777):
    return num - 305701154
  if num in range(1749392529, 1835177046):
    return num - 1749392529
  if num in range(3215713737, 3231118601):
    return num + 944982445
  if num in range(3991815655, 4098883907):
    return num + 50608753
  if num in range(207034864, 281665589):
    return num + 922041656
  if num in range(1348270322, 1456352798):
    return num - 751877531
  if num in range(2613904452, 2678497330):
    return num + 486905537
  if num in range(1114082357, 1348270322):
    return num + 212018094
  if num in range(3586796911, 3613542439):
    return num - 722287866
  if num in range(3132788465, 3215713737):
    return num - 351204692
  if num in range(477826347, 624435822):
    return num + 1082462069
  if num in range(3035541099, 3132788465):
    return num - 31978476
  if num in range(704880597, 1114082357):
    return num + 14994163
  if num in range(1875928814, 1877125477):
    return num - 551025026
  if num in range(1835177046, 1875928814):
    return num - 631469801
  return num

def temperature2humidity(num):
  if num in range(736812858, 815982827):
    return num + 1885236596
  if num in range(2854489162, 2970650384):
    return num + 1125059115
  if num in range(2175018874, 2259499680):
    return num - 2175018874
  if num in range(2400631546, 2449133080):
    return num - 1832832758
  if num in range(2837901836, 2854489162):
    return num + 789174514
  if num in range(1289368272, 1310765426):
    return num + 169856098
  if num in range(3252694507, 3346619870):
    return num - 234657318
  if num in range(4063232797, 4084637350):
    return num + 32476702
  if num in range(2560175285, 2560870352):
    return num - 884600755
  if num in range(328659590, 655919326):
    return num + 321544261
  if num in range(3475937023, 3475986599):
    return num - 332173686
  if num in range(2091337597, 2175018874):
    return num - 499444344
  if num in range(3516768137, 3556417343):
    return num + 138556305
  if num in range(2259499680, 2354082485):
    return num - 1133714685
  if num in range(280432563, 323628225):
    return num + 802156770
  if num in range(1011614859, 1015580145):
    return num + 664654738
  if num in range(4039680780, 4063232797):
    return num - 83684520
  if num in range(684725863, 736812858):
    return num + 2016493560
  if num in range(2387091631, 2400631546):
    return num - 1409628044
  if num in range(3346619870, 3358280636):
    return num + 297043806
  if num in range(3556417343, 4039680780):
    return num - 412604430
  if num in range(3358280636, 3469205876):
    return num - 451168687
  if num in range(2615629615, 2748209426):
    return num - 321685516
  if num in range(920029028, 1011614859):
    return num + 70974474
  if num in range(1015580145, 1093842728):
    return num + 498050525
  if num in range(1310765426, 1627086090):
    return num - 1114046565
  if num in range(1638774240, 1970168747):
    return num + 41460643
  if num in range(815982827, 817864973):
    return num + 1195646563
  if num in range(4084637350, 4117114052):
    return num - 1210002103
  if num in range(2998403042, 3252694507):
    return num + 703301753
  if num in range(1093842728, 1289368272):
    return num + 1332681182
  if num in range(3475986599, 3484967352):
    return num - 638084763
  if num in range(3469205876, 3475937023):
    return num + 225767772
  if num in range(3484967352, 3516768137):
    return num - 373004800
  if num in range(662956301, 684725863):
    return num - 46655979
  if num in range(1627086090, 1637578390):
    return num - 406718290
  if num in range(2354082485, 2387091631):
    return num - 873460961
  if num in range(2970650384, 2998403042):
    return num - 123767795
  if num in range(323628225, 328659590):
    return num + 1028400725
  if num in range(655919326, 662956301):
    return num + 2097387092
  if num in range(2560870352, 2615629615):
    return num - 2047830827
  if num in range(1637578390, 1638774240):
    return num - 1553097584
  if num in range(0, 280432563):
    return num + 2013511536
  if num in range(2449133080, 2560175285):
    return num - 2363456424
  if num in range(817864973, 920029028):
    return num + 539195342
  if num in range(2748209426, 2760343393):
    return num - 2110139542
  if num in range(1970168747, 2091337597):
    return num - 739308647
  return num

def humidity2location(num):
  if num in range(3790677895, 3826197788):
    return num - 719230130
  if num in range(1470714761, 1531661205):
    return num - 969565839
  if num in range(3960084356, 3961198673):
    return num - 3010670577
  if num in range(547813284, 589945654):
    return num + 1728326688
  if num in range(0, 220957931):
    return num + 261623667
  if num in range(220957931, 428923614):
    return num - 220957931
  if num in range(2988733812, 3356696909):
    return num - 359678002
  if num in range(2507216386, 2519816910):
    return num - 1570403131
  if num in range(2402339659, 2435580058):
    return num + 704627999
  if num in range(3356696909, 3367781860):
    return num - 2446854999
  if num in range(920191219, 1261578731):
    return num + 109838481
  if num in range(3572469232, 3698288708):
    return num - 1069232898
  if num in range(1666455982, 1939508520):
    return num - 295038770
  if num in range(3367781860, 3393455884):
    return num - 370762953
  if num in range(2519816910, 2988733812):
    return num + 791277638
  if num in range(1531661205, 1615050929):
    return num + 489743539
  if num in range(1939508520, 1999387752):
    return num + 1200699537
  if num in range(428923614, 431160017):
    return num - 169536350
  if num in range(1334878052, 1414379656):
    return num - 384349956
  if num in range(1414379656, 1470714761):
    return num + 1032521573
  if num in range(3393455884, 3533750780):
    return num - 1748986134
  if num in range(3698288708, 3747043542):
    return num - 675595777
  if num in range(1999387752, 2252185620):
    return num + 2042781676
  if num in range(3981490698, 4196921113):
    return num - 2175516369
  if num in range(501148922, 522358605):
    return num + 1283615724
  if num in range(3961198673, 3981490698):
    return num - 3071648788
  if num in range(522358605, 532758551):
    return num + 3257652845
  if num in range(1261578731, 1334878052):
    return num + 843215737
  if num in range(3842084182, 3960084356):
    return num - 51672786
  if num in range(2252185620, 2365759774):
    return num + 66086722
  if num in range(3533750780, 3572469232):
    return num + 469700196
  if num in range(4196921113, 4294967296):
    return num - 2018827324
  if num in range(3747043542, 3790677895):
    return num + 161368028
  if num in range(2435580058, 2507216386):
    return num - 1873484692
  if num in range(532758551, 547813284):
    return num + 1899087945
  if num in range(3826197788, 3842084182):
    return num - 2905270927
  if num in range(1615050929, 1666455982):
    return num + 2336994994
  if num in range(431160017, 482581598):
    return num - 223194334
  if num in range(2365759774, 2402339659):
    return num - 1732028080
  if num in range(700952913, 920191219):
    return num - 30641334
  if num in range(589945654, 700952913):
    return num + 2610141635
  return num

mySeeds = "3640772818 104094365 1236480411 161072229 376099792 370219099 1590268366 273715765 3224333694 68979978 2070154278 189826014 3855332650 230434913 3033760782 82305885 837883389 177854788 2442602612 571881366"
n = mySeeds.split(' ')
seeds = []
for x in n:
  seeds.append(int(x))
print(f"seeds: {seeds}")

Minimum = -1
RefNum = -1
lnSeeds = len(seeds)
Minima = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
def handler(ix, startSeed, seedRange):
  global Minima
  print(f"Seed: {startSeed}, {seedRange}")
  myMinimum = -1
  for nn in range(0, seedRange):
    s = startSeed + nn
    myNum = s
    currNum = humidity2location(temperature2humidity(light2temperature(water2light(fertilizer2water(soil2fertilizer(seed2soil(s)))))))
    if myMinimum == -1:
      myMinimum = currNum
      RefNum = myNum
    elif myMinimum > currNum:
      myMinimum = currNum
      RefNum = myNum
  print(f"Minimum: {myMinimum} for {ix}")
  Minima[ix] = myMinimum

ix = 0
cnt = 0
thrds = []
while ix < lnSeeds:
  startSeed = seeds[ix]
  ix += 1
  seedRange = seeds[ix]
  ix += 1
  thrds.append(threading.Thread(target=handler, args=(cnt, startSeed, seedRange)))
  cnt += 1
for t in thrds:
  t.start()
for t in thrds:
  t.join()

print(Minima)
print(f"Minimum number: {min(Minima)}")
