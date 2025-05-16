import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Find all email addresses using regex
        found = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', self.emails)
        # Remove duplicates and sort
        return sorted(set(found))

def test_hello_world():
    assert True