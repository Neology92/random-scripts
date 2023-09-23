# Inspired with https://github.com/tickelton/ico-pdf repo
# and related PagedOut article: https://pagedout.institute/download/PagedOut_001_beta1.pdf (page 14)

import struct


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


# 💡 PDF things: https://web.archive.org/web/20141010035745/http://gnupdf.org/Introduction_to_PDF
