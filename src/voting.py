class Voting:
    def __init__(self):
        self.votes = {}

    def cast_vote(self, voter_id, candidate):
        """
        This function is used to cast a vote. It takes voter_id and candidate as parameters.
        """
        if voter_id in self.votes:
            print("Voter has already voted!")
            return False

        self.votes[voter_id] = candidate
        return True

    def validate_vote(self, voter_id, candidate):
        """
        This function is used to validate a vote. It takes voter_id and candidate as parameters.
        """
        # Add your validation logic here
        return True

    def store_vote(self, voter_id, candidate):
        """
        This function is used to store a vote. It takes voter_id and candidate as parameters.
        """
        if self.validate_vote(voter_id, candidate):
            return self.cast_vote(voter_id, candidate)
        else:
            print("Invalid vote!")
            return False