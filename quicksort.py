import time

def drawData(data, colorArray):
    # Visualization code to display the data array
    pass

def partition(data, low, high, drawData, timeTick):
    border = low
    pivot = data[high]

    drawData(data, colorArray(len(data), low, high, border, border))
    time.sleep(timeTick)

    for j in range(low, high):
        if data[j] < pivot:
            drawData(data, colorArray(len(data), low, high, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
            drawData(data, colorArray(len(data), low, high, border, j))
            time.sleep(timeTick)

    data[border], data[high] = data[high], data[border]
    return border

def quick_sort(data, low, high, drawData, timeTick):

    if low < high:
        partitionIdx = partition(data, low, high, drawData, timeTick)
#left position
        quick_sort(data, low, partitionIdx - 1, drawData, timeTick)
#right position
        quick_sort(data, partitionIdx + 1, high, drawData, timeTick)


def colorArray(dataLen, low, high, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(dataLen):
        if i >= low and i <= high:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == high:
            colorArray[i] = 'orange'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray


