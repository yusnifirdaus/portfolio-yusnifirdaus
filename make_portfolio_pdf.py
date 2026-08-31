from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).parent
OUT = ROOT / 'output' / 'pdf' / 'muhammad-yusni-firdaus-portfolio.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)

try:
    pdfmetrics.registerFont(TTFont('PortfolioSans', r'C:\Windows\Fonts\arial.ttf'))
    BODY_FONT = 'PortfolioSans'
except Exception:
    BODY_FONT = 'Helvetica'

INK = colors.HexColor('#172c32')
TEAL = colors.HexColor('#25b9b1')
PALE = colors.HexColor('#eef8f6')
MUTED = colors.HexColor('#58747a')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Kicker', parent=styles['Normal'], fontName=BODY_FONT, fontSize=8, leading=11, textColor=TEAL, spaceAfter=8))
styles.add(ParagraphStyle(name='TitleBig', parent=styles['Title'], fontName=BODY_FONT, fontSize=36, leading=38, textColor=INK, spaceAfter=14))
styles.add(ParagraphStyle(name='Heading', parent=styles['Heading2'], fontName=BODY_FONT, fontSize=25, leading=27, textColor=INK, spaceAfter=12))
styles.add(ParagraphStyle(name='BodyClean', parent=styles['BodyText'], fontName=BODY_FONT, fontSize=10, leading=16, textColor=MUTED, spaceAfter=8))
styles.add(ParagraphStyle(name='CardTitle', parent=styles['Heading3'], fontName=BODY_FONT, fontSize=12, leading=14, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name='Small', parent=styles['Normal'], fontName=BODY_FONT, fontSize=8, leading=11, textColor=MUTED))

def photo(name, width, height):
    path = ROOT / name
    if not path.exists():
        return Spacer(width, height)
    img = Image(str(path), width=width, height=height)
    img.hAlign = 'CENTER'
    return img

def page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PALE if doc.page == 1 else colors.white)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setFillColor(MUTED)
    canvas.setFont(BODY_FONT, 7)
    canvas.drawString(18*mm, 12*mm, 'MUHAMMAD YUSNI FIRDAUS')
    canvas.drawRightString(A4[0]-18*mm, 12*mm, f'{doc.page:02d}')
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=18*mm, bottomMargin=20*mm)
story = []

story += [Spacer(1, 13*mm), Paragraph('PORTFOLIO / 2026', styles['Kicker']), Paragraph('Muhammad Yusni<br/>Firdaus.', styles['TitleBig']), Paragraph('Video Editor  ×  Photographer', styles['Heading']), Paragraph('Saya mengubah momen, cerita, dan ide menjadi visual yang terasa dekat—lewat editing video dan fotografi.', styles['BodyClean']), Spacer(1, 7*mm), photo('Yuu.jpg', 72*mm, 92*mm), Spacer(1, 10*mm), Paragraph('Tentang saya', styles['CardTitle']), Paragraph('Saya tertarik pada proses menyusun footage, menangkap suasana melalui foto, dan mengeksplorasi typography sebagai bagian dari komunikasi visual.', styles['BodyClean']), PageBreak()]

story += [Paragraph('PHOTOGRAPHY ARCHIVE / 01', styles['Kicker']), Paragraph('Frames that stay.', styles['Heading']), Paragraph('Kumpulan foto pilihan yang menangkap cahaya, suasana, dan cerita di balik momen sehari-hari.', styles['BodyClean']), Spacer(1, 5*mm)]
photo_names = ['20260519_183750.jpg', '20260705_173328.jpg', '20260716_173540.jpg', '20260730_181512.jpg']
cells = [photo(n, 39*mm, 60*mm) for n in photo_names]
table = Table([cells[:2], cells[2:]], colWidths=[82*mm, 82*mm], rowHeights=[68*mm, 68*mm], hAlign='CENTER')
table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('INNERGRID',(0,0),(-1,-1),5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
story += [table, Spacer(1, 8*mm), Paragraph('Visual language: light, geometry, atmosphere.', styles['Small']), PageBreak()]

story += [Paragraph('VIDEO EDITING ARCHIVE / 02', styles['Kicker']), Paragraph('Motion that moves.', styles['Heading']), Paragraph('Beragam cerita yang dirangkai lewat editing—mulai dari talking head, kegiatan sekolah, perjalanan jalan-jalan, hingga dunia Roblox.', styles['BodyClean']), Spacer(1, 5*mm)]
video_rows = [[Paragraph('01  Talking Head Edit', styles['CardTitle']), Paragraph('02  School Days', styles['CardTitle']), Paragraph('03  Jalan-Jalan', styles['CardTitle']), Paragraph('04  Roblox World', styles['CardTitle'])], [Paragraph('<font color="#25b9b1" size="18">PLAY</font><br/><br/>Local video edits', styles['BodyClean']), Paragraph('<font color="#25b9b1" size="18">PLAY</font><br/><br/>Instagram reels', styles['BodyClean']), Paragraph('<font color="#25b9b1" size="18">PLAY</font><br/><br/>Instagram reels', styles['BodyClean']), Paragraph('<font color="#25b9b1" size="18">PLAY</font><br/><br/>TikTok edits', styles['BodyClean'])], [Paragraph('2 local video versions', styles['Small']), Paragraph('<link href="https://www.instagram.com/reel/DSuf7CxCYMl/" color="#25aaa4">Open 5 video projects</link>', styles['Small']), Paragraph('<link href="https://www.instagram.com/reel/CvT47VZv35D/" color="#25aaa4">Open 4 video projects</link>', styles['Small']), Paragraph('<link href="https://www.tiktok.com/@yuujooo12/video/7638506124433493256" color="#25aaa4">Open 7 video projects</link>', styles['Small'])]]
vt = Table(video_rows, colWidths=[42*mm]*4, rowHeights=[10*mm, 68*mm, 14*mm], hAlign='CENTER')
vt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.5,colors.HexColor('#c9e1df')),('INNERGRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]))
story += [vt, Spacer(1, 10*mm), Paragraph('Video playback remains available through the original TikTok and Instagram links on the website.', styles['Small']), PageBreak()]

story += [Paragraph('TYPOGRAPHY ARCHIVE / 03', styles['Kicker']), Paragraph('Letters that speak.', styles['Heading']), Paragraph('Eksplorasi typography melalui susunan huruf, anotasi, warna, dan komposisi visual yang komunikatif.', styles['BodyClean']), Spacer(1, 4*mm)]
type_names = ['cf405fb3eb16cba7.jpg','9e7f1e6e93e73c4b.jpg','362ff972e2f0399e.jpg','655a4c6e93fbb1de.jpg','5c8c84e396f616fc.jpg','ac424de06f55e39a.jpg']
type_cells = [photo(n, 39*mm, 53*mm) for n in type_names]
tt = Table([type_cells[:3], type_cells[3:]], colWidths=[55*mm]*3, rowHeights=[60*mm,60*mm], hAlign='CENTER')
tt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('INNERGRID',(0,0),(-1,-1),4,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
story += [tt, Spacer(1, 9*mm), Paragraph('SKILLS', styles['Kicker']), Paragraph('Sosial Media  ·  Office  ·  Photography & Videography  ·  Editing Video  ·  Public Speaking', styles['BodyClean']), Spacer(1, 5*mm), Paragraph('CONTACT ME', styles['Kicker']), Paragraph('Terbuka untuk kolaborasi kreatif dan proyek visual.', styles['BodyClean']), Paragraph('Instagram: yusnifirdaus<br/>TikTok: yuujooo12<br/>Email: yusnifirdaus@gmail.com', styles['BodyClean'])]

doc.build(story, onFirstPage=page_bg, onLaterPages=page_bg)
print(OUT)
