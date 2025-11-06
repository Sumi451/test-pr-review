"""
Simple example file that intentionally includes lint and security issues.
- Flake8 should flag style issues (unused imports/variables, long lines, import formatting).
- Bandit should flag insecure uses (pickle.load, os.system / shell=True style usage, hardcoded password).

This file is safe as long as you DON'T execute it. It's provided for static analysis only.
"""

import os, sys, pickle


def insecure_function(data_path):
    # Hardcoded credential (Bandit: B105)
    secret = "s3cr3t_password"

    # Open file and use pickle (Bandit: unsafe deserialization)
    f = open(data_path,'rb')
    data = pickle.load(f)
    f.close()

    # Use os.system with user data - potential shell injection (Bandit: B602/B204)
    os.system("ls -la %s" % data_path)

    # intentionally long line to trigger flake8 E501
    print("This is a very long line that will exceed typical line-length limits set by flake8 to demonstrate a style warning from Flake8 tools.")

    return data


def helper():
    unused_var = 42
    return None
