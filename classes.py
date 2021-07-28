# Class with the issues structure
class IssuesInput:
    def __init__(self, users = {}, issues = []):
        self.users = users
        self.issues = issues