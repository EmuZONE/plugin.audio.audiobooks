# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Zombie Survival Guide': [{'name': 'Wiedergabe starten',
                       'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/ZSG.jpg',
                       'video': 'https://archive.org/download/Zombie.Survival.Guide/Zombie.Survival.Guide.mp3',
                       'genre': 'Horror'}
                      ],
            'Alien': [{'name': 'Band 1: In den Schatten',
                      'thumb': 'https://archive.org/download/ALIEN-ABook/Alien_01.jpg',
                      'video': 'https://archive.org/download/ALIEN-ABook/ALIEN%20-%20In%20den%20Schatten%20-%20Teil%201%20-%20H%C3%B6rspiel.mp3',
                      'genre': 'Sience Fiction'},
                     {'name': 'Band 2: Fluss des Todes',
                      'thumb': 'https://archive.org/download/ALIEN-ABook/Alien_02.jpg',
                      'video': 'https://archive.org/download/ALIEN-ABook/ALIEN%20-%20Fluss%20des%20Todes%20-%20Teil%202%20-%20H%C3%B6rspiel%20zum%20Film.mp3',
                      'genre': 'Sience Fiction'}
                     ],
                     
            'Star Wars': [{'name': 'Band I - Erben des Imperiums',
                      'thumb': 'https://archive.org/download/StarWarsBK/SW_01.jpg',
                      'video': 'https://archive.org/download/StarWarsBK/Star%20Wars%20Erben%20des%20Imperiums%20H%C3%B6rbuch%20%28Band%201%29.mp3',
                      'genre': 'Wissenschaft'},
                     {'name': 'Band II - Die dunkle Seite der Macht',
                      'thumb': 'https://archive.org/download/StarWarsBK/SW_02.jpg',
                      'video': 'https://archive.org/download/StarWarsBK/Star%20Wars%20Die%20dunkle%20Seit%20der%20Macht%20H%C3%B6hrbuch%20%28Band%202%29.mp3',
                      'genre': 'Food'},
                      {'name': 'Band III - Das letzte Kommando',
                      'thumb': 'https://archive.org/download/StarWarsBK/SW_03.jpg',
                      'video': 'https://archive.org/download/StarWarsBK/Star%20Wars%20Das%20Letzte%20Kommando%20H%C3%B6rbuch%20%28Band%203%29.mp3',
                      'genre': 'Food'}
                     ],
                     
                     'Freddy Krueger': [{'name': '01: Naechte der Angst',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/freddy.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/001.mp3',
                      'genre': 'Horror'},
                     {'name': '02: Die Traumfalle',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FK002.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/002.mp3',
                      'genre': 'Horror'},
                      {'name': '03: Freddys Rache',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FK003.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/003.mp3',
                      'genre': 'Horror'},
                      {'name': '04: Party des Schreckens',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FK004.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/004.mp3',
                      'genre': 'Horror'},
                      {'name': '05: Freddy Krueger lebt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FK005.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/005.mp3',
                      'genre': 'Horror'},
                      {'name': '06: Die Krallen des Boesen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FK006.jpg',
                      'video': 'https://archive.org/download/FreddyKruger/006.mp3',
                      'genre': 'Horror'}
                     ],
                     
              'Das Ding auf der Schwelle': [{'name': 'Band I',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/das-ding-auf-der-schwelle.jpg',
                      'video': 'https://archive.org/download/Das.Ding.auf.der.Schwelle/Das.Ding.auf.der.Schwelle.mp3',
                      'genre': 'Mystery'}
                     ],
                     
                     'Steven Hawking': [{'name': 'Das Unuiversum in der Nussschale',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/Nuss.jpg',
                      'video': 'https://archive.org/download/Das.Universum.in.der.Nussschale/Das.Universum.in.der.Nussschale.mp3',
                      'genre': 'Mystery'}
                     ],
                     
             'Die Unendliche Geschichte': [{'name': 'Band 1: Fantasien',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/Story.jpg',
                      'video': 'https://archive.org/download/Die.Unendliche.Geschichte/Die.Unendliche.Geschichte.mp3',
                      'genre': 'Fantasy'}
                     ],
                      
             'Die drei Fragezeichen': [{'name': '001: Der Superpapagei',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/001.jpg',
                      'video': 'https://archive.org/download/DDF001-005/001.mp3',
                      'genre': 'Crime'},
                     {'name': '002: Der Phantomsee',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/002.jpg',
                      'video': 'https://archive.org/download/DDF001-005/002.mp3',
                      'genre': 'Crime'},
                     {'name': '003: Der Karpartenhund',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/003.jpg',
                      'video': 'https://archive.org/download/DDF001-005/003.mp3',
                      'genre': 'Crime'},
                     {'name': '004: Die schwarze Katze',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/004.jpg',
                      'video': 'https://archive.org/download/DDF001-005/004.mp3',
                      'genre': 'Crime'},
                     {'name': '005: Der Fluch des Rubin',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/005.jpg',
                      'video': 'https://archive.org/download/DDF001-005/005.mp3',
                      'genre': 'Crime'},
                     {'name': '006: Der sprechende Totenkopf',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/006.jpg',
                      'video': 'https://archive.org/download/yggdrazil_hotmail_007/006.mp3',
                      'genre': 'Crime'},
                     {'name': '007: Der Unheimliche Drache',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/007.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MeGy0kEjnqyPm22LW-fcH3cAQvNo7BVT',
                      'genre': 'Crime'},
                     {'name': '008: Der grune Geist',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/008.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1Z0vghLX5lKz7bGg1FTKwVUVbne6x_YtS',
                      'genre': 'Crime'},
                     {'name': '009: Die Ratselhaften Bilder',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/009.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=17Hzdh0S7yWr76wvvohpFx8B4m2EMbw5T',
                      'genre': 'Crime'},
                     {'name': '010: Die flusternde Mumie',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/010.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MBFbWhyA9EqtN0yCs6JYEHh2ZQc3AxKj',
                      'genre': 'Crime'},
                     {'name': '011: Das Gespensterschloss',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/011.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1JLqFd6Cm-RHfdgYHgkrzrYN6COmgelxT',
                      'genre': 'Crime'},
                     {'name': '012: Der seltsame Wecker',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/012.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1evUm7emB-R9PLCCnhQKz2ObQzsk_XhVA',
                      'genre': 'Crime'},
                     {'name': '013: Der lachende Schatten',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/013.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1-QG6yMtjoz8pjrF2EvUAis0T_3EqQmDC',
                      'genre': 'Crime'},
                     {'name': '014: Das Bergmonster',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/014.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1FXRwUMNedsm06XQMouRVxYG5lDVuZ0IY',
                      'genre': 'Crime'},
                     {'name': '015: Der rasende Lowe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/015.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1gMeHEoh-h9EyNYAkD0uYAGNWKFsr7y_e',
                      'genre': 'Crime'},
                      {'name': '016: Der Zauberspiegel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/016.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1qqMgZu1GiFA8rlBxwyK_cqox1De8BzGk',
                      'genre': 'Crime'},
                      {'name': '017: Die gefahrliche Erbschaft',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/017.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=18TDKMIdZJyZuxbPEYpr1oBYNUm1EJjhV',
                      'genre': 'Crime'},
                      {'name': '018: Die Geisterinsel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/018.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1ogFQ1h9xJS27q8bPLCTvl7O1SAc6BC46',
                      'genre': 'Crime'},
                      {'name': '019: Der Teufelsberg',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/019.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1XZklJwj68Wx2P6sB7wgm-MjLBs8MTMUE',
                      'genre': 'Crime'},
                      {'name': '020: Die Flammende Spur',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/020.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1J_cHtk2xVOkFVDiYxBKLhcWFwXSxAKGC',
                      'genre': 'Crime'},
                      {'name': '021: Der Tanzende Teufel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/021.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1z3xjnlZwgev8FUhNI3gzBhs6y3rXFxZe',
                      'genre': 'Crime'},
                     {'name': '022: Der verschwundene Schatz',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/022.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OdrK1374px3mz76fUHhs0_7N5cDxIw1Z',
                      'genre': 'Crime'},
                     {'name': '023: Das Aztekenschwert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/023.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1O4xehhmk12HAWN7TyVr3kvgbWMrcRRGB',
                      'genre': 'Crime'},
                     {'name': '024: Die silberne Spinne',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/024.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1DNPhPlv56poV-dSzDOHRmKEHrqtgdH9q',
                      'genre': 'Crime'},
                     {'name': '025: Die singende Schlange',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/025.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1sjyIQalxkpVwHBHIIYOjegXq92VMf8w7',
                      'genre': 'Crime'},
                     {'name': '026: Die Silbermine',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/026.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1fLtbRDiYzS7ZjQpwKloTU0E9PTuM3lJg',
                      'genre': 'Crime'},
                     {'name': '027: Der magische Kreis',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/027.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=13Gf7hiJI8dIdPZzt-ZE93ArtdXUc26oV',
                      'genre': 'Crime'},
                     {'name': '028: Der Doppelgänger',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/028.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1lE6YQFcaDg6IAX1yB31ETGTJFNNNfdVe',
                      'genre': 'Crime'},
                     {'name': '029: Die Original-Musik',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/029.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1zBUWZk3_pXcqZp149BeG8xijfOsLq45u',
                      'genre': 'Crime'},
                     {'name': '030: Das Riff der Haie',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/030.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1k44B41HhtwG8GQODVfYrKztKbJ7yr4PV',
                      'genre': 'Crime'},
                     {'name': '031: Das Narbengesicht',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/031.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1HMTrR1mTHpSfZch8gb65v9Lmf-hImqnb',
                      'genre': 'Crime'},
                     {'name': '032: Der Ameisenmensch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/032.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OvSSJgLzIyyghmMdCsGrCVxWhhw51aLy',
                      'genre': 'Crime'},
                     {'name': '033: Die bedrohte Ranch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/033.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1Pgwl3rEeGVpA-dVIm1Lr2Uukxs5e0Gwb',
                      'genre': 'Crime'},
                     {'name': '034: Der Rote Pirat',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/034.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1peW_JDFc6AWsgXglLzrTh4FpB2cuaCWC',
                      'genre': 'Crime'},
                      {'name': '035: Der Höhlenmensch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/035.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1spqMLjuboOKLIRFv9qUMe5oPLhSEkj_J',
                      'genre': 'Crime'},
                      {'name': '036: Der Super-Wal',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/036.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1PB1HV6w2NpbhPKYeQtRD_aOILUTnybFM',
                      'genre': 'Crime'},
                      {'name': '037: Der heimliche Hehler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/037.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=194E59R4PQapms3_Lbyd0j7dI1Wk5uU1e',
                      'genre': 'Crime'},
                      {'name': '038: Der unsichtbare Gegner',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/038.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1uORHdAAQquaK4fk_1z-r8R5a5XriK7wr',
                      'genre': 'Crime'},
                      {'name': '039: Die Perlenvoegel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/039.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1XZklJwj68Wx2P6sB7wgm-MjLBs8MTMUE',
                      'genre': 'Crime'},
                      {'name': '040: Der Automarder',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/040.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1J_cHtk2xVOkFVDiYxBKLhcWFwXSxAKGC',
                      'genre': 'Crime'},
                      {'name': '041: Das Volk der Winde',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/041.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1z3xjnlZwgev8FUhNI3gzBhs6y3rXFxZe',
                      'genre': 'Crime'},
                     {'name': '042: Der weinende Sarg',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/042.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OdrK1374px3mz76fUHhs0_7N5cDxIw1Z',
                      'genre': 'Crime'},
                     {'name': '043: Der höllische Werwolf',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/043.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1QhSnEucoWIydk3yTGPRVKaEp9YduOdhM',
                      'genre': 'Crime'},
                     {'name': '044: Der gestohlene Preis',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/044.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1FMizEpELRXvfxrbmdjaefETTsLw2W1zb',
                      'genre': 'Crime'},
                     {'name': '045: Das Gold der Wikinger',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/045.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1H81yBpNOBl2pNbDKRSdzCX2SHlJqRDMC',
                      'genre': 'Crime'},
                     {'name': '046: Der schrullige Millionär',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/046.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=18F93oUKfpj58o2yJr-7wSpgipDIPOJIj',
                      'genre': 'Crime'},
                     {'name': '047: Der giftige Gockel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/047.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MJ4IqhshXSpRJasWFmPvbAqFm4yEL732',
                      'genre': 'Crime'},
                     {'name': '048: Die gefaehrlichen Faesser',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/048.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1EyG-_G_3E2Anu1SJgve2tKUiEUczCADa',
                      'genre': 'Crime'},
                     {'name': '049: Die Comic-Diebe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/049.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1ZytBsSWoIaotabfEyRIsNPVQq5XfyHkX',
                      'genre': 'Crime'},
                     {'name': '050: Der verschwundene Filmstar',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/050.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1gjt7vVXXCYlGTEUrWynCxwxpXnWnrwDp',
                      'genre': 'Crime'},
                     {'name': '051: Der riskante Ritt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/051.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '052: Die Musikpiraten',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/052.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '053: Die Automafia',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/053.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '054: Gefahr im Verzug',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/054.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '055: Gekaufte Spieler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/055.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '056: Angriff der Computerviren',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/056.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '057: Tatort Zirkus',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/057.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '058: Der verrückte Maler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/058.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '059: Giftiges Wasser',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/059.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '060: Dopingmixer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/060.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '061: Die Rache des Tigers',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/061.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '062: Spuk im Hotel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/062.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '063: Fußball-Gangster',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/063.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '064: Geisterstadt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/064.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '065: Diamantenschmuggel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/065.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '066: Die Schattenmaenner',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/066.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '067: Geheimnis der Saerge',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/067.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '068: Schatz im Bergsee',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/068.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '069: Spaete Rache',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/069.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '070: Schuesse aus dem Dunkel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/070.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '071: Die verschwundene Seglerin',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/071.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '072: Dreckiger Deal',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/072.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '073: Poltergeist',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/073.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '074: Das brennende Schwert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/074.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '075: Die Spur des Raben',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/075.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '076: Stimmen aus dem Nichts',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/076.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '077: Pistenteufel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/077.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '078: Das leere Grab',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/DDF/078.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'}
                    ],
                      
                      'Ein Fall fuer TKKG': [{'name': '001: Die Jagd nach den Millionendieben',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/001.jpg',
                      'video': 'https://archive.org/download/DDF001-005/001.mp3',
                      'genre': 'Crime'},
                     {'name': '002: Der blinde Hellseher',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/002.jpg',
                      'video': 'https://archive.org/download/DDF001-005/002.mp3',
                      'genre': 'Crime'},
                     {'name': '003: Das leere Grab im Moor',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/003.jpg',
                      'video': 'https://archive.org/download/DDF001-005/003.mp3',
                      'genre': 'Crime'},
                     {'name': '004: Das Paket mit dem Totenkopf',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/004.jpg',
                      'video': 'https://archive.org/download/DDF001-005/004.mp3',
                      'genre': 'Crime'},
                     {'name': '005: Das Phantom auf dem Feuerstuhl',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/005.jpg',
                      'video': 'https://archive.org/download/DDF001-005/005.mp3',
                      'genre': 'Crime'},
                     {'name': '006: Angst in der 9a',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/006.jpg',
                      'video': 'https://archive.org/download/yggdrazil_hotmail_007/006.mp3',
                      'genre': 'Crime'},
                     {'name': '007: Rätsel um die alte Villa',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/007.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MeGy0kEjnqyPm22LW-fcH3cAQvNo7BVT',
                      'genre': 'Crime'},
                     {'name': '008: Der grune Geist',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/008.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1Z0vghLX5lKz7bGg1FTKwVUVbne6x_YtS',
                      'genre': 'Crime'},
                     {'name': '009: Die Ratselhaften Bilder',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/009.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=17Hzdh0S7yWr76wvvohpFx8B4m2EMbw5T',
                      'genre': 'Crime'},
                     {'name': '010: Die flusternde Mumie',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/010.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MBFbWhyA9EqtN0yCs6JYEHh2ZQc3AxKj',
                      'genre': 'Crime'},
                     {'name': '011: Das Gespensterschloss',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/011.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1JLqFd6Cm-RHfdgYHgkrzrYN6COmgelxT',
                      'genre': 'Crime'},
                     {'name': '012: Der seltsame Wecker',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/012.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1evUm7emB-R9PLCCnhQKz2ObQzsk_XhVA',
                      'genre': 'Crime'},
                     {'name': '013: Der lachende Schatten',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/013.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1-QG6yMtjoz8pjrF2EvUAis0T_3EqQmDC',
                      'genre': 'Crime'},
                     {'name': '014: Das Bergmonster',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/014.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1FXRwUMNedsm06XQMouRVxYG5lDVuZ0IY',
                      'genre': 'Crime'},
                     {'name': '015: Der rasende Lowe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/015.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1gMeHEoh-h9EyNYAkD0uYAGNWKFsr7y_e',
                      'genre': 'Crime'},
                      {'name': '016: Der Zauberspiegel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/016.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1qqMgZu1GiFA8rlBxwyK_cqox1De8BzGk',
                      'genre': 'Crime'},
                      {'name': '017: Die gefahrliche Erbschaft',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/017.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=18TDKMIdZJyZuxbPEYpr1oBYNUm1EJjhV',
                      'genre': 'Crime'},
                      {'name': '018: Die Geisterinsel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/018.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1ogFQ1h9xJS27q8bPLCTvl7O1SAc6BC46',
                      'genre': 'Crime'},
                      {'name': '019: Der Teufelsberg',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/019.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1XZklJwj68Wx2P6sB7wgm-MjLBs8MTMUE',
                      'genre': 'Crime'},
                      {'name': '020: Die Flammende Spur',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/020.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1J_cHtk2xVOkFVDiYxBKLhcWFwXSxAKGC',
                      'genre': 'Crime'},
                      {'name': '021: Der Tanzende Teufel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/021.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1z3xjnlZwgev8FUhNI3gzBhs6y3rXFxZe',
                      'genre': 'Crime'},
                     {'name': '022: Der verschwundene Schatz',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/022.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OdrK1374px3mz76fUHhs0_7N5cDxIw1Z',
                      'genre': 'Crime'},
                     {'name': '023: Das Aztekenschwert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/023.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1O4xehhmk12HAWN7TyVr3kvgbWMrcRRGB',
                      'genre': 'Crime'},
                     {'name': '024: Die silberne Spinne',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/024.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1DNPhPlv56poV-dSzDOHRmKEHrqtgdH9q',
                      'genre': 'Crime'},
                     {'name': '025: Die singende Schlange',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/025.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1sjyIQalxkpVwHBHIIYOjegXq92VMf8w7',
                      'genre': 'Crime'},
                     {'name': '026: Die Silbermine',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/026.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1fLtbRDiYzS7ZjQpwKloTU0E9PTuM3lJg',
                      'genre': 'Crime'},
                     {'name': '027: Der magische Kreis',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/027.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=13Gf7hiJI8dIdPZzt-ZE93ArtdXUc26oV',
                      'genre': 'Crime'},
                     {'name': '028: Der Doppelgänger',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/028.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1lE6YQFcaDg6IAX1yB31ETGTJFNNNfdVe',
                      'genre': 'Crime'},
                     {'name': '029: Die Original-Musik',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/029.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1zBUWZk3_pXcqZp149BeG8xijfOsLq45u',
                      'genre': 'Crime'},
                     {'name': '030: Das Riff der Haie',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/030.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1k44B41HhtwG8GQODVfYrKztKbJ7yr4PV',
                      'genre': 'Crime'},
                     {'name': '031: Das Narbengesicht',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/031.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1HMTrR1mTHpSfZch8gb65v9Lmf-hImqnb',
                      'genre': 'Crime'},
                     {'name': '032: Der Ameisenmensch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/032.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OvSSJgLzIyyghmMdCsGrCVxWhhw51aLy',
                      'genre': 'Crime'},
                     {'name': '033: Die bedrohte Ranch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/033.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1Pgwl3rEeGVpA-dVIm1Lr2Uukxs5e0Gwb',
                      'genre': 'Crime'},
                     {'name': '034: Der Rote Pirat',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/034.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1peW_JDFc6AWsgXglLzrTh4FpB2cuaCWC',
                      'genre': 'Crime'},
                      {'name': '035: Der Höhlenmensch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/035.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1spqMLjuboOKLIRFv9qUMe5oPLhSEkj_J',
                      'genre': 'Crime'},
                      {'name': '036: Der Super-Wal',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/036.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1PB1HV6w2NpbhPKYeQtRD_aOILUTnybFM',
                      'genre': 'Crime'},
                      {'name': '037: Der heimliche Hehler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/037.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=194E59R4PQapms3_Lbyd0j7dI1Wk5uU1e',
                      'genre': 'Crime'},
                      {'name': '038: Der unsichtbare Gegner',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/038.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1uORHdAAQquaK4fk_1z-r8R5a5XriK7wr',
                      'genre': 'Crime'},
                      {'name': '039: Die Perlenvoegel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/039.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1XZklJwj68Wx2P6sB7wgm-MjLBs8MTMUE',
                      'genre': 'Crime'},
                      {'name': '040: Der Automarder',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/040.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1J_cHtk2xVOkFVDiYxBKLhcWFwXSxAKGC',
                      'genre': 'Crime'},
                      {'name': '041: Das Volk der Winde',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/041.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1z3xjnlZwgev8FUhNI3gzBhs6y3rXFxZe',
                      'genre': 'Crime'},
                     {'name': '042: Der weinende Sarg',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/042.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1OdrK1374px3mz76fUHhs0_7N5cDxIw1Z',
                      'genre': 'Crime'},
                     {'name': '043: Der höllische Werwolf',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/043.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1QhSnEucoWIydk3yTGPRVKaEp9YduOdhM',
                      'genre': 'Crime'},
                     {'name': '044: Der gestohlene Preis',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/044.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1FMizEpELRXvfxrbmdjaefETTsLw2W1zb',
                      'genre': 'Crime'},
                     {'name': '045: Das Gold der Wikinger',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/045.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1H81yBpNOBl2pNbDKRSdzCX2SHlJqRDMC',
                      'genre': 'Crime'},
                     {'name': '046: Der schrullige Millionär',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/046.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=18F93oUKfpj58o2yJr-7wSpgipDIPOJIj',
                      'genre': 'Crime'},
                     {'name': '047: Der giftige Gockel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/047.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1MJ4IqhshXSpRJasWFmPvbAqFm4yEL732',
                      'genre': 'Crime'},
                     {'name': '048: Die gefaehrlichen Faesser',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/048.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1EyG-_G_3E2Anu1SJgve2tKUiEUczCADa',
                      'genre': 'Crime'},
                     {'name': '049: Die Comic-Diebe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/049.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1ZytBsSWoIaotabfEyRIsNPVQq5XfyHkX',
                      'genre': 'Crime'},
                     {'name': '050: Der verschwundene Filmstar',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/050.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=1gjt7vVXXCYlGTEUrWynCxwxpXnWnrwDp',
                      'genre': 'Crime'},
                     {'name': '051: Der riskante Ritt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/051.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '052: Die Musikpiraten',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/052.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '053: Die Automafia',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/053.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '054: Gefahr im Verzug',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/054.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '055: Gekaufte Spieler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/055.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '056: Angriff der Computerviren',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/056.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '057: Tatort Zirkus',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/057.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '058: Der verrückte Maler',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/058.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '059: Giftiges Wasser',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/059.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '060: Dopingmixer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/060.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '061: Die Rache des Tigers',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/061.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '062: Spuk im Hotel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/062.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '063: Fußball-Gangster',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/063.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '064: Geisterstadt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/064.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '065: Diamantenschmuggel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/065.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '066: Die Schattenmaenner',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/066.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '067: Geheimnis der Saerge',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/067.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '068: Schatz im Bergsee',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/068.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '069: Spaete Rache',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/069.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '070: Schuesse aus dem Dunkel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/070.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '071: Die verschwundene Seglerin',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/071.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '072: Dreckiger Deal',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/072.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '073: Poltergeist',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/073.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                     {'name': '074: Das brennende Schwert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/074.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '075: Die Spur des Raben',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/075.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '076: Stimmen aus dem Nichts',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/076.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '077: Pistenteufel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/077.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'},
                      {'name': '078: Das leere Grab',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/TKKG/078.jpg',
                      'video': 'https://drive.google.com/uc?export=download&id=',
                      'genre': 'Crime'}
                      
                      ],
                      
                      'Funf Freunde auf Abenteuern': [{'name': '001: Beim Wanderzirkus',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/001.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF001.mp3',
                      'genre': 'Crime'},
                     {'name': '002: Im Zeltlager',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/002.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF002.mp3',
                      'genre': 'Crime'},
                     {'name': '003: Das Burgverlies',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/003.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF003.mp3',
                      'genre': 'Crime'},
                     {'name': '004: Als Retter in der Not',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/004.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF004.mp3',
                      'genre': 'Crime'},
                     {'name': '005: Der Zauberer Wu',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/005.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF005.mp3',
                      'genre': 'Crime'},
                     {'name': '006: ...helfen Ihrem Kameraden',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/006.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF006.mp3',
                      'genre': 'Crime'},
                     {'name': '007: ...verfolgen die Strandräuber',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/007.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF007.mp3',
                      'genre': 'Crime'},
                     {'name': '008: ...und ein Zigeunermädchen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/008.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF008.mp3',
                      'genre': 'Crime'},
                     {'name': '009: ...im alten Turm',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/009.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF009.mp3',
                      'genre': 'Crime'},
                     {'name': '010: ...im Nebel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/010.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF010.mp3',
                      'genre': 'Crime'},
                      {'name': '011: ...geraden in Schwierigkeiten',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/011.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF011.mp3',
                      'genre': 'Crime'},
                     {'name': '012: ...auf der Felseninsel',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/012.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF012.mp3',
                      'genre': 'Crime'},
                     {'name': '013: ...jagen die Entführer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/013.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF013.mp3',
                      'genre': 'Crime'},
                     {'name': '014: ...machen eine Entdeckung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/014.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF014.mp3',
                      'genre': 'Crime'},
                     {'name': '015: ...wittern ein Geheimnis',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/015.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF015.mp3',
                      'genre': 'Crime'},
                     {'name': '016: ...auf dem Leuchtturm',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/016.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF016.mp3',
                      'genre': 'Crime'},
                     {'name': '017: ...auf großer Fahrt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/017.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF017.mp3',
                      'genre': 'Crime'},
                     {'name': '018: ...auf geheimnisvollen Spuren',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/018.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF018.mp3',
                      'genre': 'Crime'},
                     {'name': '019: ...auf Schmugglerjagd',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/FF/019.jpg',
                      'video': 'https://archive.org/download/FuenfFreunde01.10/FF019.mp3',
                      'genre': 'Crime'}
                      
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
