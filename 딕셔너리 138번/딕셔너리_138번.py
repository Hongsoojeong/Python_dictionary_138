#연습 138번
#빙고게임
#딕셔너리 키 값에 여러 값을 어떻게 넣을 수 있을까/
def bingo():
    import random
    B=[]
    I=[]
    N=[]
    G=[]
    O=[]
    for i in range(1,16):
        B.append(i)
    for i in range(16,31):
        I.append(i)
    for i in range(31,46):
        N.append(i)
    for i in range(46,61):
        G.append(i)
    for i in range(61,76):
        O.append(i)
    card={B:"B",I:"I",N:"N",G:"G",O:"O"}
    return card
card=bingo()
import random
print(card[random.randrange(1,76)])
#연습 140번

