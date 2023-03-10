#
# @author: Brian
#
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.timezone import make_aware
from django.conf import settings
from django.core import serializers
from pokerhandapp.models import pokerCards, PokerHand
import pprint
import json
import datetime
import time


def index(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    cards = pokerCards()
    now = mytime2()
    year = now.year
    pathTo = '/homeapp/cards/'
    map = ['playing52cards', 'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, ]
    app = {"map": "%s%s.jpg"%(pathTo, map[0]), "info": "%s %s"%(now, map[1])}
    return render(
        request, 'poker.html', context={'pname': pname, 'message': now,
        "app": app, 'ip': ip, 'year': year},
    )

def pokerhandTool(request):
    cards = []
    try:
        cards = pokerCards()
        if request.method == 'POST':
            req = request.POST
            try:
                req = json.loads(request.body.decode('utf-8'))
                print('body: %s'%(req))
            except Exception as e:
                print('pokerTool: %s'%(e))
            #print('POST = body: %s, req: %s, request: %s'%('body', req, request))
            card01 = req['card01'].strip()
            card02 = req['card02'].strip()
            card03 = req['card03'].strip()
            card04 = req['card04'].strip()
            card05 = req['card05'].strip()
            cards = [card01, card02, card03, card04, card05]
            print("Processing: %s"%(cards))
            #
            poker = PokerHand(cards)
            results = poker.evaluate()
            print('results: %s'%(results))
            #
            return JsonResponse(results, safe=False)
    except Exception as e:
        print('pokerTool: %s'%(e))
    return JsonResponse(cards, safe=False)

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    unow = make_aware(utcnow)
    dt = (dnow - unow)
    print("UTC:  %s,   %s, %s-%s"%(utcnow, dt, unow, unow.tzinfo))
    print("Home: %s-%s,       %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
