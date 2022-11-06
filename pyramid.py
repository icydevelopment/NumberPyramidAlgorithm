pyramid = [None] * 15
# for i in pyramid:
#     print(i)
print("0   1   2   3   4")
print("  5   6   7   8")
print("    9   10  11")
print("      12  13")
print("        14")
pyramid[0:5] = [15,15,15,15,15]
pyramid_map ={}
for i in range (1,16):
    pyramid_map[i] = False

keepLooping = True
#print(pyramid[14])
while keepLooping:
    if pyramid[0] < 1:
        pyramid[0] += 1
        break
    pyramid_map.clear()
    for i in range (1,16):
        pyramid_map[i] = False
    pyramid_map[pyramid[0]] = True
    pyramid[1:5] = [15,15,15,15]
    pyramid[5:15] = [0,0,0,0,0,0,0,0,0,0]
    #print(pyramid[14])
    while keepLooping:
        if pyramid[1] < 1:
            pyramid[1] += 1
            break
        pyramid_map.clear()
        for i in range (1,16):
            pyramid_map[i] = False
        pyramid_map[pyramid[0]] = True
        
        if pyramid_map[pyramid[1]]:
            pyramid [1] -= 1
            continue
        pyramid_map[pyramid[1]] = True
        pyramid[5] = abs(pyramid[0]-pyramid[1])
        if pyramid_map[pyramid[5]]:
            pyramid [1] -= 1
            continue
        pyramid_map[pyramid[5]] = True

        pyramid[2:5] = [15,15,15]
        pyramid[6:15] = [0,0,0,0,0,0,0,0,0]
        #print(pyramid)
        while keepLooping:
            if pyramid[2] < 1:
                pyramid[2] += 1
                break
            pyramid_map.clear()
            for i in range (1,16):
                pyramid_map[i] = False
            pyramid_map[pyramid[0]] = True
            pyramid_map[pyramid[1]] = True
            pyramid_map[pyramid[5]] = True

            if pyramid_map[pyramid[2]]:
                pyramid[2] -= 1
                continue
            pyramid_map[pyramid[2]] = True

            pyramid[6] = abs(pyramid[1]-pyramid[2])
            if pyramid_map[pyramid[6]]: 
                pyramid[2] -= 1
                continue
            pyramid_map[pyramid[6]] = True

            pyramid[9] = abs(pyramid[5]-pyramid[6])
            if pyramid_map[pyramid[9]]: 
                pyramid[2] -= 1
                continue
            pyramid_map[pyramid[9]] = True

            pyramid[3:5] = [15,15]
            pyramid[7:9] = [0,0]
            pyramid[10:15] =[0,0,0,0,0]
            #print(pyramid)
            while keepLooping:
                if pyramid[3] < 1:
                    pyramid[3] += 1
                    break
                pyramid_map.clear()
                for i in range (1,16):
                    pyramid_map[i] = False
                pyramid_map[pyramid[0]] = True
                pyramid_map[pyramid[1]] = True
                pyramid_map[pyramid[5]] = True
                pyramid_map[pyramid[2]] = True
                pyramid_map[pyramid[6]] = True
                pyramid_map[pyramid[9]] = True

                if pyramid_map[pyramid[3]]:
                    pyramid[3] -= 1
                    continue
                pyramid_map[pyramid[3]] = True
                pyramid[7] = abs(pyramid[2]-pyramid[3])
                if pyramid_map[pyramid[7]]:
                    pyramid[3] -= 1
                    continue
                pyramid_map[pyramid[7]] = True

                pyramid[10] = abs(pyramid[6]-pyramid[7])
                if pyramid_map[pyramid[10]]:
                    pyramid[3] -= 1
                    continue
                pyramid_map[pyramid[10]] = True

                pyramid[12] = abs(pyramid[9]-pyramid[10])
                if pyramid_map[pyramid[12]]:
                    pyramid[3] -= 1
                    continue
                pyramid_map[pyramid[12]] = True

                pyramid[4] = 15
                pyramid[8] = 0
                pyramid[11] = 0
                pyramid[13] = 0
                pyramid[14] = 0
                #print(pyramid)
                while keepLooping:
                    if pyramid[4] < 1:
                        pyramid[4] += 1
                        break
                    pyramid_map.clear()
                    for i in range (1,16):
                        pyramid_map[i] = False
                    pyramid_map[pyramid[0]] = True
                    pyramid_map[pyramid[1]] = True
                    pyramid_map[pyramid[5]] = True
                    pyramid_map[pyramid[2]] = True
                    pyramid_map[pyramid[6]] = True
                    pyramid_map[pyramid[9]] = True
                    pyramid_map[pyramid[3]] = True    
                    pyramid_map[pyramid[7]] = True   
                    pyramid_map[pyramid[10]] = True  
                    pyramid_map[pyramid[12]] = True

                    if pyramid_map[pyramid[4]]:
                        pyramid[4] -= 1
                        continue
                    pyramid_map[pyramid[4]] = True
                    pyramid[8] = abs(pyramid[3]-pyramid[4])
                    if pyramid_map[pyramid[8]]:
                        pyramid[4] -= 1
                        continue
                    pyramid_map[pyramid[8]] = True
                    pyramid[11] = abs(pyramid[8]-pyramid[7])
                    if pyramid_map[pyramid[11]]:
                        pyramid[4] -= 1
                        continue
                    pyramid_map[pyramid[11]] = True

                    pyramid[13] = abs(pyramid[10]-pyramid[11])
                    if pyramid_map[pyramid[13]]:
                        pyramid[4] -= 1
                        continue
                    pyramid_map[pyramid[13]] = True

                    pyramid[14] = abs(pyramid[13]-pyramid[12])
                    if pyramid_map[pyramid[14]]:
                        pyramid[4] -= 1
                        continue
                    pyramid_map[pyramid[14]] = True

                    keepLooping = False
                    for i in range(1,16):
                        if not pyramid_map[i]: keepLooping = True
                    #print(pyramid)
                if pyramid[3] < 2: break
                if not keepLooping: break
                pyramid[3] -= 1

            if pyramid[2] < 2: break
            if not keepLooping: break
            pyramid[2] -= 1

        if pyramid[1] < 2: break
        if not keepLooping: break
        pyramid[1] -= 1

    if pyramid[0] < 2: break
    if not keepLooping: break
    pyramid[0] -= 1

print(pyramid)




