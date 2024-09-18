# automate-the-boring-stuff
Source code made based on book [Automate the boring stuff with Python](https://automatetheboringstuff.com/)


## Random notes
- When a variable is created on a for loop statment that variable can be used outside the loop. \
  Look at guessTheNumber.py program for an example of it being used.

- Some of the if statements in these examples are kind of weird and with a few extra checks that I for now don't see the reason for it. \
  Looking at rpsGame.py has checks for all the possibilities for losing. \
  I would have though that if the you have checked of ties and all the winning scenraios the only other possibility would be a loss, so a single else should suffice. \
  I'm guessing the book does this so its easier for the new person to understand what is happening while also giving a some practice of typing if statements?

- "You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam." \
  This sounds like a nightmare waiting to happen. \
  Some more details on how exacly this works can be found on the "Local and Global Variables with the Same Name" section and localGlobalSameName.py program. \
  Also important to note that "local scope" by default only reads global variables, however that can be changed using the "global" statement. \
  Looking at the sameNameError.py exercise, that would be something that I would first expect the it to use the global variable and then create a local one with the same name. \
  I guess I just need to be a bit more carefull with local and globals scopes.

- This didn't click to me until now but you can turn something single value into a list by encapsulating the value in square brakets. \
  ```py
  [variable1]
  ```
  Is the list equivalent of:
  ```py
  int(variable1)
  ```