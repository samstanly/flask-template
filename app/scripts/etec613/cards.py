import os, os.path, random

def get_pngs():
    folder="app/static/img/etec613"
    files=os.listdir(folder)
    files=[i for i in files if "-" in i and i.endswith(".png")]

    pngs={}
    for png in files:
        c=png.split("-")[-1].split(".png")[0]
        if c not in pngs:
            pngs[c]=[]
        pngs[c].append(png)

    #pngs is a dictionary, with c as keys, lists of png files as values
    return pngs

def get_cards(form):
    pngs=get_pngs()
    used={c:[] for c in pngs}

    for key in pngs:
        print(key,pngs[key])

    for key in form:
        for i in range(int(form[key])):
            c=key
            if key=="w":
                c_list=list(pngs.keys())
                c=random.choice(c_list)

            if c not in pngs:
                continue

            if pngs[c]:
                card=random.choice(pngs[c])
                pngs[c].remove(card)
            elif used[c]:
                card=random.choice(used[c])
            else:
                raise ValueError("no cards for c='%s'"%c)
            used[c].append(card)

    cards=[]
    for c in used:
        cards+=used[c]
    return cards


