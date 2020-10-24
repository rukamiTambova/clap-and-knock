from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTAnno
import os
def label_func():
    return '1. Определение'

labels_txt = open('labels.txt', 'w')

for page_layout in extract_pages("text1.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                if isinstance(element, LTTextContainer):
                    if str(LTTextContainer.get_text(self=text_line)).startswith(label_func()):
                        print(str(LTTextContainer.get_text(self=text_line)))

