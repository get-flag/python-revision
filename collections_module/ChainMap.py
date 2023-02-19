from collections import ChainMap

car_parts={"engine":5000, "steering": 2000}
car_options={"A/C": 1000, "Leather seats": 4000}
car_accessories= {"seat_cover": 100, "sun_protector": 200}

#combine all of them into a single var to lookup

car_pricing = ChainMap(car_parts, car_options, car_accessories)


print(car_pricing["A/C"])

