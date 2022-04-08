def make_readable(seconds):
    l = [0,0,seconds]
    while l[2] >= 3600:
        l[0] += 1
        l[2] -= 3600
    while l[2] >= 60:
        l[1] += 1
        l[2] -= 60
    for i in range(0,3):
        if len(str(l[i])) == 1:
            l[i] = ('{}'.format(0) + str(l[i]))
    return '{}:{}:{}'.format(l[0],l[1],l[2])




print(make_readable(int(input())))
