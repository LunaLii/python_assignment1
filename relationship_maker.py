class RelationshipMaker:
    def __init__(self, new_relationship):
        self.relationship = new_relationship

    def __str__(self):
        return f"       my{self.relationship} = []"