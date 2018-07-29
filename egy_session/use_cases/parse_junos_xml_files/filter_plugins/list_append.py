class FilterModule(object):

    def list_append(self, l, *args):
        for item in args:
            l.append(item)
        return l

    def filters(self):
        return {'list_append': self.list_append}
