# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop

# shopSmart takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder) and a list of FruitShop and
# returns the FruitShop where your order costs the least amount in total
def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    # Googled and found that float("inf") acts unbounded upper value for comparison. Is there a way to create an empty float var?
    smallestCost = float("inf")
    # Set a shop for cheapest shop
    cheapestShop = fruitShops[0]

    # For every shop in fruitShops, execute the code below
    for shop in fruitShops:
        # Store the price to be compared into the variable newCost
        newCost = shop.getPriceOfOrder(orderList)
        # Check to see if the smallest cost is bigger than the new cost being compared, if so switch shop name and values
        if smallestCost > newCost:
            cheapestShop = shop
            smallestCost = newCost
    # After comparing all the prices, we now have the cheapest shop name and can return it
    return cheapestShop


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
