from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(patient, prediction, probability, summary, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b><font size=20>🏥 MedIntel</font></b>", styles["Title"]))

    story.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/><b>Patient Information</b>", styles["Heading2"]))

    for key, value in patient.items():
        story.append(
            Paragraph(f"<b>{key.replace('_',' ').title()}:</b> {value}", styles["Normal"])
        )

    story.append(Paragraph("<br/><b>Prediction</b>", styles["Heading2"]))

    result = "High Diabetes Risk" if prediction else "Low Diabetes Risk"

    story.append(
        Paragraph(f"<b>Prediction:</b> {result}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Risk Probability:</b> {probability*100:.2f}%", styles["Normal"])
    )

    story.append(Paragraph("<br/><b>AI Clinical Summary</b>", styles["Heading2"]))

    # Preserve line breaks from Gemini response
    for line in summary.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>Disclaimer:</b> This report is generated for educational purposes only and is not a medical diagnosis.",
            styles["Italic"]
        )
    )

    doc.build(story)