import math

def Euclid_distance(prefs,person1,person2):
    si = []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(str(item))

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
                         for item in prefs[person1] if item in prefs[person2]])
    # return 1.0/(1.0+sum_of_squares)
    return math.log(1+sum_of_squares)


def correlation_of_Pearson(prefs,p1,p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if n==0: return 0
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
    
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    num = pSum-(sum1*sum2/n)
    den = math.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r = num/den
    return r

def index_of_Jaccard(prefs,p1,p2):
    a = len(prefs[p1])
    b = len(prefs[p2])
    c = len([item for item in prefs[p1] if item in prefs[p2]])
    return c/(a+b-c)




def Manhattan_distanse(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    if len(si) == 0: return 0
    result_sum = sum([abs(prefs[person1][item]-prefs[person2][item])
                         for item in prefs[person1] if item in prefs[person2]])
    return math.log(1.0+result_sum)
