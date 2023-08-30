from django import forms
from businessplace_app.models import BusinessPlace, BusinessType
from test_app.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'image', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        image = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file'}
            )
        )

class BusinessPlaceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        DISTRICT_CHOICES = [
            ('เมืองอุดรธานี', 'เมืองอุดรธานี'),
            ('กุดจับ', 'กุดจับ'),
            ('หนองวัวซอ', 'หนองวัวซอ'),
            ('กุมภวาปี', 'กุมภวาปี'),
            ('โนนสะอาด', 'โนนสะอาด'),
            ('หนองหาน', 'หนองหาน'),
            ('ทุ่งฝน', 'ทุ่งฝน'),
            ('ไชยวาน', 'ไชยวาน'),
            ('ศรีธาตุ', 'ศรีธาตุ'),
            ('วังสามหมอ', 'วังสามหมอ'),
            ('บ้านดุง', 'บ้านดุง'),
            ('บ้านผือ', 'บ้านผือ'),
            ('น้ำโสม', 'น้ำโสม'),
            ('เพ็ญ', 'เพ็ญ'),
            ('สร้างคอม', 'สร้างคอม'),
            ('หนองแสง', 'หนองแสง'),
            ('นายูง', 'นายูง'),
            ('พิบูลย์รักษ์', 'พิบูลย์รักษ์'),
            ('กู่แก้ว', 'กู่แก้ว'),
            ('ประจักษ์ศิลปาคม', 'ประจักษ์ศิลปาคม'),
        ]
        
        TYPE_CHOICES = [
            ('1', 'สถานที่ท่องเที่ยว'),
            ('2', 'ที่พัก'),
            ('3', 'ร้านหรือคาเฟ่'),
        ]

        # HOURS_CHOICES = [
        #     ('00', '00'),
        #     ('01', '01'),
        #     ('02', '02'),
        #     ('03', '03'),
        #     ('04', '04'),
        #     ('05', '05'),
        #     ('06', '06'),
        #     ('07', '07'),
        #     ('08', '08'),
        #     ('09', '09'),
        #     ('10', '10'),
        #     ('11', '11'),
        #     ('12', '12'),
        #     ('13', '13'),
        #     ('14', '14'),
        #     ('15', '15'),
        #     ('16', '16'),
        #     ('17', '17'),
        #     ('18', '18'),
        #     ('19', '19'),
        #     ('20', '20'),
        #     ('21', '21'),
        #     ('22', '22'),
        #     ('23', '23'),
        # ]
        
        # MINUTES_CHOICES = [
        #     ('00', '00'),
        #     ('01', '01'),
        #     ('02', '02'),
        #     ('03', '03'),
        #     ('04', '04'),
        #     ('05', '05'),
        #     ('06', '06'),
        #     ('07', '07'),
        #     ('08', '08'),
        #     ('09', '09'),
        #     ('10', '10'),
        #     ('11', '11'),
        #     ('12', '12'),
        #     ('13', '13'),
        #     ('14', '14'),
        #     ('15', '15'),
        #     ('16', '16'),
        #     ('17', '17'),
        #     ('18', '18'),
        #     ('19', '19'),
        #     ('20', '20'),
        #     ('21', '21'),
        #     ('22', '22'),
        #     ('23', '23'),
        #     ('24', '24'),
        #     ('25', '25'),
        #     ('26', '26'),
        #     ('27', '27'),
        #     ('28', '28'),
        #     ('29', '29'),
        #     ('30', '30'),
        #     ('31', '31'),
        #     ('32', '32'),
        #     ('33', '33'),
        #     ('34', '34'),
        #     ('35', '35'),
        #     ('36', '36'),
        #     ('37', '37'),
        #     ('38', '38'),
        #     ('39', '39'),
        #     ('40', '40'),
        #     ('41', '41'),
        #     ('42', '42'),
        #     ('43', '43'),
        #     ('44', '44'),
        #     ('45', '45'),
        #     ('46', '46'),
        #     ('47', '47'),
        #     ('48', '48'),
        #     ('49', '49'),
        #     ('50', '50'),
        #     ('51', '51'),
        #     ('52', '52'),
        #     ('53', '53'),
        #     ('54', '54'),
        #     ('55', '55'),
        #     ('56', '56'),
        #     ('57', '57'),
        #     ('58', '58'),
        #     ('59', '59'),
        #     ('60', '60'),
        # ]
    
        super().__init__(*args, **kwargs)

        self.fields['district'].widget = forms.Select(
            choices=DISTRICT_CHOICES, attrs={'class': 'form-control'})
        self.fields['type'].widget = forms.Select(
            choices=TYPE_CHOICES, attrs={'class': 'form-control'})
        self.fields['detail'].required = False
        self.fields['vr'].required = False
        self.fields['website'].required = False
        self.fields['timeOpen'].required = False
        self.fields['timeClose'].required = False

    class Meta:
        model = BusinessPlace

        fields = ['name', 'district', 'type', 'address', 'lat', 'lng',  'detail', 'timeOpen', 'timeClose',
                  'website', 'pic1', 'pic2', 'pic3', 'vr', 'place_user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'timeOpen': forms.TimeInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'timeClose': forms.TimeInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'vr': forms.URLInput(attrs={'class': 'form-control'},),
            'place_user': forms.NumberInput(attrs={'class': 'form-control'},),
        }
        detail = forms.CharField(required=False, widget=forms.Textarea(
            attrs={'class': 'form-label', 'rows': 4, 'cols': 40}, ), )
        
        pic1 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic1'}
            )
        )
        pic2 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic2'}
            )
        )
        pic3 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic3'}
            )
        )
        
        lat = forms.FloatField(
            required=False, max_value=10, min_value=0,
            widget=forms.NumberInput(
                attrs={'class': 'form-label', 'type': 'number'}
            )
        )
        lng = forms.FloatField(
            required=False, max_value=10, min_value=0,
            widget=forms.NumberInput(
                attrs={'class': 'form-label', 'type': 'number'}
            )
        )

class BusinessPlaceEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        DISTRICT_CHOICES = [
            ('เมืองอุดรธานี', 'เมืองอุดรธานี'),
            ('กุดจับ', 'กุดจับ'),
            ('หนองวัวซอ', 'หนองวัวซอ'),
            ('กุมภวาปี', 'กุมภวาปี'),
            ('โนนสะอาด', 'โนนสะอาด'),
            ('หนองหาน', 'หนองหาน'),
            ('ทุ่งฝน', 'ทุ่งฝน'),
            ('ไชยวาน', 'ไชยวาน'),
            ('ศรีธาตุ', 'ศรีธาตุ'),
            ('วังสามหมอ', 'วังสามหมอ'),
            ('บ้านดุง', 'บ้านดุง'),
            ('บ้านผือ', 'บ้านผือ'),
            ('น้ำโสม', 'น้ำโสม'),
            ('เพ็ญ', 'เพ็ญ'),
            ('สร้างคอม', 'สร้างคอม'),
            ('หนองแสง', 'หนองแสง'),
            ('นายูง', 'นายูง'),
            ('พิบูลย์รักษ์', 'พิบูลย์รักษ์'),
            ('กู่แก้ว', 'กู่แก้ว'),
            ('ประจักษ์ศิลปาคม', 'ประจักษ์ศิลปาคม'),
        ]
        TYPE_CHOICES = [
            ('1', 'สถานที่ท่องเที่ยว'),
            ('2', 'ที่พัก'),
            ('3', 'ร้านหรือคาเฟ่'),
        ]
        
        HOURS_CHOICES = [
            ('00', '00'),
            ('01', '01'),
            ('02', '02'),
            ('03', '03'),
            ('04', '04'),
            ('05', '05'),
            ('06', '06'),
            ('07', '07'),
            ('08', '08'),
            ('09', '09'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
        ]
        
        MINUTES_CHOICES = [
            ('00', '00'),
            ('01', '01'),
            ('02', '02'),
            ('03', '03'),
            ('04', '04'),
            ('05', '05'),
            ('06', '06'),
            ('07', '07'),
            ('08', '08'),
            ('09', '09'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
            ('26', '26'),
            ('27', '27'),
            ('28', '28'),
            ('29', '29'),
            ('30', '30'),
            ('31', '31'),
            ('32', '32'),
            ('33', '33'),
            ('34', '34'),
            ('35', '35'),
            ('36', '36'),
            ('37', '37'),
            ('38', '38'),
            ('39', '39'),
            ('40', '40'),
            ('41', '41'),
            ('42', '42'),
            ('43', '43'),
            ('44', '44'),
            ('45', '45'),
            ('46', '46'),
            ('47', '47'),
            ('48', '48'),
            ('49', '49'),
            ('50', '50'),
            ('51', '51'),
            ('52', '52'),
            ('53', '53'),
            ('54', '54'),
            ('55', '55'),
            ('56', '56'),
            ('57', '57'),
            ('58', '58'),
            ('59', '59'),
            ('60', '60'),
        ]

        super().__init__(*args, **kwargs)

        self.fields['district'].widget = forms.Select(
            choices=DISTRICT_CHOICES, attrs={'class': 'form-control'})
        self.fields['type'].widget = forms.Select(
            choices=TYPE_CHOICES, attrs={'class': 'form-control'})
        self.fields['timeOpen'].widget = forms.Select(
            choices=HOURS_CHOICES, attrs={'class': 'form-control'})
        self.fields['timeClose'].widget = forms.Select(
            choices=MINUTES_CHOICES, attrs={'class': 'form-control'})
        self.fields['detail'].required = False
        self.fields['vr'].required = False
        self.fields['website'].required = False
        self.fields['timeOpen'].required = False
        self.fields['timeClose'].required = False

    class Meta:
        model = BusinessPlace

        fields = ['name', 'district', 'type', 'address', 'lat', 'lng',  'detail', 'timeOpen', 'timeClose',
                  'website', 'pic1', 'pic2', 'pic3', 'vr', 'place_user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'timeOpen': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            # 'timeClose': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'vr': forms.URLInput(attrs={'class': 'form-control'},),
            'place_user': forms.NumberInput(attrs={'class': 'form-control'},),
        }
        detail = forms.CharField(required=False, widget=forms.Textarea(
            attrs={'class': 'form-label', 'rows': 4, 'cols': 40}, ), )
        
        pic1 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic1'}
            )
        )
        pic2 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic2'}
            )
        )
        pic3 = forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'name': 'pic3'}
            )
        )
        
        lat = forms.FloatField(
            required=False, max_value=10, min_value=0,
            widget=forms.NumberInput(
                attrs={'class': 'form-label', 'type': 'number'}
            )
        )
        lng = forms.FloatField(
            required=False, max_value=10, min_value=0,
            widget=forms.NumberInput(
                attrs={'class': 'form-label', 'type': 'number'}
            )
        )
