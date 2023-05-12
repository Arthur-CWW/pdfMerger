# pdf_utils/merge_pdfs.py
import argparse
from pypdf import PdfWriter
import click
from glob import glob
from os import path





@click.command()
@click.argument("pdf_files",nargs=-1,type=click.Path(exists=True)  )
@click.option( '-o','--output',  default=f'{path.basename(path.abspath("."))}.pdf', help='Output file name (default: current directory name)')
def merge(pdf_files, output):
    if not pdf_files:
        # If no PDF files are provided in the command line, get all PDF files in the current directory
        pdf_files = glob("*.pdf")
        if not pdf_files:
            click.echo("No PDF files found in the current directory.")
            return
    with PdfWriter() as merger:
        for i, pdf_file in enumerate(pdf_files):
            filename = pdf_file.split(".pdf")[0]
            merger.append(pdf_file, outline_item=filename)
        merger.write(output)

if __name__ == '__main__':
    merge()
