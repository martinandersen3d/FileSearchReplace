

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

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])
       
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
            camelCaseOldWord = camel_case(oldWord)
            camelCaseNewWord = camel_case(newWord)
            content = content.replace(camelCaseOldWord, camelCaseNewWord)
            
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



	# 1. camelCase
    # 2. PascalCase
    # 3. snake_case
    # 4. kebab-case