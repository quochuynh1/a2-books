[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hO_xRIac)
# CP1404 Assignment 2: Books To Read 2.0 by Quoc Huynh

Assignment details: Books To Read 2.0 is a Kivy-based GUI application for keeping track of a reading list. The program demonstrates the use of object-orientated programming 
and allows users to add new books, sort by multiple attributes, track completed/unread books, and view live page counts. Data is loaded and saved in "books.JSON" which is stored 
as a list of dictionaries. The program utilises the previously written classes of Book and BookCollection.

> The project reflection is complete and describes development and learning well, shows careful thought, highlights
> insights made during code development.

## 1. How many hours did you spend working on this assignment 2 project?

Altogether, I spent approximately 16-17 hours on this assignment. This included writing and testing the classes, refactoring a1_classes,
building and refining the GUI, and implementing the functionality to the GUI. 

## 2. What are you most satisfied with?

I'm most satisfied with how modular my assignment 1 was. It meant that when it came time for me to refactor a1_classes to implement the classes
I had written, it was very intuitive and didn't take long at all. Additionally, I'm happy with how clean and functional the final application 
feels. 

## 3. What are you least satisfied with?

I am least satisfied with the time it took to fully understand the sorting functionality. It definitely took a while for me to wrap my head around the dictionary
that maps GUI spinner to the keys that correspond to the Book object attributes. I also think I could have written more extensive automated tests earlier so that I 
would do less debugging while implementing classes. 

## 4. What worked well in your development process?

I think that I did a particularly good job of incremental development as well as my use of version control, commiting regularly to document each small "milestone". With regard
to the incremental development, I began with creating the two classes, testing them, then proceeded to implement them into a1_classes. It was only after I had verified that every
worked as intended that I allowed myself to proceed to the GUI program. Of which, I began by creating a skeleton BoxLayout in kivy to kind of get a sense/plan out where everything 
should be. Then I essentially followed the order that the demo video showed of the functionality and built the program from the ground up. 

## 5. What about your process could be improved the next time you do a project like this?

Next time, I should write more comprehensive tests for the classes using assert rather than just printing an expected output and then the actual output. Even though almost everything
worked properly, it would allow for extra piece of mind when it comes time to actually implement the classes. 

## 6. Describe what learning resources you used and how you used them.

I used several resources including my past practical work from the cp1404practicals, example code from lecture recordings, as well as the styles guide. The Kivy demos in the lecture 
recordings helped me plan out the BoxLayout for the GUI. Past practical work helped me write and implement classes while the styles guide helped me to properly structure code. 

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The biggest challenge for me was understanding dictionaries. As previously mentioned, it took me quite some time to understand how the dictionary that maps GUI spinner to the keys that 
correspond to the Book object attributes. I overcame this by looking back on previous practical work as well as lecture recordings as I believe I never fully grasped how dictionaries are unpacked
and mapped. An additional challenge I faces was with validation and error handling. I overcame this by separating the logic into a dedicated function (get_valid_text_fields()), to better follow the 
SRP which made testing and debugging much easier. 
