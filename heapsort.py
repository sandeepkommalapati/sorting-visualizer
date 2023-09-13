import time

def heap_sort(data, drawData, timeTick):
    n = len(data)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap
        drawData(data, ['yellow' if x == i else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, i, 0, drawData, timeTick)

    # Draw the final sorted array
    drawData(data, ['yellow' for _ in range(len(data))])

def heapify(data, n, i, drawData, timeTick):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # Swap
        drawData(data, ['yellow' if x == i or x == largest else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, n, largest, drawData, timeTick)
