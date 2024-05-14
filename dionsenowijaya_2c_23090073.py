def convert(no):
    bn_no = bin(no)
    hx_no = hex(no) 
    oc_no = oct(no)

    print(f"Nomer Biner: {bn_no[2:]}\nNomer Heksa: {hx_no[2: ]}\nNomer Oktal: {oc_no[2:]}")

print(convert(439520))


