from fpdf import FPDF
from pypdf import PdfReader
import os

class _Create_PDF:

    def ccc(self,name,email):
        output =None
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font('arial', 'B', 13.0)
            pdf.cell(ln=0, h=5.0, align='L', w=0, txt=name, border=0)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt=email, border=0)
            output=pdf.output('/home/anik-deb-biswas/PycharmProjects/1msChallange/static/test.pdf', 'F')
            print(PdfReader('test.pdf'))

        except Exception as e:
            print(e)
        return output
    def _delete_pdf(self):
        os.remove('test.pdf')



if __name__ == '__main__':
    obj = _Create_PDF()
    obj.ccc('name','email')