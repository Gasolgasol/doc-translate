from reportlab.pdfgen.canvas import Canvas
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth
from textwrap import wrap
from tika import parser
from easynmt import EasyNMT
model = EasyNMT('opus-mt')



PAGE_WIDTH  = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]

raw = parser.from_file('pdf-test.pdf')

  
c = Canvas("ura.pdf")
t = c.beginText()
t.setFont('Helvetica-Bold', 10)
t.setCharSpace(3)
t.setTextOrigin(50, 800)
#text =  raw['content']#"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
text = model.translate(raw['content'], target_lang='es')


wraped_text = "\n".join(wrap(text, 65)) # 80 is line width
t.textLines(wraped_text)
c.drawText(t)
c.showPage()
c.save()

#canvas.save()