from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf(name)

def pdf(n):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(80)
    pdf.cell(25, 50, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", 11, 70, 190)
    pdf.set_font('helvetica', 'B', 24)
    pdf.set_text_color(225)
    pdf.cell(-15, 255, f"{n} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()
