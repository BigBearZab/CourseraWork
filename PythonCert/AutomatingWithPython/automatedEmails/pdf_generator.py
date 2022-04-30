# example pdf generation script
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

def flatten_dict(d):
    return [[k,v] for k,v in d.items()]

def generate_pie_chart(dict_to_chart):
    report_pie = Pie(width=3*2.5, height=3*2.5)
    report_pie.data = [dict_to_chart[d] for d in sorted(dict_to_chart)]
    report_pie.labels = [d for d in sorted(dict_to_chart)]
    chart = Drawing()
    chart.add(report_pie)
    return chart

def generate_report(path, dict_for_table):
    report = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()
    report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data=flatten_dict(dict_for_table),style=table_style,hAlign="LEFT")
    report_chart = generate_pie_chart(dict_for_table)
    report.build([report_title, report_table, report_chart])

def main():
    print('Creating report')
    generate_report('report.pdf', fruit)

if __name__ == "__main__":
    main()

# generate_pie_chart(fruit)