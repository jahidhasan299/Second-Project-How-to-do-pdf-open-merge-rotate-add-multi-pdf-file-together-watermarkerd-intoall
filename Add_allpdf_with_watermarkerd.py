import PyPDF2
original_pdf = PyPDF2.PdfFileReader(open("Add_all_Pdf.pdf","rb"))
watermark_pdf = PyPDF2.PdfFileReader(open("watermarkered.pdf", "rb"))
output = PyPDF2.PdfFileWriter()
for i in range (original_pdf.getNumPages()):
    page = original_pdf.getPage(i)
    page.mergePage(watermark_pdf.getPage(0))
    output.addPage(page)
with open("Watermarked_output.pdf","wb") as file:
    output.write(file)

