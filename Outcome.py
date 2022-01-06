class Outcome:

    def _odds(self):
        if self.n in ['even','odd','first half','second half','red','black']:
            return int(1)
        elif self.n in ['first 12',"second 12",'third 12',"column one","column two","column three"]:
            return int(2)
        elif self.n in range(0,37):
            return int(35)

    def __init__(self, n):
        self.n = n
        self.odds = Outcome._odds(self)

    def __repr__(self):
        return "The odds are {}:1".format(self.odds)

# testing

# o1 = Outcome('black')
# print(o1)
# o2 = Outcome(4)
# print(o2)
# o3 = Outcome(00)
# print(o3)
# o4 = Outcome('first 12')
# print(o4)

    