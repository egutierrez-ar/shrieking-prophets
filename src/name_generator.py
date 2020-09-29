import re
from itertools import permutations

import requests

NAMES = ['Thijs', 'Enrique', 'Kalle', 'Job', 'Dominique']
N_PERM = 2


def wutang_name(seed: str) -> str:
    url = 'http://www.blazonry.com/name_generator/wuname.php'
    data = {'realname': seed}
    r = requests.post(url=url, data=data)
    # TODO: Add validations to regex capture
    capture = re.findall(r"you will also be known as <font size=\'\+2\'><b> (.+)\n(.+)", r.text)[0]
    wu_name = ''.join(capture)
    return wu_name


if __name__ == '__main__':
    for perm in permutations(NAMES, N_PERM):
        combined_name = ' '.join(perm)
        print(f"{wutang_name(seed=combined_name)}\t({combined_name})")
