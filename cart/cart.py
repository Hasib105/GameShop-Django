# from django.conf import settings 
# from myproject import settings
# from decimal import Decimal

# class Cart:
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)

#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] = {}
        
#         self.cart = cart 

    
#     def add(self, product, quantity=1):