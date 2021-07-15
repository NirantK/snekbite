"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]
    
"""
import sys
import docopt
from catalogue import importlib_metadata as metadata

normal_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

fancy_snek = """\
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
"""


def get_sneks():
    sneks = {}
    eps = metadata.entry_points()
    snek_types = eps["snek_types"]
    for ep in snek_types:
        sneks[ep.name] = ep.load()
    return sneks


def main():
    args = docopt.docopt(__doc__)
    snek_type = args["--type"] or "normal"
    print(get_sneks()[snek_type])


if __name__ == "__main__":
    main()
