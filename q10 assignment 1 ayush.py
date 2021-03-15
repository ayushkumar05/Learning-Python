def q10():

    print('enter data to find simple intrest')

    _p= input('enter principle')
    _r= input('rate of intrest')
    _t= input('enter time in years')


    p= int(_p)
    r= int(_r)
    t= int(_t)


    prt = (p*r)*t

    ans = prt/100

    print(ans)


q10()
