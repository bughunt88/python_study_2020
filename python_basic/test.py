def solution(arr, divisor):
    answer = []
    
    list = []
    for i in arr:
        
        if i%divisor == 0:
            list.append(i)
    
    list.sort()
    
    return list






print(sum(range(1,3)))