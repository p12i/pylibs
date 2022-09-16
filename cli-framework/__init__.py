#!/usr/bin/env python
# (C) 2015, Pawel Michalski, <pawel@michalski.it>

# xv is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# xv is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with xv.  If not, see <http://www.gnu.org/licenses/>.

#######################################################

__author__ = 'Pawel Michalski'
__version__ = '0.0.1'

import os
import sys
import argparse


def run():
    prog = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(
        prog=prog, description='Pomocnik dystrybutora')

    # Dodaje dostepne akcje
    # ActionCommit(parser)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    run()
