# Data-from-doc-to-excel
In this simple django project a user can choose to add any type file with different extensions(doc,docx,txt,pdf), convert it to pdf format and extract data like E-mail, Phone No. and location of the pdf file from the file the user gives.



After active installation to run the file just write the following in command prompt:

1: pip install docx2pdf 

(Note: this will only covert docx to pdf to use it for other files you have to make changes in the modules __init__.py file)

2: pip install PyPDF2

3: pip install xlwt

(Note: MS Office required to run the program as per the requirements by the library xlwt)

Now run using 

4: python manage.py runserver
