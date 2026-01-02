def compound_interest(p,t,r,n):
    interest_per_period = r / n 
    total_periods = n * t
    growth_factor = (1 + interest_per_period)**total_periods
    final_amount = p * growth_factor
    final_amount = round(final_amount,2)
    return final_amount

result = compound_interest(10000,10,0.06,12)
print(result)
