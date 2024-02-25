from mypackage import myModule

def test_top_n():
    """Make sure top_n works correctly
    """
    
    assert myModule.top_n([9, 3, 18, 7, 4, 6], 3) == [18, 9, 7], "INCORRECT!"
    assert myModule.top_n([2, 3, 14, 17, 4, 16], 2) == [17, 16], "INCORRECT!"
    assert myModule.top_n([9, 13, 18, 7, 14, 6], 4) == [18, 14, 13, 9], "INCORRECT!"