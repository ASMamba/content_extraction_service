import pathlib,sys,base64
from typing import List
from extractor_pymudf import *
# filename="CrowdStrikeGlobalThreatReport2025.pdf"
filename="Receipr.pdf"

if __name__ == "__main__":
    """When using the script as a CLI program."""
    print("inside main")
    extractor = PDFExtractor(pdf_path=filename,extract_output_dir="./output")
    for page_num in range(len(extractor.doc)):
        if page_num == 9:
            page = extractor.doc[page_num]
            extractor.extract_page_with_order(page=page,page_num=page_num)


    # output document text as one string