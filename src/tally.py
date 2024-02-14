from bulletinboard import BullitinBoard

class Tally:
    def __init__(self):
        self.votes = {}
        self.bulletinboard = BullitinBoard()
    
    def tally(self):
        cr_ids = []
        eligible_voters = self.bulletinboard.get_eligible_voters()
        for eligible_voter in eligible_voters:
            cr_ids.append(eligible_voter["cr_id"])
        print("cr_ids", cr_ids)
        print()
        for cr_id in cr_ids:
            self.add_vote_same_pseudonym(cr_id)

    def add_vote_same_pseudonym(self, cr_id):
        ballots = self.bulletinboard.get_ballot_by_cr_id(cr_id)
        # print(ballots)
        for i in range(len(ballots)):
            if 0 == i :
                final_ballot = ballots[i]
            else :
                final_ballot['1'] = self.homomorphic_addition(final_ballot['1'], ballots[i]['1'])
        
        # self.bulletinboard.set_final_ballots(final_ballot)
        # return (final_ballot)
    pass

    def homomorphic_addition(self, x, y):
        (x1, x2) = x
        (y1, y2) = y
        return ((x1.__int__() * y1.__int__()), (x2.__int__() * y2.__int__()))