import uuid

import hashlib

def enc_pwd(pwd):
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode('utf-8'))
    return  sha256.hexdigest()

def create_unique_str():
    uuid_str = str(uuid.uuid4()).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()