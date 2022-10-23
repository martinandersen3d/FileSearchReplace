# Goal
The purpose is to have a file structure with a sample files.
This script can be used to create multiple files from the sample files, where a given word is replaced in both the new file name, but also inside the new files.

Script will
- Search Replace in files
- Create new files from 


## Example

You have a file in the following directory:

.\HelloWorldController.txt

With the content:

```
class HelloWorldController {

}
```

### Search
The search variable is the search word we will search for:

```python
searchWord="HelloWorld"
```

### Replace

In the top of the script there is a variable called ReplaceWords:

```python
ReplaceWords=[
    "Product",
    "Order",
    "ProductOrder",
    "User",
]
```

From these it will generete the files:

.\ProductController.txt
.\OrderController.txt
.\ProductOrderController.txt
.\UserController.txt


In all the files the word "HelloWorld" is replaced with the correct word