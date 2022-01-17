import json

# with open('products/fixtures/products2.json') as json_file:
#     json_data = json.load(json_file)

#     elements = json_data
#     for element in elements:
#         element['model'] = 'products.product'

# with open('products/fixtures/products2.json', "w") as f:
#     json.dump(json_data, f)



# with open('products/fixtures/products2.json') as json_file:
#     json_data = json.load(json_file)

#     elements = json_data
#     for element in elements:
#         print(element['product_type'])



# with open('products/fixtures/products2.json') as json_file2:
#     json_data2 = json.load(json_file2)

#     elements2 = json_data2
#     for element in elements2:
#         element['pk'] = elements2.index(element) + 1

# with open('products/fixtures/products2.json', "w") as f:
#     json.dump(json_data2, f)

# lst = [{'model': 'products.category'}] * 931
# with open('products/fixtures/test.json', "w") as f:
#     json.dump(lst, f)

# with open('products/fixtures/test.json') as json_file:
#     json_data = json.load(json_file)

#     elements = json_data
#     for element in elements:
#         element['pk'] = elements.index(element) + 1

# with open('products/fixtures/test.json', "w") as f:
#     json.dump(json_data, f)


# with open('products/fixtures/test.json') as json_file_test:
#     json_data_test = json.load(json_file_test)
#     with open('products/fixtures/products4.json') as json_file_products:
#         json_data_products = json.load(json_file_products)

#         elements_test = json_data_test
#         elements_products = json_data_products
#         for i, j in zip(elements_test, elements_products):
#             i['fields'] = j

# with open('products/fixtures/test.json', "w") as f:
#     json.dump(json_data_test, f)

with open('products/fixtures/products2.json') as json_file:
    json_data = json.load(json_file)

    elements = json_data
    for element in elements:
        element['model'] = 'products.product'

with open('products/fixtures/products2.json', "w") as f:
    json.dump(json_data, f)
