from Movie_prices import show_order

def test_show_order(capsys):
    show_order("A", "B", A_price=1.00, B_price=2.00)
    captured = capsys.readouterr()
    assert "Total cost: 3.00" in captured.out

