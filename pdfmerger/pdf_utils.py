# pdf_utils/merge_pdfs.py
import argparse
from pypdf import PdfWriter
import click
from glob import glob




@click.command()
@click.argument("pdf_files",nargs=-1,type=click.Path(exists=True)  )
@click.option( '-o','--output',  default='combined.pdf', help='Output file name (default: combined.pdf)')
def merge(pdf_files, output):
    with PdfWriter() as merger:
        for i, pdf_file in enumerate(pdf_files):
            # Get the base filename without the extension
            filename = pdf_file.split(".pdf")[0]
            merger.append(pdf_file, outline_item=filename)
        merger.write(output)

if __name__ == '__main__':
    merge()
