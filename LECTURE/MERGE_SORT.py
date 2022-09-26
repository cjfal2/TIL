"""
O(n log n)
재귀방식은 메모리를 많이 잡아먹음
포인터방식은 메모리를 덜 잡아먹음
"""
def merge_sort(arr):
    """
    재귀 방식
    """
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


def swea_ms_div(m):
    """
    분할과정
    """
    if len(m) <= 1:
        return m
    # 찢는 부분
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = swea_ms_div(left)
    right = swea_ms_div(right)


def swea_ms_merge(left, right):
    """
    병합 과정
    """
    result = [] # 두 개의 분할된 리스트를 병합하여 result를 만듦

    while len(left) > 0 and len(right) > 0: # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 리스트의 첫 원소들을 빅하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0: # 왼쪽 리스트에 원소가 남아있을 경우
        result.extend(left)
    if len(right) > 0: # 오른쪽 리스트에 원소가 남아있을 경우
        result.extend(right)

    return result
