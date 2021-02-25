# Password Manager

---

## **About**

This is a **Password Manager GUI** made with Python (_Tkinter module and SQLite3_) that allows the user to:

> - _**Add**_ a password for a specific website
> - _**Delete**_ their passwords and associated website
> - _**Update**_ their passwords and associated website
> - _**Clear**_ the input data

---

## **Original Design**

![password m design](https://user-images.githubusercontent.com/57025422/108607809-808da100-7377-11eb-9a1a-e74770e46f16.PNG)

I decided to make a _design_ (**on Notability**) for the Password Manager before I dove right into the code. Although the final product looks different, this allowed me to visualize the _GUI_ while coding and streamlined the entire process!

---

## **The Result**

![password manager](https://user-images.githubusercontent.com/57025422/108784152-95a73300-7523-11eb-9365-b99c87d8275a.PNG)

I changed a bit of the layout from the original design, but the functionality is the same as I intended it to be.

### **Potential improvements:**

> - Display data in the listbox in a more _accurate_ manner. (it's hard to tell what is what)
> - Make design more symmetrical. (also, add more styling)
> - Add RegEx to authenticate passwords
> - Recognize and handle duplicate data

---

## **Here's a sneak peak!**

![Hnet-image](https://user-images.githubusercontent.com/57025422/108933178-8e555780-75ff-11eb-8650-3102df9e1523.gif)

---

## **Install**

```bash
pip install tk
```

---

## **Import**

```python
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import askquestion
from db import Database
```

---

## **Run**

```bash
python password_manager.py
```

---

### **Inspiration**

Brad Traversy's Part Manager. Watch the [video](https://www.youtube.com/watch?v=ELkaEpN29PU "Traversy Media") and check out his [repo](https://github.com/bradtraversy/part_manager "Part Manager").
