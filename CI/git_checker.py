# encoding utf8

import os
import re

ExecPath = os.getcwd()
CommitIDPath = os.path.join(ExecPath, ".commit")
CmdGetCommitIDPath = os.path.join(ExecPath, "GetCommitID.bat")
CmdUpdateSourcePath = os.path.join(ExecPath, "UpdateSource.bat")


def check_updated():
    if os.path.exists(CommitIDPath):
        os.remove(CommitIDPath)
    current_commit_id = get_commit_id()
    git_update()
    new_commit_id = get_commit_id()
    if current_commit_id != new_commit_id:
        with open(CommitIDPath, "w") as f:
            f.writelines(newCommitId)


def get_commit_id():
    commit_info = os.popen(CmdGetCommitIDPath).read()
    matches = re.findall("(?<=commit )[0-9a-z]*", commit_info)
    return matches[0]


def git_update():
    update_info = os.popen(CmdUpdateSourcePath).read()
    print(update_info)


check_updated()

if __name__ == "__main__":
    check_updated()
