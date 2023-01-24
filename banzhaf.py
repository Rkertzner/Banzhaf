#-------- This code is a modification of the code by Heinrich Hartmann, who modified the code of
Ruben
#-------- R. Puentedora (http://www.hippasus.com/resources/socialsoftware/index.html)
#-------- which was published under CC-License in 2004.
#This script calculates, according to the Banzhaf index, how much bargaining power each political 
#party in the Knesset held in each of the ten most recent governments and was adapted to best fit this purpose.


def banzhaf(weight, quota):

    max_order = sum(weight)

    polynomial = [1] + max_order*[0]

    current_order = 0
    aux_polynomial = polynomial[:]

    for i in range(len(weight)):
        current_order = current_order + weight[i]
        offset_polynomial = weight[i]*[0]+polynomial
        for j in range(current_order+1):
            aux_polynomial[j] = polynomial[j] + offset_polynomial[j]
        polynomial = aux_polynomial[:]

    banzhaf_power = len(weight)*[0]
    swings = quota*[0]

    for i in range(len(weight)):
        for j in range(quota):
            if (j<weight[i]):
                swings[j] = polynomial[j]
            else:
                swings[j] = polynomial[j] - swings[j-weight[i]]
        for k in range(weight[i]):
            banzhaf_power[i] = banzhaf_power[i] + swings[quota-1-k]

    total_power = float(sum(banzhaf_power))

    banzhaf_index = (lambda x: (x / total_power), banzhaf_power)
    return banzhaf_index


test_weight = [7, 9, 36, 7, 7, 15, 33, 6]
test_quota = 61
test_index = banzhaf(test_weight, test_quota)
print(list(test_index))
