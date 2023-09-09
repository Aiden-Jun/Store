import sys
import os

currentDirPath = os.path.dirname(os.path.relpath(__file__))
rootPath = os.path.abspath(os.path.join(currentDirPath, '..'))
sys.path.append(rootPath)

from src.UI.Store import Store

if __name__ == "__main__":
    store = Store()
    store.start()