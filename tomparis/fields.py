from tomparis.model import Field, FieldInstance, ValidatorError


class StringDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, str) and value is not None:
            raise TypeError(f"{value} is not string!")
        return super().__setitem__(key, value)


class ValidateType:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, value):
        return isinstance(value, self.cls) or value is None

    def __str__(self):
        return f"ValidateType:{self.cls.__name__}"


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


class PortField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(int), self._validate_port] + (validators or [])
        super().__init__(default, name, getter, validators)

    def _validate_port(self, value):
        return value >= 1 and value <= 65535


class DictField(Field):
    def __init__(self, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(StringDict)] + (validators or [])
        default = default or StringDict
        super().__init__(default, name, getter, validators)


class EnumField(Field):
    def __init__(self, enum, default=None, name=None, getter=None, validators=None):
        validators = [ValidateType(str), self._validate_is_in_enum] + (validators or [])
        default = default or dict
        super().__init__(default, name, getter, validators)
        self.enum = enum

    def _validate_is_in_enum(self, value):
        return value in self.enum


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
