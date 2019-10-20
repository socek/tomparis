class ValidatorError(Exception):
    def __init__(self, validator, value):
        self.validator = validator
        self.value = value

    def __str__(self):
        return f"[{self.validator}] bad value: {self.value}"


class Field:
    def __init__(self, default=None, name=None, getter=None, validators=None):
        self.name = name
        self.default = default
        self.getter = getter
        self.validators = validators or []

    def __call__(self, instance, fieldname):
        return FieldInstance(
            instance, self.name or fieldname, self.default, self.getter, self.validators
        )


class FieldInstance:
    def __init__(self, instance, name, default, getter, validators=[]):
        self.name = name
        self.value = self._get_default(default, instance)
        self.getter = getter
        self.validators = validators

    def _get_default(self, default, instance):
        if default:
            try:
                if issubclass(default, (Model, dict, list)):
                    return default()
                else:
                    return default(instance)
            except TypeError:
                return default(instance)
        else:
            return None

    def get(self, instance=None):
        if self.getter:
            return self.getter(self.value)
        else:
            return self.value

    def set(self, value):
        for validator in self.validators:
            if not validator(value):
                raise ValidatorError(validator, value)
        self.value = value


class Model:
    def __init__(self):
        self.chart = None
        self.fields = {}
        for attrname in dir(self):
            try:
                attr = getattr(self, attrname)
                if isinstance(attr, Field):
                    self.fields[attrname] = attr(self, attrname)
            except AttributeError:
                pass

    def __setattr__(self, key, value):
        if key in ("chart", "fields"):
            return super().__setattr__(key, value)
        elif key in self.fields:
            self.fields[key].set(value)
        else:
            raise RuntimeError(
                f"Name '{key}' is not valid in this scope: {self.__class__.__name__}"
            )

    def __getattribute__(self, name):
        if name == "fields":
            return super().__getattribute__(name)
        elif name in self.fields:
            return self.fields[name].get(self)
        else:
            return super().__getattribute__(name)

    @property
    def settings(self):
        return self.chart.settings

    def set_chart(self, chart):
        self.chart = chart

    def serialize(self, chart=None):
        if chart:
            self.set_chart(chart)
        self.prepare()

        data = {}
        for field in self.fields.values():
            value = field.get()
            if isinstance(value, Model):
                value = value.serialize(self.chart)
            elif isinstance(value, list):
                value = [
                    item.serialize(self.chart) if isinstance(item, Model) else item
                    for item in value
                ]
            elif isinstance(value, dict):
                value = {
                    key: item.serialize(self.chart)
                    if isinstance(item, Model)
                    else item
                    for key, item in value.items()
                }
            if value or value is False:
                data[field.name] = value
        return data

    def prepare(self):
        pass
