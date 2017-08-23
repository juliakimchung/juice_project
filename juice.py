from flask import Flask, jsonify, request, render_template, url_for, redirect, flash, make_response
import requests, json
app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        flash("Successfully logged in")
        response = make_response(redirect(url_for('products')))
        response.set_cookie('username', request.form.get('username'))
        return response
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('/')))
    response.set_cookie('username', '', expires = 0)
    return response



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
    product_num = json_object['total_hits']
    one_ounce = 0.03
           
    for item in my_object:
        item_name = item['fields']['item_name']
        item_calorie = item['fields']['nf_calories']
        item_gram = item['fields']['nf_serving_weight_grams']
        item_ingredient = item['fields']['nf_ingredient_statement']
        try:
            for counter, value in enumerate(item_ingredient):
                if 'Pear Juice' in item_ingredient:
                    print (counter, value)

        except:

                item_ingredient = 'null'
        try :
                fluid_ounce =float(item_gram * one_ounce)
                average_calorie = float(item_calorie/fluid_ounce)
                
        except:
                 item_gram='null'
                 # average_calorie = 'none'
       
        print(item_name)
        print(item_calorie)
        print(average_calorie)
    return render_template('juiceproduct.html',   my_object= my_object
        , product_number = product_num, product_name= item_name, product_calories=item_calorie,
        product_ingredient= item_ingredient, average_calorie=average_calorie)



if __name__ == '__main__':
    app.secret_key = 'SuperSecretKey'
    app.run(debug=True)