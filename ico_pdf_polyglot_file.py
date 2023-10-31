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

xref_table = []
last_id = -1
pdf_file.seek(xref_table_addr, os.SEEK_SET)
for i, line in enumerate(pdf_file):
    if i == 0 and line != b"xref\n":
        # Note: This might happend if the PDF file uses cross-reference stream, which were introduced in PDF 1.5
        # This script does not support them to keep it simple (Most PDF files are using cross-reference tables, anyway)
        # See: https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf#page=57
        raise Exception("No xref keyword found on the x-ref table address")

    if i == 1:
        # Find last object id
        vals_str = line.decode().rstrip().split(" ")
        [first_id, objects_count] = [int(i) for i in vals_str]

        # print([first_id, objects_count])
        last_id = first_id + objects_count
        break

# 3. Get end of the last object before xref table

last_obj_end_offset = -1
for i in range(xref_table_addr, xref_table_addr - 10, -1):
    pdf_file.seek(i, os.SEEK_SET)
    if pdf_file.read(6) == b'endobj':
        last_obj_end_offset = pdf_file.tell()

print(f"Last object end offset: {last_obj_end_offset}")


# 4. Write this into the new polyglot file

# 5. Create ico data obj and write into the new polyglot file

# 6. Write rest of the PDF input into the new polyglot file

# 7. Adjust some values - to find out which

# https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf#page=49

# 3. Write PDF bytes until last end_of_last_object_offset to the ICO file
# 4. Write ICO bytes from img_offset to the end of the file
# 5. Write PDF bytes from end_of_last_object_offset to the end of the file
# 6. Fix ICO image offset in the ICONDIRENTRY structure
# 7. Save new ico-pdf polyglot file
