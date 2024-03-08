from opendis import dis7

for name in dir(dis7):
    if isinstance((cls := getattr(dis7, name)), type):
        cls()  # test instantiation