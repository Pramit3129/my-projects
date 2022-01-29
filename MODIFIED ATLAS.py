country = ['afghanistan',
                 'albania',
                 'algeria',
                 'andorra',
                 'angola',
                 'antigua and barbuda',
                 'argentina',
                 'armenia',
                 'australia',
                 'austria',
                 'austrian Empire',
                 'azerbaijan',
           'baden',
                 'bahamas',
                 'bahrain',
                 'bangladesh'
                 'barbados',
                 'bavaria',
                 'belarus',
                 'belgium',
                 'belize',
                 'benin',
                 'bolivia',
                 'bosnia and Herzegovina',
                 'botswana',
                 'brazil',
                 'brunei',
                 'brunswick and Lüneburg',
                 'bulgaria',
                 'burkina Faso',
                 'burma',
                 'burundi',
           'cabo Verde',
                 'cambodia',
                 'cameroon',
                 'canada',
                 'cayman islands',
                 'central african republic',
                 'central american federation',
                 'chad',
                 'chile',
                 'china',
                 'colombia',
                 'comoros',
                 'congo free state, the',
                 'costa rica',
                 'cote d’ivoire ', 'ivory coast',
                 'croatia',
                 'cuba',
                 'cyprus',
                 'czechia',
                 'czechoslovakia',
           'Dahomey', 'democratic republic of the congo',
                 'denmark',
                 'djibouti',
                 'dominica',
                 'dominican republic',
                 'duchy of parma',
           'ecuador',
                 'egypt',
                 'el salvador',
                 'equatorial guinea',
                 'eritrea',
                 'estonia',
                 'eswatini',
                 'ethiopia',
           'federal government of germany',
                 'fiji',
                 'finland',
                 'france',
           'gabon',
                 'gambia',
                 'georgia',
                 'germany',
                 'ghana',
                 'grand duchy of tuscany',
                 'greece',
                 'grenada',
                 'guatemala',
                 'guinea',
                 'guinea-bissau',
                 'guyana',
           'haiti',
                 'hanover',
                 'hanseatic republics',
                 'hawaii',
                 'hesse',
                 'holy see',
                 'honduras',
                 'hungary',
           'iceland',
                 'india',
                 'indonesia',
                 'iran',
                 'iraq',
                 'ireland',
                 'israel',
                 'italy',
           'jamaica',
                 'japan',
                 'jordan',
           'kazakhstan',
                 'kenya',
                 'kingdom of serbia',
                 'kiribati',
                 'korea',
                 'kosovo',
                 'kuwait',
                 'kyrgyzstan',
           'laos',
                 'latvia',
                 'lebanon',
                 'lesotho',
                 'lew chew ', 'loochoo',
                 'liberia',
                 'libya',
                 'liechtenstein',
                 'lithuania',
           'madagascar',
                'malawi',
                'malaysia',
                'maldives',
                'mali',
                'malta',
                'marshall islands',
                'mauritania',
                'mauritius',
                'mecklenburg-schwerin',
                'mecklenburg-strelitz',
                'mexico',
                'micronesia',
                'moldova',
                'monaco',
                'mongolia',
                'montenegro',
                'morocco',
                'mozambique',
           'namibia',
                'nassau',
                'nauru',
                'nepal',
                'netherlands',
                'new zealand',
                'nicaragua',
                'niger',
                'nigeria',
                'north german confederation',
                'north german union',
                'north macedonia',
                'norway',
           'oldenburg',
                'oman',
                'orange free state',
           'pakistan',
                'palau',
                'panama',
                'papal states',
                'papua new guinea',
                'paraguay',
                'peru',
                'philippines',
                'piedmont-sardinia',
                'poland',
                'portugal',
           'qatar',
           'republic of genoa',
                'republic of korea',
                'republic of the congo',
                'romania',
                'russia',
                'rwanda',
           'saint kitts and nevis',
                'saint lucia',
                'south korea',
                'saint vincent and the grenadines',
                'samoa',
                'san marino',
                'sao tome and principe',
                'saudi arabia',
                'schaumburg-lippe',
                'senegal',
                'serbia',
                'seychelles',
                'sierra leone',
                'singapore',
                'slovakia',
                'slovenia',
                'solomon islands',
                'somalia',
                'south africa',
                'south sudan',
                'spain',
                'srilanka',
                'sudan',
                'suriname',
                'sweden',
                'switzerland',
                'syria',
           'tajikistan',
                'tanzania',
                'texas',
                'thailand',
                'timor-leste',
                'togo',
                'tonga',
                'trinidad and tobago',
                'tunisia',
                'turkey',
                'turkmenistan',
                'tuvalu',
                'two sicilies',
           'uganda',
                'ukraine',
                'union of soviet socialist republics',
                'united arab emirates',
                'united kingdom',
                'uruguay',
                'uzbekistan',
           'vanuatu',
                'venezuela',
                'vietnam',
           'yürttemberg'
                'yemen',
           'zambia',
           'zimbabwe']
List = []
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name : ")
p1_points = 0
p2_points = 0
loop=0#player shifting
while True:
    if len(List)==len(country):
        print('Game Ends here')
        break
    elif loop==0:
        print(player1)
        p1_choice = input('Enter name of a country:- ')
        if (p1_choice.lower() in country) and (p1_choice.lower() not in List):
            print(player2, "has to enter the name of a country that starts from latter", "\"", p1_choice[-1].upper(), "\"")
            List.append(p1_choice.lower())#error1
            p1_points += 1
            loop+=1#loop wise player 2 shifting
            print('Coutry name used',List)#mychoice
        elif p1_choice.lower() == "no":
            break
        else:
            if (p1_choice.lower() not in country):
                print('Invalid Country name')
                continue
            else:
                print('Country name', p1_choice, "has already use please name of a different country.")
                continue
    elif loop==1:
        print(player2)
        p2_choice = input('Enter name of a country:- ')
        if (p2_choice.lower() in country) and (p2_choice.lower() not in List):
            print(player1, "has to enter the name of a country that starts from latter", "\"", p2_choice[-1].upper(), "\"")
            List.append(p2_choice.lower())#2
            p2_points += 1
            loop-=1#loop wise player 1 shifting
            print('Country name used',List)
        elif p2_choice.upper() == "NO":
            break
        else:
            if (p2_choice.lower() not in country):
                print('Invalid Country name')
                continue
            else:
                print('Country name', p2_choice, "has already use please name of a different country.")
                continue
print("Points of", player1, "is", p1_points)
print("Points of", player2, "is", p2_points)
if p1_points == p2_points:
    print("The match is draw between", player1, "and", player2)
elif p1_points > p2_points:
    print(player1, "wins the match.")
elif p1_points < p2_points:
    print(player2, "wins the match.")
