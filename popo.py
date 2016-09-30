class BaseField(object):

    def __get__(self, obj, objtype=None):
        raise NotImplementedError()

    def __set__(self, obj, value):
        raise NotImplementedError()

    def validate(self, value):
        return True


class Field(BaseField):
    def __init__(self, field_type=object):
        self.field_type  = field_type

    @property
    def var_name(self):
        return '__{}'.format(id(self))

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if hasattr(obj, self.var_name):
            return getattr(obj, self.var_name)
        return None

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.var_name, value)

    def validate(self, value):
        if not isinstance(value, self.field_type):
            raise ValueError('Expected type {}, but get {}'.format(self.field_type, type(value)))


class Popo(object):

    def __init__(self, **kwargs):
        field_names = self.get_field_names()
        for name, value in kwargs.items():
            if name not in field_names:
                raise ValueError('Can not  find property with name: "{}"'.format(name))
            setattr(self, name, value)

    def get_field_names(self):
        cls = type(self)
        return [name for name in dir(cls) if isinstance(getattr(cls, name), BaseField)]

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        for field in self.get_field_names():
            if not(getattr(self, field) == getattr(other, field)):
                return False
        return True

    def __ne__(self, other):
        return not(self.__eq__(other))

    def to_dict(self):
        def get_value(obj, key):
            val = getattr(obj, key)
            try:
                return val.to_dict()
            except AttributeError:
                return val

        return {
            key: get_value(self, key)
            for key in self.get_field_names()
            }

    def __repr__(self):
        return str(self.to_dict())
