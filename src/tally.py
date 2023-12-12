class Tally:
    def __init__(self):
        self.votes = {}

    def add_vote(self, candidate):
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1

    def get_results(self):
        return self.votes

    def get_winner(self):
        return max(self.votes, key=self.votes.get)

if __name__ == "__main__":
    tally = Tally()
    tally.add_vote('Candidate1')
    tally.add_vote('Candidate2')
    tally.add_vote('Candidate1')
    print(tally.get_results())
    print(tally.get_winner())