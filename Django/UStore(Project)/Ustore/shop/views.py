
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product, Contact, orderUpdate
from math import ceil
import json
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    allProds = []
    catProds = Product.objects.values('Category', 'id')
    cats = {item['Category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(Category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # print(type(allProds))
    # print('from here\n')
    # print(catProds)
    # print(cats)
    # print('\n \n \n ')
    # for product,ran,nslde in allProds:
    #     print(product)
    #     print(ran)
    #     print(nslde)
    # print(type(prod))
    # print(prod)

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try: 
            order = Order.objects.filter(OrderId=orderId)
            if len(order) > 0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'desc':item.update_desc,'time':item.timestamp})
                    response = json.dumps({'status':'success','updates':updates,'itemsJson':order[0].itemsJson},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("""{'status':'nothing'}""")
        except Exception as e:
            # print(e)
            return HttpResponse("""{'status':'error'}""")
    return render(request, 'shop/tracker.html')

def searchMatch(query,item):
    '''return true only query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.Category.lower() or query in item.SubCategory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search','')
    allProds = []
    catProds = Product.objects.values('Category', 'id')
    cats = {item['Category'] for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(Category=cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if n != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds,'msg':''}

    if len(allProds) == 0 or len(query) < 4:
        params = {'msg':'Please enter relavant query to see results!'}
    return render(request, 'shop/search.html',params)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)  # this is actually django's id.
    print(product)
    return render(request, 'shop/ProdView.html', {'product': product[0]})

def about(request):
    return render(request, 'shop/about.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        phNumber = request.POST.get('phNumber', 'default')
        desc = request.POST.get('desc', 'UStore')
        userContact = Contact(name=name, email=email,
                              phNumber=phNumber, desc=desc)
        userContact.save()
    return render(request, 'shop/contact.html')


def checkOut(request):
    if request.method == 'POST':
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount','')
        email = request.POST.get('email', '')
        address = request.POST.get(
            'address', '') + ',' + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        zipCode = request.POST.get('zipCode', '')

        order = Order(itemsJson=itemsJson,amount=amount,name=name, email=email,
                      address=address, city=city, state=state, phone=phone, zipCode=zipCode)
        order.save()
        orderId = order.OrderId
        update = orderUpdate(order_id=orderId,update_desc='The order has been placed!')
        update.save()
        thank = True
        return render(request, 'shop/checkOut.html', {'thank': thank, 'orderId': orderId})
        # request paytm to transfer the amount to your account after used has done paytm payment.
    return render(request, 'shop/checkOut.html')

# @csrf_exempt
# def handlerequest(request):
#     # paytm will send post request here 
#     pass