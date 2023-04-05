# 0x09. Python - Everything is object
![Cat image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)
## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

![Batman gif](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)
This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours.**

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.

## Resources
**Read or watch:**
- [9.10. Objects and values](https://intranet.alxswe.com/rltoken/MrtBogRzYETxnSKG97E7Sg)
- [9.11. Aliasing](https://intranet.alxswe.com/rltoken/Ro-7kVXtmWyAeOXEw7RhSg)
- [Immutable vs mutable types](https://intranet.alxswe.com/rltoken/X1lEmkwQRWI3fP4W7bq_qw)
- [Mutation](https://intranet.alxswe.com/rltoken/HpKOdgDg6GIoBoG0UPOgPA) *(Only this chapter)*
- [9.12. Cloning lists](https://intranet.alxswe.com/rltoken/-Gi4PX4srBYFKpZ5Er6sqA)
- [Python tuples: immutable but potentially changing](https://intranet.alxswe.com/rltoken/NZIom4L-tS0HjpY_uEVr9A)

### General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

### `.txt` Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Tasks
### 0. Who am I?
- `0-answer.txt` - a function used to print the type of an object.
### 1. Where are you?
- `1-answer.txt` - function used to get the variable identifier (which is the memory address in the CPython implementation).
### 2. Right count
- `2-answer.txt`
### 3. Right count =
- `3-answer.txt`
### 4. Right count =
- `4-answer.txt`
### 5. Right count =+
- `5-answer.txt`
### 6. Is equal
- `6-answer.txt`
### 7. Is the same
- `7-answer.txt`
### 8. Is really equal
- `8-answer.txt`
### 9. Is really the same
- `9-answer.txt`
### 10. And with a list, is it equal
- `10-answer.txt`
### 11. And with a list, is it the same
- `11-answer.txt`
### 12. And with a list, is it really equal
- `12-answer.txt`
### 13. And with a list, is it really the same
- `13-answer.txt`
### 14. List append
- `14-answer.txt`
### 15. List add
- `15-answer.txt`
### 16. Integer incrementation
- `16-answer.txt`
### 17. List incrementation
- `17-answer.txt`
### 18. List assignation
- `18-answer.txt`
### 19. Copy a list object
- `19-copy_list.py` - a function `def copy_list(l):` that returns a **copy** of a list.
### 20. Tuple or not?
- `20-answer.txt`
### 21. Tuple or not?
- `21-answer.txt`
### 22. Tuple or not?
- `22-answer.txt`
### 23. Tuple or not?
- `23-answer.txt`
### 24. Who I am?
- `24-answer.txt`
### 25. Tuple or not
- `25-answer.txt`
### 26. Empty is not empty
- `26-answer.txt`
### 27. Still the same?
- `27-answer.txt`
### 28. Same or not?
- `28-answer.txt`
### 29. #pythonic
- `100-magic_string.py` - a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code).
### 30. Low memory cost
- `101-locked_class.py` -  a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.
### 31. int 1/3
- `103-line1.txt` and `103-line2.txt` - number of int objects.
### 32. int 2/3
- `104-line1.txt`, `104-line2.txt`, `104-line3.txt`, `104-line4.txt`, and `104-line5.txt` - number of int objects.
### 33. int 3/3
- `105-line1.txt` - Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS`
