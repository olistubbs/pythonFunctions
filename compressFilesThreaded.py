#!/usr/bin/env python3.6

import tarfile
from multiprocessing.dummy import Pool as ThreadPool

def compressMonthFilesThreaded(date, filename, archiveDir):
    """Compress archive files for a specified month, But this time, it's setup for running in parallel"""
    filenameSplit = filename.split("/")
    dateFolder = filenameSplit[5]
    with tarfile.open(archiveOutput + archiveDir + '/' + dateFolder + '.tgz', 'w:gz') as tar:
        print("Adding %s to the archive" % filename)
        tar.add(filename, arcname=dateFolder)
    tar.close()
    return

for archiveDir in archiveDirs:
    pool = ThreadPool(4)
    dateGlob = sorted(glob.glob(archiveBaseDir + archiveDir + "/" + date + "-*"))
    # If your function only requires one argument don't use starmap, just map, and you don't need to zip()
    pool.starmap(compressMonthFilesThreaded, zip(itertools.repeat(date), dateGlob, itertools.repeat(archiveDir)))
    pool.close()
