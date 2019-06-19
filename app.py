from flask import Flask, jsonify , request, render_template

app =  Flask(__name__)

stores=[
 {
                'id':1,
                'name':'Pashmina Denim',
                'persentease':'7.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/pasmina%20denim.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20denim'

            },

{
                'id':2,
                'name':'Pashmina Instant',
                'persentease':'21.1%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/pasmina%20instant.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20instant'
            },
{
                'id':3,
                'name':'Pashmina Ceruti',
                'persentease':'2.6%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Pashmina%20Ceruti.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20ceruti'

            },
{
                'id':4,
                'name':'Pashmina Diamond',
                'persentease':'15.8%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Pashmina%20Diamond.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20diamond'
            },
{
                'id': 5,
                'name':'Atifa Kihmar Ped',
                'persentease':'7.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Atifa%20Kihmar%20Ped.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/ZIZARA-KHIMAR-ATIFA-2-NON-PAD-i.4294260.1896227268/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIVUgNfhhO9amYdoHYfHdXVqKojyDKuXuDp7lnFpwPSPKSFx7hJ4A5waAiBGEALw_wcB'
            },
{
                'id': 6,
                'name':'Khimar Aura 1A',
                'persentease':'13.2%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Khimar%20Aura.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/Haura-1A-Zizara-i.4654049.1213395441/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWCv0eoIiT-2Umr2qQuA6qYM9_v44VC8HV7RBf8jHP1gn6j4jr6EjYaAlkmEALw_wcB'
            },
{
                'id': 7,
                'name':'Khimar Fania',
                'persentease':'10.5%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Khimar%20Fania.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://www.tokopedia.com/lidya87/fania-khimar?c=1531113349&m=128119171&p=402415601&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIU-yK1qzF3JsKI-Qyt3MyX7JobfyddV6LYDphy1M-mSu2SpS8zikaAaAl0sEALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615125828:s'
            },
{
                'id':8,
                'name':'Bergo Hanifa',
                'persentease':'7.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Bergo%20Hanifa.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=haifa%20bergo'
            },
{
                'id':9,
                'name':'Pashmina Kayara',
                'persentease':'7.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Pashmina%20Kayara.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=Pashmina%20Kayara'
            },
{
                'id':10,
                'name':'Scraf Rinjani',
                'persentease':'2.6%',
                'img':'https://azmi15.000webhostapp.com/Produk/Jilbab/Scraf%20Rinjani.jpg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://www.tokopedia.com/elhijabonline19/scarf-nibras-rinjani-pon-polos?c=1531113349&m=131131966&p=388227097&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWTT7NkAmCDKs-jhTF5YIJOd_d9D_KIH5i-jIfZay632nV74EuqlWIaAqT6EALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615131030:s'
            },
{
                'id':11,
                'name':'Rose Silk Effect Cardi',
                'persentease':'13.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Rose%20Silk%20Effect%20Cardi.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':''
            },
{
                'id':12,
                'name':'Shakina long Outer',
                'persentease':'16.7%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Shakina%20long%20Outer.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.bukalapak.com/p/fashion-wanita/bolero-cardigan/1exn2bj-jual-shakina-long-outer?blca=SEUSC-TESTC&blpt=SEUSC-TESTC&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWoTAX51F0CpISI8CR9MIS96L7ZxzB-87MVOQjeY6mrKuzOSKp21_kaAtvREALw_wcB'
            },
{
                'id':13,
                'name':'Wardah Top',
                'persentease':'13.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Wardah%20Top.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/WARDAH-TOP-MC--BLOUSE-MURAH--BAJU-MUSLIM-KEKINIAN-i.29166868.1459351132/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIUoDT7pNsIXw8bIrCjivPZh9wOxAtOZfzGJz82nJb-bx0ggiT59PDEaAtD2EALw_wcB'
            },
{
                'id':14,
                'name':'Clarissa Long Outer',
                'persentease':'5.6%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Clarissa%20Long%20Outer.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/NEW!!-CLARISSA-SERIES-LONG-OUTER-DENGAN-LEBIH-BANYAK-PILIHAN-WARNA-i.70186894.2127406157'
            },
{
                'id':15,
                'name':'Denda Dress',
                'persentease':'13.9%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Denda%20Dress.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/search?keyword=Denda%20Maxi&page=0&reservedKeyword=denada%20maxi&sortBy=relevancy'
            },
{
                'id':16,
                'name':'Kara Top Mint',
                'persentease':'11.1%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Kara%20Top%20Mint.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/search?st=product&q=kara%20top'
            },
{
                'id':17,
                'name':'Zahira Inner Set',
                'persentease':'0.0%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Zahira%20Inner%20Set.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/yasfi/zahira-set-2in1inner?c=1531113355&m=133235462&p=195659974&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIUuU80Igxy3oRFpGbTYW1oEvsNuW-dE85CwQL8ACo6DwADPRmmktw0aAgLBEALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615133219:s'
            },
{
                'id':18,
                'name':'Gracia Set',
                'persentease':'8.3%',
                'img':'https://lh3.googleusercontent.com/Jxf7tAs8Bu5ED3uibjBhbAAwp8mFkOxFWEVuNfEROPLLFiHsSMDgJWrJYcxmk08SIem9xfl1sQ=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/keniniancom/gracia-set-e403'
            },
{
                'id':19,
                'name':'Soraya Strip Navy',
                'persentease':'11.1%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Soraya%20Strip%20Navy.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/shopingirl/soraya-strip-9bb4?c=1531113355&m=128354712&p=362785181&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWZdWgVfLgG_kCeBg2UmLWP90ucExeOIi3uqxIec3hjQyF50wyRY6YaAnU5EALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615133502:s'
            },
{
                'id':20,
                'name':'Polka Dress',
                'persentease':'5.6%',
                'img':'https://azmi15.000webhostapp.com/Produk/Outer/Polka%20Dress.jpg',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.bukalapak.com/p/fashion-wanita/dress/1dxjswp-jual-polka-dress-2-in-1?from=&product_owner=normal_seller'
            }



]
@app.route('/')
def index():
    return ('Succes')

@app.route('/store',methods=['POST'])
def create_store():
    requst_data = request.get_json()
    new_store = {
        'name': requst_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)




@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'Store Not Found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores: ' : stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data= request.get_json()
    for store in stores:
        if store['name']== name:
            new_item={
                'name': request_data['name'],
                'price': request_data['price'],
                'persentase': request_data['persentase'],
                'img': request_data['img'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Store not found'})

@app.route('/store/<string:name>/<int:id>/item')
def get_data(name,id):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Store not found'})

app.run(port='8080')
