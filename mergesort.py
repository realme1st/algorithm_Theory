 
def mergesplit(data):
    if len(data)<=1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left,right)

def merge(left,right):
    merged = list()
    left_point,right_point = 0,0

    #case 1 : left/right 아직 남아 있을 때
    while len(left) > left_point and len(right) >right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    #case 2 : left만 남아있을 때 
    while len(left)> left_point:
        merged.append(left[left_point])
        left_point += 1
        
    #case 3 : right만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random
data_list = random.sample(range(100),50)
print(mergesplit(data_list))