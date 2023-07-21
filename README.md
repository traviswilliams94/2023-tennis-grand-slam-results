## Description

Welcome to the 2023 Tennis Grand Slam Results Library! Birthed from the fact that I have to do a python project for Flatiron School and we are also in the second week of Wimbledon.

With this app you can:

1. Search a player's name and get a list of their results for each of this year's Grand Slam Tournaments. (US Open will be added after the tournament occurs)

2. Search by Tournament name and see the players who reached the semi finals and beyond

3. Search by tournament result (First Round, Semis, Winner, etc) and see the  player(s) that have that result each tournament

4. Add a Tournament to the database

5. Add a Player to the database

6. Add a Result to the database

7. Update a player's ranking

8. View all players or tournaments

Players included are the men and women ranked 1-20 in the world as of July 17,2023. A couple extras because some dark horses did quite well on the women's side

Men:

1. Carlos Alcaraz
2. Novak Djokovic
3. Daniil Medvedev
4. Casper Ruud
5. Stafanos Tsitsipas
6. Holger Rune
7. Andrey Rublev
8. Jannik Sinner
9. Taylor Fritz
10. Frances Tiafoe
11. Karen Khachanov
12. Felix Auger-Aliassime
13. Cameron Norrie
14. Tommy Paul
15. Borna Coric
16. Lorenzo Musetti
17. Hubert Hurkacz
18. Alex De Minaur
19. Alexander Zverev
20. Francisco Cerundolo

Women:

1. Iga Swiatek
2. Aryna Sabalenka
3. Elena Rybakina
4. Jessica Pegula
5. Caroline Garcia
6. Ons Jabeur
7. Coco Gauff
8. Petra Kvitova
9. Maria Sakkari
10. Marketa Vondrousova
11. Daria Kasatkina
12. Barbora Krejcikova
13. Beatriz Haddad Maia
14. Veronika Kudermetova
15. Belinda Bencic
16. Madison Keys
17. Liudmila Samsonova
18. Karolina Muchova
19. Victoria Azarenka
20. Jelena Ostapenko

Extras:
Elina Svitolina - Wimbledon Semis
Magda Linnete - Aus Open Semis



## Database Schema

We have 3 databases:

player.py - contains player name, ranking at the time this was created, and gender

tournament.py - contains simply the tournament name

results.py - associating the best players and the result they achieved at each tournament

## Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

Here's what all of these things have in common (if done well): a number of
`import` statements (usually _a lot_ of import statements), an `if __name__ ==
"__main__"` block, and a number of function calls inside of that block. These
functions should be kept in other modules (ideally not _just_ `helpers.py`)

There will likely be some `print()` statements in your CLI script to let the
user know what's going on, but most of these can be placed in functions in
other modules that are grouped with others that carry out similar tasks. You'll
see some variable definitions, object initializations, and control flow
operators (especially `if/else` blocks and `while` loops) as well. When your
project is done, your `cli.py` file might look like this:

```py
from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5, function_6,
    function_7, function_8,
    function_9, function_10
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    function_9(z)
    function_10(x, y, z)
    print('Thanks for using my CLI')

```

***

