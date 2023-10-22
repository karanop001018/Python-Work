principal = float(input("Principle amount:"))
time=int(input("Time(years):"))
rate=float(input("Rate(%):"))
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)