'''  os.system('cls)

The basic operators in python are the
Arithmetic operators;
+ Addition
- Subtraction
* Multiplication
/ Division
% Mod (the remainder after dividing)
** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
// Divides and rounds down to the nearest integer

Assignment operators;
= Assigns value to variable
+= Increment variable by value
-= Decrement variable by value

Comparison operator;
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
== Equal to
!= Not equal to

Logical operators;
and  Evaluates if both side are true
or   Evaluates if at least one side it true
not  Inverse a boolean type



Basic data types are;
int     Numeric integers 
float   Numeric floating point numbers 
string  For text 
bool    True or False



Data Structures;
List      {Ordered,     Mutable (Changeable),     Allows Duplicates}
Tuple     {Ordered,     Immutable (Unchangeable), Allows Duplicates}
Set       {Not Ordered, Mutable (Changeable),     Unique values}
Dictionay {Not Ordered, Keys(Immutable)-Values(Mutable), Keys(Unique)-Values(Allows duplicates)}



Control Flow;
For vs. While loop
For loop    ->   Best when the number of iterations is known
While loop  ->   Iterates until a condition is met

Zip
zip returns an iterator that combines multiple iterables into one sequence 
of tuples. Each tuple contains the elements in that position from all the 
iterables.

list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)]


Enumerate
enumerate is a built in function that returns an iterator of tuples 
containing indices and values of a list.


List comprehension
List comprehensions allow us to create a list using a for loop in one step.
Using condition:
[x**2 for x in range(9) if x % 2 == 0]
With else:
[x**2 if x % 2 == 0 else x + 3 for x in range(9)]
'''


