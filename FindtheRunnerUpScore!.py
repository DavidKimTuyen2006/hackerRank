if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_set = set(arr)
    
    a = sorted(list(arr_set))
    
    print(a[len(arr_set)-2])
