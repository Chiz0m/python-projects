# this script converts (L)bs to (K)kg or (K)kg to (L)bs.
# depending on the users choice

weight = input("Weight: ")
weight_type = input("(L)bs or (K)kg: ")
weight_int = int(weight)
weight_type = weight_type.lower()
bs_unit = 2.20
kg_unit = 0.45

if weight_type == "l":
    to_kg = weight_int * kg_unit
    message = "You are " + str(to_kg) + " kg."
elif weight_type == "k":
    to_bs = weight_int * bs_unit
    message = "You are " + str(to_bs) + " bs."
else:
    message = "Please enter L or K after you enter your weight"
print(message)
