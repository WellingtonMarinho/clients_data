import shortuuid
import uuid


class SID2UUIDConverter:
    """Django URL Converter - Convert a SID on the url to an UUID."""
    regex = '\w{22}'

    def to_python(self, value) -> uuid:
        return shortuuid.decode(value)

    def to_url(self, value) -> str:
        return shortuuid.encode(value)
