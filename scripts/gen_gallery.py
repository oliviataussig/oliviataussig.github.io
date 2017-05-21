#!/usr/bin/env python3
import os


def get_imgs():
    imgs = []
    for root, dirs, files in os.walk('img/still'):
        for f in files:
            imgs.append(f)
    return imgs


def main():
    imgs = get_imgs()
    f = open('still.md', 'w')

    f.write('---\n')
    f.write('layout: page\n')
    f.write('title: still\n')
    f.write('permalink: /still/\n')
    f.write('---\n')
    f.write('\n')

    for path in imgs:
        f.write('![{}](/img/still/{})\n\n'.format(path, path))

    f.close()

if __name__ == '__main__':
    main()
