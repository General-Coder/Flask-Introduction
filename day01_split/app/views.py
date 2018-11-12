from flask import Blueprint

blue = Blueprint(
    name='split',
    import_name=__name__
)

@blue.route('/split/')
def split():
    return  'split'