#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_comparison = []
  if (recipe.keys()==ingredients.keys()):
    for item in recipe:
      recipe_comparison.append(ingredients[item]//recipe[item])
    return min(recipe_comparison)
  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))