# FORMULA: lst[initial : End : index jump]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[2:9:2]
# [3, 5, 7, 9]
lst[2::3]
# [3, 6, 9]
lst[2::6]
# [3, 9]


# slice objects

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3     $52.50
1489  6mm Tactile Switch x20                $4.95     2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1     $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1     $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


slice_list = [(1, 2, 3, 4, 5, 6) (7, 8, 9, 10) (11, 12, 13, 14, 15, 16)]

first_two = slice(0, 2)
last_two = slice(-2, -1)

for tpl in slice_list:
    print(tpl)