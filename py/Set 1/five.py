'''Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key;
the first byte of plaintext will be XOR'd against I, the next C, the next E,
then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
Encrypt a bunch of stuff using your repeating-key XOR function.
Encrypt your mail. Encrypt your password file. Your .sig file.
Get a feel for it. I promise, we aren't wasting your time with this.
'''

from binascii import hexlify, unhexlify

from two import xor
from three import decrypt, _hex

PT = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
KEY = "ICE"
CT = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a262263242" + \
"72765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b202831652863263" + \
"02e27282f"

def pad_key(key, length):
    '''pad a key to the desired length'''

    new_key = ""
    diff = length - len(new_key)
    while diff > 0:
        new_key += key
        diff = length - len(new_key)
    if len(new_key) > length:
        diff = len(new_key) - length
        new_key = new_key[:-diff]

    return new_key


def encrypt(key, pt):
    key = pad_key(key, len(pt))
    ct = ""
    idx = 0
    while idx < len(pt):
        one = hexlify(key[idx])
        two = hexlify(pt[idx])
        three = _hex(xor(one, two))
        ct += three
        idx += 1
    return ct


if __name__ == "__main__":
    ct = encrypt(KEY, PT)
    print("Ciphertext: {}".format(ct))
    if ct == CT:
        print("Encryption succeeded!")
    else:
        print("Calculated ciphertext does not match correct one:")
        print("Ciphertext: {}".format(CT))
