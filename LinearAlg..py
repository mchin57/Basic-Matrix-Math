import math
class matrix:

    def __init__(self, mtrx):
        try:
            x = len(mtrx[0])
            for i in range(len(mtrx)):
                if (x!=len(mtrx[i])):
                    raise unequalDimensions
            self.data = mtrx
            for i in range(len(self.data)):
                self.data[i] = vector(mtrx[i])
            print("constructor", type(self.data[0]))
            self.shape = (len(mtrx),len(mtrx[0]))
        except(unequalDimensions):
            print('Not all vectors are the same length')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        if type(key) == int:
            return self.data[key]
        if(type(key) == (list or tuple)):
            try:
                if(len(key) != 2):
                    raise wrongLengthInput
                return self.data[key[0]][key[1]]
            except(wrongLengthInput):
                print("expected list or tuple of dimension (x,n)")

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return(self.data)

    def __str__(self):
        out = [self.data[0].data]
        for i in range(1, self.shape[0]):
            out.append(self.data[i].data)
        return(str(out))

    def append(self, vec):
        try:
            if(len(vec) != self.shape[1]):
                raise wrongLength
            self.shape = (self.shape[0] + 1, self.shape[1])
            self.data.append(vec)
        except(wrongLength):
            print("This vector is not the correct length. Expected length: ", self.shape[1], " Given length: ", len(vec))

    def zeros(self,shape):
        for i in range(shape[1]):

        for i in range(shape[0]):
            vec = vector([0])
            for i in range(shape[1]-1):
                vec.append(0)

    def transpose(self):
        out = self.data[0].transpose()

        for i in self:
            out.append(i.transpose())


class vector:

    def __init__(self, vec=None):
        if vec is None:
            vec = []
        self.data = vec
        self.size = len(vec)
        self.magnitude = self.getMagnitude()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return(self.data)

    def __str__(self):
        return(str(self.data))

    def append(self,val):
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

    def to_unit_vector(self):
        x = self.scalarMult(1/self.magnitude)
        return x

    def transpose(self):
        vec = vector()
        for i in range(self.size):
            element = self.size - i - 1
            print(element)
            vec.append(self[element])
        return vec
    
    def zeros(int):
        x = []
        for i in range(int):
            x.append(0)

#exceptions
class Error(Exception):
    """base class for exceptions"""
class wrongLength(Error):
    """raised when the vectors aren't the dimension"""
    pass
class unequalDimensions(Error):
    """raised when the vectors are not equal dimensional"""
    pass
class wrongLengthInput(Error):
    """raised when the input is the wrong length"""

x = vector([1,2,3,4,5])
y = x.transpose()
print(y)

testm1 = matrix([[1,2],[3,5]])
print(((testm1)))
testm1.append([6,7])

#print(testm1)