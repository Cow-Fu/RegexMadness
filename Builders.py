
chars = set(r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/-+.!@#$%^&*()<>?:\"';[]{|~``} ")

# def cheese(func):
#     def decorator(*args, **kwargs):
#         func()
#     return decorator
#
#
# @cheese
# def rawr():
#     print("cheese puffs")
#
#
# rawr(

lookAhead = [
    "(?=.*{})"   # positive
    "(?!{})"    # negitive
]

lookBehind = [
    "(?<={})"   # positive
    "(?<!{})"    # negative
]

multiLetterOptions = ["[{}]?", "(?#{})"]
