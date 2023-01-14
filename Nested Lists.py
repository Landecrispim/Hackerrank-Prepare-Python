if __name__ == '__main__':
    lscore=[]
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lscore.append(score)
        l.append([name,score])
        
        
    l = [ i for i in l if(i[1] != min(lscore))]
    lscore = [i for i in lscore if(i != min(lscore))]
    l = [i for i in l if(i[1] == min(lscore))]
    l = sorted(l)
    
    for i in l:
      print(i[0])