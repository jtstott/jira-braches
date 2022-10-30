class Field:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id

    def append_to(self, field_str: str):
        return f"{field_str},{str(self)}" if field_str else str(self)
