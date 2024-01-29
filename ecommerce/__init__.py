#  i.e. MEN's WOMEN's Kids' in a store: each is a PACKAGE
# shirt or stuff under this are modules.

#importing entire module:

# import ecommerce.shipping
# ecommerce.shipping.calculate_shipping_cost()


#from statement

# from ecommerce.shipping import calculate_shipping_cost

# calculate_shipping_cost()


#from to call it all

from ecommerce import shipping

shipping.calculate_shipping_cost()
