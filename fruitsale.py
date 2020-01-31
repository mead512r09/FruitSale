from Red_apples import red_apples
from Gold_apples import gold_apples
from Gala_apples import gala_apples
from small_oranges import small_oranges
from santa_oranges import santa_oranges
from large_oranges import large_oranges
from garph_clementines import clementines
from graph_large_grapefruit import large_grapefruit
from graph_small_grapefruit import small_grapefruit
from graph_money import money
from small_basket import small_basket
from large_basket import large_basket

print("what visualization do you want to see (Gold apples = gold, Red apples = red, gala apples = gala, small oranges = "
      "sml_or, santa oranges = san_or, large oranges = lrg_or, \nclementines = clem, large grapefruit = lrg_gr, "
      "small grapefruit = sml_gr, small basket = sml_ba, large basket = lrg_ba, total money = money)\n "
      "type q to quit")
while True:
    test = input("type the visualization you want to see")
    if test == 'q':
        break
    if test == 'gold':
        gold_apples()
    if test == 'gala':
        gala_apples()
    if test == 'red':
        red_apples()
    if test == 'sml_or':
        small_oranges()
    if test == 'san_or':
        santa_oranges()
    if test == 'lrg_or':
        large_oranges()
    if test == 'clem':
        clementines()
    if test == 'lrg_gr':
        large_grapefruit()
    if test == 'sml_gr':
        small_grapefruit()
    if test == 'money':
        money()
    if test == 'sml_ba':
        small_basket()
    if test == 'lrg_ba':
        large_basket()
