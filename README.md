
#  SpiceScript

  

Spicescript is a stack-based esoteric programming language designed to emulate the lyrical style of the artist "Ice Spice." Just like Ice Spice is revolutionizing the rap game, this project is intended to revolutionize the world of esoteric programming languages. The language is inspired by RPN and Forth, meaning that most operations occur as postfix. Functionally, all of the operations occur on a stack. 

The goal of SpiceScript is not to write functional code, but rather to write code that closely resembles Ice Spice lyrics. "IceSpythonic", if you will.

 But it is possible to write functional code, as it is nearly Turing-Complete. Here's an example of functional and running code in IceScript:
```
you_thought_i_was_feelin_u?

dat boys_a_liar like
she in_ha_mood like

oh, she in_ha_mood ( damn )
lose already chose like damn ( grah )

boy [] like
boy anteater he eat_it_for_lunch ( grah )
```
  

![Ice Spice Logo](https://i.imgur.com/C8Q8RxT.jpg)
## Features
- Dynamic typing
- Interpreted language
- Open source
- Fun to read
- Whitespace-agnostic
- Dynamic memory allocation
- Ice Spice syntax
## Installation 
To use this language, extract the contents from the file after using this command in your terminal.
```
git clone https://github.com/luigimagdamit/spicescript.git
```
## Usage
Modify the contents of ``test.mood`` using the syntax provided below. After making said adjustments, go ahead and run ``Parser.py``
##  Syntax

  

The syntax of Spicescript is designed with phrases commonly seen in Ice Spice's songs.

  

- Note:  Parentheses are used to group expressions together, but they don't actually do anything. Just use it for style.


## Mandatory File Header
Files are in the extension `.mood` and must have ``you_thought_i_was_feelin_u?`` in the first line, other wise the file will not run.
```
you_thought_i_was_feelin_u?

hello! ( grah )
```
##  Variable Declaration
Use the keyword ``like`` to declare a variable. Here is an example. Variables must either be integer numbers or strings without white space, because Ice Spice concise. 
```
foo 10 like
bar orange like
```
##  String Concatenation
Use the keyword ``hold_on`` to combine strings:
```
greeting 
	hello world! hold_on 
like
```
## Printing
Use the keyword ``grah`` to print.
```
greeting 
	hello world? hold_on 
like 

greeting ( grah )
```
##  Boolean Variables
Booleans take the form of either ``in_ha_mood`` for ``True`` or ``boys_a_liar`` for ``False``
```
john boys_a_liar like # variable with a false value
jose in_ha_mood like # variable with a true value
```
##  Boolean Equality Operator
The `damn` keyword is used to indicate frustration or disappointment. It is also used as a boolean comparison operator similar to ``==``.
Use the word ``damn`` to compare to boolean variables, and the result will be placed on the stack.
```
she in_ha_mood like 
# sets she = in_ha_mood

god in_ha_mood like 
# sets god = in_ha_mood

bad boys_a_liar like 
# sets bad = boys_a_liar

she in_ha_mood ( damn )
# compares "she" and in_ha_mood and returns in_ha_mood

the boys_a_liar god damn like ( grah )
# sets a variable named "the" to the result of comparing "boys_a_liar" to god and prints the resulting variable
```
## Conditionals
Conditionals will start with a boolean followed by the keyword ``then`` with the statement following, and ending with ``duhduhduh``
```
# does not execute
boys_a_liar then 
	hello! ( grah )
duhduhduh 

# executes and prints hello world
in_ha_mood then 
	hello world hold_on ( grah )
duhduhduh
```
## Arrays
You can declare an array in the following fashion:
```
top_songs [] like 
# must always start off this way, initalizing

top_songs song1 eat_it_for_lunch 
# eat_it_for_lunch appends to list

top_songs 0 grab grah 
# prints the item at index

top_songs 0 munch 
# munch will remove a variable at the index
```

## Loops
This language has functionality with simple finite loops in the form of ``hit_wonder`` with the range preceding, the expression following and ``duhduhduh`` denoting the end of the repeating expression.
```
you_thought_i_was_feelin_u?

0 10 hit_wonder 
	yuh! ( grah )
duhduhduh

baddies [] like
0 10 hit_wonder 
	baddies me eat_it_for_lunch 
duhduhduh

baddies ( grah )
```

### Loop Incrementing Examples
```
you_thought_i_was_feelin_u?

count 0 like
0 10 hit_wonder 
    count ( count 1 + ) like 
    count ( grah )
duhduhduh
```

```
you_thought_i_was_feelin_u?

count 0 like
baddies [] like

0 10 hit_wonder 
    count ( count 1 + ) like 
    i count 1 - like
    i grah
    baddies i eat_it_for_lunch
duhduhduh

baddies ( grah )
count 0 like

\n ( grah )

0 10 hit_wonder 
    baddies 0 munch
duhduhduh

baddies grah
```

## Full Example
Here is an example program in the Ice Spice programming language. Also note that the program file requires the header ``you_thought_i_was_feelin_u?``or else it will not run.

  

Without annotation:

```

you_thought_i_was_feelin_u?

  

soni hello world hold_on

like

soni in_ha_mood like

( soni that boys_a_liar ) damn

then anthony in_ha_mood like a duhduhduh

( soni grah )

```

With annotation:

```

you_thought_i_was_feelin_u?

### mandatory header

  

soni hello world hold_on

### concat hello, world

  

like

### store it in `soni` variable

  

soni in_ha_mood like

### change `soni` value to in_ha_mood

  

( soni that boys_a_liar ) damn

### compare in_ha_mood to boys_a_liar

### damn is a boolean == operator

  

then anthony in_ha_mood like a duhduhduh

### then takes the boolean evaluation

### and conditionally runs the code until duhduhduh

  

( soni grah )

### print the value of `soni`

```

  
  

##  Conclusion

  

stan ice spice
