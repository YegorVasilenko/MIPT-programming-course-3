def parent(i):
	return (i - 1) // 2


def left_child(i):
	return 2 * i + 1


def build_heap(a):
	n = len(a)
	i = parent(n - 1)
	while i >= 0:
		down(a, i, n - 1)
		i = i - 1


def down(a, l, r):
    i = l

    while left_child(i) <= r:
        child = left_child(i)
        swap = i

        if a[swap] < a[child]:
            swap = child
        if child + 1 <= r and a[swap] < a[child + 1]:
            swap = child + 1
        if swap == i:
            return
        else:
            a[i], a[swap] = a[swap], a[i]
            i = swap


def heapsort(a):
    n = len(a)
    build_heap(a)
    i = n - 1
    while i > 0:
        a[i], a[0] = a[0], a[i]
        i -= 1
        down(a, 0, i)


a = list(map(int, input().split()))
heapsort(a)
print(' '.join(list(map(str,a))))
