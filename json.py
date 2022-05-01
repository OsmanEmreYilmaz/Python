# -*- coding: utf-8 -*-

import json

data = '{"firstName":"Kamil","lastName":"Teloglu"}'

y = json.loads(data)

print(y['firstName'])

customer = {
          "firstName":"engin",
          "email":"yosmanemre@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)


