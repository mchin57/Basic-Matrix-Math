import math
class matrix:

    def __init__(self, mtrx):
        try:
            x = len(mtrx[0])
            for i in range(len(mtrx)):
                if (x!=len(mtrx[i])):
                    raise unequalDimensions
            self.data = mtrx
            self.shape = (len(mtrx),len(mtrx[0]))
        except(unequalDimensions):
            print('Not all your vectors are the same length')
        self.data = mtrx

class vector:

    def __init__(self, vec):
        self.data = vec
        self.size = len(vec)
        self.magnitude = self.getMagnitude()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return(str(self.data))

    def __append__(self,val):
        self.data.append(val)

    def adder(self,vecB):
        output = []
        try:
            if(vecB.size != len(self.data)):
                raise wrongLength
            for i in range(vecB.size):
                output.append(vecB[i] + self.data[i])
            return vector(output)
        except(wrongLength):
            print("These vectors are two different dimensions. Please input two vectors of the same dimension")

    def dot(self,vecB):
        mid = []
        output = 0
        try:
            if (vecB.size != len(self.data)):
                raise wrongLength
            for i in range(vecB.size):
                mid.append(vecB[i] * self.data[i])
            for i in mid:
                output += i
            return output
        except(wrongLength):
            print("These vectors are two different dimensions. Please input two vectors of the same dimension")

    def getMagnitude(self):
        sumA = 0
        for i in self.data:
            sumA += i**2
        return math.sqrt(sumA)

    def scalarMult(self,scalar):
        output = []
        for i in self.data:
            output.append(i*scalar)
        return vector(output)

    def project(self, vecB):
        """projects vecB onto itself"""
        try:
            if (vecB.size != len(self.data)):
                raise wrongLength
            top = self.dot(vecB)
            bot = (self.magnitude)**2
            scalar = top/bot
            out = self.scalarMult(scalar)
            return(out)
        except(wrongLength):
            print("These vectors are two different dimensions. Please input two vectors of the same dimension")

    def to_unit_vecrot(self):
        x = self.scalarMult(1/self.magnitude)
        return x

#exceptions
class Error(Exception):
    """base class for exceptions"""
class wrongLength(Error):
    """raised when the vectors aren't the dimension"""
    pass
class unequalDimensions(Error):
    """raised when the vectors are not equal dimensional"""

test1 = vector([1,2,3])
test2 = vector([4,5,6])

test3 = test1.project(test2)

print((test3))