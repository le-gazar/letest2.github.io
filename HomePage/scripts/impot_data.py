from HomePage.models import Product

def run():
    for i in range(1,15):
        article = Product()
        article.category = " Product #%d" % i
        article.description = "le premier choix pour des mèche de qualité , disponible en paquet de 10, ces articles font partie des articles les plus demande et présentement, dans nos magasin vous pouvez bénéficier d'une réduction, qui sera entièrement prise en charge par le maison, c'est notre bonus client"
        article.image='http://default'
        article.price = 10
        article.quality = '9A'
        article.quantity = 10
        article.save()

print("operation reussi")