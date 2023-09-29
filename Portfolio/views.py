from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers


# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 3  # Set the number of items to be displayed per page
    page_size_query_param = "page"

    def paginate_queryset(self, queryset, request, view=None):
        # Sort the queryset by the 'uploaded_at' field in descending order
        queryset = sorted(queryset, key=lambda x: x['uploaded_at'], reverse=True)

        # Call the base class method to apply pagination on the sorted queryset
        return super().paginate_queryset(queryset, request, view)



class AllFilesListView(APIView):
    pagination_class = CustomPagination  # Use the custom pagination class


    def get(self, request):
        images = models.Images.objects.all().select_related().order_by('-uploaded_at')
        videos = models.Videos.objects.all().select_related().order_by('-uploaded_at')
        pdfs = models.PDF.objects.all().select_related().order_by('-uploaded_at')

        images_serializer = serializers.ImageSerializer(images, many=True)
        videos_serializer = serializers.VideoSerializer(videos, many=True)
        pdfs_serializer = serializers.PDFSerializer(pdfs, many=True)

        data = list()

        for image in images_serializer.data:
            data.append({
                "type_of_file": "image",
                "uploaded_at": image["uploaded_at"],
                "name": {"heading": image["heading"], "caption": image["caption"]},
                "file": {
                    "thumbnail_small": request.build_absolute_uri(image.get("thumbnail_small")),
                    "thumbnail": request.build_absolute_uri(image.get("thumbnail")),
                    "url": request.build_absolute_uri(image.get("image"))
                }
            })

        for video in videos_serializer.data:
            data.append({
                "type_file": "video",
                "uploaded_at": video["uploaded_at"],
                "name": {"heading": video["heading"], "caption": video["caption"]},
                "file": {
                    "thumbnail_small": request.build_absolute_uri(video.get("thumbnail_small")),
                    "thumbnail": request.build_absolute_uri(video.get("thumbnail")),
                    "url": request.build_absolute_uri(video.get("video"))
                }
            })

        for pdf in pdfs_serializer.data:
            data.append({
                "type_of_file": "pdf",
                "uploaded_at": pdf["uploaded_at"],
                "name": {"heading": pdf["heading"], "caption": pdf["caption"]},
                "file": {
                    "thumbnail_small": request.build_absolute_uri(pdf.get("thumbnail_small")),
                    "thumbnail": request.build_absolute_uri(pdf.get("thumbnail")),
                    "url": request.build_absolute_uri(pdf.get("pdf"))
                }
            })

        # Apply pagination using the custom pagination class
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(data, request, view=self)

        return Response(paginated_data)
