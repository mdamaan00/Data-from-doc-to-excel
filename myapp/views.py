from django.shortcuts import redirect, render
from .models import *
from .forms import DocumentForm
from docx2pdf import convert
import PyPDF2 
import re
import xlwt
from xlwt import Workbook 

def my_view(request):
    message = ""
    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('docfile')
            lst = []
            for file in files:
                p = str(file)
                p=p.split(".")
                print(file)
                dummyexcelobj = Excel.objects.get(docfile="documents_excel/Password_6bv8Dy0.txt")
                if p[-1]=="pdf":
                    newdoc = Pdf.objects.create(docfile=file,excel=dummyexcelobj)
                    newdoc.save()
                    k=str(newdoc.docfile)
                    k=k.replace("documents_pdf/",'')
                    k=k.split(".")
                    n=k[-1]
                    k=".".join(k)
                    k=k.replace("."+n,'')
                else:
                    newdoc = Document(docfile=file)
                    newdoc.save()
                    k=str(newdoc.docfile)
                    convert("media/"+k,"media/documents_pdf/")
                    k=k.replace("documents_other/",'')
                    k=k.split(".")
                    n=k[-1]
                    k=".".join(k)
                    k=k.replace("."+n,'')
                    newdoc = Pdf.objects.create(docfile="documents_pdf/"+k+".pdf",excel=dummyexcelobj)
                    newdoc.save()
                
                pdffileobj = open("media/documents_pdf/"+k+".pdf", 'rb')
                pdfreader = PyPDF2.PdfFileReader(pdffileobj)
                pageObj = pdfreader.getPage(0)
                page=pageObj.extractText()
                page = page.rstrip()
                number = re.search(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',page)
                try:
                    number = number.group(0)
                except:
                    number = ""
                email = re.search(r'[\w\.\w-]+@[a-z0-9\.-]+', page)
                try:
                    email = email.group(0)
                except:
                    email = ""
                print("Phone No.: ",number)
                print("E-mail: ",email)
                print("Location: ","media/documents_pdf/"+k+".pdf")
                lst.append([email,number,"media/documents_pdf/"+k+".pdf","documents_pdf/"+k+".pdf"])
            wb = Workbook()
            sheet1 = wb.add_sheet('Sheet 1')
            first_col=sheet1.col(0)
            second_col=sheet1.col(1)
            third_col=sheet1.col(2)
            first_col.width = 420*20
            second_col.width = 320*20
            third_col.width = 1200*20
            sheet1.write(0, 0,'E-mail')
            sheet1.write(0, 1,'Phone')
            sheet1.write(0, 2,'File Location')
            for i in range(len(lst)):
                sheet1.write(i+1, 0,lst[i][0])
                sheet1.write(i+1, 1,lst[i][1])
                sheet1.write(i+1, 2,lst[i][2])
            wb.save("media/documents_excel/"+k+".xls")
            pdf = Pdf.objects.get(docfile="documents_pdf/"+k+".pdf")
            newpdf = Excel.objects.create(docfile="documents_excel/"+k+".xls")
            newpdf.save()
            excelobj = Excel.objects.get(docfile="documents_excel/"+k+".xls")
            for i in range(len(lst)):
                pdfobj = Pdf.objects.get(docfile=lst[i][3])
                pdfobj.excel = excelobj
                pdfobj.save()
            message = 'Files uploaded and converted to pdf succesfully!'
          
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  

   
    excels = Excel.objects.all()
    context = {'excels': excels, 'form': form, 'message': message}
    return render(request, 'list.html', context)


def pdfview(request,pkid):
    excel = Excel.objects.get(id=pkid)
    pdfs = excel.pdf_set.all()
    context = {'pdfs':pdfs}
    return render(request, 'pdfview.html', context)