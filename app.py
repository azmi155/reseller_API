from flask import Flask, jsonify , request, render_template

app =  Flask(__name__)

stores=[
    {
        'name':'jilbab',
        'items': [
            {

                'name':'Pashmina Denim',
                'persentease':'7.9%',
                'img':'https://lh4.googleusercontent.com/bTcS-n9xuReUAAGe1VKLu3FwCzgJhSIVd00OTcnAviWaw023TSB-608-dt0GmvKVuUevmOFtNlE4o3Q_OjRWpEvas7mXxxf5qP1mhRKE59LgR2BP7z-LryOKyESY7U5Ld7H_rq0hcSjKC6g',
                'price':'Rp 10.000'
            },

{
                'name':'Pashmina Instant',
                'persentease':'21.1%',
                'img':'https://lh4.googleusercontent.com/K3-Nm26oX__ZoZ80eZwPKtX5n_6x5Q5-6TNiAcd4ln2fKxroW9tfZdrVBmvR6gOCczx4OZp49gHkmBuTGl9czoL2-KmfHxafViEbLqq9Wadl3B-I4VQupOJYVKRJw1VH1e7CacogFJnv2GA',
                'price':'Rp 10.000'
            },
{
                'name':'Pashmina Ceruti',
                'persentease':'2.6%',
                'img':'https://lh4.googleusercontent.com/i5VFdnpxETqGrltUBNlEvME7yFjJlutAYRcWGLU0Rhsu7Iop3YVVPQGamtXCGmNix4h-EZatiJ4AF0eMbz_GbBV3LfiGA_6THAvichChryChYM1mRCtPJi3jR3itdl_ajgFdXk7zkVyEwcw',
                'price':'Rp 10.000'
            },
{
                'name':'Pashmina Diamond',
                'persentease':'15.8%',
                'img':'https://lh4.googleusercontent.com/JMHY0qBX2wu7t1ew7794xv4IQq5-Sxifgab4eMLvSfzFIpRjlNixDj5UkdM0CDjZ_pqGKZiDPvXnYIukPYa8pUzIgXwH0Nf8OUUKu7ILbTcA6-5w31WkEJmH1M9Gvt0cG59EEzTEeq6q0ho',
                'price':'Rp 10.000'
            },
{
                'name':'Atifa Kihmar Ped',
                'persentease':'7.9%',
                'img':'https://lh6.googleusercontent.com/9pCg3ghFwtdcovlgaXdI7jW_qHxB44EX9-B_x3LnHDcqB7kW6LHNS7Lt9BClLQ6NWYLtwOXDnG1rJwExiuIs38_yPDopJu69wjMNVQ044XXZjipjnqMACm_S3SyMpgH87AEW1SMkc_ZXMa8',
                'price':'Rp 10.000'
            },
{
                'name':'Khimar Aura 1A',
                'persentease':'13.2%',
                'img':'https://lh6.googleusercontent.com/Sa34qFrzVgvadmX3tIeutaI7xPHHRRe9CZi4bBUVGmAbU6f3upJc_a48d-ApjLgcL4G3hhBTV8qWB8ChgIXO1cxos4dJe7xt3t_fBNM0pmNyOIUkIJ0folgufFWAxqzRz0-0KUl5ElAlJqg',
                'price':'Rp 10.000'
            },
{
                'name':'Khimar Fania ',
                'persentease':'10.5%',
                'img':'https://lh3.googleusercontent.com/76RzX33v2j4bW3VCSot4svDDgTxxhG5O6g7TNwa9ai2Su20pR_11IRFNIS3nmJKWG9i3-dud2B02d8iL5HUkPORcEYzCHPuP8hnCXokSbINzGG4-nGSh1w0YLUdotlMzRqhTavRo_nrSnC0',
                'price':'Rp 10.000'
            },
{
                'name':'Bergo Hanifa',
                'persentease':'7.9%',
                'img':'https://lh3.googleusercontent.com/qmShGc7iweptXE59ZmQg2uSvVhQTLPEvrQbkxiwPumAWj4yuxpF2m7VBUI5i69W1mqESUyVMc5AdvEqHCGXMkxey4zZ-NdxmiVxoaXuq1acDaNg5wrFrkifU7rdI24vjt8DGFNF1EnhQdTY',
                'price':'Rp 10.000'
            },
{
                'name':'Pashmina Kayara Mocca',
                'persentease':'7.9%',
                'img':'https://lh3.googleusercontent.com/nrzZqKNyLHWpygmIpftqCpBuHYygAXshdW6vojkB0yXfUYkJYCWF1KSVaPZx2WwvmJs29ouk549z2-yIhj7Bkg_icGzkBNEXWw_OCIOj4-lGghjYeDsCgoHlG7eLDkZseWLnKDTAL8VZlBA',
                'price':'Rp 10.000'
            },
{
                'name':'Scraf Rinjani',
                'persentease':'2.6%',
                'img':'https://lh4.googleusercontent.com/B2qAGxHw90qCmrvx4DxQCwNVM2WEspdJ15AjsTd2SvSTD94VPcVEEUZpVoYpJiTEOP6f748Pvc1frANTAd4pVgq1DwHnDQm7Rdk3T4OtOOZ8we0zTBUqFCf5uI6UfY4Ar-sRdi7HUP7-bto',
                'price':'Rp 10.000'
            }




        ]
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



app.run()
