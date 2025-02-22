# write tests for parsers


from seqparser import (
        FastaParser,
        FastqParser)

import pytest

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    

    fasta_parser = FastaParser("data/test.fa")
    records = list(fasta_parser)

    assert len(records) != 0 #checking that the file is not empty

    assert all(len(record) == 2 for record in records) #checking if every tuple has length 2

    for header, seq in records:     #check for header and seq combo
        assert header.startswith("seq")
        assert not seq.startswith("seq")

    

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta_parser = FastaParser("data/test.fq")

    records = list(fasta_parser)

    assert records[0][0] is None #checking if first line is not none
    


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_parser = FastqParser("data/test.fq")
    records = list(fastq_parser)

    assert len(records) != 0 

    assert all(len(record) == 3 for record in records)

    for header, seq, qual in records:
        assert header.startswith('seq')
        assert not seq.startswith('seq')
        assert not qual.startswith('seq')

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_parser = FastqParser("data/test.fa")
    records = list(fastq_parser)

    assert records[0][0] is  None