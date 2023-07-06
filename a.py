Sum=0
a=0
b=0
c=0

def time():
    
    A=int(input("봉사활동 번호: "))
    B=int(input("자원봉사자 수: "))

    def each(Time, B):
        if B > 20:
            Time=Time*0.05

        elif B >=2 and B <=5:
            Time= Time*0.5

        elif B>=6 and B<=10:
            Time=Time*0.25

        elif B >=11 and B<=20:
            Time=Time*0.1

        else:
            pass
        return Time

    global a
    global b
    global c

    if A == 1:
        Time = 60
        a = a+1
        Time=Time*a
        Time= each(Time, B)

    elif A== 2:
        Time= 100
        b = b+1
        Time=Time*b    
        Time= each(Time, B)

    else:
        Time=120
        c=c+1
        Time=Time*c
        Time= each(Time, B)

    return Time


while Sum<300:
    Add= time()
    Sum= Sum +Add
    

print( str(int(Sum)) + "총 봉사 시간")