import hashlib


def make_pkw(username, password):
    v = username[:5] + password
    md5 = hashlib.md5(v.encode()).hexdigest()
    return md5[2:]