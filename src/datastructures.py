
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            # "id": self._generateId(),
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age": 25,
            "lucky_numbers": [3, 2, 7]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        for element in self._members:
            if element.id==id:
                self._members.remove(element)
        return self._members
    
    def update_member(self, id, member):
        ## you have to implement this method
        for element in self._members:
            if element.id==id:
                index = self._members.index(element)
                self._members[index] = member
        return self._members

    def get_member(self, id):
        for element in self._members:
            if element[id]==int(id):
                return element
        return {}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
