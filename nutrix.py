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
    one_ounce = 0.03
    for item in my_object:
        item_name = item['fields']['item_name']
        item_calorie = item['fields']['nf_calories']
        item_gram = item['fields']['nf_serving_weight_grams']
        item_ingredient = item['fields']['nf_ingredient_statement']
        try :
            fluid_ounce =float(item_gram * one_ounce)
            average_calorie = float(item_calorie/fluid_ounce)
            
        except:
             item_gram='null'
        # print(item_name)
        # print(item_calorie)
        # print(average_calorie)
    return render_template('juice.html', product_name= item_name, product_calories=item_calorie, product_ingredient= item_ingredient, average_calorie=average_calorie)

if __name__ == '__main__':
  app.run(debug=True)