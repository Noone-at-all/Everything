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
#Returns the GCF of two numbers, made for pointslope()
def pointslope(): #Dependent on GCF
    x1 = int(raw_input('x1?'))
    y1 = int(raw_input('y1?'))
    S = raw_input('Do you have a slope?').lower()
    if S not in 'yn' or S == '':
        print 'Only "y" and "n" are accepted inputs'
        pointslope()
    elif S == 'n':
        x2 = int(raw_input('x2?'))
        y2 = int(raw_input('y2?'))
        motionu = str(y2 - y1)
        motionl = str(x2 - x1)
        motiont = int(y2 - y1) / GCF(int(motionu), int(motionl))
        motionb = int(x2 - x1) / GCF(int(motionu), int(motionl))
        while GCF(int(motiont), int(motionb)) > 1:
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
        print 'Point-slope form: y - %s = %s(x - %s)' % (y1, slope, k)
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
def IOPC():
    top = float(raw_input('What number should I multiply?'))
    bottom = float(raw_input('By what number?'))
    div = float(raw_input('And what should I divide their product by?'))
    tote = top*bottom
    while GCF(tote, div) > 1:
        gcf = GCF(tote, div)
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
        return int(frac)
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
    print str(Ans) + ', Distance.' + str(Ans**2) + 'Squared'
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
    while GCF(RCoX, CoY) > 1:
        TheGCF = GCF(RCoX, CoY)
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

class RegPolygon: #A regular polygon
    def __init__(self,sides):
        self.sides = sides
        self.SumIntAng = self.sides*180-360
        self.IndivIntAng = self.SumIntAng/float(self.sides)
        self.SumExtAng = 180.0
        self.IndivExtAng = 180.0/self.sides
    def __repr__(self):
        print "Number of sides: %s" % self.sides
        print "Sum of interior angle's measures: %s degrees" % self.SumIntAng
        print "Measure of individual angles: %s degrees" % self.IndivIntAng
        print "Sum of the measures of the exterior angles:  %s degrees" % self.SumExtAng
        return "Measure of the indiviudal exterior angles: %s degrees" % self.IndivExtAng #Will only print if called by print
def UseRegPolygon(sides, VarName="Regular Polygon"):
    RegularPolygonDict = {}
    RegularPolygonDict[VarName] = RegPolygon(sides)
    print RegularPolygonDict[VarName]
#It's a class for a regular polygon, and a function for using it to calculate
def FindNumSides(Intang):
    return 360.0/(180.0-Intang)
    #It takes a measure of an interior angle and returns the number of sides of the regular polygon that produces it.
#from math import sqrt
def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
def SimplifyRadical(Rad, coeff = 1):
    if coeff > 0:
        rad = Rad*coeff
    else:
        rad = Rad
    def GetPerfectSquares(argument):
        PerfectSquares = []
        for item in range(1+(argument/2)):
            PerfectSquares.append(item**2)
        return PerfectSquares
    PerfectSquares = GetPerfectSquares(rad)
    def GetFactors(arg):
        factors = {}
        templista = []
        for tien in range(2, arg-1):
            if arg % tien == 0:
                templista.append(tien)
            else:
                pass
        templistb = templista[::-1]
        for item in range(len(templista)):
            if templistb[item] in factors:
                pass
            else:
                factors[templista[item]] = templistb[item]
        return factors
    def GetPSquare(factors, NoSquares = False):
        keylist = []
        for key in factors:
            if factors[key] in PerfectSquares:
                return key
            else:
                keylist.append(key)
        keylist.sort()
        return (keylist[::-1])[0]
    PrevPSquare = 1
    NumSteps = 0
    while not IsPrime(rad):
        NumSteps += 1
        factors = GetFactors(rad)
        PSquare = GetPSquare(factors)
        rad = rad/PSquare
        print PSquare, ' sqrt', PrevPSquare
        if IsPrime(rad):
            break
        PrevPSquare = PSquare
    return ['%s sqrt(%s)' % (PSquare, PrevPSquare), NumSteps]
print SimplifyRadical(raw_input('What do you need simplified? [coefficent is second arg]')
#Simplifies radicals
def ImpCFS(): #Improved version of CFS(), should handle when x^2 has a coefficent
    #Is still in progress, use CFS() when possible.
    #Using the input sequence 8, -3, -10, and 6, -3, -10 throws error about string formatting.
    #Line 35, 400 in git
    #Seems to always fail with multiples of 6 and 4 as Coarga
    #Fails often
    """
    Traceback (most recent call last):
    File "<stdin>", line 80, in <module>
    File "<stdin>", line 35, in ImpCFS
    TypeError: not all arguments converted during string formatting
    """
    #Line 80 was function call
    #Do not want
    #Back to hard way
    Coarga = int(raw_input('x^2\'s coefficent?')) 
    arga = int(raw_input('What do you want factored?'))
    arga = arga*Coarga
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
        if h[v] % Coarga != 0 and CF[v] % Coarga != 0:
            Diff = h[v] - CF[v]
            Sum = h[v] + CF[v]
            CFDD[Diff] = 'Diff: %s, factors: %sx%s,(-)%s, sum: %s.' % (Diff, Coarga, h[v], Coarga, CF[v], Sum)
            CFSD[Sum] = 'Diff: %s, factors: %sx%s,%sx(+)%s, sum: %s.' % (Diff, Coarga, h[v], Coarga, CF[v], Sum)
            v += 1
        elif h[v] % Coarga != 0:
            Diff = h[v] - CF[v]
            Sum = h[v] + CF[v]
            CFDD[Diff] = 'Diff: %s, factors: %sx%s,(-)%s, sum: %s.' % (Diff, Coarga, h[v], (CF[v]/Coarga), Sum)
            CFSD[Sum] = 'Diff: %s, factors: %sx%s,(+)%s, sum: %s.' % (Diff, Coarga, h[v], (CF[v]/Coarga), Sum)
            v += 1
        elif CF[v] % Coarga != 0:
            Diff = h[v] - CF[v]
            Sum = h[v] + CF[v]
            CFDD[Diff] = 'Diff: %s, factors: %s,%sx(-)%s, sum: %s.' % (Diff, (h[v]/Coarga), Coarga, (CF[v]), Sum)
            CFSD[Sum] = 'Diff: %s, factors: %s,%sx(+)%s, sum: %s.' % (Diff, (h[v]/Coarga), Coarga, (CF[v]), Sum)
            v += 1
        else:
            Diff = h[v] - CF[v]
            Sum = h[v] + CF[v]
            CFDD[Diff] = 'Diff: %s, factors: %s,(-)%s, sum: %s.' % (Diff, (h[v]/Coarga), (CF[v]/Coarga), Sum)
            CFSD[Sum] = 'Diff: %s, factors: %s,(+)%s, sum: %s.' % (Diff, (h[v]/Coarga), (CF[v]/Coarga), Sum)
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
    print 'Source EQ: %sx^2 + %sx + %s' % (Coarga, Want*-1, arga/Coarga)
