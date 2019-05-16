import os

class fileFinder:
    def __init__(self):
        self.projectsFolder = "/Users/willtuff/Devprojects"
        self.workspaceList = []

    def findFiles(self):
        for root, dirs, files in os.walk(self.projectsFolder):
            for file in files:
                if file.endswith(".code-workspace"):
                    self.workspaceList.append(os.path.join(file))
                    self.workspaceList.append("\n")

    def printList(self):
        print(self.workspaceList)