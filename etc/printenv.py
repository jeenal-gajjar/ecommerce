"""
This module print command to set environment
variables on local system or elastic beanstalk.
"""

import argparse


def main(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        new_lines = list()
        for l in lines:
            l = l.strip('\n')
            if l:
                new_lines.append(l)
        print('\nHit below command to set environment variables locally:\n')
        print('export ' + ' '.join(new_lines) + '\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",
                        required=True,
                        type=str,
                        help="[local.env|dev.env|production.dev]")
    args = parser.parse_args()
    main(args.filename)