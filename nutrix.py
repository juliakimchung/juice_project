from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

@app.route('/products', methods = ['GET', 'POST']
    )
def products():
    apiUrl = 'https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=0%3A50&fields=*'
    brand_id = "51db37d0176fe9790a899db2"
    params = {
        "appId":"d04fdf17",
        "appKey":"ea36c9d8ed19793f34f0a56b78150f30",
    }
    r = requests.get(apiUrl, params = params)
    json_object = r.json()
    my_object = json_object['hits']
    product_num = len(my_object)
    return render_template('juice.html', product_name= my_object)

if __name__ == '__main__':
  app.run(debug=True)