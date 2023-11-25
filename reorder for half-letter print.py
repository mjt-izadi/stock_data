import numpy as np
from pypdf import PdfReader, PdfWriter


def find_new_order(n_pages):
    len_new = np.int8(np.ceil(n_pages / 4)) * 4
    new_order = np.reshape(np.array([[4 * j + 1, 4 * j + 3,
                                      4 * j + 4, 4 * j + 2]
                                      for j in range(len_new // 4)]),
                           (len_new,))
    new_order[new_order > n_pages] = 0
    return(new_order)

file_path = "/Users/"
file_name = "file.pdf"
file = file_path + file_name
reordered_file = file[:-4] + "_reordered.pdf"

pdf_reader = PdfReader(file)
pdf_writer = PdfWriter()

total_pages = len(pdf_reader.pages)
new_order = find_new_order(total_pages)

for page in new_order:
    print(page)
    if page == 0:
        pdf_writer.add_blank_page()
    else:
        pdf_writer.add_page(pdf_reader.pages[int(page - 1)])

with open(reordered_file, 'wb') as fh:
    pdf_writer.write(fh)