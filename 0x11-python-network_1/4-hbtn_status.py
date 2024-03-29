#!/usr/bin/python3
""" What's my Status using requests module """

import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {r.text}')
