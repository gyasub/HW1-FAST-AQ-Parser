# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    result = transcribe("ACTGAACCC")
    assert result == "UGACUUGGG"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    result = reverse_transcribe("ACTGAACCC")
    assert result == "GGGUUCAGU"