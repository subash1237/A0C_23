from sys import argv 
from collections import defaultdict

hand:dict[int,list]=defaultdict(list)

def rank_checker(_argv)->int:
    _greatness="J23456789TQKA"
    for i in range(len(_greatness)):
        if _argv==_greatness[i]:
            return  i
    print("sorry more then jocker enters the house")
    exit()

def indexer(_index ,_spl)->None:
    _flag=False
    if hand[_index]:
        _counter=-1
        for i in  hand[_index]:
            _counter+=1
            for j in range(5):
                if rank_checker(i[j])<rank_checker(_spl[j]) :
                    break
                elif rank_checker(_spl[j])<rank_checker(i[j]):
                    hand[_index].insert(_counter,_spl)
                    _flag=True 
                    break 

            if _flag:
                break
    if not _flag:                 
        hand[_index].append(_spl)

def main(dataset)->None:
    hash_rank:dict[str,int]={}
    counter:dict[str,int]={}
    for i in dataset:
        _spl1=i.split()  
        _spl=_spl1[0]     
        hash_rank[_spl]=int(_spl1[1])
        _j_counter=0
        for k in _spl:
            # counter[k]=(counter.get(k,0))+1
            if k=="J":
                _j_counter+=1
            else:
                counter[k]=(counter.get(k,0))+1

        _cou_var=counter.values()
        if _cou_var: 
            _x=max(_cou_var)+_j_counter 
        else:
            _x=+_j_counter
        # print("_X",_x,max(_cou_var),_j_counter)
        print(_spl,"   ",_cou_var,_x)
        if _x==5:  # five of kind
            indexer(6,_spl)
        elif _x==4:  # four of kind
            indexer(5,_spl)
        elif _x==3  and len(_cou_var)==2 : # house full
            indexer(4,_spl)
        elif  _x==3:  # Three of kind
            indexer(3,_spl)
        elif len((_cou_var))==3:  # Two pair
            indexer(2,_spl)
        elif _x== 2 : # One paie
            indexer(1,_spl)
        elif len(_cou_var)==5: # High pair
            indexer(0,_spl)
        else:
            print("ERROR Occured",_cou_var,_spl) 
            exit()
        counter={} # reset counter 
    _rankiser=1
    _return=0
    for i in range(7):
        if hand[i]:
            for k in hand[i]:
                _return+=hash_rank[k]*_rankiser
                _rankiser+=1

    print(_return)
if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  