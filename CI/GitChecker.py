#encoding utf8

import os
import re

ExecPath = os.getcwd()
CmdGetCommitIDPath = os.path.join(ExecPath, "GetCommitID.cmd")
CmdUpdateSourcePath = os.path.join(ExecPath, "UpdateSource.cmd")

class GitChecker():
    
    def __init__(self, srcPath):
        self.SrcPath = srcPath

    

    def IsUpdated(self):
        currentCommitId = self.GetCommitId()
        self.GitUpdate()
        newCommitId = self.GetCommitId()
        if currentCommitId != newCommitId:
            return True
 

    def GetCommitId(self):
        commitInfo = os.popen(CmdGetCommitIDPath).read()
        matches = re.findall("(?<=commit )[0-9a-z]*", commitInfo)
        return matches[0]

    def GitUpdate(self):
        updateInfo = os.popen(CmdUpdateSourcePath).read()
        print(updateInfo)


if __name__ == "__main__":
    gc = GitChecker("D:\Dev\Src\spiderT")
    print(gc.IsUpdated())