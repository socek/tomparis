from tomparis.config import Field, FieldInstance, ValidatorError


class ValidateType:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, value):
        return isinstance(value, self.cls)


class StringField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(str)] + (validators or [])
        super().__init__(default, name, getter, validators)


class BoolField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(bool)] + (validators or [])
        super().__init__(default, name, getter, validators)


class IntField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(int)] + (validators or [])
        super().__init__(default, name, getter, validators)


class DictField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(dict)] + (validators or [])
        default = default or dict
        super().__init__(default, name, getter, validators)


class ValidatedList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validators = []

    def append(self, value):
        for validator in self._validators:
            if not validator(value):
                raise ValidatorError()

        super().append(value)


class ListFieldInstance(FieldInstance):
    def set(self, value):
        for element in value:
            for validator in self.validators:
                if not validator(element):
                    raise ValidatorError()
        self.value = value


class ListField(Field):
    def __init__(self, type_=None, name=None, getter=None, validators=None):
        validators = validators or []
        if type_:
            validators.append(ValidateType(type_))
        value = ValidatedList()
        value.validators = validators
        super().__init__(lambda instance: value, name, getter, validators)

    def __call__(self, instance, fieldname):
        return ListFieldInstance(
            instance, self.name or fieldname, self.default, self.getter, self.validators
        )


class ModelField(Field):
    def __init__(self, cls, name=None, getter=None, validators=None):
        validators = validators or []
        validators.append(ValidateType(cls))
        super().__init__(cls, name, getter, validators)
