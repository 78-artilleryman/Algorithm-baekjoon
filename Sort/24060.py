a, k = map(int, input().split())
l = list(map(int, input().split()))
n = 0
temp = []
tmp = []


def merge_sort(p, r):
    global l
    if p < r:
        q = int((p + r) / 2) # 중간지점 찾기
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)


def merge(p, q, r):
    global temp
    tmp = []

    i = p
    j = q + 1

    while i <= q and j <= r:
        if l[i] <= l[j]:
            tmp.append(l[i])
            temp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            temp.append(l[j])
            j += 1
    while i <= q:
        tmp.append(l[i])
        temp.append(l[i])
        i += 1
    while j <= r:
        tmp.append(l[j])
        temp.append(l[j])
        j += 1

    for i in range(p, r + 1):
        l[i] = tmp[i - p]


merge_sort(0, len(l) - 1)

if len(temp) < k:
    print(-1)
else:
    print(temp[k - 1])