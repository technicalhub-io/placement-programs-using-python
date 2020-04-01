import fpdf
import csv
with open("data1.csv")as f1:
    records=list(csv.reader(f1))

pdf=fpdf.FPDF()

for i in records[1:]:
    pdf.add_page()
    pdf.image("img.jpg",0,0,210,297)
    pdf.set_font("Times","B",12)
    pdf.set_xy(100,100)
    pdf.cell(0,0,i[1])
    
pdf.output("download.pdf")
