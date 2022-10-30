from jira.api.field import Field
from jira.api.field_collection import FieldCollection


class JiraRequest:
    fields: FieldCollection = FieldCollection([])

    def __init__(self, entity: str, entity_id: str):
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
