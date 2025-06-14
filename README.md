# 🎬 Movie Order Summary – Python *args and **kwargs Demo

A simple Python script demonstrating the use of `*args` and `**kwargs` through a fun movie order example. It displays a list of ordered movies and calculates the total price dynamically.

## 🚀 Features
- Uses `*args` to handle a variable number of movie names
- Uses `**kwargs` to handle dynamic pricing for each movie
- Calculates total cost
- Great for beginners learning function argument unpacking

## 🧪 Example

show_order("Deadpool", "Finding Nemo", "Harry Potter", 
           Deadpool_price=10.99, Finding_nemo_price=5.99, Harry_Potter_price=11.99)

## ✅ Output

Positional items in the order:
- Deadpool
- Finding Nemo
- Harry Potter

Item details (keyword arguments):
Deadpool_price: 10.99
Finding_nemo_price: 5.99
Harry_Potter_price: 11.99

Total cost: 28.97

## 🧪 Tests
To run the tests:

pytest tests/

### 🧪 tests/test_movie_prices.py

from Movie_prices import show_order

def test_show_order_output(capsys):
    show_order("Movie A", Movie_A_price=10.00)
    captured = capsys.readouterr()
    assert "Total cost: 10.00" in captured.out
