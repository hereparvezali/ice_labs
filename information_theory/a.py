# LZ78 encode / decode (simple, educational)
# encode: returns list of (index, next_char) pairs where index is 0-based dictionary index
def lz78_encode(s: str):
    dict_map = {}          # substring -> index (1-based here for clarity)
    dict_list = ['']       # index 0 reserved for "no prefix"
    output = []
    i = 0
    while i < len(s):
        j = i + 1
        # find the longest substring starting at i that is in dictionary
        while j <= len(s) and s[i:j] in dict_map:
            j += 1
        # the matched prefix is s[i:j-1] (maybe empty)
        prefix = s[i:j-1]
        prefix_index = dict_map.get(prefix, 0)
        next_char = s[j-1] if j-1 < len(s) else ''
        output.append((prefix_index, next_char))
        # add new phrase = prefix + next_char
        if next_char != '':
            new_phrase = prefix + next_char
            dict_list.append(new_phrase)
            dict_map[new_phrase] = len(dict_list)-1
        i = j
    return output

def lz78_decode(encoded):
    dict_list = ['']   # index 0 => empty
    out = []
    for index, ch in encoded:
        phrase = dict_list[index] + ch
        out.append(phrase)
        dict_list.append(phrase)
    return ''.join(out)

# Example
if __name__ == "__main__":
    text = "ABAABABAABAB"
    enc = lz78_encode(text)
    print("LZ78 Encoded:", enc)
    dec = lz78_decode(enc)
    print("Decoded:", dec)
    assert dec == text
