import io
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
# import aspose.pdf as ap
import pdf2image
import time
# Create your views here.

DIR_INPUT = "../upload_files/"
DIR_OUTPUT = "../output_files/"


def index(request):
    return render(request, "index.html")

# def pdf_to_word(request):
#     input_pdf = DIR_INPUT + "sample.pdf"
#     output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
#     # Open PDF document
#     document = ap.Document(input_pdf)
#     # Save the file into MS Word document format
#     document.save(output_pdf, ap.SaveFormat.DOC)


# def pdf_to_jpg(uploadfile):
#     input_pdf = DIR_INPUT + uploadfile.name
#     # uploadfile = requests.POST.get()
#     print(type(uploadfile))
#     output_pdf = DIR_OUTPUT + uploadfile.name + "convert_pdf_to_jpg"
#
#
#     # 打开 PDF 文档
#     document = ap.Document(input_pdf)
#
#     # ap.DocumentInfo
#     # 创建分辨率对象
#     resolution = ap.devices.Resolution(300)
#     device = ap.devices.JpegDevice(resolution)
#
#     for i in range(0, len(document.pages)):
#         # 创建文件保存
#         imageStream = io.FileIO(
#             output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
#         )
#
#         # 转换特定页面并将图像保存到流
#         device.process(document.pages[i + 1], imageStream)
#         imageStream.close()

def pdf2img():
    # This method reads a pdf and converts it into a sequence of images
    # PDF_PATH sets the path to the PDF file
    # dpi parameter assists in adjusting the resolution of the image
    # output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
    # first_page parameter allows you to set a first page to be processed by pdftoppm
    # last_page parameter allows you to set a last page to be processed by pdftoppm
    # fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
    # thread_count parameter allows you to set how many thread will be used for conversion.
    # userpw parameter allows you to set a password to unlock the converted PDF
    # use_cropbox parameter allows you to use the crop box instead of the media box when converting
    # strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError

    start_time = time.time()
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
                                             last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD,
                                             use_cropbox=USE_CROPBOX, strict=STRICT)
    print("Time taken : " + str(time.time() - start_time))
    return pil_images


class upload_files(View):
    def post(self, request):
        uploadfile = request.FILES.get('File')
        trans = request.POST.get('trans')
        print(uploadfile)
        if uploadfile:
            # 保存数据到本地服务器
            # file_dir = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload_files'),
            #                         uploadfile.name)
            # f = open(file_dir, 'wb')
            # for i in uploadfile.chunks():
            #     f.write(i)
            # f.close()

            # pdf_to_jpg(uploadfile)
            # func = locals()[trans]
            # func(uploadfile)

            status = "Storage Success"
        else:
            status = "Storage Fail"
        return JsonResponse({"data": "hello world.","status":status})
    # def pdf(self, request):

    def get(self, request, format=None):
        """
        提供get请求
        :param request:
        :param format:
        :return:
        """
        return JsonResponse({"data":"hello world."})


