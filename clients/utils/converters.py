import shortuuid
import uuid


class SID2UUIDConverter:

    def to_python(self, value):
        return shortuuid.decode(value)

    def to_url(self, value):
        return shortuuid.encode(value)
