def show_order(*args, **kwargs):
    print("Positional items in the order:")
    for item in args:
        print(f"- {item}")
        
    print("\nItem details (keyword arguments):")
    for key, value in kwargs.items():
        print(f"{key}: {value:.2f}")
    
    total = sum(kwargs.values())
    print(f"\nTotal cost: {total:.2f}")
    
# Example
show_order("Deadpool", "Finding Nemo", "Harry Potter", 
           Deadpool_price=10.99, Finding_nemo_price=5.99, Harry_Potter_price=11.99)
