import string


class Field:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id

    def append_to(self, field_str: string):
        return f"{field_str},{str(self)}" if field_str else str(self)


class FieldCollection:
    fields = []

    def __init__(self, fields):
        self.fields = fields

    def __str__(self):
        field_str = ''
        if self.fields:
            for field in self.fields:
                field_str = field.append_to(field_str)

            field_str = 'fields=' + field_str

        return field_str


class JiraRequest:
    fields: FieldCollection = FieldCollection([])

    def __init__(self, entity: string, entity_id: string):
        self.entity = entity
        self.entity_id = entity_id

    def select(self, *fields):
        for field in fields:
            self.fields.fields.append(Field(field))

    def __str__(self):
        request_str = f"/rest/api/latest/{self.entity}/{self.entity_id}?"

        if self.fields:
            request_str += str(self.fields)

        return request_str
