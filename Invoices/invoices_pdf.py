import pandas as pd
import glob
from os import sep
from pathlib import Path
from fpdf import FPDF
from datetime import datetime

filepaths = glob.glob('/home/PDF/Invoices/invoices/*.xlsx')

for file in filepaths:
    df = pd.read_excel(file)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    # Get the invoice number and date
    inv_id, date = Path(file).stem.split('-')
    date = datetime.strptime(date, '%Y.%m.%d').strftime('%d/%m/%Y')
    print(inv_id,date)
    
    # Create the first page
    pdf.add_page()
    # Add the invoice number
    pdf.set_font('Times', size=25, style='B')
    text = f"Invoice nbr: {inv_id}"
    pdf.cell(w=0, h=20, txt=text, border=0, ln=1, align='L')
    # Add the date
    pdf.set_font('Times', size=25, style='B')
    text = f"Date: {date}"
    pdf.cell(w=0, h=8, txt=text, border=0, ln=1, align='L')
    pdf.ln(10)
    # Add the table
    pdf.set_font('Times', size=12, style='B')
    
    
    
    
    
    pdf.output(f"{file.rsplit('.',1)[0]}.pdf")