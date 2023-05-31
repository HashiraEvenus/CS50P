from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica","B",size = 50)
        self.text(37,40,"CS50 Shirtificate")
#name = input("Name:")
pdf = PDF()
#Get input
text = input("Name:")



#Add a new page and the image
pdf.add_page()
pdf.image("shirtificate.png",x=00,y=60)

#Set the font and the color before text input
pdf.set_font('helvetica', size = 30)
pdf.set_text_color(255,255,255)
#calculate input's width
text_width = pdf.get_string_width(text + " took CS50")

#centralize it
x = (pdf.w - text_width)/2
#Put the text
pdf.text(x,120,text+"took CS50")
#Output new file
pdf.output("shirtificate.pdf")
