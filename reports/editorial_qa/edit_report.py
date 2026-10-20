from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path
from zipfile import ZipFile
import re

root=Path(__file__).resolve().parents[1]
src=root/'Data_Driven_Process_Improvement_Report_RAW.docx'
out=root/'Data_Driven_Process_Improvement_Report_EDITED.docx'
d=Document(src)
ps=list(d.paragraphs)
edits={
0:'School Exam Analytics Report',
6:'1 Performance Snapshot',
8:'Snapshot Interpretation',
9:'The average exam score is 67.25, which this report considers unsatisfactory. The 6,378 students have an average attendance rate of 80%. The analysis identifies a strong correlation between attendance and exam scores, making attendance a priority for more effective monitoring and enforcement.',
10:'2 Introduction',
12:'This report examines exam-related data to inform decisions about student performance. Building on the performance snapshot, it identifies opportunities to improve attendance within the school.',
13:'3 Primary Focus',
14:'Attendance is the primary focus because it is a factor the school can work to improve through enforcement.',
15:'4 Findings and Visual Evidence',
16:'4.1 Attendance',
18:'4.2 Hours Studied',
20:'4.3 Access to Resources',
23:'5 Improvement Opportunities',
24:'5.1 Attendance',
25:'The analysis identifies attendance as a problem associated with exam scores. Attendance Works states that students who missed 2 to 4 days in September were 5 times more likely to be chronically absent during the year than those who missed fewer than 2 days [1]. This highlights the risk that attendance problems can compound alongside declining grades. The California Department of Education emphasizes the importance of ensuring that everyone in the school system understands the positive and negative effects of attendance [2]. The proposed actions are to focus more closely on barriers to attendance and to explain in each class both the expectation to attend and why attendance matters.',
29:'5.2 Hours Studied',
30:'The analysis identifies hours studied as an important factor associated with exam scores, with marginal increases in scores as study hours rise. However, study quality and study quantity are distinct considerations. Proposed approaches include a dedicated study hall and greater awareness of effective study habits. The UNC Learning Center offers guidance on improving both the amount of time spent studying and how that time is used [3]. The report also notes cases in which students studied extensively but received low scores, suggesting poor study habits or a lack of honesty on the test as possible explanations.',
32:'5.3 Access to Resources',
33:'The chart shows the correlation between access to resources and exam scores. The Stanford Report discusses the disadvantages that a lack of resources can create [4]. Drawing on its guidance, the proposed approach is to ask students to identify the best resources available to them, whether through the school or elsewhere. This information could help the school allocate resources more efficiently to students who need them.',
35:'6 Closing Remarks',
36:'School faculty have limits on what they can accomplish, but sharing these findings with both staff and students can make an impact. Students are regularly told to attend school; explaining the reasons through data can help them understand why attendance matters.',
38:'The next steps are to increase awareness of attendance and study habits, provide more study time within classes, and secure additional funding to support students with limited access to resources.',
40:'Because this analysis uses synthetic data, it cannot by itself justify action in a real school. Data also provide only part of the picture. Meaningful change requires an understanding of the school’s existing support and practices. The analysis can serve as a starting point; examining specific problems in greater detail can help identify the most appropriate course of action.'
}
for i,text in edits.items(): ps[i].text=text
ps[0].style='Title'
ps[35].style='Heading 1'
for i in (25,36,38,40): ps[i].style='Normal'
for i in (11,19,27,28,31,34): ps[i]._element.getparent().remove(ps[i]._element)
# Remove unused template instructions, while retaining all substantive tables.
d.tables[-1]._element.getparent().remove(d.tables[-1]._element)
for p in list(d.paragraphs):
    if not p.text.strip() and not p._p.xpath('.//w:drawing'): p._element.getparent().remove(p._element)
tables=d.tables
tables[0].cell(0,1).text='Stakeholders'
tables[0].cell(3,1).text='10/12/2026'
for c,t in zip(tables[1].rows[0].cells,['Average exam score','Student count','Average attendance (%)']): c.text=t
cap=ps[8].insert_paragraph_before('Table 1. Student performance snapshot',style='Caption')
tables[1]._element.addprevious(cap._element)
captions=['Figure 1. Attendance and exam scores','Figure 2. Average exam score by hours studied','Figure 3. Access to resources and correlation with exam scores']
interpretations=[
'Of the factors examined, attendance has the strongest correlation with exam scores. Higher attendance is associated with higher exam scores, which the report interprets as an indication of higher-quality education. The report also raises the possibility that the exams are too difficult; the chart nevertheless shows that higher attendance is associated with higher grades.',
'The analysis shows a strong correlation between hours studied and exam scores, underscoring the importance of time spent studying.',
'The chart shows substantial differences in the correlation with exam scores across high, medium, and low levels of resource access. The report interprets this pattern as indicating that grades decline substantially as access to resources decreases.'
]
for t,caption,body in zip(tables[2:],captions,interpretations):
    cell=t.cell(0,0)
    drawing=next(p for p in cell.paragraphs if p._p.xpath('.//w:drawing'))
    for p in list(cell.paragraphs):
        if p is not drawing and p._p is not drawing._p: p._element.getparent().remove(p._element)
    p=drawing.insert_paragraph_before(caption,style='Caption')
    cell.add_paragraph(body)
    for row in t.rows: row.height=None
    for p in cell.paragraphs: p.paragraph_format.keep_with_next=True
    cell.paragraphs[-1].paragraph_format.keep_with_next=False

d.add_heading('7 References',level=1)
refs=[
'[1] Attendance Works. “10 Facts About School Attendance.” https://www.attendanceworks.org/chronic-absence/the-problem/10-facts-about-school-attendance/',
'[2] California Department of Education. “School Attendance Improvement Strategies.” https://www.cde.ca.gov/ls/ai/cw/attendstrategy.asp',
'[3] UNC Learning Center. “Studying 101: Study Smarter Not Harder.” https://learningcenter.unc.edu/tips-and-tools/studying-101-study-smarter-not-harder/',
'[4] Stanford Report. “Studying more strategically equals improved exam scores.” https://news.stanford.edu/stories/2017/05/studying-strategically-equals-improved-exam-scores'
]
for ref in refs:
    d.add_paragraph(ref)
    p=d.add_paragraph('Citation incomplete: publication date and individual author details, if applicable, were not supplied.')
    for r in p.runs: r.italic=True; r.font.size=Pt(9)

for name in ('Normal','Template Label','Caption','Title','Heading 1','Heading 2'):
    st=d.styles[name]; st.font.name='Calibri'; st.font.color.rgb=RGBColor(0,0,0)
    st.font.size=Pt({'Title':24,'Heading 1':16,'Heading 2':12,'Caption':10}.get(name,11))
    st.paragraph_format.space_after=Pt(7)
    st.paragraph_format.line_spacing=1.08
for s in d.sections:
    s.top_margin=s.bottom_margin=Inches(.65)
    s.left_margin=s.right_margin=Inches(.75)
for p in d.paragraphs:
    p.paragraph_format.page_break_before=False
    for r in p.runs: r.font.name='Calibri'; r.font.color.rgb=RGBColor(0,0,0); r.font.size=None
    if p.style.name.startswith('Heading'): p.paragraph_format.keep_with_next=True
for i in (15,20,23,35): ps[i].paragraph_format.page_break_before=True
for t in tables:
    t.autofit=False
    for row in t.rows:
        row.height=None
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(5)
                for r in p.runs: r.font.name='Calibri'; r.font.size=Pt(10); r.font.color.rgb=RGBColor(0,0,0)
    for el in t._element.xpath('.//w:trHeight'): el.getparent().remove(el)
for shape in d.inline_shapes:
    ratio=shape.height/shape.width; shape.width=Inches(6.35); shape.height=int(shape.width*ratio)
d.save(out)
# Confirm that charts and all numeric table values are unchanged.
with ZipFile(src) as a, ZipFile(out) as b:
    for n in a.namelist():
        if n.startswith('word/media/'): assert a.read(n)==b.read(n),n
assert [[c.text for c in r.cells] for r in tables[1].rows][1]==['67.25','6,378 students','80']
print(out)
