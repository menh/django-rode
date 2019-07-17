DRF (Django REST framework) ��ܽ���(2)
https://www.cnblogs.com/yinjiangchong/p/9304318.html
������װ������
DRF��Ҫ����������
*	Python (2.7, 3.2, 3.3, 3.4, 3.5, 3.6)
*	Django (1.10, 1.11, 2.0)
DRF����Django��չӦ�õķ�ʽ�ṩ�ģ��������ǿ���ֱ���������е�Django������������´���������û��Django��������Ҫ�ȴ���������װDjango��
1. ��װDRF
pip install djangorestframework
2. ���rest_frameworkӦ��
����������Django���ѧϰ�д�����demo���̣���settings.py��INSTALLED_APPS�����'rest_framework'��
INSTALLED_APPS = [
    ...
    'rest_framework',
]
�������Ϳ���ʹ��DRF���п����ˡ�
��ʶDRF������
����������ѧϰDjango���ʱʹ�õ�ͼ��Ӣ��Ϊ������ʹ��Django REST framework����ʵ��ͼ���REST API��
1. �������л���
��booktestӦ�����½�serializers.py���ڱ����Ӧ�õ����л�����
����һ��BookInfoSerializer�������л��뷴���л���
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = '__all__'
*	model ָ�������л�������������ֶδ�ģ����BookInfo�ο�����
*	fields ָ�������л�������ģ�����е���Щ�ֶΣ�'__all__'ָ�����������ֶ�
2. ��д��ͼ
��booktestӦ�õ�views.py�д�����ͼBookInfoViewSet������һ����ͼ���ϡ�
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
*	queryset ָ������ͼ���ڲ�ѯ����ʱʹ�õĲ�ѯ��
*	serializer_class ָ������ͼ�ڽ������л������л�ʱʹ�õ����л���
3. ����·��
��booktestӦ�õ�urls.py�ж���·����Ϣ��
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    ...
]

router = DefaultRouter()  # ���Դ�����ͼ��·����
router.register(r'books', views.BookInfoViewSet)  # ��·������ע����ͼ��

urlpatterns += router.urls  # ��·�����е�����·����Ϣ׷����django��·���б���
4. ���в���
���е�ǰ����������Djangoһ����
python manage.py runserver
���������������ַ127.0.0.1:8000�����Կ���DRF�ṩ��API Web���ҳ��.
Serializer���л���
���л��������ã�
1.	�������ݵ�У��
2.	�����ݶ������ת��
����Serializer
1. ���巽��
Django REST framework�е�Serializerʹ���������壬��̳���rest_framework.serializers.Serializer��
���磬����������һ�����ݿ�ģ����BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='����')
    bpub_date = models.DateField(verbose_name='��������', null=True)
    bread = models.IntegerField(default=0, verbose_name='�Ķ���')
    bcomment = models.IntegerField(default=0, verbose_name='������')
    image = models.ImageField(upload_to='booktest', verbose_name='ͼƬ', null=True)
������Ϊ���ģ�����ṩһ�����л��������Զ������£�
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='����', max_length=20)
    bpub_date = serializers.DateField(label='��������', required=False)
    bread = serializers.IntegerField(label='�Ķ���', required=False)
    bcomment = serializers.IntegerField(label='������', required=False)
    image = serializers.ImageField(label='ͼƬ', required=False)
ע�⣺serializer����ֻ��Ϊ���ݿ�ģ���ඨ�壬Ҳ����Ϊ�����ݿ�ģ��������ݶ��塣serializer�Ƕ��������ݿ�֮��Ĵ��ڡ�
2. �ֶ���ѡ��
�����ֶ����ͣ�
�ֶ�	�ֶι��췽ʽ
BooleanField	BooleanField()
NullBooleanField	NullBooleanField()
CharField	CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
EmailField	EmailField(max_length=None, min_length=None, allow_blank=False)
RegexField	RegexField(regex, max_length=None, min_length=None, allow_blank=False)
SlugField	SlugField(maxlength=50, min_length=None, allow_blank=False)
�����ֶΣ���֤����ģʽ [a-zA-Z0-9-]+
URLField	URLField(max_length=200, min_length=None, allow_blank=False)
UUIDField	UUIDField(format='hex_verbose')
format:
1) 'hex_verbose' ��"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"
2�� 'hex' �� "5ce0e9a55ffa654bcee01238041fb31a"
3��'int' - ��: "123456789012312313134124512351145145114"
4��'urn' ��: "urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"
IPAddressField	IPAddressField(protocol='both', unpack_ipv4=False, **options)
IntegerField	IntegerField(max_value=None, min_value=None)
FloatField	FloatField(max_value=None, min_value=None)
DecimalField	DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)
max_digits: ���λ��
decimal_palces: С����λ��
DateTimeField	DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None)
DateField	DateField(format=api_settings.DATE_FORMAT, input_formats=None)
TimeField	TimeField(format=api_settings.TIME_FORMAT, input_formats=None)
DurationField	DurationField()
ChoiceField	ChoiceField(choices)
choices��Django���÷���ͬ
MultipleChoiceField	MultipleChoiceField(choices)
FileField	FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)
ImageField	ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)
ListField	ListField(child=<a_field_instance>, min_length=None, max_length=None)
DictField	DictField(child=<a_field_instance>)
ѡ�������
��������	����
max_length	��󳤶�
min_lenght	��С����
allow_blank	�Ƿ�����Ϊ��
trim_whitespace	�Ƿ�ضϿհ��ַ�
max_value	��Сֵ
min_value	���ֵ
ͨ�ò�����

��������	˵��
read_only	�������ֶν��������л������Ĭ��False
write_only	�������ֶν����ڷ����л����룬Ĭ��False
required	�������ֶ��ڷ����л�ʱ�������룬Ĭ��True
default	�����л�ʱʹ�õ�Ĭ��ֵ
allow_null	�������ֶ��Ƿ�������None��Ĭ��False
validators	���ֶ�ʹ�õ���֤��
error_messages	�����������������Ϣ���ֵ�
label	����HTMLչʾAPIҳ��ʱ����ʾ���ֶ�����
help_text	����HTMLչʾAPIҳ��ʱ����ʾ���ֶΰ�����ʾ��Ϣ

3. ����Serializer����
�����Serializer��󣬾Ϳ��Դ���Serializer�����ˡ�
Serializer�Ĺ��췽��Ϊ��
Serializer(instance=None, data=empty, **kwarg)
˵����
1���������л�ʱ����ģ���������instance����
2�����ڷ����л�ʱ����Ҫ�������л������ݴ���data����
3������instance��data�����⣬�ڹ���Serializer����ʱ������ͨ��context��������������ݣ���
serializer = AccountSerializer(account, context={'request': request})
ͨ��context�������ӵ����ݣ�����ͨ��Serializer�����context���Ի�ȡ��
���л�ʹ��
������django shell����ѧϰ���л�����ʹ�á�
python manage.py shell
1 ����ʹ��
1�� �Ȳ�ѯ��һ��ͼ�����
from booktest.models import BookInfo

book = BookInfo.objects.get(id=2)
2�� �������л�������
from booktest.serializers import BookInfoSerializer

serializer = BookInfoSerializer(book)
3����ȡ���л�����
ͨ��data���Կ��Ի�ȡ���л��������
serializer.data
# {'id': 2, 'btitle': '�����˲�', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None}
4�����Ҫ�����л����ǰ����������ݵĲ�ѯ��QuerySet������ͨ�����many=True��������˵��
book_qs = BookInfo.objects.all()
serializer = BookInfoSerializer(book_qs, many=True)
serializer.data
# [OrderedDict([('id', 2), ('btitle', '�����˲�'), ('bpub_date', '1986-07-24'), ('bread', 36), ('bcomment', 40), ('image', N]), OrderedDict([('id', 3), ('btitle', 'Ц������'), ('bpub_date', '1995-12-24'), ('bread', 20), ('bcomment', 80), ('image'ne)]), OrderedDict([('id', 4), ('btitle', 'ѩɽ�ɺ�'), ('bpub_date', '1987-11-11'), ('bread', 58), ('bcomment', 24), ('ima None)]), OrderedDict([('id', 5), ('btitle', '���μ�'), ('bpub_date', '1988-01-01'), ('bread', 10), ('bcomment', 10), ('im', 'booktest/xiyouji.png')])]
2 ��������Ƕ�����л�
�����Ҫ���л��������а�������������������Թ����������ݵ����л���Ҫָ����
���磬�ڶ���Ӣ�����ݵ����л���ʱ�����hbook����������ͼ�飩�ֶ�������л���
�����ȶ���HeroInfoSerialzier������ֶ������������
class HeroInfoSerializer(serializers.Serializer):
    """Ӣ���������л���"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='����', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='�Ա�', required=False)
    hcomment = serializers.CharField(label='������Ϣ', max_length=200, required=False, allow_null=True)
���ڹ����ֶΣ����Բ������¼��ַ�ʽ��
1�� PrimaryKeyRelatedField
���ֶν������л�Ϊ���������������
hbook = serializers.PrimaryKeyRelatedField(label='ͼ��', read_only=True)
��
hbook = serializers.PrimaryKeyRelatedField(label='ͼ��', queryset=BookInfo.objects.all())
ָ���ֶ�ʱ��Ҫ����read_only=True����queryset������
*	����read_only=True����ʱ�����ֶν��������������л�ʹ��
*	����queryset����ʱ���������������л�ʱ����У��ʹ��
ʹ��Ч����
from booktest.serializers import HeroInfoSerializer
from booktest.models import HeroInfo
hero = HeroInfo.objects.get(id=6)
serializer = HeroInfoSerializer(hero)
serializer.data
# {'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': 2}
2) StringRelatedField
���ֶν������л�Ϊ����������ַ�����ʾ��ʽ����__str__�����ķ���ֵ��
hbook = serializers.StringRelatedField(label='ͼ��')
ʹ��Ч��
{'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': '�����˲�'}
3��HyperlinkedRelatedField
���ֶν������л�Ϊ��ȡ�����������ݵĽӿ�����
hbook = serializers.HyperlinkedRelatedField(label='ͼ��', read_only=True, view_name='books-detail')
����ָ��view_name�������Ա�DRF������ͼ����Ѱ��·�ɣ�����ƴ�ӳ�����URL��
ʹ��Ч��
{'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': 'http://127.0.0.1:8000/books/2/'}
������ʱ��û�ж�����ͼ���˷�ʽ������ʾ��
4��SlugRelatedField
���ֶν������л�Ϊ���������ָ���ֶ�����
hbook = serializers.SlugRelatedField(label='ͼ��', read_only=True, slug_field='bpub_date')
slug_fieldָ��ʹ�ù���������ĸ��ֶ�
ʹ��Ч��
{'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': datetime.date(1986, 7, 24)}
5��ʹ�ù�����������л���
hbook = BookInfoSerializer()
ʹ��Ч��
{'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': OrderedDict([('id', 2), ('btitle', '�����˲�')te', '1986-07-24'), ('bread', 36), ('bcomment', 40), ('image', None)])}
6�� ��дto_representation����
���л�����ÿ���ֶ�ʵ�ʶ����ɸ��ֶ����͵�to_representation����������ʽ�ģ�����ͨ����д�÷�����������ʽ��
ע�⣬to_representations�������������ڿ��ƹ��������ʽ�ϣ������ڸ������л����ֶ����͡�
�Զ���һ���µĹ����ֶΣ�
class BookRelateField(serializers.RelatedField):
    """�Զ������ڴ���ͼ����ֶ�"""
    def to_representation(self, value):
        return 'Book: %d %s' % (value.id, value.btitle)
ָ��hbookΪBookRelateField����
hbook = BookRelateField(read_only=True)
ʹ��Ч��
{'id': 6, 'hname': '�Ƿ�', 'hgender': 1, 'hcomment': '����ʮ����', 'hbook': 'Book: 2 �����˲�'}
many����
��������Ķ������ݲ���ֻ��һ�������ǰ���������ݣ��������л�ͼ��BookInfo���ݣ�ÿ��BookInfo���������Ӣ��HeroInfo��������ж������ʱ�����ֶ����͵�ָ���Կ�ʹ���������ַ�ʽ��ֻ�������������ֶ�ʱ���ಹ��һ��many=True�������ɡ�
�˴�����PrimaryKeyRelatedField������������������ͬ��
��BookInfoSerializer����ӹ����ֶΣ�
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='����', max_length=20)
    bpub_date = serializers.DateField(label='��������', required=False)
    bread = serializers.IntegerField(label='�Ķ���', required=False)
    bcomment = serializers.IntegerField(label='������', required=False)
    image = serializers.ImageField(label='ͼƬ', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # ����
ʹ��Ч����
from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
book = BookInfo.objects.get(id=2)
serializer = BookInfoSerializer(book)
serializer.data
# {'id': 2, 'btitle': '�����˲�', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None,

�����л�ʹ��
1. ��֤
ʹ�����л������з����л�ʱ����Ҫ�����ݽ�����֤�󣬲��ܻ�ȡ��֤�ɹ������ݻ򱣴��ģ�������
�ڻ�ȡ�����л�������ǰ���������is_valid()����������֤����֤�ɹ�����True�����򷵻�False��
��֤ʧ�ܣ�����ͨ�����л��������errors���Ի�ȡ������Ϣ�������ֵ䣬�������ֶκ��ֶεĴ�������Ƿ��ֶδ��󣬿���ͨ���޸�REST framework�����е�NON_FIELD_ERRORS_KEY�����ƴ����ֵ��еļ�����
��֤�ɹ�������ͨ�����л��������validated_data���Ի�ȡ���ݡ�
�ڶ������л���ʱ��ָ��ÿ���ֶε����л����ͺ�ѡ��������������һ����֤��Ϊ��
������ǰ�涨�����BookInfoSerializer
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='����', max_length=20)
    bpub_date = serializers.DateField(label='��������', required=False)
    bread = serializers.IntegerField(label='�Ķ���', required=False)
    bcomment = serializers.IntegerField(label='������', required=False)
    image = serializers.ImageField(label='ͼƬ', required=False)
ͨ���������л������󣬲���Ҫ�����л������ݴ��ݸ�data�������������������֤
from booktest.serializers import BookInfoSerializer
data = {'bpub_date': 123}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # ����False
serializer.errors
# {'btitle': [ErrorDetail(string='This field is required.', code='required')], 'bpub_date': [ErrorDetail(string='Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]].', code='invalid')]}
serializer.validated_data  # {}

data = {'btitle': 'python'}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # True
serializer.errors  # {}
serializer.validated_data  #  OrderedDict([('btitle', 'python')])
is_valid()��������������֤ʧ��ʱ�׳��쳣serializers.ValidationError������ͨ������raise_exception=True����������REST framework���յ����쳣������ǰ�˷���HTTP 400 Bad Request��Ӧ��
# Return a 400 response if the data was invalid.
serializer.is_valid(raise_exception=True)
���������Щ����������Ҫ�ٲ��䶨����֤��Ϊ������ʹ���������ַ�������֤�����ȼ���validators >validate_<field_name> >validate
1��validate_<field_name>
��<field_name>�ֶν�����֤����
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    ...

    def validate_btitle(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("ͼ�鲻�ǹ���Django��")
        return value
����
from booktest.serializers import BookInfoSerializer
data = {'btitle': 'python'}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # False
serializer.errors
#  {'btitle': [ErrorDetail(string='ͼ�鲻�ǹ���Django��', code='invalid')]}
2��validate
�����л�������Ҫͬʱ�Զ���ֶν��бȽ���֤ʱ�����Զ���validate��������֤����
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    ...

    def validate(self, attrs):
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('�Ķ���С��������')
        return attrs
����
from booktest.serializers import BookInfoSerializer
data = {'btitle': 'about django', 'bread': 10, 'bcomment': 20}
s = BookInfoSerializer(data=data)
s.is_valid()  # False
s.errors
#  {'non_field_errors': [ErrorDetail(string='�Ķ���С��������', code='invalid')]}
3��validators
���ֶ������validatorsѡ�������Ҳ���Բ�����֤��Ϊ����

def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError("ͼ�鲻�ǹ���Django��")

class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='����', max_length=20, validators=[about_django])
    bpub_date = serializers.DateField(label='��������', required=False)
    bread = serializers.IntegerField(label='�Ķ���', required=False)
    bcomment = serializers.IntegerField(label='������', required=False)
    image = serializers.ImageField(label='ͼƬ', required=False)
���ԣ�
from booktest.serializers import BookInfoSerializer
data = {'btitle': 'python'}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # False
serializer.errors
#  {'btitle': [ErrorDetail(string='ͼ�鲻�ǹ���Django��', code='invalid')]}
REST framework�ṩ��validators:
*	UniqueValidator
���ֶ�Ψһ����
from rest_framework.validators import UniqueValidator

slug = SlugField(
    max_length=100,
    validators=[UniqueValidator(queryset=BlogPost.objects.all())]
)
*	UniqueTogetherValidation
����Ψһ����
from rest_framework.validators import UniqueTogetherValidator

class ExampleSerializer(serializers.Serializer):
    # ...
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=ToDoItem.objects.all(),
                fields=('list', 'position')
            )
        ]
2. ����
�������֤�ɹ�����Ҫ����validated_data������ݶ���Ĵ���������ͨ��ʵ��create()��update()����������ʵ�֡�
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    ...

    def create(self, validated_data):
        """�½�"""
        return BookInfo(**validated_data)

    def update(self, instance, validated_data):
        """���£�instanceΪҪ���µĶ���ʵ��"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        return instance
�����Ҫ�ڷ������ݶ����ʱ��Ҳ�����ݱ��浽���ݿ��У�����Խ��������޸�
class BookInfoSerializer(serializers.Serializer):
    """ͼ���������л���"""
    ...

    def create(self, validated_data):
        """�½�"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """���£�instanceΪҪ���µĶ���ʵ��"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance
ʵ�������������������ڷ����л����ݵ�ʱ�򣬾Ϳ���ͨ��save()��������һ�����ݶ���ʵ����
book = serializer.save()
����������л��������ʱ��û�д���instanceʵ���������save()������ʱ��create()�����ã��෴�����������instanceʵ���������save()������ʱ��update()�����á�
from db.serializers import BookInfoSerializer
data = {'btitle': '��������'}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # True
serializer.save()  # <BookInfo: ��������>

from db.models import BookInfo
book = BookInfo.objects.get(id=2)
data = {'btitle': '���콣'}
serializer = BookInfoSerializer(book, data=data)
serializer.is_valid()  # True
serializer.save()  # <BookInfo: ���콣>
book.btitle  # '���콣'
����˵����
1�� �ڶ����л�������save()����ʱ�����Զ��⴫�����ݣ���Щ���ݿ�����create()��update()�е�validated_data������ȡ��
serializer.save(owner=request.user)
2��Ĭ�����л������봫������required���ֶΣ�������׳���֤�쳣���������ǿ���ʹ��partial�������������ֶθ���
# Update `comment` with partial data
serializer = CommentSerializer(comment, data={'content': u'foo bar'}, partial=True)
ģ�������л���ModelSerializer
���������Ҫʹ�����л�����Ӧ����Django��ģ���࣬DRFΪ�����ṩ��ModelSerializerģ�������л������������ǿ��ٴ���һ��Serializer�ࡣ
ModelSerializer�볣���Serializer��ͬ�����ṩ�ˣ�
*	����ģ�����Զ�����һϵ���ֶ�
*	����ģ�����Զ�ΪSerializer����validators������unique_together
*	����Ĭ�ϵ�create()��update()��ʵ��
1. ����
�������Ǵ���һ��BookInfoSerializer
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = '__all__'
*	model ָ�������ĸ�ģ����
*	fields ָ��Ϊģ�������Щ�ֶ�����
���ǿ�����python manage.py shell�в鿴�Զ����ɵ�BookInfoSerializer�ľ���ʵ��
>>> from booktest.serializers import BookInfoSerializer
>>> serializer = BookInfoSerializer()
>>> serializer
BookInfoSerializer():
    id = IntegerField(label='ID', read_only=True)
    btitle = CharField(label='����', max_length=20)
    bpub_date = DateField(allow_null=True, label='��������', required=False)
    bread = IntegerField(label='�Ķ���', max_value=2147483647, min_value=-2147483648, required=False)
    bcomment = IntegerField(label='������', max_value=2147483647, min_value=-2147483648, required=False)
    image = ImageField(allow_null=True, label='ͼƬ', max_length=100, required=False)
2. ָ���ֶ�
1) ʹ��fields����ȷ�ֶΣ�__all__�������������ֶΣ�Ҳ����д��������Щ�ֶΣ���
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date')
2) ʹ��exclude������ȷ�ų�����Щ�ֶ�
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        exclude = ('image',)
3) Ĭ��ModelSerializerʹ��������Ϊ�����ֶΣ��������ǿ���ʹ��depth���򵥵�����Ƕ�ױ�ʾ��depthӦ��������������Ƕ�׵Ĳ㼶�������磺
class HeroInfoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'
        depth = 1
�γɵ����л������£�
HeroInfoSerializer():
    id = IntegerField(label='ID', read_only=True)
    hname = CharField(label='����', max_length=20)
    hgender = ChoiceField(choices=((0, 'male'), (1, 'female')), label='�Ա�', required=False, validators=[<django.core.valators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
    hcomment = CharField(allow_null=True, label='������Ϣ', max_length=200, required=False)
    hbook = NestedSerializer(read_only=True):
        id = IntegerField(label='ID', read_only=True)
        btitle = CharField(label='����', max_length=20)
        bpub_date = DateField(allow_null=True, label='��������', required=False)
        bread = IntegerField(label='�Ķ���', max_value=2147483647, min_value=-2147483648, required=False)
        bcomment = IntegerField(label='������', max_value=2147483647, min_value=-2147483648, required=False)
        image = ImageField(allow_null=True, label='ͼƬ', max_length=100, required=False)
4) ��ʾָ���ֶΣ��磺
class HeroInfoSerializer(serializers.ModelSerializer):
    hbook = BookInfoSerializer()

    class Meta:
        model = HeroInfo
        fields = ('id', 'hname', 'hgender', 'hcomment', 'hbook')
5) ָ��ֻ���ֶ�
����ͨ��read_only_fieldsָ��ֻ���ֶΣ������������л�������ֶ�
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date'�� 'bread', 'bcomment')
        read_only_fields = ('id', 'bread', 'bcomment')
3. ��Ӷ������
���ǿ���ʹ��extra_kwargs����ΪModelSerializer��ӻ��޸�ԭ�е�ѡ�����
class BookInfoSerializer(serializers.ModelSerializer):
    """ͼ���������л���"""
    class Meta:
        model = BookInfo
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
        extra_kwargs = {
            'bread': {'min_value': 0, 'required': True},
            'bcomment': {'min_value': 0, 'required': True},
        }

# BookInfoSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    btitle = CharField(label='����', max_length=20)
#    bpub_date = DateField(allow_null=True, label='��������', required=False)
#    bread = IntegerField(label='�Ķ���', max_value=2147483647, min_value=0, required=True)
#    bcomment = IntegerField(label='������', max_value=2147483647, min_value=0, required=True)
