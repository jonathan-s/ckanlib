try:
    from UserDict import UserDict
except:
    from collections import UserDict


class JsonObj(UserDict, object):

    def __init__(self, *args, **kwargs):
        super(JsonObj, self).__init__(*args, **kwargs)
        self.type = kwargs.get('_type', 'Package')
        if kwargs.get('_type') is not None:
            del self.data['_type']

    def __getattr__(self, name):
        if isinstance(self.data[name], dict):
            self.data[name] = JsonObj(self.data[name], _type=name.capitalize())
        elif isinstance(self.data[name], list) and len(self.data[name]) > 0:
            if isinstance(self.data[name][0], dict):
                self.data[name] = [JsonObj(obj, _type=name.capitalize())
                                   for obj in self.data[name]]

        return self.data[name]

    def __str__(self):
        return '<{type}: {container}>'.format(type=self.type,
                                              container=self.data)
