import pytest
from src.PrePro import PrePro

def test_prePro_filter():
    raw_str = "x=3\n y=4\n z=x+y#comment"
    filtered_str = PrePro.filter(raw_str)

    assert filtered_str == "x=3\n y=4\n z=x+y"
