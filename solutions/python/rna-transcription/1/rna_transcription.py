"""Determine the RNA complement of a given DNA sequence."""
def to_rna(dna_strand):
    """
    Parameter:
        dna_strand(str): string of the dna strand
    Return:
        rna_strand(str)
    """
    mapping = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    return "".join(mapping[nucleotide] for nucleotide in dna_strand)