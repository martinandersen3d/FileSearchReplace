

from dataclasses import replace
import os
from pathlib import Path

files = [
    "C:\Github\Python\FileSearchReplace\TestFiles\CreateHelloWorldController.txt",
    "C:\Github\Python\FileSearchReplace\TestFiles\Subdir\HelloWorldAPI.txt",
]

searchWord="HelloWorld"
ReplaceWords=[
    "Product",
    "Order",
    "ProductOrder",
    "User",
]

def slash():
    if ostype() == 'linux':
        return '/'
    if ostype() == 'win32':
        return '\\'
       
def ostype():
    import sys
    if sys.platform.startswith('linux'):
        # Linux specific procedures
        return 'linux'
    if sys.platform.startswith('darwin'):
        # MacOs specific procedures
        return 'darwin'
    if sys.platform.startswith('win32'):
        # Windows specific procedures
        return 'win32'


def createNewFile(oldPath, NewPath, oldWord,newWord):

    file_name = Path(oldPath)
    if file_name.exists():
        try:

            file = open(oldPath, "r")
            content = file.read()
            content = content.replace(oldWord, newWord)
            
            file2 = open(NewPath,"w") 
            file2.write(content)

        except Exception as e:
            print("[ERROR]:",e)
        finally:
            file.close()    
            file2.close()     
    else:
        print(f"[ERROR - File does not exist]: {oldPath}") 

for path in files:
    oldPath = path
    dirname = os.path.dirname(path)
    #basename with extension
    basename = os.path.basename(path)
    print(dirname, basename)
    for word in ReplaceWords:
        newFilbaseename = basename.replace(searchWord, word)
        newFilePath = f"{dirname}{slash()}{newFilbaseename}"
        print(newFilePath)
        createNewFile(oldPath, newFilePath, searchWord, word)
