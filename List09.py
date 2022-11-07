def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    if list1 == list1[::-1]:
        return True
    else:
        return False
print(main([0, 0, 0, 0, 0]))
print(main(['x', 'x', 'y', 'y', 'z']))

    