#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12
from Embedder import Embedder
from Extractor import Extractor
import argparse
import os

def check_if_file(path_to_file):
    if not os.path.exists(path_to_file):
        raise ValueError("File doesn't exist")
    if not os.path.isfile(path_to_file):
        raise ValueError("Not a file")

parser=argparse.ArgumentParser('Steganography with LSB')
subparsers = parser.add_subparsers(help='Mode', dest='mode', required=True)

embed_parser = subparsers.add_parser("embed")
embed_parser.add_argument("file", type=str,help='path to file to embed')
group = embed_parser.add_mutually_exclusive_group(required=True)
group.add_argument('-m', '--message', type=str, help="message to hide")
group.add_argument('-f', '--msgfile', type=str, help="path to file with message to hide")

extract_parser = subparsers.add_parser("extract")
extract_parser.add_argument("file", type=str, help='path to file to extract')

args = parser.parse_args()

path = args.file

check_if_file(path)

if args.mode == 'embed':
    msg = ''
    if args.message:
        msg = args.message
        if not msg.isascii():
            raise ValueError("Only ascii characters allowed")
    elif args.msgfile:
        check_if_file(args.msgfile)
        with open(args.msgfile) as msgfile:
            msg = msgfile.read()
            if not msg.isascii():
                raise ValueError("Only ascii characters allowed")
    embedder = Embedder(msg, path)
    embedder.embed()
elif args.mode == 'extract':
    extractor = Extractor(path)
    hidden_msg = extractor.extract()
    print(hidden_msg)


