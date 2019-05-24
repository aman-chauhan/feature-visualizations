import os


def make_directories():
    if not os.path.exists('docs'):
        os.mkdir('docs')

    if not os.path.exists('bin'):
        os.mkdir('bin')

    if not os.path.exists(os.path.join('bin', 'shapes')):
        os.mkdir(os.path.join('bin', 'shapes'))


if __name__=='__main__':
    make_directories()
