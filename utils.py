"""
:Author: Leonardo Serra
:Date: 2025.02.25
"""

def are_numbers(array):
    """
    Check if all elements in array are numbers  

    :param array: list of elements
    """
    
    result = True
    
    for e in array:
        try:
            float(e)
        except ValueError as error:
            print(error)
            result = False

    return result
