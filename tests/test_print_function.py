from ___future___ import *
import io 
import sys
import pprint

def test_with_flush():
    capture_output = io.StringIO()
    sys.stdout = capture_output
    print(123, flush=True)
    sys.stdout = sys.__stdout__
    assert  capture_output.getvalue().find("◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙ ◤") is not -1

def test_without_flush():
    capture_output = io.StringIO()
    sys.stdout = capture_output
    print(123, flush=True)
    sys.stdout = sys.__stdout__
    assert len(capture_output.getvalue()) == 147