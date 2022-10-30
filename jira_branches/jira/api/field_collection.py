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
