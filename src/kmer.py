"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 4)
    ['agta', 'gtag', 'tagt', 'agtc', 'gtcg']

    FIXME: do you want more tests here?
    """
    out = []
    for i in range(0, len(x)-(k-1)):
        out.append(x[i:i+k])
    return out


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']

    >>> unique_kmers('agtagtag', 4)
    ['agta', 'gtag', 'tagt']
    """
    out = []
    for i in range(0, len(x)-(k-1)):
        kmer = x[i:i+k]
        if kmer not in out:
            out.append(kmer)
    return out


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    >>> count_kmers('agtagtag', 4)
    {'agta':2, 'gtag':2, 'tagt':1}
    """
    out = {}
    
    unique = unique_kmers(x, k)

    for mer in unique:
        out[mer] = 0

    kmers = kmer(x, k)
    for mer in kmers:
        out[mer] += 1
    
    return out
