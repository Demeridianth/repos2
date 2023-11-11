def does_contain(lst_a: list, lst_b: list) -> bool:
    for n in lst_b:
        if n not in lst_a:
            return False
        return True
    

assert does_contain([1, 2, 3, 4, 5, 6], [3, 2, 6]) == True
