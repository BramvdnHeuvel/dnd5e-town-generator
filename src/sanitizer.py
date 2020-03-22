from gen.village.neighbourhood_amount import NEIGHBOURHOOD_SIZE_TO_RANGE

NEIGHBOURHOODS = NEIGHBOURHOOD_SIZE_TO_RANGE.keys()

def correct_size(size):
    return size in NEIGHBOURHOODS