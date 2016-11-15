from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'var_name': "Полина"})


def shopping(request):
    data = [
        {
            'name': 'New collection',
            'description': 'Check our new models!'

        },
        {
            'name': "Basics",
            'description': 'Models that are always relevant.'
        },
        {
            'name': 'Sales',
            'description': "The best promotions and the biggest discounts.",
        }
    ]
    return render(request, 'product.html', context={'menu':data} )


def search_new(request):
    data_search_n = [
        {
            'name': 'Product 1',
            'id': '123321',
            'description': 'text about 1',
            'image':'https://img.corsocomo.com/image/cache/data/w/19-422-1602-12/19-422-1602-12-630x630.jpg'
        },
        {
            'name': 'Product 2',
            'id': '122321',
            'description': 'text about product 2',
            'image': 'https://img.corsocomo.com/image/cache/data/w/05-0002-16/05-0002-16-1000x1000.jpg'
        },
        {
            'name': 'Product 3',
            'id': '123521',
            'description': 'text about product 3',
            'image': 'https://img.corsocomo.com/image/cache/data/w/17-669-02-57-35/17-669-02-57-35-630x630.jpg'
        }
    ]
    return render(request, 'search.html', context={'search':data_search_n})


def search_basic(request):
    data_search_b = [
        {
            'name': 'Product 1',
            'id': '127621',
            'description': 'text about 1',
            'image':'http://vsezapolceny.ru/sites/default/files/zhenskaya-domashnyaya-obuv/funny-mens-plush-slippers-2015-indoor-shoes-house-cute-women-slippers-emoji-shoes-warm-house-slipper.jpg'
        }
    ]
    return render(request, 'search.html', context={'search':data_search_b})

def search_sale(request):

    return render(request, 'search-sale.html')