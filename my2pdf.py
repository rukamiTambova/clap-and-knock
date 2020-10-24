from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTAnno
import os

labels_txt = open('labels.txt', 'w')

for page_layout in extract_pages("text1.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                if isinstance(element, LTTextContainer):
                    #print(text_line)
                    for character in text_line:
                        if isinstance(character, LTChar):
                            if character.size == 20:
                                txt = str(text_line.get_text())
                                print(txt)
                                labels_txt.write(txt)
                                labels_txt.write(txt+'\n')
                                break



