def CFS():
    arga = int(raw_input('What do you want factored?'))
    if arga < 0:
        arg1 = arga * -1
    elif arga > 0:
        arg1 = arga
    arg2 = arg1
    CF = []
    l = 1
    g = arg1
    for item in range(g):
        if arg1 % l == 0 and arg2 % l == 0:
            CF.append(l)
            l += 1
        else:
            l += 1
    CF.sort()
    h = CF[::-1]
    oh = 0
    FList = []
    for item in CF:
        FList.append(''+ str(h[oh]) +' * '+ str(item) + '')
        oh += 1
    v = 0
    Want = int(raw_input('Which difference/sum do you need?'))
    CFDD = {}
    CFSD = {}
    DatInt = 3
    for item in CF:
        Diff = h[v] - CF[v]
        Sum = h[v] + CF[v]
        CFDD[Diff] = 'Diff: %s, factors: %s,(-)%s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        CFSD[Sum] = 'Diff: %s, factors: %s,(+)%s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        v += 1
    if Want in CFDD:
        print CFDD[Want]
        print 'Diff'
    if Want in CFSD:
        print CFSD[Want]
        print 'Sum'
    elif Want not in CFSD and Want not in CFDD:
        print '%s is not achievable with factors of %s' % (Want, arga)
    Want = Want * -1
    print 'Inverted diff/sum input, make changes as needed.'
    if Want in CFDD:
        print CFDD[Want]
        print 'Diff'
        DatInt = 1
    if Want in CFSD:
        print CFSD[Want]
        print 'Sum'
        DatInt = 1
    if Want not in CFSD and Want not in CFDD:
        print '%s is not achievable with factors of %s' % (Want, arga)
        DatInt = 2
    if DatInt == 3:
        print 'You have encountered bug1, the number you want is apparently in one of the the factor lists, but the program didn\'t print it'
    print 'Source EQ: x^2 + %sx + %s' % (Want*-1, arga)
#Factors a number and give you the difference/sum of the factors.
def Therom():
    a = float(raw_input('a?'))
    b = float(raw_input('b? (Or C, if you\'re finding a or b.)'))
    m = raw_input('Add or find?')
    s = m.lower()
    a2 = a**2
    b2 = b**2
    if s == 'f':
        if int(a2) > int(b2):
            print 'Invalid input(negative answer), check your numbers.'
            Therom()
        else:
            ans = b2 - a2
            print ans
            print ans ** .5
    elif s == 'a':
        ans = a2 + b2
        print ans
        print ans ** .5
    else:
        print 'You messed up'
        Therom()
#Triangles
def GCF(arg1, arg2):
    h = []
    if arg1 < 0:
        arg1 = arg1 * -1
    elif arg2 < 0:
        arg2 = arg2 * -1
    CF = []
    l = 1
    if arg1 > arg2:
        g = arg2
    elif arg2 >= arg1:
        g = arg1
    for item in range(g):
        if arg1 % l == 0 and arg2 % l == 0:
            CF.append(l)
            l += 1
        else:
            l += 1
    CF.sort()
    h = CF[::-1]
    for item in h: #Kept throwing errors, only this worked
        return item #Intentional return
#Not sure if different from GCFN, returns the GCF of two numbers, made for pointslope()
def pointslope():
    y1 = int(raw_input('y1?'))
    x1 = int(raw_input('x1?'))
    S = raw_input('Do you have a slope?').lower()
    if S not in 'yn' or S == '':
        print 'Only "y" and "n" are accepted inputs'
        pointslope()
    elif S == 'n':
        y2 = int(raw_input('y2?'))
        x2 = int(raw_input('x2?'))
        motionu = str(y2 - y1)
        motionl = str(x2 - x1)
        motiont = int(y2 - y1) / GCF(int(motionu), int(motionl))
        motionb = int(x2 - x1) / GCF(int(motionu), int(motionl))
        while GCF(int(motionu), int(motionl)) > 1:
            motiont = int(y2 - y1) / GCF(int(motionu), int(motionl))
            motionb = int(x2 - x1) / GCF(int(motionu), int(motionl))
        motion = '%s/%s' % (motiont, motionb)
        if x1 - x2 == 0 and y1 - y2 == 0:
            print 'Something happened, you tried to divide 0 by 0.'
            return 'sail'
        elif x1 - x2 == 0:
            print 'Vertical line at x=%s' % (x1)
            return 'wot'
        elif y1 - y2 == 0:
            print 'Horizontal line at y=%s' % (y1)
            return 'wot'
        m = (y2 - y1) / float(x2 - x1)
        u = False
        if m < 0:
            u = True
        S = 'y'
        k = m*x1
        cosa = y1 - k
        print m
        print motion
        print 'Point-slope form: y - %s = %sx - %s' % (y1, motion, k)
        print 'Slope-intercept form: y = %sx + %s' % (motion, cosa)
        if raw_input('Standard form?') == 'y':
            mi = float(motionb)
            cosa = cosa * mi
            if u == True:
                print 'x + %sy = %s' % (mi, cosa)
            else:
                print 'x - %sy = - %s' % (mi, cosa)
        else:
            print 'You\'re done!'
    elif S == 'y':
        upper = int(raw_input('What is the top of your slope?'))
        lower = int(raw_input('What is the bottom of your slope?'))
        while GCF(upper, lower) > 1:
            top = upper / GCF(upper, lower)
            bottom = lower / GCF(upper, lower)
            if GCF(upper, lower) == 1:
                break
        else:
            top = upper 
            bottom = lower
        m = top / float(bottom)
        h = False
        if m < 0:
            h = True
        slope = '%s/%s' % (str(top), str(bottom))
        k = m*x1
        print 'Point-slope form: y - %s = %sx - %s' % (y1, slope, k)
        cosa = y1 - k
        print 'Slope-intercept form: y = %sx + %s' % (slope, cosa)
        if raw_input('Standard form?') == 'y':
            print 'Assume this is standard form.'
            mi = bottom
            cosa = cosa * mi
            if h == True:
                print 'x + %sy = %s' % (mi, cosa)
            else:
                print 'x - %sy = - %s' % (mi, cosa)
        else:
            print 'You\'re done!'
#(x1, y1) + (slope or coord pair) = y=mx+b (and standard) format
def GCFN(arg1, arg2):
    if arg1 < 0:
        arg1 = arg1 * -1
    elif arg2 < 0:
        arg2 = arg2 * -1
    CF = [1]
    l = 1
    if arg1 > arg2:
        g = arg2
    elif arg2 >= arg1:
        g = arg1
    for item in range(int(g)):
        if arg1 % l == 0 and arg2 % l == 0:
            CF.append(l)
            l += 1
        else:
            l += 1
    CF.sort()
    h = CF[::-1]
    return h[0]
#See GCF, probably made for IOPC()
def IOPC():
    top = float(raw_input('What number should I multiply?'))
    bottom = float(raw_input('By what number?'))
    div = float(raw_input('And what should I divide their product by?'))
    tote = top*bottom
    while GCFN(tote, div) > 1:
        gcf = GCFN(tote, div)
        tote = tote / gcf
        div = div / gcf
    res = tote/(div*1.0)
    print '%s/%s' % (tote, div)
    print res
#Does is/of = %/100 for you
def fracfloat(frac):
    if '/' in frac:
        Thing = frac.split('/')
        Ans = float(Thing[0]) / float(Thing[1])
        return Ans
    else:
        return frac
#Converts fractions to floats
from math import sqrt
#Imports the sqrt function from math
def Distance():
    xaa = raw_input('X1?')
    yaa = raw_input('Y1?')
    xba = raw_input('X2?')
    yba = raw_input('Y2?')
    x1 = fracfloat(xaa)
    x2 = fracfloat(xba)
    y1 = fracfloat(yaa)
    y2 = fracfloat(yba)
    Ans = sqrt(((x2-x1)**2)+(y2-y1)**2)
    print str(Ans) + ', Distance'
    MP1 = ((x1+x2)/2)
    MP2 = ((y1+y2)/2)
    MP = '(%s, %s), midpoint.' % (MP1, MP2)
    print MP
#Takes the distance and midpoint of two coord pairs.
def count(sequence, item):
    g = 0
    result = 0
    List = [1, 2]
    Float = 1.6
    String = 'LeBron James'
    Integer = 1
    InputType = type(item)
    def IfFloat():
        Wot = 0
        for lel in sequence:
            if lel == item:
                Wot += 1
        return Wot
    def IfInt():
        CC = 0
        for numero in sequence:
            if numero == item:
                CC += 1
        return CC
    def IfStr():
        Resu = 0
        itemd = str(item)
        for thing in sequence:
            if thing == itemd:
                Resu += 1
        return Resu
    def IfList():
        Ind = 0
        Indseq = 0
        Res = 0
        CurrentRes = 0
        for thing in range(len(sequence)):
            if Ind == len(item) and CurrentRes == len(item):
                Res += 1
                CurrentRes = 0
                Ind = 0
            elif sequence[Indseq] == item[Ind]:
                if Ind < len(item):
                    Ind += 1
                    Indseq += 1
                    CurrentRes += 1
            elif sequence[Indseq] != item[Ind]:
                Indseq += 1
                Ind = 0
        return Res
    if InputType == type(List):
        return IfList()
    elif InputType == type(Float):
        return IfFloat()
    elif InputType == type(String):
        return IfStr()
    elif InputType == type(Integer):
        return IfInt()
#Counts the number of times item occurs in sequence.
def MostNums(List):
    Count = 0
    ResesDict = {}
    CountDict = {}
    for item in List:
        ResesDict[count(List, item)] = item
        Count += 1
    if max(ResesDict) <= 1:
        return List[(len(List) - 1)/2]
    return ResesDict[max(ResesDict)]
#Returns the number that occurs most often in the list.
def MMMR(List):
    List.sort()
    if ((len(List)-1)/2.0) % 1 != 0:
        Median = (List[(len(List)-1)/2] + List[len(List)/2]) / 2.0
    else:
        Median = List[(len(List)-1)/2]
    Mode = MostNums(List)
    Mean = (sum(List))/float(len(List))
    Range = max(List) - min(List)
    NewDict = {}
    NewDict['Mean'] = Mean
    NewDict['Median'] = Median
    NewDict['Mode'] = Mode
    NewDict['Range'] = Range
    return NewDict
#Return a dictonary of the Mean, Median, Mode and Range of a List of ints
def MMMRX(List, desired, x):
    for tien in range(x):
        List.append(tien)
        TheRes = MMMR(List)
        if TheRes['Mean'] == desired:
            return tien
        else:
            List.remove(tien)
#Finds the number needed to make the desired average out of a list of numbers.
def StandardConverter():
    CoX = int(raw_input('What is x\'s coefficent?'))
    CoY = int(raw_input('What is y\'s coefficent?'))
    AnInt = int(raw_input('What is the number that would be the y-intercept?'))
    RCoX = CoX * -1
    print '%sy = %sx + %s' %  (CoY, RCoX, AnInt)
    FCoX = RCoX / float(CoY)
    AnInt = AnInt / float(CoY)
    while GCFN(RCoX, CoY) > 1:
        TheGCF = GCFN(RCoX, CoY)
        RCoX = RCoX / TheGCF
        CoY = CoY / TheGCF
    FCoX = RCoX / float(CoY)
    FracCoX = '%s/%s' % (RCoX, CoY)
    print 'y = %sx + %s' % (FracCoX, AnInt)
#Converts x+y=b to y=mx+b
def Motion(x1, y1, x2, y2):
    T = y2-y1
    B = x2-x1
    if T < 0 and B < 0:
        T *= -1
        B *= -1
    while GCF(int(T), int(B)) > 1:
            Div = GCF(T, B)
            T = T / Div
            B = B / Div
    Dec = float(T)/(B)
    Frac = '%s/%s' % ((T), (B))
    return [Dec, Frac]
#Gets the motion, and just the motion
