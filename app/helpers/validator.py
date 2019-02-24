"""Validator message"""
import re
messages = {
    "required": "{} is required."
}


class Validate:
    @staticmethod
    def message(field, field_name):
        if not field:
            return ""
        return messages[field].format(field_name or field)

    @staticmethod
    def is_email(email):
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)
