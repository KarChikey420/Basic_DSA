def febbo(num):
    febi=[0,1]
    for i in range(2,num):
        febi.append(febi[i-1]+febi[i-2])
    return febi
print(febbo(10))