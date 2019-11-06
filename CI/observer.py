# encoding utf8

import subprocess
import os
import time

exec_path = os.path.join(os.getcwd(), "git_checker.py")

while True:
    try:
        print(exec_path)
        subprocess.check_output(["python.exe", exec_path], shell=False)
        time.sleep(600)
        print("next->")
    except subprocess.CalledProcessError as e:
        raise Exception("Could not update and check repository. " +
                        "Reason: %s" % e.output)
