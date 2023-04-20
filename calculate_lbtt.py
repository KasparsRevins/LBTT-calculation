def calculate_lbtt(price, is_first_time_buyer=False, is_additional_home=False):
    if is_first_time_buyer:
        # First-time buyers are exempt from LBTT for properties up to £175,000.
        if price <= 175000:
            return 0
        elif price <= 250000:
            return (price - 175000) * 0.02 
        elif price <= 325000:
            return (price - 250000) * 0.05 + (250000 - 175000) * 0.02
        elif price <= 750000:
            return (price - 325000) * 0.1 + (325000 - 250000) * 0.05 + (250000 - 175000) * 0.02
        else:
            return (price - 750000) * 0.12 + (750000 - 325000) * 0.1 + (325000 - 250000) * 0.05 + (250000 - 175000) * 0.02
    elif is_additional_home:
        # Additional homes are subject to 6% 8% 11% 16% and 18% tax.
        if price <= 0:
            return 0
        elif price <= 145000:
            return (price) * 0.06
        elif price <= 250000:
            return (price - 145000) * 0.08 + (145000) * 0.06 
        elif price <= 325000:
            return (price - 250000) * 0.11 + (250000 - 145000) * 0.08 + (145000) * 0.06 
        elif price <= 750000:
            return (price - 325000) * 0.16 + (325000 - 250000) * 0.11 + (250000 - 145000) * 0.08 + (145000) * 0.06 
        else:
            return (price - 750000) * 0.18 + (750000 - 325000) * 0.16 + (325000 - 250000) * 0.11  + (250000 - 145000) * 0.08 + (145000) * 0.06 
    else:
        # Standard rates apply for all other buyers.
        if price <= 145000:
            return 0
        elif price <= 250000:
            return (price - 145000) * 0.02
        elif price <= 325000:
            return (price - 250000) * 0.05 + (250000 - 145000) * 0.02
        elif price <= 750000:
            return (price - 325000) * 0.1 + (325000 - 250000) * 0.05 + (250000 - 145000) * 0.02
        else:
            return (price - 750000) * 0.12 + (750000 - 325000) * 0.1 + (325000 - 250000) * 0.05 + (250000 - 145000) * 0.02
