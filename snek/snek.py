"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]
    
"""
import sys
import docopt

from snek_lib import get_sneks, snek_types, normal_snek, fancy_snek

# def get_sneks():
#     sneks = {}
#     eps = metadata.entry_points()
#     snek_types = eps["snek_types"]
#     for ep in snek_types:
#         sneks[ep.name] = ep.load()
#     return sneks

@snek_types.register("fancy")
def fancy():
    return fancy_snek

@snek_types.register("normal")
def normal():
    return normal_snek

# from cute_snek import cute_snek

# @snek_types.register("cute")
# def cute():
#     return cute_snek

def main():
    args = docopt.docopt(__doc__)
    snek_type = args["--type"] or "normal"
    print(get_sneks(snek_type))

if __name__ == "__main__":
    main()