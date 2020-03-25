from gen.village.neighbourhood_amount import NEIGHBOURHOOD_SIZE_TO_RANGE
from flask import redirect, url_for
from functools import wraps

NEIGHBOURHOODS = NEIGHBOURHOOD_SIZE_TO_RANGE.keys()

def correct_size(size):
    return size in NEIGHBOURHOODS

def correct_size_only(func):
    @wraps(func)
    def exec_func(*args, **kwargs):
        if not correct_size(kwargs['size']):
            return redirect(url_for('town_menu'))
        return func(*args, **kwargs)
    return exec_func