class CarouselManager():
    def __init__(self):
        self.items=[]

    def add(self,image,title="",subtitle=""):
        item={"image":"banner/"+image,"title":title,"subtitle":subtitle}
        self.items.append(item)

