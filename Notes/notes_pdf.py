from fpdf import FPDF
import pandas as pd

# Create a PDF document
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Load the data
data = pd.read_csv('topics.csv')
break_line = 250
cell_height = 25
# Create a PDF document
for _, row in data.iterrows():
    # Create the first page
    pdf.add_page()
    pdf.set_font('Times', size=25, style='B')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=cell_height, txt=row['Topic'], border=0, ln=1, align='L')
    # Add a grid
    for rg in range(30,290,10):
        pdf.line(10, rg, 200, rg)
    # Add a break line and footer
    pdf.ln(break_line)
    pdf.set_font('Times', size=8, style='I')
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=8, txt=row['Topic'], border=0, align='R')
    
    # Add the remaining pages
    for i in range(row['Pages']-1):
        pdf.add_page()
        # Add a grid
        for rg in range(20,290,10):
            pdf.line(10, rg, 200, rg)
        # Add a break line and footer
        pdf.ln(break_line+cell_height)
        pdf.set_font('Times', size=8, style='I')
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, txt=row['Topic'], border=0, align='R')

pdf.output('output.pdf')
# This 