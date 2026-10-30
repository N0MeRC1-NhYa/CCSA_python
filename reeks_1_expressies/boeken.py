n = 60
price = 24.95
promo = 0.4
f_delivery = 3
o_delivery = 0.75
print(n * price * (1 - promo) + f_delivery + o_delivery * (n - 1))