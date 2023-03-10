#
# @author: Brian
#

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.conf import settings
from pokerhandapp.models import pokerCards, PokerHand
import pprint
import json
import datetime
import time
import random


def index(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/homeapp/cards/'
    map = ['Hearts', 'Spades', 'Diamonds', 'Clubs', 'playing52cards', 'categories']
    cards = pokerCards()
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    return render(
        request, 'home.html', context={'pname': pname, 'message': now,
        'cards': cards, 'app': app, 'ip': ip, 'year': year},
    )

def pokerTool(request):
    try:
        pname = settings.PRO_NAME
        ip = request.META['REMOTE_ADDR']
        now = mytime2()
        year = now.year
        cards = pokerCards()
        if request.method == 'POST':
            req = request.POST
            card01 = req['card01'].strip()
            card02 = req['card02'].strip()
            card03 = req['card03'].strip()
            card04 = req['card04'].strip()
            card05 = req['card05'].strip()
            cards = [card01, card02, card03, card04, card05]
            #print("Processing: %s"%(cards))
            now = [now, 'results: TodoList....']
            #
            poker = PokerHand(cards)
            results = poker.evaluate()
            #print('results: %s'%(results))
            #
            now = [now, 'results: %s'%(results)]
            return render(
                request, 'info.html', context={'pname': pname, 'message': now,
                'results': results,
                'cards': cards, 'ip': ip, 'year': year},
            )
    except Exception as e:
        print(e)
        now = [e,now]
    return render(
                request, 'info.html', context={'pname': pname, 'message': now,
                'cards': cards, 'ip': ip, 'year': year},
            )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    unow = make_aware(utcnow)
    dt = (dnow - unow)
    print("UTC:  %s,   %s, %s-%s"%(utcnow, dt, unow, unow.tzinfo))
    print("Home: %s-%s,       %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
