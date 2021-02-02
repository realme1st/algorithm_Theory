def binary_search(data,search):
    if len(data) ==1 and search == data[0]:
        return True
    if len(data) ==1 and search != data[0]:
        return False
    if len(data) ==0:
        return False
    
    medium = len(data)//2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:],search)
        else:
            return binary_search(data[:medium],search)

import random

data_list = random.sample(range(100),10)
data_list.sort() # 이진 탐색은 정렬이 되어 있는 상태여야 한다.

print(binary_search(data_list,7))
