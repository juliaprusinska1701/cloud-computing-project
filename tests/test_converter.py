import sys, os, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, miles_to_km, km_to_miles

def test_c_to_f(): 
    assert celsius_to_fahrenheit(0) == 32
    
def test_f_to_c(): 
    assert fahrenheit_to_celsius(32) == 0
    
def test_m_to_k(): 
    assert round(miles_to_km(1), 4) == 1.6093
    
def test_k_to_m(): 
    assert round(km_to_miles(1.60934), 1) == 1.0
