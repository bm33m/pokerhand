#
# @author: Brian
#
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from django.conf import settings
#from homeapp.models import gisTablesHome, mapHome, maps
#from pokerhandtool.models import checkFile
from pokerhandapp.models import pokerCards
import pprint
import json
import datetime
import time


def index(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    map = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, ]
    cards = pokerCards()
    app = {"map": map[0], "info": "%s %s"%(now, map[1])}
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
            print("Processing: %s"%(cards))
            now = [now, 'results: TodoList....']
            return render(
                request, 'info.html', context={'pname': pname, 'message': now,
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
