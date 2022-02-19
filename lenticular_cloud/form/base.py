from wtforms import SelectField, FieldList as WTFFieldList, Form
from wtforms.fields import Field
from ..model import db


class FieldList(WTFFieldList):
    def __init__(self, *args, **kwargs):
        self.modify = kwargs.pop("modify", True)
        super().__init__(*args, **kwargs)

    def get_template(self) -> Field:
        class CustomForm(Form):
            custom = self.unbound_field
        return CustomForm().custom


class ModelFieldList(FieldList):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop("model", None)
        super(ModelFieldList, self).__init__(*args, **kwargs)
        if not self.model:
            raise ValueError("ModelFieldList requires model to be set")

    def populate_obj(self, obj: object, name: str) -> None:
        while len(getattr(obj, name)) < len(self.entries):
            newModel = self.model()
            db.session.add(newModel)
            getattr(obj, name).append(newModel)
        while len(getattr(obj, name)) > len(self.entries):
            db.session.delete(getattr(obj, name).pop())
        super(ModelFieldList, self).populate_obj(obj, name)

