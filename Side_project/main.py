from fpdf import FPDF
import glob
from pathlib import Path

filepaths = sorted(glob.glob('/home/PDF/Side_project/Text+Files/*.txt'))
# Create a PDF document
pdf = FPDF(orientation='P', unit='mm', format='A4')

for file in filepaths:
    # Get the name of the file
    filename = Path(file).stem.capitalize()
    
    # Add the page
    pdf.add_page()
    pdf.set_font('Times', size=25, style='B')
    pdf.cell(w=0, h=20, txt=filename, border=0, ln=1, align='L')
    
    # Add the content
    with open(file, 'r') as f:
        content = f.read()
    pdf.set_font('Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content, border=0, align='J')
    
# Convert to pdf
pdf.output('output.pdf')
    