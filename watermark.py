import fitz
import numpy as np


def remove_img_on_pdf(idoc, page):
    img_list = idoc.getPageImageList(page)
    b = [(13, 0, 120, 74, 8, 'DeviceRGB', '', 'Image1', 'DCTDecode')]
    b = np.array(b)
    for x in img_list:
        for y in b:
            if img_list[x] == b[y]:
                img_removal = img_list[x]
            else:
                continue
            print(img_removal)

    con_list = idoc[page].get_contents()

    for i in con_list:
        c = idoc.xref_stream(i)
        if c != None:
            for v in img_removal:
                arr = bytes(v[7], 'utf-8')
                r = c.find(arr)
                if r != -1:
                    cnew = c.replace(arr, b"")
                    idoc.update_stream(i, cnew)
                    c = idoc.xref_stream(i)
    return idoc


doc = fitz.open('ELN_Mod3AzDOCUMENTS.PDF')
for i in range(doc.page_count):
    rdoc = remove_img_on_pdf(doc, i) 
    rdoc.save('no_img_example.pdf')