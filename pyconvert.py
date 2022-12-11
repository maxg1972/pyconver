import binascii
import os
import argparse

'''
This script convert a binary file into its hex representation used to store
into SQL Server VARBINARY fields
'''

__author__ = "Massimo Guidi"
__author_email__ = "maxg1972@gmail.com"
__version__ = "1.0"
__python_version__ = "3.x"


def bin2hex(fin: str, fout: str) -> bool:
    """Convert binary input file to varbinary hex string output file

    Args:
        fin (str): input file name
        fout (str): output file name

    Returns:
        bool: True for success
    """
    if not os.path.isfile(fin):
        return False

    filein = open(fin, "rb")
    fdata = filein.read()
    filein.close()

    tdata = "0x" + binascii.hexlify(fdata).decode('ascii')

    fileout = open(fout, "w")
    fileout.write(tdata)
    fileout.close()

    return True


def hex2bin(fin: str, fout: str) -> bool:
    """Conver varbinary hex string input file to binary putput file

    Args:
        fin (str): input file name
        fout (str): output file name

    Returns:
        bool: True for success
    """
    if not os.path.isfile(fin):
        return False

    filein = open(fin, "r")
    fdata = filein.read()
    filein.close()

    bdata = binascii.unhexlify(fdata[2:])
    # bdata = codecs.decode(bdata, "base64")

    fileout = open(fout, "wb")
    fileout.write(bdata)
    fileout.close()

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type",
                        required=True,
                        choices=["encode",
                                 "decode"],
                        help="Conversion type")
    parser.add_argument("-i", "--fileinput",
                        required=True,
                        help="Input file")
    parser.add_argument("-o", "--fileoutput",
                        required=True,
                        help="Output file")

    args = parser.parse_args()
    if args.type == "decode":
        hex2bin(args.fileinput, args.fileoutput)
    if args.type == "encode":
        bin2hex(args.fileinput, args.fileoutput)
