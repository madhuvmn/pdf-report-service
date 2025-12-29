from flask import Flask, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "PDF Report Service is running"

@app.route("/generate-pdf")
def generate_pdf():
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Monthly Report", styles["Title"]))
    elements.append(Paragraph("Generated using Python only", styles["Normal"]))

    table_data = [
        ["ID", "Name", "Amount"],
        ["1", "వెలినేని. మధుసూదన్", "5000"],
        ["2", "వడ్లమాని. మధు బాబు", "4200"]
    ]

    elements.append(Table(table_data))
    doc.build(elements)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="report.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run()

