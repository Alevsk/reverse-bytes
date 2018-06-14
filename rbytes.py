#!/usr/bin/env python

"""
A simple python script for reverse the bytes of a file.

Author: Lenin Alevski Huerta Arias
Year: 2018

"""

from __future__ import print_function
import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('rb'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('wb'))

    args = parser.parse_args(arguments)
    args.outfile.write(args.infile.read()[::-1])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))