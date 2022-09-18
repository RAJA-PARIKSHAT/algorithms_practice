########## PROBLEM STATEMENT ##############
# https://www.codewars.com/kata/54d7660d2daf68c619000d95


def gcd(a,b):
  if a < b:
    a, b = b, a

  if b == 0:
    return a
  else:
     return gcd(b, a%b) 

def lcm(a,b):

  return int(a*b / gcd(a,b))

def convert_fracts(lst):
    
    ## Checking if there is any reducible fraction in the lst
    if len(lst)> 0:
        lst = [(1, frac[1] // frac[0]) if ( frac[0] != 1 and (frac[1] % frac[0]) == 0) else frac for frac in lst ]

        least_common_multiple  = lst[0][1]
        for i in range(1, len(lst)):

            least_common_multiple = lcm(least_common_multiple, lst[i][1])

        return [[least_common_multiple // frac[1] * frac[0], least_common_multiple] for frac in lst]
    else:
        return []

### Explanation
# The problem requires fractions to be in common denominator, once the fractions are irreducible, the common divisor is the LCM of the denominators, and then we
# just have to do some scaling for numerators
