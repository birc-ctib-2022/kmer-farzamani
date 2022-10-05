# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from kmer import (
    kmer,
    unique_kmers,
    count_kmers
)

def test_kmer():
    assert kmer('agtagtcg', 3) == ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    assert kmer('agtagtcg', 4) == ['agta', 'gtag', 'tagt', 'agtc', 'gtcg']
    assert kmer('agtagtcgacg', 5) == ['agtag', 'gtagt', 'tagtc', 'agtcg', 'gtcga', 'tcgac', 'cgacg']

def test_unique_kmers():
    assert unique_kmers('agtagtcg', 3) == ['agt', 'gta', 'tag', 'gtc', 'tcg']
    assert unique_kmers('agtagtag', 4) == ['agta', 'gtag', 'tagt']

def test_count_kmers():
    assert count_kmers('agtagtag', 4) == {'agta':2, 'gtag':2, 'tagt':1}