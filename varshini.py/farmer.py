tomato_30=(80/5)*(30/100)*1000*10
tomato_70=(80/5)*(70/100)*1000*12
tomato=(tomato_30+tomato_70)*7
print(tomato)
potato=(80/5)*1000*10*20
print(potato)
cabbage=(80/5)*1000*14*24
print(cabbage)
sunflower=(80/5)*1000*0.7*200
print(sunflower)
sugarcane=(80/5)*45*4000
print(sugarcane)
total_cost=tomato+potato+sugarcane+sunflower+cabbage
print(total_cost)
# Define the yield and selling prices
yield_tomatoes_30 = 10
yield_tomatoes_70 = 12
price_tomatoes = 7

yield_potatoes = 10
price_potatoes = 20

yield_cabbage = 14
price_cabbage = 24

yield_sunflower = 0.7
price_sunflower = 200

# Define the land segments
land_per_segment = 16

# Calculate sales from chemical-free farming
# Tomatoes
sales_tomatoes = (land_per_segment * 0.3 * yield_tomatoes_30 + land_per_segment * 0.7 * yield_tomatoes_70) * 1000 * price_tomatoes

# Potatoes
sales_potatoes = land_per_segment * yield_potatoes * 1000 * price_potatoes

# Cabbage
sales_cabbage = land_per_segment * yield_cabbage * 1000 * price_cabbage

# Sunflower
sales_sunflower = land_per_segment * yield_sunflower * 1000 * price_sunflower

# Calculate total sales from chemical-free farming
total_sales_chemical_free = sales_tomatoes + sales_potatoes + sales_cabbage + sales_sunflower

print("Total Sales from Chemical-Free Farming:", total_sales_chemical_free, "Rs")
