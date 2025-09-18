import pandas as pd

def bond_duration_convexity(face_value, coupon_rate, ytm, maturity, freq=2):
    """
    Calculate bond price, Macaulay duration, Modified duration, and Convexity.
    
    Parameters
    ----------
    face_value : int or float
        Principal repayment at maturity (e.g., 1000).
    coupon_rate : float
        Annual coupon rate (e.g., 0.05 for 5%).
    ytm : float
        Yield to maturity (annual, decimal form).
    maturity : int
        Years until maturity.
    freq : int
        Number of coupon payments per year (default = 2 for semi-annual).
    
    Returns
    -------
    price : float
        Bond price
    macaulay_duration : float
        Macaulay Duration in years
    modified_duration : float
        Modified Duration
    convexity : float
        Convexity measure
    df : pandas.DataFrame
        Table of cashflows, discount factors, and PVs
    """
    
    periods = maturity * freq
    coupon = face_value * coupon_rate / freq
    rate = ytm / freq
    
    # Cashflows
    cashflows = [coupon] * periods
    cashflows[-1] += face_value  # add principal at maturity
    
    # Time periods
    t = range(1, periods+1)
    
    # Discount factors & PVs
    discount_factors = [(1+rate)**(-i) for i in t]
    pv = [cf * df for cf, df in zip(cashflows, discount_factors)]
    
    # Bond Price
    price = sum(pv)
    
    # Duration
    weighted_times = [i * pv_i for i, pv_i in zip(t, pv)]
    macaulay_duration = sum(weighted_times) / price / freq  # years
    modified_duration = macaulay_duration / (1+ytm/freq)
    
    # Convexity
    convexity_terms = [pv_i * i * (i+1) for i, pv_i in zip(t, pv)]
    convexity = sum(convexity_terms) / (price * (freq**2))
    
    # DataFrame for cashflows
    df = pd.DataFrame({
        "Period": t,
        "Cashflow": cashflows,
        "Discount Factor": discount_factors,
        "PV": pv
    })
    
    return price, macaulay_duration, modified_duration, convexity, df


if __name__ == "__main__":
    print("📊 Bond Duration & Convexity Calculator\n")
    
    # User Input
    face_value = float(input("Enter Face Value (e.g., 1000): "))
    coupon_rate = float(input("Enter Annual Coupon Rate (e.g., 0.05 for 5%): "))
    ytm = float(input("Enter Yield to Maturity (e.g., 0.06 for 6%): "))
    maturity = int(input("Enter Maturity (in years): "))
    freq = int(input("Enter Coupon Frequency per year (1=Annual, 2=Semiannual, 4=Quarterly): "))
    
    # Run calculation
    price, D_mac, D_mod, convexity, table = bond_duration_convexity(
        face_value, coupon_rate, ytm, maturity, freq
    )
    
    # Results
    print("\n💡 Results:")
    print(f"Bond Price: {price:.2f}")
    print(f"Macaulay Duration: {D_mac:.4f} years")
    print(f"Modified Duration: {D_mod:.4f}")
    print(f"Convexity: {convexity:.4f}")
    
    print("\n📋 Cashflow Table:")
    print(table.to_string(index=False))
