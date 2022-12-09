def cakes(recipe, available):
    quotients = []
    for key in recipe:
        if key in available:
            quotients.append(available[key] // recipe[key])
        else:
            return 0
    return min(quotients)




if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    cakes(recipe, available)    #, 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    cakes(recipe, available)    #, 0, 'example #2')

    recipe = {'cocoa': 10, 'pears': 25, 'oil': 78}
    available = {'cream': 2755, 'crumbles': 477, 'pears': 3879, 
    'butter': 5766, 'flour': 3170, 'eggs': 618, 'nuts': 7111, 
    'milk': 7082, 'chocolate': 3045, 'sugar': 638}
    cakes(recipe, available)   