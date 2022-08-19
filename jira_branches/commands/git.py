import os
import subprocess


def run(*args):
    os.system(*args)


def checkout(branch, create=False):
    run(f"git checkout -b '{branch}'") if create else run(f"git checkout '{branch}'")


def check_branch(branch):
    output = subprocess.run(["git", "rev-parse", "--verify", "--quiet", branch], capture_output=True, text=True).stdout
    return bool(output)
