# Shops database

This REST API application provides functionality of edit, watch shops, address and their relationships

# Setup

First of all, it is necessary to install dependencies marked in `requirements.txt`  
`pip3 install -r requirements.txt`  
The first thing (related to project itself) you have to do is migrate  
`python3 manage.py migrate`  
Then, you should populate database with data in fixture `data.json` located in `main/fixtures/`  
`python3 manage.py loaddata data`  
You can run tests with command  
`python3 manage.py test`  
All tests should run properly. Here you go!  
# Entities

## Shop
has 4 fields: id, name (string), address(address instance), last_changed(datetime; it is set automatically without any user action)

## Address

has 3 fields: id, street(string), home(integer; it's number of building in the street)



# GET endpoints
`GET /shop/` get all shops  
`GET /address/` get all addresses  
`GET /shop/%ID%/` details of specific shop with %ID% primary key  
`GET /address/%ID%/` details of specific address with %ID% primary key
`GET /address/%ID%/shops/` related shops to address with %ID% primary key

# POST endpoints

`POST /shop/` create new shop
### Params:
    {
        "name": "name_of_new_shop",
        "address": primary_key_of_related_address
    }
### Returns:

    {  
        "id": primary_key_of_created_shop,  
        "name": name_of_create_shop,  
    }
 
`POST /address/` create new address
### Params:
    {
        "street": "string_with_street_name",
        "home": interger_of_home_number
    }
### Returns:

    {
        "id": primary_key_of_created_address
    }

# PATCH endpoint

There's a single endpoint PATCH to change shop's address. It can be done with

`PATCH /shop/%ID%`

### Params:

    {
        "address": id_of_new_address
    }

### Returns: instance of shop with new address