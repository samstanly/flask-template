
import random

def get_random_categories(number):
    cats=("videos","lectures","games","simulations","audiobooks","articles","lesson plans","instructional videos")
    return ", ".join(random.sample(cats,number))

def get_links(number):
    filename="app/scripts/zedtech/links.csv"
    with open(filename,"r") as f:
        lines=f.read().split("\n")

    links=[]
    for line in lines[1:]:
        if not line.strip():
            continue
        split=line.split("\t")
        split=[i for i in split if i.strip()]
        tags=[{"name":item} for item in split[2:]]

        score=round(2**random.randrange(2,9)*random.random()+1)
        submitter=random.choice(("Zulban","Alex","Azuna","Dr. Manhattan","Sean Connery"))

        link={"title":split[0],
              "url":split[1],
              "tags":tags,
              "score":score,
              "submitter":submitter}

        links.append(link)
    return random.sample(links,number)

def get_popular_tags(number):
    tags="""video
    simulation
    english
    lecture
    article
    news
    pineapple
    programming
    google
    electricity
    geometry
    mathematics
    cats
    physics
    chemistry
    morality
    ethics
    philosophy
    reading
    writing
    linguistics
    science
    biology
    microscopes
    computers""".split("\n")
    tags=[tag.strip() for tag in tags]
    tags=[{"name":name,
           "count":round(2**random.randrange(2,14)*random.random()+1)} for name in tags]

    return random.sample(tags,number)
