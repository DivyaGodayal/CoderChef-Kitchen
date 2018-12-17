<p align="center">
<img src="../../Images/magic-dict.png" width="600">
</p>

---
### Solution 1: Using Location Hash

#### Motivation

The idea here springs from the question description itself. Essentially, we want to 
modify a character at a specific location and replace that character with some other (unknown)
character so that the resulting string appears in our dictionary. 

* Consider the following examples to understand the problem statement better. 

```
*************************** TEST CASE 1 ***************************
dict = ['hello', 'bad', 'sad', 'said']
word = 'hello'

NO. 
We can't modify any of the characters in 'hello' to any other character and have a resulting 
string from our given dictionary. Granted that the word 'hello' appears as is in the 
dictionary. But, we are required to modify EXACTLY one character and the resulting string 
should be in our dictionary

*************************** TEST CASE 2 ***************************
dict = ['bello', 'bad', 'sad']
word = 'hello'

YES
We can replace the 'h' with 'b' and get 'bello'

*************************** TEST CASE 3 ***************************

dict = ['bello', 'sad', 'bad']
word = 'helloooooooooo'

NO 
because this sting is too large and all our dictionary strings are smaller than this 
word. 

*************************** TEST CASE 4 ***************************

dict = ['bello', 'sad', 'bad']
word = 'bed'

YES
We can change the 'e' with an 'a' to get 'bad'
```

You should have a fairly decent idea now about the problem statement now with the help of the examples above. 
The idea here is very simple. We keep track of all the unique characters that can occur at individual 
indexes. So, for a dictionary with words
 
```
['bello', 'bad', 'sad'] we would have something like

location[0] = {'b', 's'}
location[1] = {'e', 'a'}
location[2] = {'l', 'd'}
location[3] = {'l'}
location[4] = {'o'}
```

#### Algorithm

1. Given a word to search in the dictionary, we iterate over it's characters one index at a time and for each index, we see what all character options are possible ***other*** than the one that's originally there. 

2. We try all the character options in a particulr index and form a new string for each of these options. If any of the new string is in our dictionary we are done. We do this for every location and all possible characters and check if a modified string exists in our dictionary or not. 

3. Of course, since we can have only 26 unique characters per index and we have to only make 1 modification, so in
all we can have `26*N` string that we might have to look up given that our word is composed of `N` characters. 
This is essentially an `O(N)` solution to searching the word. 

4. While storing a word in the dictionary, we will have to iterate over its characters to build out the location
based character set that we discussed above. So, adding a word takes `O(k)` considering there were `k` characters 
in our word and this `k` will vary from one word to another. 

#### Complexity Analysis

* Time Complexity: `O(N)` considering the size of the alphabet to be fixed for the question statement.
* Space Complexity: `O(N)` since we have to hash the words given to us for better lookup.

---
### Solution 1: Using Neighboring Strings

#### Motivation

It turns out, we can do a slight optimization to our previous algorithm and make it even better. Consider the following dictionary and a search word. 

```
dict = ['bello', 'helbo']
word = 'hello'
```

If we look at the words `bello` and `hello`, then the only difference is that of the first character. Remaining characters are the same. So, the answer for our word would be YES. We can change the `h` to `b` and get `bello`. 

The question however does not ask us what modification we should make to get a word in the dictionary.The question simply asks us to find if such a modification is possible at all or not. 

If you look at the structures of the two words, you will see this similar structure.

```
*ello
```

Similarly, for the dictionary word `helbo` and our search word `hello`, we will have the following similar structure.

```
hel*o
```
    
> What if, given a dictionary word, we can store all its possible structures in our dictionary. Instead of 
storing the actual word itself. So, for a given word we will have the following structures possible. 

```
dictionary word = hello

* e l l o
h * l l o
h e * l o
h e l * o
h e l l *

Number of structures = length of the string. 
```    

#### Algorithm

1. For every dictionary word, we will save its corresponding structures in our dictionary rather than the original word. 

2. When we have to search a given word, we will generate all of it's possible structures which will be `K` considering the string is of length `K`. 

3. We will see if any of the structures for our search word appears in our dictionary or not. 

This idea here is simpler as compared to the previous one because we are not asked to exactly find what modification we need to do. If that was the case, then the first solution would work and not this one. 

This solution is a bit slow, implementation wise because for a given string of length `K`, we have to generate
`K` new strings representing the different structures and that can be slow. But, the idea here resonates 
with the problem statement more than the previous one. 

#### Complexity Analysis

* Time Complexity: `O(NK)` is the time to preprocess the dictionary of words given to us. The dictionary contains `N` words and `K` represents the length of the longest string. Once the neighbor hash is constructed, searching for a modification is then `O(K)` since we have to form all the neigbors of the given word.
* Space Complexity: `O(NK)`

#### Link to OJ

https://leetcode.com/submissions/detail/158673389/

---
Article contributed by [Sachin](https://github.com/edorado93)
