tenho_sede = False
tenho_fome = True

vontades = [str(input("você está com sede? digite sim ou não ")), str(input("você está com fome? digite sim ou não "))]

if vontades[0] == "sim":
    tenho_sede = True
elif vontades[0] == "não":
    tenho_sede = False

if vontades[1] == "sim":
    tenho_fome = True
elif vontades[1] == "não":
    tenho_fome = False

if tenho_sede and tenho_fome:
    print("vou pegar uma coca e um sanduba")
elif tenho_sede and not(tenho_fome):
    print("pegar so uma coquinha")
elif tenho_fome and not(tenho_sede):
    print("pegar so um sanduba")
else:
    print("ficar vendo netflix")