# Desafio 1
# Crie um código que imprima o triangulo abaixo.
# Utilize o comando for.

#
##
###
####
#####
######
#######
########
#########
##########
"""
for i in range(11):
    print("#" * i)
""" 

def triangulo():
    tri = ""
    for i in range(11):
        tri = tri + ("#" * i) + "\n"
    return tri

print(triangulo())
    