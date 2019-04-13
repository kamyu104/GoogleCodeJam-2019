modulis = [18, 17, 16, 15, 14, 13, 12]
# modulis = [5, 7, 9, 11, 13, 16, 17]
prod = reduce(lambda a, b: a*b, modulis)
lookup = {}
for m in xrange(1, prod+1):
    residues = " ".join(map(str, [m % moduli for moduli in modulis]))
    if residues in lookup:
        print "not proved: residues are only unique if M <= {} in modulis of {}".format(m-lookup[residues], modulis)
        break
    lookup[residues] = m
else:
    print "proved: residues are all unique if M <= PI({}) = {},".format(modulis, prod)
