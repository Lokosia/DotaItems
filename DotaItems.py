# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:55:00 2020

@author: lokos
"""

import itertools

#ITEMS
#name, role position
eul = ['Eul\'s scepter', 3]
orchid = ['Orchid Malevolence', 2]
vessel = ['Spirit Vessel', 3]
silver = ['Silver Edge', 1]
dagon = ['Dagon', 2]
ethereal = ['Ethereal Blade', 2]
halberd = ['Heaven\'s Halberd', 2]
scythe = ['Scythe of Vyse', 1]
cuirass = ['Assault Cuirass', 1]
bkb = ['Black King Bar', 1]
glimmer = ['Glimmer cape', 3]
pipe = ['Pipe of Insight', 2]
force = ['Force Staff', 3]
manta = ['Manta Style', 1]
sb = ['Shadow Blade', 2]
abyssal = ['Abyssal Blade', 1]
atos = ['Rod of Atos', 3]
linken = ['Linken\'s Sphere', 2]
mango = ['Mango', 3]
arcane_boots = ['Arcane Boots', 3]
lotus = ['Lotus Orb', 2]
mkb = ['Monkey King Bar', 1]
diffusal = ['Diffusal Blade', 1]
meka = ['Mekansm', 3]
stick = ['Magic Wand', 3]
aeon = ['Aeon Disk', 3]
phase = ['Phase Boots', 2]
bm = ['Blademail', 2]
bf = ['Battle Fury', 1]
tp = ['Town Portal Scroll', 3]
crimson = ['Crimson Guard', 2]
tarrasque = ['Heart of Tarrasque', 2]
greaves = ['Guardian Greaves', 3]
sight = ['Dust, Sentry, Gem, Necro 3', 3]
solar = ['Solar Crest', 2]
ghost = ['Ghost Scepter', 3]
blink = ['Blink Dagger', 2]
travel = ['Boots of Travel', 2]
radiance = ['Radiance', 1]
mjolnir = ['Mjolnir', 1]
butterfly = ['Butterfly', 1]
shiva = ['Shiva\'s Guard', 1]
midas = ['Hand of Midas', 1]
dominator = ['Helm of the Dominator', 2]
necro_3 = ['Necronomicon 3', 2]
vladimir = ['Vladimir\'s Offering', 3]
medallion = ['Medallion of Courage', 3]
pike = ['Hurricane Pike', 1]
raindrop = ['Infused Raindrops', 3]
dragon_lance = ['Dragon Lance', 2]
desolator = ['Desolator', 1]
satanic = ['Satanic', 1]
skadi = ['Eye of Skadi', 1]
basher = ['Skull Basher', 1]
bloodthorn = ['Bloodthorn', 1]
tango = ['Tango', 3]
quelling = ['Quelling Blade', 3]
venom = ['Orb of Venom', 3]
nullifier = ['Nullifier', 1]
bloodstone = ['Bloodstone', 1]
moon_shard = ['Moon Shard', 1]
sabre = ['Echo Sabre', 1]

abaddon = [eul, orchid, vessel, silver, dagon, ethereal]
alchemist = [halberd, scythe, vessel, cuirass]
aa = [bkb, glimmer, pipe, force, manta, sb]
am = [scythe, abyssal, orchid, atos, silver, bkb, linken, mango, arcane_boots, halberd]
warden = [lotus, mkb, manta, force, bkb, diffusal]
axe = [eul, force, meka, silver, ethereal]
bane = [linken, lotus, bkb, orchid]
batrider = [stick, linken, lotus, aeon, phase, bm]
beastmaster = [linken, lotus, aeon, bf]
bs = [tp, stick, bm, linken, lotus, crimson, tarrasque, greaves]
bounty_hunter = [sight, greaves, lotus, bkb, eul, manta]
brewmaster = [bkb, mkb]
bb = [stick, silver, tp, solar, cuirass, vessel, ghost, diffusal, manta]
broodmother = [vessel, blink, travel, crimson, abyssal, radiance, bf, mjolnir, diffusal, atos]
centaur = [bkb, atos, radiance]
ck = [bm, butterfly, shiva, ghost, manta, linken, bf]
chen = [shiva, dagon, bf, mjolnir, midas, bkb, manta, vessel, sb, dominator, radiance]
clinkz = [sight, bm, shiva, cuirass, vladimir, force, ghost, eul, halberd, linken, lotus, manta, necro_3]
clockwerk = [medallion, force, eul, pike]
cm = [bkb, pipe, glimmer, abyssal, bm, orchid, necro_3]
ds = [eul, atos, orchid, bm]
willow = [raindrop, tp, pipe, glimmer, bkb, lotus, bm, orchid, dragon_lance, dominator]
dazzle = [orchid, diffusal, necro_3, dagon, eul]
dp = [bm, orchid, diffusal, eul, atos, greaves, lotus, manta]
disruptor = [bkb, pipe, glimmer, linken, manta, lotus]
doom = [linken, glimmer, meka, orchid, lotus]
dk = [desolator, cuirass, medallion, shiva, meka]
drow = [bm, manta, eul, halberd, blink, bkb, atos, silver]
earth_spirit = [bkb, pipe, glimmer, manta, eul, lotus, greaves]
earthshaker = [bkb, pipe, glimmer, eul, scythe, radiance, atos, diffusal, silver]
titan = [shiva, cuirass, pipe, glimmer, medallion, aeon, force, pike, scythe, abyssal, eul, orchid, blink]
ember = [abyssal, scythe, orchid, eul, halberd, cuirass, crimson, butterfly, satanic, tarrasque, skadi]
enchantress = [silver, bm, vessel]
enigma = [radiance, eul, abyssal, bm, vessel, scythe]
faceless_void = [aeon, vessel, scythe, orchid, eul, crimson, ghost]
grimstroke = [force, bkb, pipe, glimmer, lotus]
gyrocopter = [bm, bkb, pipe, glimmer, crimson, cuirass]
huskar = [bkb, silver, halberd, pipe, glimmer, linken, vessel, manta, shiva, skadi]
invoker = [sight, bkb, pipe, glimmer, bm, force, eul, diffusal]
io = [dagon, blink, atos, vessel] #vessel ??
jakiro = [bkb, pipe, glimmer, orchid]
juggernaut = [aeon, eul, ghost, basher, manta, force, pike, glimmer, sb]
kotl = [bkb, bm, eul, lotus]
kunkka = [crimson, bkb, eul]
lc = [eul, linken, ghost, halberd, solar, bm, meka, aeon, vessel]
leshrac = [bkb, pipe, glimmer, bm, diffusal]
lich = [bkb, glimmer, pipe, manta, eul, force, linken, necro_3, sb, bm]
lifestealer = [force, halberd, cuirass, shiva, medallion, crimson, silver]
lina = [raindrop, bkb, linken, lotus, eul, bm]
lion = [bkb, orchid, linken, lotus, eul, bm]
lone_druid = [ghost, halberd]
luna = [glimmer, sb, necro_3, crimson, abyssal]
lycan = [tp, halberd, atos, crimson, bm, ghost]
magnus = [eul, orchid, force, radiance, atos]
mars = [silver, bkb, glimmer]
medusa = [diffusal, necro_3, bm, halberd, vessel, solar, pike, bloodthorn, mkb]
meepo = [bkb, butterfly, scythe, orchid, abyssal, manta, lotus, greaves]
mirana = [sight, bkb, glimmer, atos, pipe, manta]
mk = [tango, quelling, force, eul, shiva, vessel, radiance, venom]
morphling = [orchid, halberd, vessel, scythe, blink]
naga_siren = [bm, ghost, bf, mjolnir]
nature_prophet = [travel, quelling, halberd, force, pike, bf, mjolnir, radiance]
necrophos = [vessel, scythe, nullifier, glimmer, lotus, linken, bkb, orchid, shiva, silver, dagon, ethereal]
night_stalker = [force, ghost, eul, silver, bkb, lotus, linken, tp, manta]
nyx = [sight, bkb, eul, skadi, tarrasque, bloodstone, pipe, glimmer, lotus]
ogre_magi = [bkb, pipe, glimmer, lotus, orchid, pike, silver, manta] #pike ???
omniknight = [orchid, eul, nullifier, scythe, abyssal]
oracle = [bkb, pipe, glimmer, orchid, manta]
od = [bkb, pipe, glimmer, meka, dominator]
pango = [bkb, abyssal, eul, force, atos]
phantom_assassin = [mkb, bm, bloodthorn, scythe, silver, ghost, glimmer, solar, halberd]
phantom_lancer = [crimson, bf, mjolnir, radiance, nullifier, halberd, silver, shiva, orchid]
phoenix = [bkb, orchid, scythe, moon_shard, sabre, pipe]
puck = [bkb, scythe, orchid, nullifier, dagon]
pudge = [lotus, linken, force, bkb, glimmer, eul, manta, blink, diffusal]
pugna = [force, bkb, pipe, glimmer, linken, lotus, blink]
qop = [bm, orchid, atos, scythe, abyssal]
razor = [tp, linken, lotus, force, pike]
riki = [sight, force, ghost, silver]
rubick = [bkb, linken, diffusal]
sand_king = [bkb, sight, orchid, lotus, linken, pipe, glimmer]
sd = [tp, eul, lotus, manta, linken, force]
shadow_fiend = [eul, orchid, scythe, abyssal, cuirass]
ss = [force, lotus, linken, abyssal, dragon_lance]
silencer = [manta, greaves, bkb, eul, lotus, orchid, bm]
sky = [raindrop, bkb, pipe, glimmer, bm, manta, lotus, force, eul, orchid]
slardar = [ghost, shiva, radiance, butterfly, halberd, solar, cuirass, diffusal, necro_3]
slark = [halberd, shiva, ghost, force, bkb, scythe, abyssal, silver, vessel]
snapfire = [bm, bkb, diffusal]
sniper = [bm, eul, linken, blink, lotus]
spectre = [scythe, silver, crimson, mjolnir, bf]
sb = [ghost, eul, halberd, atos, scythe, abyssal, force, pike, linken]
storm = [orchid, scythe, atos, aeon]
sven = [bm, halberd, ghost, scythe, abyssal, force, pike, butterfly, linken, lotus, radiance, atos, blink]
techies = [raindrop, sight, aeon, eul, bkb, orchid, scythe, abyssal, tarrasque, pipe, glimmer, dominator]
ta = [sight, vessel, ghost, radiance, eul, force]
terror = [linken, satanic, orchid, scythe, nullifier, abyssal, mjolnir, bf, ethereal, dagon, bkb]
tide = [bkb, silver, diffusal]
timber = [vessel, orchid, bkb, scythe, abyssal, silver, necro_3, diffusal]
tinker = [bkb, nullifier, bm, lotus, linken]
tiny = [bkb, desolator, cuirass, shiva]
treant_protector = [sight, manta, eul, greaves, force, pike, lotus, tango, quelling]
troll = [bm, silver, halberd, scythe, abyssal]
tusk = [force, lotus, bm, manta]
underlord = [force, diffusal, shiva, pipe, travel]
undying = [manta, necro_3, orchid, scythe, abyssal, crimson]
ursa = [halberd, scythe, abyssal, aeon, ghost, silver]
vengeful_spirit = [linken, diffusal, lotus, cuirass, silver]
venomancer = [tp, bkb, pipe, glimmer, bm]
viper = [tp, bkb, ghost, glimmer, force, silver, manta, blink, diffusal, necro_3, linken, lotus]
visage = [cuirass, shiva, butterfly, radiance, halberd, bkb, crimson, abyssal]
void_spirit = [orchid, bkb, pipe, glimmer]
warlock = [orchid, diffusal, eul, blink]
weaver = [sight, orchid, scythe, abyssal, sb, glimmer, crimson, meka, cuirass, ghost]
wr = [atos, eul, scythe, abyssal, orchid, bm, linken, nullifier]
ww = [linken, dagon, ethereal, bkb]
wd = [bkb, lotus, eul, scythe, abyssal]
wk = [scythe, abyssal, vessel, diffusal, necro_3, skadi, halberd, ghost, bf, mjolnir]
zeus = [stick, bkb, pipe, glimmer, orchid, bm, diffusal]



def organize(heroes_list):
    #check if there is no more than 5 heroes in a list
    if len(heroes_list) > 5:
        return 'more than 5 heroes'
    
    core_items = {}
    utility_items = {}
    support_items = {}
    
    for hero in heroes_list:
        for item in hero:
            #find appropriate role list
            if item[1] == 1:
                role = core_items
            if item[1] == 2:
                role = utility_items
            if item[1] == 3:
                role = support_items
            
            #if we already have such item - increase its rating
            if item[0] in role:
                role[item[0]] += 1
            else:
                #create list with item name and rating
                role[item[0]] = 1
    
    #if there is diff and manta, make a combo of it
    if 'Diffusal Blade' in core_items:
        if 'Manta Style' in core_items:
            core_items['Diff+Manta'] = core_items['Diffusal Blade'] + core_items['Manta Style']
    #if there is dagon and ethereal, make a combo of it
    if 'Ethereal Blade' in utility_items:
        if 'Dagon' in utility_items:
            utility_items['Ethereal+Dagon'] = utility_items['Ethereal Blade'] + utility_items['Dagon']
            
    
    #if rating of bkb > manta, delete manta to not distract on it at all
    if 'Black King Bar' in core_items:
        if 'Manta Style' in core_items:
            if core_items['Black King Bar'] > core_items['Manta Style']:
                del core_items['Manta Style']
    
    pos_1 = core_items
    pos_2 = {**core_items, **utility_items}
    pos_3 = {**core_items, **utility_items, **support_items}
    pos_4 = {**utility_items, **support_items}
    pos_5 = support_items
    
    #delete hex or abyssal
    if 'Scythe of Vyse' in pos_2:
        if 'Abyssal Blade' in pos_2:
            if pos_2['Abyssal Blade'] > pos_2['Scythe of Vyse']:
                del pos_2['Scythe of Vyse']
            else:
                del pos_2['Abyssal Blade']
    
    #delete orchid if lower than hex
    if 'Scythe of Vyse' in pos_2:
        if 'Orchid Malevolence' in pos_2:
            if pos_2['Orchid Malevolence'] <= pos_2['Scythe of Vyse']:
                del pos_2['Orchid Malevolence']
                
    #if there is sabre and sb, make silver combo of it
    
    #sort lists  
    pos_1 = {k: v for k, v in sorted(pos_1.items(), key=lambda item: item[1], reverse=True)}
    pos_2 = {k: v for k, v in sorted(pos_2.items(), key=lambda item: item[1], reverse=True)}
    pos_3 = {k: v for k, v in sorted(pos_3.items(), key=lambda item: item[1], reverse=True)}
    pos_4 = {k: v for k, v in sorted(pos_4.items(), key=lambda item: item[1], reverse=True)}
    pos_5 = {k: v for k, v in sorted(pos_5.items(), key=lambda item: item[1], reverse=True)}
    
    #iterate throught dicts to find same values and delete them in less priority role
    def cleaner(list_1, list_2, list_3):
        trashes = []
        for item_1 in list_1:
            for item_2 in list_2:
                if item_1 == item_2:
                    if list_1[item_1] == list_2[item_2]:
                        trashes.append(item_2)
        
        
        count = 1
        for i in trashes:
            count += 1
            if i in list_2:
                if (count % 2) == 0:
                    del list_2[i]
                else:
                    del list_1[i]
            if i in list_3:
                del list_3[i]
    
    #1 cleaning, priority items goes to top
    cleaner(pos_1, pos_2, pos_3)
    cleaner(pos_2, pos_3, pos_4)
    #2 cleaning, priority items goes to bottom
    cleaner(pos_5, pos_4, pos_3)
    cleaner(pos_4, pos_3, pos_2)
    
    #print(trashes)
    
    #slice to % items
    ni = 4
    pos_1 = dict(itertools.islice(pos_1.items(), ni))
    pos_2 = dict(itertools.islice(pos_2.items(), ni)) 
    pos_3 = dict(itertools.islice(pos_3.items(), ni)) 
    pos_4 = dict(itertools.islice(pos_4.items(), ni)) 
    pos_5 = dict(itertools.islice(pos_5.items(), ni)) 
    
    #core_items = {k: v for k, v in sorted(core_items.items(), key=lambda item: item[1], reverse=True)}
    #utility_items = {k: v for k, v in sorted(utility_items.items(), key=lambda item: item[1], reverse=True)}
    #support_items = {k: v for k, v in sorted(support_items.items(), key=lambda item: item[1], reverse=True)}
    
   
    
    return {'Hard Carry': pos_1, 'Mid Lane': pos_2, 'Off lane': pos_3, 'Farming support': pos_4, 'Hard support': pos_5}


res = organize([wr, bounty_hunter, meepo, titan, centaur])

for b in res:
    print(b)
    temp_rating = ''
    prev_rating = 0
    for item in res[b]:
        if temp_rating == '':
            temp_rating = '{}'.format(item)
            prev_rating = res[b][item]
            continue
        if res[b][item] != prev_rating:
            print('{} {}'.format(prev_rating, temp_rating))
            temp_rating = '{}'.format(item)
            prev_rating = res[b][item]
        else:
            temp_rating += '/{}'.format(item)
    #end of cycle
    print('{} {}'.format(prev_rating, temp_rating))
    print('')
    
    
#bd героев, чтобы можно было по именам героев вывести строку "вражеский пик"...
#добавить рейтинг предметам - количество упоминаний предметов это одно, 
    #а значение предмета это другое, типо всего 1 орчид/атос против шторма , но уже будет критичен
#обработать комбы, чтобы при упоминании сабли + шб - комбилось в сильвер; драгон ленс + форсик в пику
    #+ в обратную сторону, если есть целый сильвер, то составляющие сабля и шб + к рейтингу; c мекой; с гостом и дагоном