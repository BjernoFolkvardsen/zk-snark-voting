class Registration:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        if self.validate_user(user):
            self.users.append(user)
            return True
        else:
            return False

    def validate_user(self, user):
        # Add your validation logic here
        return True