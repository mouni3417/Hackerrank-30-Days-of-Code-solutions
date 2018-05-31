class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxValue = max(a)
        minValue = min(a)
        self.maximumDifference = maxValue - minValue





# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)