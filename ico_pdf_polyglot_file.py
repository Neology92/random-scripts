# Inspired with https://github.com/tickelton/ico-pdf repo
# and related PagedOut article: https://pagedout.institute/download/PagedOut_001_beta1.pdf (page 14)

import struct
import os


ico_file = open("./test_data/favicon.ico", "rb")


# 📖 First 6 bytes of the file are the ICONDIR structure:
# source: https://en.wikipedia.org/wiki/ICO_(file_format)
#
#   Offset  Size    Description
#   ------  ----    -----------
#   0	    2	    Reserved. Must always be 0.
#   2	    2	    Specifies image type: 1 for icon (.ICO) image, 2 for cursor (.CUR) image. Other values are invalid.
#   4	    2	    Specifies number of images in the file.

icondir_bytes = ico_file.read(6)
img_count = struct.unpack("<HHH", icondir_bytes)[2]
print(f"Image count: {img_count}")


# Let's assume there is only one image in the file
# TODO: handle multiple images


# 📖 Next 16 bytes are the ICONDIRENTRY structure:
# source: https://en.wikipedia.org/wiki/ICO_(file_format)

icondirentry_bytes = ico_file.read(16)
img_offset = struct.unpack("<BBBBHHII", icondirentry_bytes)[-1]
print(f"Image offset: {img_offset}")


# Get PDF bytes untill the end of last object
# 💡 PDF things: https://web.archive.org/web/20141010035745/http://gnupdf.org/Introduction_to_PDF
# 📄 PDF spec: https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf
pdf_file = open("./test_data/time-machine.pdf", "rb")

# 1. get cross-reference table offset

# - Find %%EOF marker
# - Each character is exactly one byte

eof_offset = 0
for i in range(-5, -512, -1):
    pdf_file.seek(i, os.SEEK_END)
    tmp = pdf_file.read(5)
    if (tmp == b"%%EOF"):
        eof_offset = i
        break

if eof_offset == 0:
    raise Exception("No %%EOF marker found")

# - Go back byte by byte and find the "startxref" marker

xref_table_addr = 0
for i in range(min(eof_offset, -9), -128, -1):
    pdf_file.seek(i, os.SEEK_END)
    tmp = pdf_file.read(9)
    if (tmp == b"startxref"):
        # Take into account 1 byte \n character at the beginning and the end
        xref_addr_offset = i + 9 + 1
        xref_addr_length = (eof_offset - xref_addr_offset - 1)

        pdf_file.seek(xref_addr_offset, os.SEEK_END)
        xref_table_addr = int(pdf_file.read(xref_addr_length))

if xref_table_addr == 0:
    raise Exception("No startxref marker found")

# 2. Get cross-reference table

pdf_file.seek(xref_table_addr, os.SEEK_SET)
for i, line in enumerate(pdf_file):
    if i == 0 and line != b"xref\n":
        raise Exception(
            "No xref keyword found on the first line of the cross-reference table at given address")

    print(line)


# pdf_file.seek(xref_table_offset, os.SEEK_SET)
# for line in pdf_file:
#     print(line)
