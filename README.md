# pokerhand
Poker hand evaluator

A software tool that can evaluate a poker hand.
User can submit 5 cards and receive an answer that tells them the highest rank that can be obtained using those 5 cards.

For example:
• Ace of Spades
• 10 of Clubs
• 10 of Hearts,
• 3 of Diamonds
• 3 of Spades
Should return Two pairs.


Source code:
```
'''

git clone https://github.com/bm33m/pokerhand.git

cd pokerhand

python manage.py runserver

Django version 3.0.5, using settings 'pokerhand.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

'''
```
Visit:
http://127.0.0.1:8000/

Testing123:

```
'''

$ python manage.py test pokerhandapp
randomCards: ['Ace of Diamonds', '7 of Clubs', '10 of Clubs', 'Jack of Hearts', '6 of Diamonds
'],
 results: High card
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 0.015s

OK
Destroying test database for alias 'default'...



'''
```


Enjoy.
