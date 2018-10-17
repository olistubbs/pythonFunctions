#!/usr/bin/env python3.6

# This is to be used when the total size of a directory is larger than 25G (The limit of a single layer Bluray)

import pycdlib

def addToOutIsos():
    """Use chunks() to split the list of files in the outdir into 'equal' length elements based on the amount of out isos created"""
    outCountIsos = calculateOutDisks()
    outPath = archiveOutput + 'out/'
    outFiles = os.listdir(outPath)
    splitOut = math.ceil(len(outFiles) / int(outCountIsos))
    isosWritten = 1
    outFullList = list(chunks(os.listdir(archiveOutput + 'out/'), int(splitOut)))
    outFullListCount = 0
    while isosWritten <= outCountIsos:
         iso = pycdlib.PyCdlib()
         iso.open(archiveOutput + 'isos/disk' + str(isosWritten) + '.iso')
         for a in outFullList[int(outFullListCount)]:
             fullPath = archiveOutput + "out/" + a
             isoPath = "/OUT/" + a.replace('-', '').upper()
             udfPath = "/out/" + a
             print("Adding " + a + " to " + archiveOutput + 'isos/disk' + str(isosWritten) + '.iso')
             iso.add_file(fullPath, isoPath, udf_path=udfPath)
         print("Writing " + archiveOutput + 'isos/disk' + str(isosWritten) + '.iso')
         iso.write(archiveOutput + 'isos/disk' + str(isosWritten) + '.iso')
         iso.close()
         outFullListCount += 1
         isosWritten += 1
    return
