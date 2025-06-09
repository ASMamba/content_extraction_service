import pymupdf,pymupdf4llm

from pymupdf4llm.helpers.multi_column import column_boxes
from pymupdf4llm.helpers.get_text_lines import get_text_lines
import pathlib
from pathlib import Path
import fitz

class PDFExtractor:
    def __init__(self, pdf_path: str, extract_output_dir: str = "pa.md"):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.extract_output_dir = Path(extract_output_dir)
        self.extract_output_dir.mkdir(exist_ok=True)

    def get_page_text(self,page):
        """Extract plain text respecting any page columns."""
        alltext = ""  # result text goes in here

         # ensure automatic resolution of hyphenated words
        flags = pymupdf.TEXT_DEHYPHENATE

        # make a TextPage object to ensure optimum performance
        tp = page.get_textpage(flags=flags)

        # identify text blocks that respect page columns
        text_blocks = column_boxes(page, textpage=tp)

        # separately extract, then join text per column block
        for block in text_blocks:
            text = get_text_lines(page, textpage=tp, clip=block)
            alltext += text

        # return text of the page
        return alltext    
    
    def extract_page_with_order(self, page: fitz.Page, page_num: int) -> str:
        print(f'page number {page_num}')
        md_text = self.get_page_text(page)
        outname =f"MD-page-{page_num + 1}.md"
        pathlib.Path(outname).write_bytes(md_text.encode())
        # print(md_text)
        # output document markdown text as one string
        return outname
    
    def all_mardown(self):
        md_text = pymupdf4llm.to_markdown(self.pdf_path)
        print(md_text)
        # output document markdown text as one string
        pathlib.Path("pa.md").write_bytes(md_text.encode())    
