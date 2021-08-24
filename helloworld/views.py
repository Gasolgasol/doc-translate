# in views.py
from datetime import datetime
from pyramid.view import view_config
from helloworld.models import Tester, File  # Task, User,
from pyramid.response import Response, FileResponse
import os
import uuid
import shutil
import PyPDF2
from PyPDF2.utils import PdfReadError
from PyPDF2 import PdfFileReader,  PdfFileWriter
from pyramid.httpexceptions import HTTPFound
from helloworld.pdf_conversion import convert
from hurry.filesize import size, si




INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'

@view_config(route_name="default")
def hello_world(request):
    return Response("Hello Hell!")  #{'msg': 'rama'} # Response('Hello World!')


@view_config(route_name="main", request_method="GET", renderer='templates/main.jinja2')
def mainmain(request):
    files = request.dbsession.query(File).all()
   # testers = request.dbsession.query(Tester).filter_by(name="Valera").first()
    return {"list": files}  

#testers = request.dbsession.query(Tester).all()#.first()
#testers = request.dbsession.query(Tester).filter_by(name="Valera").first()


@view_config(route_name="download_view", renderer="")
def server_view1010(request):
    print("vieeeeeeeee   reached")
    if request.matchdict["bool"] == "first":
        download_name = "attachment; filename=" + request.matchdict["name"]
        filepath = "/tmp/" + request.matchdict["server_name"] 
    else:
        download_name = "attachment; filename=" + request.matchdict["name"][:-4] + "-esp.pdf" 
        filepath = "/tmp/" + request.matchdict["server_name"][:-4] + "-esp.pdf" 
  
    response = FileResponse(filepath)
    

    response.headers['Content-Disposition'] = (download_name)
    return response #"Draaako"#response

@view_config(route_name="wrong_format", renderer='templates/wrong_format.jinja2')
def wrong_format(request):
   return {'msg': 'wrong'}
    
@view_config(route_name="good_upload", renderer='templates/success.jinja2')
def good_upload(request):
    #return HTTPFound(location='http://127.0.0.1:6543/good_upload')
    return {'msg': 'good'}    

@view_config(route_name="store_pdf_view")
def store_pdf_view(request):
   
    filename = request.POST['pdf'].filename

    input_file = request.POST['pdf'].file

    
    try:
        pdf = PyPDF2.PdfFileReader(input_file)
    except PdfReadError:
        return HTTPFound(location=request.host_url + '/wrong_format') 
       

    input_file.seek(0, os.SEEK_END)
   
    server_name = uuid.uuid4()
    file_path = os.path.join('/tmp', '%s.pdf' % server_name)

    temp_file_path = file_path + '~'

    input_file.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    os.rename(temp_file_path, file_path)
    
    transPath = convert(file_path)
    theNumber = size(input_file.tell(), system=si)
    file = File( name = filename, size = size(input_file.tell(), system=si), server_name = str(server_name) + ".pdf", original = file_path, translated = transPath)
    request.dbsession.add(file)


    #return good_upload(request)
    return HTTPFound(location=request.host_url + '/good_upload')  