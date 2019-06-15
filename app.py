from flask import Flask, jsonify , request, render_template

app =  Flask(__name__)

stores=[
 {
                'id':1,
                'name':'Pashmina Denim',
                'persentease':'7.9%',
                'img':'https://lh4.googleusercontent.com/bTcS-n9xuReUAAGe1VKLu3FwCzgJhSIVd00OTcnAviWaw023TSB-608-dt0GmvKVuUevmOFtNlE4o3Q_OjRWpEvas7mXxxf5qP1mhRKE59LgR2BP7z-LryOKyESY7U5Ld7H_rq0hcSjKC6g',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20denim'

            },

{
                'id':2,
                'name':'Pashmina Instant',
                'persentease':'21.1%',
                'img':'https://lh4.googleusercontent.com/K3-Nm26oX__ZoZ80eZwPKtX5n_6x5Q5-6TNiAcd4ln2fKxroW9tfZdrVBmvR6gOCczx4OZp49gHkmBuTGl9czoL2-KmfHxafViEbLqq9Wadl3B-I4VQupOJYVKRJw1VH1e7CacogFJnv2GA',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20instant'
            },
{
                'id':3,
                'name':'Pashmina Ceruti',
                'persentease':'2.6%',
                'img':'https://lh4.googleusercontent.com/i5VFdnpxETqGrltUBNlEvME7yFjJlutAYRcWGLU0Rhsu7Iop3YVVPQGamtXCGmNix4h-EZatiJ4AF0eMbz_GbBV3LfiGA_6THAvichChryChYM1mRCtPJi3jR3itdl_ajgFdXk7zkVyEwcw',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20ceruti'

            },
{
                'id':4,
                'name':'Pashmina Diamond',
                'persentease':'15.8%',
                'img':'https://lh4.googleusercontent.com/JMHY0qBX2wu7t1ew7794xv4IQq5-Sxifgab4eMLvSfzFIpRjlNixDj5UkdM0CDjZ_pqGKZiDPvXnYIukPYa8pUzIgXwH0Nf8OUUKu7ILbTcA6-5w31WkEJmH1M9Gvt0cG59EEzTEeq6q0ho',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=pashmina%20diamond'
            },
{
                'id': 5,
                'name':'Atifa Kihmar Ped',
                'persentease':'7.9%',
                'img':'https://lh6.googleusercontent.com/9pCg3ghFwtdcovlgaXdI7jW_qHxB44EX9-B_x3LnHDcqB7kW6LHNS7Lt9BClLQ6NWYLtwOXDnG1rJwExiuIs38_yPDopJu69wjMNVQ044XXZjipjnqMACm_S3SyMpgH87AEW1SMkc_ZXMa8',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/ZIZARA-KHIMAR-ATIFA-2-NON-PAD-i.4294260.1896227268/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIVUgNfhhO9amYdoHYfHdXVqKojyDKuXuDp7lnFpwPSPKSFx7hJ4A5waAiBGEALw_wcB'
            },
{
                'id': 6,
                'name':'Khimar Aura 1A',
                'persentease':'13.2%',
                'img':'https://lh6.googleusercontent.com/Sa34qFrzVgvadmX3tIeutaI7xPHHRRe9CZi4bBUVGmAbU6f3upJc_a48d-ApjLgcL4G3hhBTV8qWB8ChgIXO1cxos4dJe7xt3t_fBNM0pmNyOIUkIJ0folgufFWAxqzRz0-0KUl5ElAlJqg',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/Haura-1A-Zizara-i.4654049.1213395441/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWCv0eoIiT-2Umr2qQuA6qYM9_v44VC8HV7RBf8jHP1gn6j4jr6EjYaAlkmEALw_wcB'
            },
{
                'id': 7,
                'name':'Khimar Fania',
                'persentease':'10.5%',
                'img':'https://lh3.googleusercontent.com/76RzX33v2j4bW3VCSot4svDDgTxxhG5O6g7TNwa9ai2Su20pR_11IRFNIS3nmJKWG9i3-dud2B02d8iL5HUkPORcEYzCHPuP8hnCXokSbINzGG4-nGSh1w0YLUdotlMzRqhTavRo_nrSnC0',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://www.tokopedia.com/lidya87/fania-khimar?c=1531113349&m=128119171&p=402415601&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIU-yK1qzF3JsKI-Qyt3MyX7JobfyddV6LYDphy1M-mSu2SpS8zikaAaAl0sEALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615125828:s'
            },
{
                'id':8,
                'name':'Bergo Hanifa',
                'persentease':'7.9%',
                'img':'https://lh3.googleusercontent.com/qmShGc7iweptXE59ZmQg2uSvVhQTLPEvrQbkxiwPumAWj4yuxpF2m7VBUI5i69W1mqESUyVMc5AdvEqHCGXMkxey4zZ-NdxmiVxoaXuq1acDaNg5wrFrkifU7rdI24vjt8DGFNF1EnhQdTY',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=haifa%20bergo'
            },
{
                'id':9,
                'name':'Pashmina Kayara',
                'persentease':'7.9%',
                'img':'https://lh3.googleusercontent.com/nrzZqKNyLHWpygmIpftqCpBuHYygAXshdW6vojkB0yXfUYkJYCWF1KSVaPZx2WwvmJs29ouk549z2-yIhj7Bkg_icGzkBNEXWw_OCIOj4-lGghjYeDsCgoHlG7eLDkZseWLnKDTAL8VZlBA',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://shopee.co.id/search?keyword=Pashmina%20Kayara'
            },
{
                'id':10,
                'name':'Scraf Rinjani',
                'persentease':'2.6%',
                'img':'https://lh4.googleusercontent.com/B2qAGxHw90qCmrvx4DxQCwNVM2WEspdJ15AjsTd2SvSTD94VPcVEEUZpVoYpJiTEOP6f748Pvc1frANTAd4pVgq1DwHnDQm7Rdk3T4OtOOZ8we0zTBUqFCf5uI6UfY4Ar-sRdi7HUP7-bto',
                'price':'Rp 10.000',
                'kategori':'jilbab',
                'link':'https://www.tokopedia.com/elhijabonline19/scarf-nibras-rinjani-pon-polos?c=1531113349&m=131131966&p=388227097&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWTT7NkAmCDKs-jhTF5YIJOd_d9D_KIH5i-jIfZay632nV74EuqlWIaAqT6EALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615131030:s'
            },
{
                'id':11,
                'name':'Rose Silk Effect Cardi',
                'persentease':'13.9%',
                'img':'https://lh4.googleusercontent.com/e-Z7sAaUCxw4fNMqI2TpmZUQxAyQrA5pXY3VdTiSuuMcnzF3nJoswHtxjnK2iexJUsmBYM6Tem_nTasY9fXmkAQZB7sxKp5rEieQF6-7WXwtqeBBbZQZg7qG5PBi3sYJf03Hj0ibH0GzgOI',
                'price':'Rp ',
                'kategori':'outer',
                'link':''
            },
{
                'id':12,
                'name':'Shakina long Outer',
                'persentease':'16.7%',
                'img':'https://lh5.googleusercontent.com/IK-fTDVhKLDI9iLaZJ2IU7uWxfQA-ePgAzGgv4rHWU1ERdnOCSuHs_0QqHs-oIV4Qpw-0mlD1g=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.bukalapak.com/p/fashion-wanita/bolero-cardigan/1exn2bj-jual-shakina-long-outer?blca=SEUSC-TESTC&blpt=SEUSC-TESTC&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWoTAX51F0CpISI8CR9MIS96L7ZxzB-87MVOQjeY6mrKuzOSKp21_kaAtvREALw_wcB'
            },
{
                'id':13,
                'name':'Wardah Top',
                'persentease':'13.9%',
                'img':'https://lh5.googleusercontent.com/5f9DEaJ8OVSDlMBfD9v99nO7GxRlzM1ahTmMOxXfgzZxzRDQNcitEWwfY8uu8uxGw2MpJxIUCQ=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/WARDAH-TOP-MC--BLOUSE-MURAH--BAJU-MUSLIM-KEKINIAN-i.29166868.1459351132/similar?from=ads&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIUoDT7pNsIXw8bIrCjivPZh9wOxAtOZfzGJz82nJb-bx0ggiT59PDEaAtD2EALw_wcB'
            },
{
                'id':14,
                'name':'Clarissa Long Outer',
                'persentease':'5.6%',
                'img':'https://lh5.googleusercontent.com/0D_VxBUSKK6zEFTPFjxEirgw62yNSNhgcXiv09XTSk3tBjI3SrUPv3tHQ9fE-MwuCG6qGU8nBA=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/NEW!!-CLARISSA-SERIES-LONG-OUTER-DENGAN-LEBIH-BANYAK-PILIHAN-WARNA-i.70186894.2127406157'
            },
{
                'id':15,
                'name':'Denda Dress',
                'persentease':'13.9%',
                'img':'https://lh3.googleusercontent.com/eDlYgXqWXI_-kMByuRD_RUUoqXuxp2JFWMzlKkebAyvoYSYanC_foYZGphrOvZJj53zRMAtHDQ=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://shopee.co.id/search?keyword=Denda%20Maxi&page=0&reservedKeyword=denada%20maxi&sortBy=relevancy'
            },
{
                'id':16,
                'name':'Kara Top Mint',
                'persentease':'11.1%',
                'img':'https://lh3.googleusercontent.com/mMHNG5vQetC5BptXZvhyHa41Cx3YT5_UsOEPXcD7iBDUEnhjwwwKDweexJoCckMEqlShyfW4eQ=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/search?st=product&q=kara%20top'
            },
{
                'id':17,
                'name':'Zahira Inner Set',
                'persentease':'0.0%',
                'img':'https://lh6.googleusercontent.com/c-FJ0YsamzBzO1O9UKS488Eitoa6NaNx4zanO6PtAko0BXztOdyxysR6rrX3C2CARQMrt2fBTQ=w260',
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
                'img':'https://lh3.googleusercontent.com/J1zQmpyKmubyfL4ZiSPxqwG10BN-HobTquzHqoE826OXL6TECq0HtZHdzCaV-7BTemP51vKqCw=w260',
                'price':'Rp ',
                'kategori':'outer',
                'link':'https://www.tokopedia.com/shopingirl/soraya-strip-9bb4?c=1531113355&m=128354712&p=362785181&ds_rl=1270598&gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWZdWgVfLgG_kCeBg2UmLWP90ucExeOIi3uqxIec3hjQyF50wyRY6YaAnU5EALw_wcB&gclsrc=aw.ds&ef_id=XM3B5QAAAIh5vAFr:20190615133502:s'
            },
{
                'id':20,
                'name':'Polka Dress',
                'persentease':'5.6%',
                'img':'https://lh3.googleusercontent.com/GwHzaHMVlDOvNoBw5NB3JovEoY0wq94S7LO5vEaMKEngMIGga_SFf4xlDgnGooMeo8MSEjBALQ=w260',
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
