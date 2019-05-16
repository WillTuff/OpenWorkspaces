import filelist

def findNewFiles():
    newFiles = filelist.fileFinder()
    newFiles.findFiles()
    newFiles.printList()

print("Finding files...")
findNewFiles()
