import base64
import io
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import View
# import aspose.pdf as ap

import pdf2image
import time
# Create your views here.

DIR_INPUT = "../upload_files/"
DIR_OUTPUT = "../output_files/"


def index(request):
    return render(request, "index.html")


class pdftopil():
    dir_input = "upload_files/"
    dir_output = "output_files/"

    def __init__(self, uploadfile):
        self.uploadfile = uploadfile
    def ret_img(self, img):
        file_img = open(img, "rb")
        img = file_img.read()
        # f = io.BytesIO()
        # img.save(f, 'PNG')
        # # f.seek(0)
        # im_io_png = base64.b64encode(f.getvalue())
        # im_io_png = base64.b64encode(img)
        # img_tag = mark_safe(f"img src='data:image/png;base64,{im_io_png}")
        return img
    def to_png(self):
        try:
            start_time = time.time()
            pil_images = pdf2image.convert_from_bytes(open(self.dir_input + self.uploadfile, 'rb').read())
            # pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
            #                                          last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT,
            #                                          userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)

            print("Time taken: " + str(time.time() - start_time))
            img_list = []
            for i, image in enumerate(pil_images):
                fname = self.dir_output + self.uploadfile +"image" + str(i) + ".png"
                image.save(fname, "PNG")
                print(fname)
                img = self.ret_img(fname)
                img_list.append(img)
            status = "success"
        except:
            status = "fail"
        return img_list
        # return img
    # def post(self, request):
    #     return JsonResponse({'Method': "POST"})
    # def get(self, request):
    #     # PDF_PATH = "../upload_files/python2023final(1).pdf"
    #     # DPI = 200
    #     # OUTPUT_FOLDER = DIR_OUTPUT
    #     # FIRST_PAGE = None
    #     # LAST_PAGE = None
    #     # FORMAT = 'jpg'
    #     # THREAD_COUNT = 1
    #     # USERPWD = None
    #     # USE_CROPBOX = False
    #     # STRICT = False
    #
    #
    #     return JsonResponse({"Method": "GET"})





class upload_files(View):
    def post(self, request):
        uploadfile = request.FILES.get('File')
        # trans = request.POST.get('trans')
        # print(uploadfile)
        if uploadfile:

            # 保存数据到本地服务器
            file_dir = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload_files'),
                                    uploadfile.name)
            f = open(file_dir, 'wb')
            for i in uploadfile.chunks():
                f.write(i)
            f.close()

            # 转换为img
            pil_images = pdftopil(uploadfile.name)
            pngfile = pil_images.to_png()
            # print(pngfile)

            # for i in request.img_list:
            #     print(i['file_name'])
            # pdf_to_jpg(uploadfile)
            # func = locals()[trans]
            # func(uploadfile)

            status = "Storage Success"
        else:
            status = "Storage Fail"
        return HttpResponse(pngfile, content_type='image/png')
        # return JsonResponse({"status": status, "img": pngfile})
        # return render(request, "index.html", {"status": status, "file_data": request.img_list, "img": pngfile['img']})

    # def pdf(self, request):

    def get(self, request, format=None):
        """
        提供get请求
        :param request:
        :param format:
        :return:
        """
        return JsonResponse({"data": "hello world."})


# class pdf2img():
#     # This method reads a pdf and converts it into a sequence of images
#     # PDF_PATH sets the path to the PDF file
#     # dpi parameter assists in adjusting the resolution of the image
#     # output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
#     # first_page parameter allows you to set a first page to be processed by pdftoppm
#     # last_page parameter allows you to set a last page to be processed by pdftoppm
#     # fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
#     # thread_count parameter allows you to set how many thread will be used for conversion.
#     # userpw parameter allows you to set a password to unlock the converted PDF
#     # use_cropbox parameter allows you to use the crop box instead of the media box when converting
#     # strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError
#     # DECLARE CONSTANTS
#     def tojpg(self, upload_file):
#         PDF_PATH = DIR_INPUT + upload_file
#         print(PDF_PATH)
#         print(upload_file)
#         DPI = 200
#         OUTPUT_FOLDER = DIR_OUTPUT
#         FIRST_PAGE = None
#         LAST_PAGE = None
#         FORMAT = 'jpg'
#         THREAD_COUNT = 1
#         USERPWD = None
#         USE_CROPBOX = False
#         STRICT = False
#         index = 1
#
#
#         start_time = time.time()
#         pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
#                                                  last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT,
#                                                  userpw=USERPWD,
#                                                  use_cropbox=USE_CROPBOX, strict=STRICT)
#         print("Time taken : " + str(time.time() - start_time))
#
#         # for image in pil_images:
#         #     image.save(DIR_OUTPUT + upload_file + str(index) + ".jpg")
#         #     index += 1
#         #     request.img_list.append({'file_name': upload_file, 'file_base64': base64.b64encode(pil_images)})
#         return pil_images
#         # return pil_images

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
