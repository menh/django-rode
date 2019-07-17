DRF (Django REST framework) ��ܽ���(3)
DRF�е�Request �� Response
1. Request
REST framework ������ͼ��request��������DjangoĬ�ϵ�HttpRequest���󣬶���REST framework�ṩ����չ��HttpRequest���Request��Ķ���

REST framework �ṩ��Parser���������ڽ��յ��������Զ�����Content-Typeָ���������������ͣ���JSON�����ȣ����������ݽ���parse����������Ϊ���ֵ���󱣴浽Request�����С�

Request������������Զ�����ǰ�˷������ݵĸ�ʽ���н���֮��Ľ����

����ǰ�˷��͵����ָ�ʽ�����ݣ����Ƕ�������ͳһ�ķ�ʽ��ȡ���ݡ�

��������
1��.data
request.data ���ؽ���֮������������ݡ�������Django�б�׼��request.POST�� request.FILES���ԣ����ṩ�������ԣ�

�����˽���֮����ļ��ͷ��ļ�����
�����˶�POST��PUT��PATCH����ʽ�����������
������REST framework��parsers������������֧�ֱ��������ݣ�Ҳ֧��JSON����
2��.query_params
request.query_params��Django��׼��request.GET��ͬ��ֻ�Ǹ����˸���ȷ�����ƶ��ѡ�

2. Response
rest_framework.response.Response

REST framework�ṩ��һ����Ӧ��Response��ʹ�ø��๹����Ӧ����ʱ����Ӧ�ľ����������ݻᱻת����render��Ⱦ���ɷ���ǰ����������͡�

REST framework�ṩ��Renderer ��Ⱦ����������������ͷ�е�Accept�����������������������Զ�ת����Ӧ���ݵ���Ӧ��ʽ�����ǰ��������δ����Accept������������Ĭ�Ϸ�ʽ������Ӧ���ݣ����ǿ���ͨ���������޸�Ĭ����Ӧ��ʽ��

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # Ĭ����Ӧ��Ⱦ��
        'rest_framework.renderers.JSONRenderer',  # json��Ⱦ��
        'rest_framework.renderers.BrowsableAPIRenderer',  # ���API��Ⱦ��
    )
}
���췽ʽ
Response(data, status=None, template_name=None, headers=None, content_type=None)
data���ݲ�Ҫ��render����֮������ݣ�ֻ�贫��python���ڽ��������ݼ��ɣ�REST framework��ʹ��renderer��Ⱦ������data��

data�����Ǹ��ӽṹ�����ݣ���Django��ģ������󣬶����������������ǿ���ʹ��Serializer���л������л������תΪ��Python�ֵ����ͣ��ٴ��ݸ�data������

����˵����

data: Ϊ��Ӧ׼�������л����������ݣ�
status: ״̬�룬Ĭ��200��
template_name: ģ�����ƣ����ʹ��HTMLRenderer ʱ��ָ����
headers: ���ڴ����Ӧͷ��Ϣ���ֵ䣻
content_type: ��Ӧ���ݵ�Content-Type��ͨ���˲������贫�ݣ�REST framework�����ǰ�������������������øò�����
�������ԣ�
1��.data
����response��������л��󣬵���δrender���������

2��.status_code
״̬�������

3��.content
����render��������Ӧ����

3. ״̬��
Ϊ�˷�������״̬�룬REST framewrok��rest_framework.statusģ�����ṩ�˳���״̬�볣����

1����Ϣ��֪ - 1xx
HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS
2���ɹ� - 2xx
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
3���ض��� - 3xx
HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
4���ͻ��˴��� - 4xx
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
5������������ - 5xx
HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_507_INSUFFICIENT_STORAGE
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED

��ͼ˵��
1. ��������
1��APIView
rest_framework.views.APIView

APIView��REST framework�ṩ��������ͼ�Ļ��࣬�̳���Django��View���ࡣ

APIView��View�Ĳ�֮ͬ�����ڣ�

���뵽��ͼ�����е���REST framework��Request���󣬶�����Django��HttpRequeset����
��ͼ�������Է���REST framework��Response������ͼ��Ϊ��Ӧ�������ã�render������ǰ��Ҫ��ĸ�ʽ��
�κ�APIException�쳣���ᱻ���񵽣����Ҵ���ɺ��ʵ���Ӧ��Ϣ��
�ڽ���dispatch()�ַ�ǰ�����������������֤��Ȩ�޼�顢�������ơ�
֧�ֶ�������ԣ�
authentication_classes �б��Ԫ�棬�����֤��
permissoin_classes �б��Ԫ�棬Ȩ�޼����
throttle_classes �б��Ԫ�棬����������
��APIView�����Գ��������ͼ���巽����ʵ��get() ��post() ������������ʽ�ķ�����

������

from rest_framework.views import APIView
from rest_framework.response import Response

# url(r'^books/$', views.BookListView.as_view()),
class BookListView(APIView):
    def get(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)
2��GenericAPIView
rest_framework.generics.GenericAPIView

�̳���APIVIew�������˶����б���ͼ��������ͼ�����õ���ͨ��֧�ַ�����ͨ��ʹ��ʱ���ɴ���һ������Mixin��չ�ࡣ

֧�ֶ�������ԣ�
�б���ͼ��������ͼͨ�ã�
queryset �б���ͼ�Ĳ�ѯ��
serializer_class ��ͼʹ�õ����л���
�б���ͼʹ�ã�
pagination_class ��ҳ������
filter_backends ���˿��ƺ��
����ҳ��ͼʹ�ã�
lookup_field ��ѯ��һ���ݿ����ʱʹ�õ������ֶΣ�Ĭ��Ϊ'pk'
lookup_url_kwarg ��ѯ��һ����ʱURL�еĲ����ؼ������ƣ�Ĭ����look_field��ͬ
�ṩ�ķ�����
�б���ͼ��������ͼͨ�ã�

get_queryset(self)

������ͼʹ�õĲ�ѯ�������б���ͼ��������ͼ��ȡ���ݵĻ�����Ĭ�Ϸ���queryset���ԣ�������д�����磺

def get_queryset(self):
    user = self.request.user
    return user.accounts.all()
get_serializer_class(self)

�������л����࣬Ĭ�Ϸ���serializer_class��������д�����磺

def get_serializer_class(self):
    if self.request.user.is_staff:
        return FullAccountSerializer
    return BasicAccountSerializer
get_serializer(self, args, *kwargs)
�������л������󣬱�������ͼ����չ��ʹ�ã������������ͼ����Ҫ��ȡ���л������󣬿���ֱ�ӵ��ô˷�����

ע�⣬���ṩ���л��������ʱ��REST framework��������context���Բ����������ݣ�request��format��view�����������ݶ�������ڶ������л���ʱʹ�á�

������ͼʹ�ã�

get_object(self) ����������ͼ�����ģ�������ݶ���Ĭ��ʹ��lookup_field����������queryset�� ����ͼ�п��Ե��ø÷�����ȡ������Ϣ��ģ�������

��������ʵ�ģ������󲻴��ڣ��᷵��404��

�÷�����Ĭ��ʹ��APIView�ṩ��check_object_permissions������鵱ǰ�����Ƿ���Ȩ�ޱ����ʡ�

������

# url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
class BookDetailView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
2. �����չ��
1��ListModelMixin
�б���ͼ��չ�࣬�ṩlist(request, *args, **kwargs)��������ʵ���б���ͼ������200״̬�롣

��Mixin��list����������ݽ��й��˺ͷ�ҳ��

Դ���룺

class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        # ����
        queryset = self.filter_queryset(self.get_queryset())
        # ��ҳ
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # ���л�
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
������

from rest_framework.mixins import ListModelMixin

class BookListView(ListModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request):
        return self.list(request)
2��CreateModelMixin
������ͼ��չ�࣬�ṩcreate(request, *args, **kwargs)��������ʵ�ִ�����Դ����ͼ���ɹ�����201״̬�롣

������л�����ǰ�˷��͵�������֤ʧ�ܣ�����400����

Դ���룺

class CreateModelMixin(object):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        # ��ȡ���л���
        serializer = self.get_serializer(data=request.data)
        # ��֤
        serializer.is_valid(raise_exception=True)
        # ����
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
3�� RetrieveModelMixin
������ͼ��չ�࣬�ṩretrieve(request, *args, **kwargs)���������Կ���ʵ�ַ���һ�����ڵ����ݶ���

������ڣ�����200�� ���򷵻�404��

Դ���룺

class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        # ��ȡ���󣬻�������Ȩ��
        instance = self.get_object()
        # ���л�
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
������

class BookDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        return self.retrieve(request)
4��UpdateModelMixin
������ͼ��չ�࣬�ṩupdate(request, *args, **kwargs)���������Կ���ʵ�ָ���һ�����ڵ����ݶ���

ͬʱҲ�ṩpartial_update(request, *args, **kwargs)����������ʵ�־ֲ����¡�

�ɹ�����200�����л���У������ʧ��ʱ������400����

Դ���룺

class UpdateModelMixin(object):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
5��DestroyModelMixin
ɾ����ͼ��չ�࣬�ṩdestroy(request, *args, **kwargs)���������Կ���ʵ��ɾ��һ�����ڵ����ݶ���

�ɹ�����204�������ڷ���404��

Դ���룺

class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
3. ��������������ͼ
1�� CreateAPIView
�ṩ post ����

�̳��ԣ� GenericAPIView��CreateModelMixin

2��ListAPIView
�ṩ get ����

�̳��ԣ�GenericAPIView��ListModelMixin

3��RetireveAPIView
�ṩ get ����

�̳���: GenericAPIView��RetrieveModelMixin

4��DestoryAPIView
�ṩ delete ����

�̳��ԣ�GenericAPIView��DestoryModelMixin

5��UpdateAPIView
�ṩ put �� patch ����

�̳��ԣ�GenericAPIView��UpdateModelMixin

6��RetrieveUpdateAPIView
�ṩ get��put��patch����

�̳��ԣ� GenericAPIView��RetrieveModelMixin��UpdateModelMixin

7��RetrieveUpdateDestoryAPIView
�ṩ get��put��patch��delete����

�̳��ԣ�GenericAPIView��RetrieveModelMixin��UpdateModelMixin��DestoryModelMixin

��ͼ��ViewSet
ʹ����ͼ��ViewSet�����Խ�һϵ���߼���صĶ����ŵ�һ�����У�

list() �ṩһ������
retrieve() �ṩ��������
create() ��������
update() ��������
destory() ɾ������
ViewSet��ͼ���಻��ʵ��get()��post()�ȷ���������ʵ�ֶ��� action �� list() ��create() �ȡ�

��ͼ��ֻ��ʹ��as_view()������ʱ�򣬲ŻὫaction�������������ʽ��Ӧ�ϡ��磺

class BookInfoViewSet(viewsets.ViewSet):

    def list(self, request):
        ...

    def retrieve(self, request, pk=None):
        ...
������·��ʱ�����ǿ������²���

urlpatterns = [
    url(r'^books/$', BookInfoViewSet.as_view({'get':'list'}),
    url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({'get': 'retrieve'})
]
action����
����ͼ���У����ǿ���ͨ��action������������ȡ��ǰ������ͼ��ʱ��action�������ĸ���

���磺

def get_serializer_class(self):
    if self.action == 'create':
        return OrderCommitSerializer
    else:
        return OrderDataSerializer
������ͼ������
1�� ViewSet
�̳���APIView������Ҳ��APIView�������ƣ��ṩ�������֤��Ȩ��У�顢��������ȡ�

��ViewSet�У�û���ṩ�κζ���action��������Ҫ�����Լ�ʵ��action������

2��GenericViewSet
�̳���GenericAPIView������Ҳ��GenericAPIVIew���ƣ��ṩ��get_object��get_queryset�ȷ��������б���ͼ��������Ϣ��ͼ�Ŀ�����

3��ModelViewSet
�̳���GenericAPIVIew��ͬʱ������ListModelMixin��RetrieveModelMixin��CreateModelMixin��UpdateModelMixin��DestoryModelMixin��

4��ReadOnlyModelViewSet
�̳���GenericAPIVIew��ͬʱ������ListModelMixin��RetrieveModelMixin��

��ͼ���ж��帽��action����
����ͼ���У���������Ĭ�ϵķ��������⣬����������Զ��嶯����

����Զ��嶯����Ҫʹ��rest_framework.decorators.actionװ������

��actionװ����װ�εķ���������Ϊaction����������list��retrieve��ͬ��

actionװ�������Խ�������������

methods: ��action֧�ֵ�����ʽ���б���
detail: ��ʾ��action��Ҫ������Ƿ�����ͼ��Դ�Ķ��󣨼��Ƿ�ͨ��url·����ȡ������
True ��ʾʹ��ͨ��URL��ȡ��������Ӧ�����ݶ���
False ��ʾ��ʹ��URL��ȡ����
������

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # detailΪFalse ��ʾ����Ҫ��������BookInfo����
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        �������µ�ͼ����Ϣ
        """
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    # detailΪTrue����ʾҪ���������pk������Ӧ��BookInfo����
    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        """
        �޸�ͼ����Ķ�������
        """
        book = self.get_object()
        book.bread = request.data.get('read')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
url�Ķ���

urlpatterns = [
    url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/latest/$', views.BookInfoViewSet.as_view({'get': 'latest'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({'put': 'read'})),
]



·��Routers
������ͼ��ViewSet�����ǳ��˿����Լ��ֶ�ָ������ʽ�붯��action֮��Ķ�Ӧ��ϵ�⣬������ʹ��Routers���������ǿ���ʵ��·����Ϣ��

REST framework�ṩ������router

SimpleRouter
DefaultRouter
1. ʹ�÷���
1�� ����router���󣬲�ע����ͼ��������

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BookInfoViewSet, base_name='book')
register(prefix, viewset, base_name)

prefix ����ͼ����·��ǰ׺
viewset ��ͼ��
base_name ·�����Ƶ�ǰ׺
������������γɵ�·�����£�

^books/$    name: book-list
^books/{pk}/$   name: book-detail
2�����·������

���������ַ�ʽ��

urlpatterns = [
    ...
]
urlpatterns += router.urls
��

urlpatterns = [
    ...
    url(r'^', include(router.urls))
]
2. ��ͼ���а�������action��
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        ...

    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        ...
����ͼ�����γɵ�·�ɣ�

^books/latest/$    name: book-latest
^books/{pk}/read/$  name: book-read
3. ·��router�γ�URL�ķ�ʽ
1�� SimpleRouter



2��DefaultRouter



DefaultRouter��SimpleRouter�������ǣ�DefaultRouter��฽��һ��Ĭ�ϵ�API����ͼ������һ�����������б���ͼ�ĳ�������Ӧ���ݡ�



��֤Authentication
�����������ļ�������ȫ��Ĭ�ϵ���֤����

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',   # ������֤
        'rest_framework.authentication.SessionAuthentication',  # session��֤
    )
}
Ҳ������ÿ����ͼ��ͨ������authentication_classess����������

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    ...
��֤ʧ�ܻ������ֿ��ܵķ���ֵ��

401 Unauthorized δ��֤
403 Permission Denied Ȩ�ޱ���ֹ
Ȩ��Permissions
Ȩ�޿��ƿ��������û�������ͼ�ķ��ʺͶ��ھ������ݶ���ķ��ʡ�

��ִ����ͼ��dispatch()����ǰ�����Ƚ�����ͼ����Ȩ�޵��ж�
��ͨ��get_object()��ȡ�������ʱ������ж������Ȩ�޵��ж�
ʹ��
�����������ļ�������Ĭ�ϵ�Ȩ�޹����࣬��

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
���δָ�������������Ĭ������

'DEFAULT_PERMISSION_CLASSES': (
   'rest_framework.permissions.AllowAny',
)
Ҳ�����ھ������ͼ��ͨ��permission_classes���������ã���

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    ...
�ṩ��Ȩ��
AllowAny ���������û�
IsAuthenticated ��ͨ����֤���û�
IsAdminUser ������Ա�û�
IsAuthenticatedOrReadOnly ��֤���û�������ȫ����������ֻ��get��ȡ
����
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

class BookDetailView(RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
�Զ���Ȩ��
�����Զ���Ȩ�ޣ���̳�rest_framework.permissions.BasePermission���࣬��ʵ�����������κ�һ��������ȫ��

.has_permission(self, request, view)

�Ƿ���Է�����ͼ�� view��ʾ��ǰ��ͼ����

.has_object_permission(self, request, view, obj)

�Ƿ���Է������ݶ��� view��ʾ��ǰ��ͼ�� objΪ���ݶ���

���磺

class MyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """���ƶ�obj����ķ���Ȩ�ޣ��˰����������жԶ���ķ���"""
        return False

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = [IsAuthenticated, MyPermission]


����Throttling
���ԶԽӿڷ��ʵ�Ƶ�ν������ƣ��Լ��������ѹ����

ʹ��
�����������ļ��У�ʹ��DEFAULT_THROTTLE_CLASSES �� DEFAULT_THROTTLE_RATES����ȫ�����ã�

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
DEFAULT_THROTTLE_RATES ����ʹ�� second, minute, hour ��day��ָ�����ڡ�

Ҳ�����ھ�����ͼ��ͨ��throttle_classess���������ã���

from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

class ExampleView(APIView):
    throttle_classes = (UserRateThrottle,)
    ...
��ѡ������
1�� AnonRateThrottle

������������δ��֤�û���ʹ��IP�����û���

ʹ��DEFAULT_THROTTLE_RATES['anon'] ������Ƶ��

2��UserRateThrottle

������֤�û���ʹ��User id �����֡�

ʹ��DEFAULT_THROTTLE_RATES['user'] ������Ƶ��

3��ScopedRateThrottle

�����û�����ÿ����ͼ�ķ���Ƶ�Σ�ʹ��ip��user id��

���磺

class ContactListView(APIView):
    throttle_scope = 'contacts'
    ...

class ContactDetailView(APIView):
    throttle_scope = 'contacts'
    ...

class UploadView(APIView):
    throttle_scope = 'uploads'
    ...
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'contacts': '1000/day',
        'uploads': '20/day'
    }
}
ʵ��
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.throttling import UserRateThrottle

class BookDetailView(RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = (UserRateThrottle,)


����Filtering
�����б����ݿ�����Ҫ�����ֶν��й��ˣ����ǿ���ͨ�����django-fitlter��չ����ǿ֧�֡�

pip insall django-filter
�������ļ������ӹ��˺�˵����ã�

INSTALLED_APPS = [
    ...
    'django_filters',  # ��Ҫע��Ӧ�ã�
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
����ͼ�����filter_fields���ԣ�ָ�����Թ��˵��ֶ�

class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_fields = ('btitle', 'bread')

# 127.0.0.1:8000/books/?btitle=���μ�


����
�����б����ݣ�REST framework�ṩ��OrderingFilter���������������ǿ���ָ�����ݰ���ָ���ֶν�������

ʹ�÷�����
������ͼ������filter_backends��ʹ��rest_framework.filters.OrderingFilter��������REST framework��������Ĳ�ѯ�ַ��������м���Ƿ������ordering���������������ordering����������ordering����ָ���������ֶζ����ݼ���������

ǰ�˿��Դ��ݵ�ordering�����Ŀ�ѡ�ֶ�ֵ��Ҫ��ordering_fields��ָ����

ʾ����

class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'bread', 'bpub_date')

# 127.0.0.1:8000/books/?ordering=-bread



��ҳPagination
REST framework�ṩ�˷�ҳ��֧�֡�

���ǿ����������ļ�������ȫ�ֵķ�ҳ��ʽ���磺

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100  # ÿҳ��Ŀ
}
Ҳ��ͨ���Զ���Pagination�࣬��Ϊ��ͼ��Ӳ�ͬ��ҳ��Ϊ������ͼ��ͨ��pagination_clas������ָ����

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
class BookDetailView(RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    pagination_class = LargeResultsSetPagination
ע�⣺�������ͼ�ڹرշ�ҳ���ܣ�ֻ������ͼ������

pagination_class = None
��ѡ��ҳ��
1�� PageNumberPagination

ǰ�˷�����ַ��ʽ��

GET  http://api.example.org/books/?page=4
�����������ж�������ԣ�

page_size ÿҳ��Ŀ
page_query_param ǰ�˷��͵�ҳ���ؼ�������Ĭ��Ϊ"page"
page_size_query_param ǰ�˷��͵�ÿҳ��Ŀ�ؼ�������Ĭ��ΪNone
max_page_size ǰ����������õ�ÿҳ����
from rest_framework.pagination import PageNumberPagination

class StandardPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10

class BookListView(ListAPIView):
    queryset = BookInfo.objects.all().order_by('id')
    serializer_class = BookInfoSerializer
    pagination_class = StandardPageNumberPagination

# 127.0.0.1/books/?page=1&page_size=2
2��LimitOffsetPagination

ǰ�˷�����ַ��ʽ��

GET http://api.example.org/books/?limit=100&offset=400
�����������ж�������ԣ�

default_limit Ĭ�����ƣ�Ĭ��ֵ��PAGE_SIZE����һֱ
limit_query_param limit��������Ĭ��'limit'
offset_query_param offset��������Ĭ��'offset'
max_limit ���limit���ƣ�Ĭ��None
from rest_framework.pagination import LimitOffsetPagination

class BookListView(ListAPIView):
    queryset = BookInfo.objects.all().order_by('id')
    serializer_class = BookInfoSerializer
    pagination_class = LimitOffsetPagination

# 127.0.0.1:8000/books/?offset=3&limit=2


�汾Versioning
REST framework�ṩ�˰汾�ŵ�֧�֡�

����Ҫ��ȡ����İ汾��ʱ������ͨ��request.version����ȡ��

Ĭ�ϰ汾����δ������request.version ����None��

�����汾֧�ֹ��ܣ���Ҫ�������ļ�������DEFAULT_VERSIONING_CLASS

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
}
������ѡ���ã�

DEFAULT_VERSION Ĭ�ϰ汾�ţ�Ĭ��ֵΪNone
ALLOWED_VERSIONS ��������İ汾�ţ�Ĭ��ֵΪNone
VERSION_PARAM ʶ��汾�Ų��������ƣ�Ĭ��ֵΪ'version'
֧�ֵİ汾����ʽ
1�� AcceptHeaderVersioning

����ͷ�д��ݵ�AcceptЯ��version

GET /bookings/ HTTP/1.1
Host: example.com
Accept: application/json; version=1.0
2��URLPathVersioning

URL·����Я��

urlpatterns = [
    url(
        r'^(?P<version>(v1|v2))/bookings/$',
        bookings_list,
        name='bookings-list'
    ),
    url(
        r'^(?P<version>(v1|v2))/bookings/(?P<pk>[0-9]+)/$',
        bookings_detail,
        name='bookings-detail'
    )
]
3��NamespaceVersioning

�����ռ��ж���

# bookings/urls.py
urlpatterns = [
    url(r'^$', bookings_list, name='bookings-list'),
    url(r'^(?P<pk>[0-9]+)/$', bookings_detail, name='bookings-detail')
]

# urls.py
urlpatterns = [
    url(r'^v1/bookings/', include('bookings.urls', namespace='v1')),
    url(r'^v2/bookings/', include('bookings.urls', namespace='v2'))
]
4��HostNameVersioning

��������Я��

GET /bookings/ HTTP/1.1
Host: v1.example.com
Accept: application/json
5��QueryParameterVersioning

��ѯ�ַ���Я��

GET /something/?version=0.1 HTTP/1.1
Host: example.com
Accept: application/json
ʾ��
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning'
}
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')

class BookInfoSerializer2(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date')

class BookDetailView(RetrieveAPIView):
    queryset = BookInfo.objects.all()

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return BookInfoSerializer
        else:
            return BookInfoSerializer2

# 127.0.0.1:8000/books/2/
# 127.0.0.1:8000/books/2/?version=1.0



�쳣���� Exceptions
REST framework�ṩ���쳣�������ǿ����Զ����쳣��������

from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # �ȵ���REST frameworkĬ�ϵ��쳣��������ñ�׼������Ӧ����
    response = exception_handler(exc, context)

    # �ڴ˴������Զ�����쳣����
    if response is not None:
        response.data['status_code'] = response.status_code

    return response
�������ļ��������Զ�����쳣����

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'my_project.my_app.utils.custom_exception_handler'
}
���δ�����������Ĭ�ϵķ�ʽ������

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
���磺

�����ϴ���������ݿ���쳣

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from django.db import DatabaseError

def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '�������ڲ�����'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
REST framework������쳣
APIException �����쳣�ĸ���
ParseError ��������
AuthenticationFailed ��֤ʧ��
NotAuthenticated ��δ��֤
PermissionDenied Ȩ�޾���
NotFound δ�ҵ�
MethodNotAllowed ����ʽ��֧��
NotAcceptable Ҫ��ȡ�����ݸ�ʽ��֧��
Throttled ������������
ValidationError У��ʧ��
�Զ����ɽӿ��ĵ�
REST framework�����Զ������������ɽӿ��ĵ���

�ӿ��ĵ�����ҳ�ķ�ʽ���֡�

�Զ��ӿ��ĵ������ɵ��Ǽ̳���APIView�����������ͼ��

1. ��װ����
REST framewrok���ɽӿ��ĵ���Ҫcoreapi���֧�֡�

pip install coreapi
2. ���ýӿ��ĵ�����·��
����·������ӽӿ��ĵ�·����

�ĵ�·�ɶ�Ӧ����ͼ����Ϊrest_framework.documentation.include_docs_urls��

����titleΪ�ӿ��ĵ���վ�ı��⡣

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    ...
    url(r'^docs/', include_docs_urls(title='My API title'))
]
3. �ĵ�����˵���Ķ���λ��
1�� ��һ��������ͼ����ֱ��ʹ������ͼ���ĵ��ַ�������

class BookListView(generics.ListAPIView):
    """
    ��������ͼ����Ϣ.
    """
2�����������������ͼ��������ͼ���ĵ��ַ����У��ֿ��������壬��

class BookListCreateView(generics.ListCreateAPIView):
    """
    get:
    ��������ͼ����Ϣ.

    post:
    �½�ͼ��.
    """
3��������ͼ��ViewSet����������ͼ���ĵ��ַ����з⿪���壬����Ӧʹ��action�������֣���

class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:
    ����ͼ���б�����

    retrieve:
    ����ͼ����������

    latest:
    �������µ�ͼ������

    read:
    �޸�ͼ����Ķ���
    """
4. ���ʽӿ��ĵ���ҳ
��������� 127.0.0.1:8000/docs/�����ɿ����Զ����ɵĽӿ��ĵ���

����˵����
1�� ��ͼ��ViewSet�е�retrieve���ƣ��ڽӿ��ĵ���վ�н���read

2��������Description��Ҫ��ģ��������л�������ֶ�����help_textѡ��壬�磺

class BookInfo(models.Model):
    ...
    bread = models.IntegerField(default=0, verbose_name='�Ķ���', help_text='�Ķ���')
    ...
��

class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ('bread', )
        extra_kwargs = {
            'bread': {
                'required': True,
                'help_text': '�Ķ���'
            }
        }
