# -*- coding: utf-8 -*-
import datetime
import re
import unicodedata
from decimal import Decimal
from unidecode import unidecode

import six


_PROTECTED_TYPES = six.integer_types + (
    type(None), float, Decimal, datetime.datetime, datetime.date, datetime.time,
)


def is_protected_type(obj):
    """Determine if the object instance is of a protected type.

    Objects of protected types are preserved as-is when passed to
    force_text(strings_only=True).
    """
    return isinstance(obj, _PROTECTED_TYPES)


def force_text(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_text, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    # Handle the common case first for performance reasons.
    if issubclass(type(s), six.text_type):
        return s
    if strings_only and is_protected_type(s):
        return s
    try:
        if not issubclass(type(s), six.string_types):
            if six.PY3:
                if isinstance(s, bytes):
                    s = six.text_type(s, encoding, errors)
                else:
                    s = six.text_type(s)
            elif hasattr(s, '__unicode__'):
                s = six.text_type(s)
            else:
                s = six.text_type(bytes(s), encoding, errors)
        else:
            # Note: We use .decode() here, instead of six.text_type(s, encoding,
            # errors), so that if s is a SafeBytes, it ends up being a
            # SafeText at the end.
            s = s.decode(encoding, errors)
    except UnicodeDecodeError as e:
        if not isinstance(s, Exception):
            raise
        else:
            # If we get to here, the caller has passed in an Exception
            # subclass populated with non-ASCII bytestring data without a
            # working unicode method. Try to handle this without raising a
            # further exception by individually forcing the exception args
            # to unicode.
            s = ' '.join(
                force_text(arg, encoding, strings_only, errors) for arg in s
            )
    return s


def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = force_text(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
        value = re.sub(r'[^\w\s-]', '', value, flags=re.U).strip().lower()
        return re.sub(r'[-\s]+', '-', value, flags=re.U)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


def refine_git_username(username):
    # can contain only letters, digits, '_', '-' and '.'.
    # Cannot start with '-' or end in '.', '.git' or '.atom'."
    username = slugify(unidecode(username))
    for ch in ('.', '-', ' '):
        username = username.replace(ch, '_')
    while username.startswith('_'):
        username = username[1:]
    while username.endswith('_'):
        username = username[:-1]
    if not username.isalnum():
        # просто скипуем все не нужное
        username = [c for c in username if c.isalnum() or c in ('_', )]
        username = ''.join(username)
    return username


"""
Теулова Юлиана	theulianna@gmail.com
Алексей Музыченко	muzychenko.aleksey@gmail.com
"""

if __name__ == '__main__':
    # TODO важно что бы фамилия шла первой!!!
    username = 'Музыченко Алексей'
    gitlab_username = refine_git_username(username)
    print(gitlab_username)
