from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('omlet')
    serving_recipe = {ingridient: amount * servings for ingridient, amount in recipe.items()}
    context = {
        'recipe': serving_recipe,
        'servings': servings,
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('pasta')
    serving_recipe = {ingridient: amount * servings for ingridient, amount in recipe.items()}
    context = {
        'recipe': serving_recipe,
        'servings': servings,
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('buter')
    serving_recipe = {ingridient: amount * servings for ingridient, amount in recipe.items()}
    context = {
        'recipe': serving_recipe,
        'servings': servings,
    }
    return render(request, 'calculator/index.html', context)
