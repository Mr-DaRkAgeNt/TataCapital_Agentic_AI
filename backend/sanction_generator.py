from reportlab.pdfgen import canvas
import os

def generate_pdf(name, amount):
    filename = f"Sanction_Letter_{name}.pdf"
    path = os.path.join("static", filename)
    
    # Ensure static folder exists
    if not os.path.exists("static"):
        os.makedirs("static")

    c = canvas.Canvas(path)
    c.drawString(100, 800, "TATA CAPITAL - LOAN SANCTION LETTER")
    c.drawString(100, 780, "-----------------------------------")
    c.drawString(100, 750, f"Dear {name},")
    c.drawString(100, 730, f"We are pleased to approve your loan of Rs. {amount}.")
    c.drawString(100, 710, "Interest Rate: 10.5% p.a.")
    c.drawString(100, 690, "Tenure: 48 Months")
    c.drawString(100, 650, "Authorized Signatory,")
    c.drawString(100, 630, "Tata Capital AI Division")
    c.save()
    return filename