if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=[]
    for i in arr:
      if(i != ' '):
          l.append(int(i))
    
    print(max([ i for i in l if(i != max(l))]))