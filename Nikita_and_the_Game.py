def get_partitions(a):
    target_sum = sum(a)/2
    current_sum = 0
    if len(a) == 1:
        return 0
    for i in range(0,len(a)):
        current_sum += a[i]
        if current_sum == target_sum:
            return 1 + max(get_partitions(a[:i+1]),get_partitions(a[i+1:]))
    return 0

numTests = int(input())
for each in range(0,numTests):
    numElems = int(input())
    a = input().split()
    a = [int(x) for x in a]
    print(get_partitions(a))
