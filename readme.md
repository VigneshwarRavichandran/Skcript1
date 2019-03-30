# Programming Logics

This the solution to the problem in the given url: https://gist.github.com/swaathi/3356d2d2a1476be21f6938b77d61f82d

## Installation
Programming Logic requires python3.

This install all the necessary dependancies:
```
$ pip install -r requirements.txt
```

This install the logic as python packages:
```
$ python setup.py install
$ python setup.py develop
```


## Get Started
The main class is logic which is located in the `skcript1/logic/__init__.py`
The cli commands were referred from click `https://click.palletsprojects.com/en/7.x/` and from your redmon repository `https://github.com/skcript/redmon`

#### To do magic

```
$ magic --string1 "edzlatsh" --string2 "hazel"
```
returns "True" for the above case.


```
$ magic --string1 "uwtaqicy" --string2 "watch"
```
returns "False" for the above case.


```
$ magic --string1 "d??????" --string2 "code"
```
returns "True" for the above case.


```
$ magic --string1 "g???" --string2 "code"
```
returns "False" for the above case.


#### To do longest

```
$ longest --string "uruqrnytrois" --filename enable1.txt
```
returns "turquois" for the above case.

```
$ longest --string "rryqeiaegicgeo??" --filename enable1.txt
```
returns "greengrocery" for the above case.

## Testing
The test file is located in the `skcript1/tests/test_logic.py`
The unit testing is done by nosetests `https://nose.readthedocs.io/en/latest/`. 

The function to test whether the string are alphabet
```
test_is_alpha(self)
````
The function to test : 

magic("edzlatsh", "hazel") -> true

magic("d??????", "code") -> true
```
test_example_1(self)
```
The function to test : 

magic("uwtaqicy", "watch") -> false

magic("g???", "code") -> false

```
test_example_2(self)
```