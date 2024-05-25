import pandas as pd
import glob
from os import sep
from os.path import join
from pathlib import Path
from fpdf import FPDF
from datetime import datetime

filepaths = glob.glob('/home/PDF/Invoices/invoices/*.xlsx')

for file in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    # Get the invoice number and date
    filename = Path(file).stem
    inv_id, date = filename.split('-')
    date = datetime.strptime(date, '%Y.%m.%d').strftime('%d/%m/%Y')
    
    # Create the first page
    pdf.add_page()
    # Add the invoice number
    pdf.set_font('Times', size=16, style='B')
    text = f"Invoice nb: {inv_id}"
    pdf.cell(w=50, h=8, txt=text, border=0, ln=1, align='L')
    # Add the date
    pdf.set_font('Times', size=16, style='B')
    text = f"Date: {date}"
    pdf.cell(w=50, h=8, txt=text, border=0, ln=1, align='L')
    pdf.ln(10)
    
    # Set up the table
    df = pd.read_excel(file)
    cols = ["Product ID","Product Name","Amount","Price per Unit","Total Price"]
    width_col = [30, 70, 30, 30, 30]
    
    # Add the headers
    pdf.set_font('Times', size=12, style='B')
    for width,col in zip(width_col,cols):
        pdf.cell(w=width, h=8, txt=col, border=1, ln=0, align='L')
    pdf.ln(8)
    
    # Add the data
    pdf.set_font('Times', size=11)
    for idx, row in df.iterrows():
        for width,col in zip(width_col,df.columns):
            pdf.cell(w=width, h=8, txt=str(row[col]), border=1, ln=0, align='L')
        pdf.ln(8)
        
    # Add the total price
    total_price = str(df["total_price"].sum())
    last_row = ["","","","",total_price]
    for width,col in zip(width_col,last_row):
        pdf.cell(w=width, h=8, txt=col, border=1, ln=0, align='L')
    
    # Add the summary
    pdf.ln(24)
    pdf.set_font('Times', size=12, style='B')
    pdf.cell(w=0, h=8, txt=f"The total due amount is {total_price} Euros.", border=0, ln=1, align='L')
    # Add the company name and logo
    pdf.cell(w=30, h=8, txt="PythonHow")
    pdf.image("/home/PDF/Invoices/images/pythonhow.png",w=10,x=33,y=91)
    
    # Save pdfs
    parent_path = str(Path(file).parent).rsplit(sep, 1)[0]
    pdf.output(join(parent_path,"pdfs",f"{filename}.pdf"))