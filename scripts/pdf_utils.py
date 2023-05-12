# pdf_utils/merge_pdfs.py
import argparse
from pypdf import PdfWriter




def mergePdfs(pdf_files, output_file):
    with PdfWriter() as merger:
        for i, pdf_file in enumerate(pdf_files):
            # Get the base filename without the extension
            filename = pdf_file.split(".pdf")[0]
            merger.append(pdf_file, outline_item=filename)
        merger.write(output_file)

def main():
    # Create the CLI parser
    parser = argparse.ArgumentParser(
        description='Merge PDF files and add bookmarks based on their names.')
    parser.add_argument('pdf_files', nargs='+', help='PDF files to merge')
    parser.add_argument('-o',
                        '--output',
                        default='combined.pdf',
                        help='Output file name (default: combined.pdf)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Merge the PDFs with bookmarks
    mergePdfs(args.pdf_files, args.output)


if __name__ == '__main__':
    main()
