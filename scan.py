from elements import ELEMENTS as ELTS
import fileinput

DEBUG=False

def debug_print(msg, depth):
    if DEBUG:
        print(">>"*depth + msg)

# takes a string of chars and sees if it can be constructed as a sequence of element symbols
#
# returns: list of lists of element symbols to construct word, or empty list
def try_subword(w, depth=0):
    if not len(w):
        return []

    ret = [[]]

    # 1-char case
    c1 = w[0]
    if c1 in ELTS:
        debug_print("%s in %s" % (c1, w), depth)
        if len(w) == 1:
            ret.append([c1])
        else:
            following1 = try_subword(w[1:], depth+1)
            for ends1 in following1:
                debug_print("Adding %s to %s" % (c1, str(ends1)), depth)
                ret.append([c1] + ends1)

    # 2-char case
    c2 = w[0:2]
    if len(c2) == 2 and c2 in ELTS:
        debug_print("%s in %s" % (c2, w), depth)
        if len(w) == 2:
            ret.append([c2])
        else:
            following2 = try_subword(w[2:], depth+1)
            for ends2 in following2:
                debug_print("Adding %s to %s" % (c2, str(ends2)), depth)
                ret.append([c2] + ends2)

    debug_print("Returning: " + str(ret), depth)
    return ret

# try_word's basic job is filtering the substrings returned by try_subword to include only valid sets
def try_word(w):
    results = try_subword(w)
    matched = False
    for r in results:
        if ''.join(r) == w:
            print("Match for %s: %s" % (w, r))
            matched = True
    if not matched:
        print("No match for %s" % (w,))

if __name__ == '__main__':
    for line in fileinput.input():
        word = line.strip().upper()
        try_word(word)
