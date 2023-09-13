#INSERTION SORT

import time

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['yellow' if x == j+1 else "#A90042" for x in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key

    # Draw the final sorted array
    drawData(data, ['yellow' for _ in range(len(data))])


#BUBBLE SORT

#import time
#def bubble_sort(data,drawData,timeTick):
#   for i in range(len(data)-1):
#      for j in range(len(data)-1):
#         if data[j] > data[j+1]:
#            data[j], data[j+1] = data[j+1], data[j]
#           drawData(data, ['yellow' if x ==j or x == j+1 else "#A90042" for x in range(len(data))])
#          time.sleep(timeTick)
#     drawData(data, ['yellow' for x in range(len(data))])


#SELECTION SORT

#import time
#def selection_sort(data, drawData, timeTick):
#   for i in range(len(data)):
#      min_idx = i
#
#       for j in range(i + 1, len(data)):
#          if data[j] < data[min_idx]:
#             min_idx = j
#
#       data[i], data[min_idx] = data[min_idx], data[i]
#      drawData(data, ['yellow' if x == i or x == min_idx else "#A90042" for x in range(len(data))])
#     time.sleep(timeTick)
