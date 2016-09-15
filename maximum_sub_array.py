def kadane(a):
    i,j = 0,0
    temp_i = 0
    max_end,max_so_far = 0,0
    non_contiguous = 0
    for (ind,x) in enumerate(a):
        if x > 0:
            non_contiguous += x
        max_end = max(0,max_end+x)
        if max_end == 0:
            temp_i = ind+1
        max_so_far = max(max_end,max_so_far)
        if max_so_far == max_end:
            i = temp_i
            j = ind
    if not max_so_far and not non_contiguous:
        m = max(a)
        max_so_far,non_contiguous = m,m
    return (i,j,max_so_far,non_contiguous)
numTests = int(input())
for each in range(0,numTests):
    temp = input()
    a = list(map(int,input().split()))
    i,j,contiguous,non_contiguous = kadane(a)
    print(contiguous,non_contiguous)
