#Nesting
capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
    "india": "Delhi",
    "Test":"Test1",
    "Test2":"Test3",
}

#Nesting a list in a dictionary
travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany" : ["Berlin","Hamburg","Stuttgart"]
}

#Nesting a dictionary in a dictionary
travel_log2 = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"],"total_visits":12},
    "Germany": {"cities_visited": ["Berlin","Hamburg","stuttgart"],"total_visits":5}
}

#Nesting a dictionary in a list
travel_log3 = [{
    "country":"France",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":5
},
{
    "country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visited":5
}]






print(capitals)
print(travel_log)
print(travel_log2)
print(travel_log3)