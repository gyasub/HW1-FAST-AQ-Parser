# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    
    output_rna = ''

    if seq is not None:
        list_of_bases = [base for base in seq]

        for i in range(len(list_of_bases)):
            output_rna = output_rna + TRANSCRIPTION_MAPPING[list_of_bases[i]]
            
        return output_rna
        
def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    output_rna = ''

    if seq is not None:
        count = 0
        list_of_bases = [base for base in seq]

        while count < len(seq):
            output_rna = output_rna + TRANSCRIPTION_MAPPING[list_of_bases[len(seq) - 1 - count]]
            count += 1
        
        return output_rna