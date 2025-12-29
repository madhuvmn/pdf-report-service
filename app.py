from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------------- FONT REGISTRATION ----------------
TELUGU_FONT_NAME = "NotoSerifTelugu"
TELUGU_FONT_FILE = "NotoSerifTelugu-Regular.ttf"

pdfmetrics.registerFont(TTFont(TELUGU_FONT_NAME, TELUGU_FONT_FILE))

# ---------------- PDF FILE ----------------
output_pdf = "monthly_report_telugu.pdf"
doc = SimpleDocTemplate(
    output_pdf,
    pagesize=A4,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36,
)

styles = getSampleStyleSheet()

# Override default style to support Telugu
styles["Normal"].fontName = TELUGU_FONT_NAME
styles["Normal"].fontSize = 10

title_style = ParagraphStyle(
    name="TitleStyle",
    fontName=TELUGU_FONT_NAME,
    fontSize=14,
    alignment=1,  # center
    spaceAfter=12
)

elements = []

# ---------------- TITLE ----------------
elements.append(Paragraph("Monthly Report", title_style))
elements.append(Paragraph("Generated using Python only", styles["Normal"]))

# ---------------- HARD-CODED DATA ----------------
table_data = [
    ["ID", "Name", "Amount"],
    ["1", "వడ్లమాని. రాఘవులు నాయుడు", "5000"],
    ["2", "కుట్టుబోయిన. వరలక్ష్మమ్మ", "4200"],
    ["3", "చిట్టిబోయిన. వెంకటేశ్వర్లు", "6100"],
]

# Convert text cells to Paragraph (IMPORTANT for Unicode)
formatted_data = []
for row in table_data:
    formatted_row = []
    for cell in row:
        formatted_row.append(Paragraph(str(cell), styles["Normal"]))
    formatted_data.append(formatted_row)

# ---------------- TABLE ----------------
table = Table(formatted_data, colWidths=[50, 300, 100])

table.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ("ALIGN", (2, 1), (2, -1), "RIGHT"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))

elements.append(table)

# ---------------- BUILD PDF ----------------
doc.build(elements)

print(f"PDF generated successfully: {output_pdf}")
