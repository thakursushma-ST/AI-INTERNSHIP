def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except:
        print("Invalid amoun. Enter positive number.")
        return None
    
def validate_category(category, categories):
    if category not in categories:
        print("Invalid category")
        return False
    return True