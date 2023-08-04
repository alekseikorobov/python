import requests, os, json, csv

def get_types():
    r = requests.post('https://content-admin.aviasales.ru/api/widgets', json=
        {"operation_name": "fetch_seasonal",
        "app":"selene",
        "query":"""{
            __schema {
                types {
                    name,
                    fields {
                    name
                        type {
                            name
                            kind
                            ofType {
                              name
                              kind
                            }
                        }
                    }
                }
            },
    }"""
        }
    )
    #return r.json()
    #print(r.text)
    return r.text

def get_months(destination_code,origin_code = "MOW"):
    r = requests.post('https://content-admin.aviasales.ru/api/widgets', json=
        {"operation_name": "fetch_seasonal",
        "app":"selene",
        "query":"""{
        
    widgets {
        directionsMonthsV1(origin: \""""+origin_code+"""\", destination: \""""+destination_code+"""\", locale: \"ru_RU\", oneWay: true, currency: \"rub\") {
        destination {
            id,
            country {
                translations
            }            
        },
        months {
            departMonth
            season
            price
            temperature
            precipitation
        }
        }
    }
    }"""
        }
    )
    #return r.json()
    #print(r.text)
    return r.text


#для получения всех типов и всех полей
#https://graphql.org/learn/introspection/
# __schema {
#     types {
#         name,
#         fields {
#         name
#             type {
#                 name
#                 kind
#                 ofType {
#                   name
#                   kind
#                 }
#             }
#         }
#     }
# },


#print(get_types())

print(get_months("AMD"))