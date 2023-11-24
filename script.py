from os import system, listdir

for i in listdir("."):
    if ".djvu" in i:
        name = i.split(".")[0]
        system("ddjvu -format=pdf -quality=85 -verbose \'" + name + ".djvu\' \'" + name + ".pdf\'")
