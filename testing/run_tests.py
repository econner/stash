import os
import sys

import nose

os.environ['trail_testing'] = 'True'

# ensure app initailization completes
from app import app


if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    nose.main(argv=sys.argv, defaultTest='tests')
