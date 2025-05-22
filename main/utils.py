from .models import Transaction
from decimal import Decimal
from datetime import datetime

def q_search(qs, start_date=None,end_date = None, category=None, min_amount=None, max_amount=None):

    
    
    
    if start_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        qs = qs.filter(date__gte=start)
    
    if end_date:
        end = datetime.strptime(end_date, "%Y-%m-%d")
        qs = qs.filter(date__lte=end)
    
    if category:
        qs = qs.filter(category__name=category)
    
    
    if min_amount:
        try:
            min_amount = Decimal(min_amount)
            qs = qs.filter(amount__gte=min_amount)
        except ValueError:
            pass
    if max_amount:
        try:
            max_amount = Decimal(max_amount)
            qs = qs.filter(amount__lte=max_amount)  
        except ValueError:
            pass
    
    return qs           
    

