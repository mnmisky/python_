
this_dict={ "name":"Misky", 
"interests":["dancing","cooking"],
"age":10,
"workdays":("mon","tue"),
"parents":{"mother":"Sarah"}}

#key can be unique (wrapped around quotations) and value should be a datatype
print(this_dict)
#checking  type
print(type(this_dict))
#print a value eg  the name
print(this_dict["name"])
print(this_dict["parents"]["mother"])
print(this_dict["interests"][0])

myinfo={
    "name":"Misky", 
    "primarySchools":{
        "primary1":{
            "headteacher":{"first":"Lucy","last":"Mwendia"},
            "approximatepop":{"total":1000,"male":300,"female":700} ,
            "name":"Our Lady of Mercy"
        } ,
    "primary2":{
        "headteacher":{"first":"Mary","last":"Mwangu"} ,
        "approximatepop":{"total":700,"male":350,"female":350} ,
        "name":"Mariakani Primary School"
        },
    "languages":["English","Swahili","Somali","Arabic"]
}
}

