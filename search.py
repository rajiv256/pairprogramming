def lower_bound(arr, prefix):
    lo = 0
    hi = len(arr)-1
    length = len(prefix)
    iter = 0
    while (lo < hi) & (iter<100):
        mid = int((lo + hi) / 2)

        if arr[mid][:length] > prefix:
            hi = mid-1
        elif arr[mid][:length] < prefix:
            lo = mid+1
        else:
            hi = mid
    iter += 1

    return lo


def upper_bound(arr, prefix):
    lo = 0
    hi = len(arr)-1
    length = len(prefix)
    iter = 0
    while (lo < hi) & (iter<100):

        mid = int((lo+hi)/2)
        if arr[mid][:length] > prefix:
            hi = mid - 1
        elif arr[mid][:length] < prefix:
            lo = mid + 1
        else:
            lo = mid
        iter += 1

    return hi

def range(arr, prefix):
    return lower_bound(arr, prefix), upper_bound(arr, prefix)

l = ['aacdef', 'abbcddn','absdjjdk', 'abskjfej','abfkjeifi']
l.sort()
st, en = range(l, 'ab')
print(st,en)
