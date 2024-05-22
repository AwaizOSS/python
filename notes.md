# Notes

## interview questions

- python is an interpreted language
- byte code isnt machine code, its just for python(PVM I guess) not for the hardware
- data type is assigned to the value, not the variable as its just a reference to the value thats in memory => there's no data type in python but it is assigned in memory
- it has a garbage collector that treats numbers and strings a little differently than others. It delays their deletion in assumption of it being used again but this can be manipulated.
- 1<2<3 is 1<2 and 2<3, similarly for all the signs having this pattern
- i=iter(list)<br>
  i has the memory address of the first item in the list and will have it always, even when we are iterating and arent on the first item because it only needs first item's address. it goes to the further items via a mechanism

## everything is an object in python

- type()
- import os, sys, math, random, copy
- ps.getcwd() - cwd:current working directory
- sys.platform
- math.pi, math.floor(), math.trunc() - rounds off and gives whichever is closest to 0
- random.random(), random.randint(1,100), random.choice(list), random.shuffle(list)
- random.choice([1,2,3])
- copy.copy() copies only first level of values in the data type but copy.deepcopy() goes beyond
- from importlib import reload
- reload(filename) - reloads the file dynamically
- variables are also called attributes
- len(data_type)
- dir(") - gives all possible methods applicable
- m is n - gives if they're actually referencing to the same data in memory
- del for delete
- scope is also called namespaces

## data types

- string
  string[1:5] - gives letters from 1 till 4
- list=[] - mutable
- tuple=() - generally faster and more memory-efficient than lists because of their immutability
- dictionary = {}
- set=set() for empty set and for non-empty it is {} with just values not key-value pairs

## numbers

- its not a good practice to operate on diff types of numbers. Convert them into one type using the required methods such as int(), float(),...
- its also not a good practice to create confusion like y*z+3, instead we should use parenthesis like (y*z)+3 or y\*(z+3)
- multiple numbers when queried comes in a tuple as a result for ex: y,x will come as (2,3)
- oct(), hex(), bin(), int('value',2 or 8 or 16)
- from decimal import Decimal<br>
  Decimal('value') should be used of dealing with decimals. For more info we can look into decimal context manager
- similarly we have Fraction method from fraction library
- setone={1,2,3} then setone & {1,2} is for intersection. similarly we have | for union and more

## strings

- repr() provides a string representation suitable for debugging, str() provides a more user-friendly string representation, and print() is a function for outputting text or values to the console internally useing str() to get object and print it.
- for learning about slicing operations we can use the string '0123456789' and play with [: :], yes it can take a third parameter. this is actually not used in production
- we have upper(), lower(), strip(), replace("string1","string2"), find(), count('str'), "a" in "abc"
- chai="masala, lemon, mint" for converting into list strip(", ")
- string with variables<br>
  chai='lemon'<br>
  order='I want {} tea'<br>
  order.format(chai) will give I want lemon tea<br>
  more variables can be accomadated with commas in format
- " ".join(list) gives string with list elements joined
- d="i can use \"\" like this" and similarly for other characters that may create problems
- s=r"c:drive\nice" can be used which is raw string but s=r"c:drive\nice\" will give problems

## lists

- most of the string methods will work as they were considering as a list which means of course it'll work for lists
- list[1:2]='something' will cause trouble as the value is considered as array not a string so to get the proper op we need to use it like this list[1:2]=['something']. similarly we can replace multiple values this way
- if we do list[1:1]=['nice'] we'll insert it at 1 position and similarly we can get rid of element(s) by giving [] at thier place(s)
- append(), remove('string'), pop(), insert(1,'nice'), copy(), count()
- squared_nums = [x**2 for x in range(10)]

## dictionary

- get("key") returns nothing if there's no matching key whereas normal querying like dict['key'] will return an error
- pop(key), popitem()
- d['key']['key'] for nested dicts
- d={x:x\*\*2 for x in range(6)}
- clear()
- new_dict=dict.fromkeys(keys,default_value)

## tuple

- most of list methods works here
- (w,h,o)=tup

## confusions

- sys.getrefcount() doesnt give the actual reference count of variables
- mutable list<br>
  l1=[1,2,3]<br>
  l2=l1<br>
  l1=[1,2,3]<br>
  now if we change l1 it wont change l2 as it got the reference of a new list in memory
- similarly l1=[1,2,3]<br>
  l2=l1<br>
  but now if we change l1 it' ll also change l2
- l2=l1[:] - here we are making a copy of l1 via slicing operation, not just referencing l1
- setone - {1,2,3} is set() not {} as thats an empty dictionary
