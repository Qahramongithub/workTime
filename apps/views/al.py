# from PyPDF2 import PdfReader
# from drf_spectacular.utils import extend_schema
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from transformers import pipeline
#
# from apps.models import AlData
# from apps.serializer import AlSerializer, AlModelSerializer
#
#
# @extend_schema(
#     request=AlSerializer,
#     tags=['al']
# )
# class AlAPiView(APIView):
#     def post(self, request):
#         string = request.data['string']
#
#
# @extend_schema(
#     request=AlModelSerializer,
# )
# class AlDataCreateAPiView(APIView):
#     parser_classes = (MultiPartParser, FormParser)  # Fayl yuklash uchun parser
#
#     def post(self, request, *args, **kwargs):
#         string = request.data['string']
#         file = request.data['file']
#         audios = request.data['audios']
#
# # import os
# # import zipfile
# # import PyMuPDF  # PDF o'qish
# # import docx  # DOCX o'qish
# # import pandas as pd  # CSV va Excel uchun
# # import textract  # Matn chiqarish uchun
# # from moviepy.editor import VideoFileClip  # MP4 uchun (video uzunligi va metadatalar)
# #
# #
# # def extract_text_from_pdf(pdf_path):
# #     """ PDF fayldan matn chiqarish """
# #     doc = PyMuPDF.open(pdf_path)
# #     text = ""
# #     for page in doc:
# #         text += page.get_text()
# #     return text.strip()
# #
# #
# # def extract_text_from_docx(docx_path):
# #     """ Word (DOCX) fayldan matn chiqarish """
# #     doc = docx.Document(docx_path)
# #     text = "\n".join([para.text for para in doc.paragraphs])
# #     return text.strip()
# #
# #
# # def extract_text_from_txt(txt_path):
# #     """ TXT fayldan matn chiqarish """
# #     with open(txt_path, "r", encoding="utf-8") as file:
# #         return file.read().strip()
# #
# #
# # def extract_text_from_csv(csv_path):
# #     """ CSV fayldan matn chiqarish """
# #     df = pd.read_csv(csv_path)
# #     return df.to_string()
# #
# #
# # def extract_text_from_xlsx(xlsx_path):
# #     """ Excel fayldan matn chiqarish """
# #     df = pd.read_excel(xlsx_path)
# #     return df.to_string()
# #
# #
# # def extract_text_from_zip(zip_path):
# #     """ ZIP fayl ichidagi barcha hujjatlarni ochish """
# #     extracted_text = ""
# #     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
# #         zip_ref.extractall("temp_extracted")  # Fayllarni vaqtinchalik chiqaramiz
# #         for file in os.listdir("temp_extracted"):
# #             file_path = os.path.join("temp_extracted", file)
# #             if file.endswith(".pdf"):
# #                 extracted_text += extract_text_from_pdf(file_path) + "\n"
# #             elif file.endswith(".docx"):
# #                 extracted_text += extract_text_from_docx(file_path) + "\n"
# #             elif file.endswith(".txt"):
# #                 extracted_text += extract_text_from_txt(file_path) + "\n"
# #             elif file.endswith(".csv"):
# #                 extracted_text += extract_text_from_csv(file_path) + "\n"
# #             elif file.endswith(".xlsx"):
# #                 extracted_text += extract_text_from_xlsx(file_path) + "\n"
# #         os.system("rm -rf temp_extracted")  # Vaqtinchalik papkani o‘chirib tashlash
# #     return extracted_text.strip()
# #
# #
# # def extract_info_from_mp4(mp4_path):
# #     """ MP4 fayldan metadata olish (matn o‘rniga video metama’lumotlari) """
# #     clip = VideoFileClip(mp4_path)
# #     return f"Video uzunligi: {clip.duration} soniya, FPS: {clip.fps}, Resolution: {clip.size}"
# #
# #
# # def extract_text_from_file(file_path):
# #     """ Har qanday fayldan ma’lumot olish """
# #     if file_path.endswith(".pdf"):
# #         return extract_text_from_pdf(file_path)
# #     elif file_path.endswith(".docx"):
# #         return extract_text_from_docx(file_path)
# #     elif file_path.endswith(".txt"):
# #         return extract_text_from_txt(file_path)
# #     elif file_path.endswith(".csv"):
# #         return extract_text_from_csv(file_path)
# #     elif file_path.endswith(".xlsx"):
# #         return extract_text_from_xlsx(file_path)
# #     elif file_path.endswith(".zip"):
# #         return extract_text_from_zip(file_path)
# #     elif file_path.endswith(".mp4"):
# #         return extract_info_from_mp4(file_path)
# #     else:
# #         return "Bu fayl formati qo‘llab-quvvatlanmaydi"
