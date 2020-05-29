import math

def PolynomDivision(term: int, polynom: int)->int:
    """
        Performs a polynom division.

        Keyword arguments:
        term -- the term, which should be divided
        polynom -- the polynom to divide by

        return -- the result of the division
    """
    # shift the term to get the first carry
    shift = math.floor(math.log2(term)) - math.floor(math.log2(polynom))
    carryPolynom = polynom << shift
    carry = (term >> shift) << shift

    result = 0
    while(carryPolynom >= polynom):
        if(carry < 1 << math.floor(math.log2(carryPolynom))):
            # add 0 to the result if the reverse multiplication is 0
            result <<= 1
            # get the next carry
            carry |= (1 << math.floor(math.log2(carryPolynom)) - math.floor(math.log2(polynom)) - 1) & term
        else:
            # else add 1 to the result
            result = (result << 1) + 1
            if(carryPolynom > polynom):
                # transform XOR (polynomial substraction in the 2er arithmetic is equal to XOR) and get the next carry
                carry = carryPolynom ^ carry | (1 << math.floor(math.log2(carryPolynom)) - math.floor(math.log2(polynom)) - 1) & term
        carryPolynom >>= 1
    return result



res = PolynomDivision(0b1001001100000, 0b110101);
print(res)