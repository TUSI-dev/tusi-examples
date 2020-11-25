import argparse
import os
import subprocess
import sys


def is_virtual_env() -> bool:
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
            os.getenv('CONDA_PREFIX'))


def validatePythonVersion():
    versionInfo = sys.version_info
    if not (versionInfo.major >= 3 and versionInfo.minor >= 6):
        print('==============')
        print('Error: Python version is lower than 3.6')
        return False

    return True


def getItasInstallationPath():
    itasPath = os.path.abspath(__file__)
    itasPath = os.path.dirname(itasPath)
    return os.path.expanduser(itasPath)


def setupItas():
    # Install tusi-example with pip.
    try:
        # Get installation path automatically.
        itasPath = getItasInstallationPath()

        argv_fixed = [sys.executable, '-m', 'pip', '--disable-pip-version-check', 'install']
        if is_virtual_env():
            argv = argv_fixed + ['-e', itasPath]
        else:
            argv = argv_fixed + ['--user', '-e', itasPath]

        try:
            subprocess.run(argv, check=True)
        except subprocess.CalledProcessError as error:
            if error.returncode:
                return False

    except Exception as ex:
        print(ex)
        return False

    return True


def install(args):
    print('############################################')
    print('Start setup tusi-example')

    # Validate python version.
    if not validatePythonVersion():
        return False

    if not setupItas():
        print('==============')
        print('Failed to setup tusi-example')
        return False

    # # call sparse checkout
    # if args.quiet:
    #     choice = 'n'
    # else:
    #     while True:
    #         print('Checkout for specific product categories? Please enter y/n:')
    #         choice = input().lower()
    #         if choice == 'y' or choice == 'n':
    #             break
    #
    # if choice == 'y':
    #     sc = SparseCheckout()
    #     if not sc.run():
    #         print('==============')
    #         print('Failed to checkout specific product categories')
    #         return False

    return True


if __name__ == '__main__':
    # Setup argument parser.
    parser = argparse.ArgumentParser(description='tusi-example installer')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='specify whether to run the install without user interaction.')
    args = parser.parse_args()

    if install(args):
        print('\nInstallation for tusi-example completed')
    else:
        print('\nInstallation for tusi-example terminated')
