#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os
import re

def text_to_dict(text_file):
    with open(text_file, 'r') as f:
        out_ls = [line.strip('\n') for line in f.readlines()]
        out_dict = {
            "name":out_ls[0],
            "weight":int(re.findall(r'\d+ ',out_ls[1])[0].strip()),
            "description":out_ls[2],
            "image_name":re.sub('txt','jpeg',text_file)
        }
    return out_dict

def generate_body():
    body = ""
    for file in os.listdir('supplier-data/descriptions/'):
        t = text_to_dict('supplier-data/descriptions/'+file)
        body += f"""
        \n
        name: {t['name']}\n
        weight: {t['weight']} lbs
        """
    return body


def generate_report():
    text = generate_body()
    report = SimpleDocTemplate("processed.pdf")
    styles = getSampleStyleSheet()
    report_title = Paragraph(f"Processed Update on {datetime.date.today()}", styles["h1"])
    report_body = Paragraph(text)
    report.build([report_title, report_body])

if __name__ == "__main__":
    generate_report()