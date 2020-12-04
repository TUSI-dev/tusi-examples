import argparse
import os
import subprocess
import sys
import sysconfig
import pathlib


def is_virtual_env() -> bool:
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
            os.getenv('CONDA_PREFIX'))

def is_msys2_env() -> bool:
    return (sysconfig.get_platform() == "mingw")

def check_msys64_installed() ->bool:
    return (os.path.exists(pathlib.Path.home().drive+"\msys64"))

def validatePythonVersion():
    versionInfo = sys.version_info
    if not (versionInfo.major >= 3 and versionInfo.minor >= 6):
        print('==============')
        print('Error: Python version is lower than 3.6')
        return False

    return True


def getTusiExamplerInstallationPath():
    tusiexamplePath = os.path.abspath(__file__)
    tusiexamplePath = os.path.dirname(tusiexamplePath)
    return os.path.expanduser(tusiexamplePath)


def setupTusiExample():
    # Install tusi-example with pip.
    try:
        # Get installation path automatically.
        tusiexamplePath = getTusiExamplerInstallationPath()

        if is_virtual_env():
            argv_fixed = [sys.executable, '-m', 'pip', '--disable-pip-version-check', 'install']
            argv = argv_fixed + ['-e', tusiexamplePath]
        else:
            if check_msys64_installed():
                if is_msys2_env():
                    argv =[pathlib.Path.home().drive+"\msys64\mingw64.exe"]
                else:
                    print("Not in msys2 python environment")
                    return False
            else:
                argv_fixed = [sys.executable, '-m', 'pip', '--disable-pip-version-check', 'install']
                argv = argv_fixed + ['--user', '-e', tusiexamplePath]

        try:
            subprocess.run(argv, check=True)
        except subprocess.CalledProcessError as error:
            if error.returncode:
                return False

    except Exception as ex:
        print(ex)
        return False

    return True


def install():
    print('############################################')
    print('Start setup tusi-example')

    # Validate python version.
    if not validatePythonVersion():
        return False

    if not setupTusiExample():
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
