from django import forms

class ContactForm(forms.Form):
    age = forms.IntegerField(
        min_value=18,
        max_value=100,
        label="العمر",
        help_text="يجب أن يكون العمر بين 18 و100 سنة."
    )

    gender = forms.ChoiceField(
        choices=[('M', 'ذكر'), ('F', 'أنثى'), ('O', 'أخرى')],
        label="الجنس",
        widget=forms.RadioSelect,
    )

    height = forms.FloatField(
        min_value=50.0,
        max_value=250.0,
        label="الطول (سم)",
        help_text="يجب أن يكون الطول بين 50 سم و250 سم."
    )

    weight = forms.FloatField(
        min_value=30.0,
        max_value=300.0,
        label="الوزن (كجم)",
        help_text="يجب أن يكون الوزن بين 30 كجم و300 كجم."
    )

    preference = forms.MultipleChoiceField(
        choices=[
            ('vegetarian', 'نباتي'),
            ('vegan', 'نباتي صرف'),
            ('omnivore', 'آكل كل شيء'),
            ('keto', 'نظام الكيتو'),
            ('paleo', 'نظام باليو')
        ],
        label="التفضيلات الغذائية",
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_preference = forms.CharField(
        label="تفضيلات غذائية أخرى",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'اكتب أي تفضيلات غذائية أخرى هنا'})
    )

    allergy = forms.MultipleChoiceField(
        choices=[
            ('nuts', 'المكسرات'),
            ('gluten', 'الغلوتين'),
            ('dairy', 'منتجات الألبان'),
            ('seafood', 'المأكولات البحرية')
        ],
        label="الحساسية",
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_allergy = forms.CharField(
        label="حساسية أخرى",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'اكتب أي حساسية أخرى هنا'})
    )

    activity_level = forms.ChoiceField(
        choices=[
            ('sedentary', 'قليل النشاط (لا تمارس رياضة)'),
            ('light', 'نشاط خفيف (تمارس رياضة 1-3 أيام في الأسبوع)'),
            ('moderate', 'نشاط متوسط (تمارس رياضة 3-5 أيام في الأسبوع)'),
            ('active', 'نشيط (تمارس رياضة 6-7 أيام في الأسبوع)'),
            ('very_active', 'نشيط جدًا (تمارس رياضة مكثفة يوميًا)')
        ],
        label="مستوى النشاط",
        widget=forms.Select,
    )

    goal = forms.ChoiceField(
        choices=[
            ('weight_loss', 'فقدان الوزن'),
            ('weight_gain', 'زيادة الوزن'),
            ('maintenance', 'الحفاظ على الوزن'),
            ('muscle_building', 'بناء العضلات')
        ],
        label="الهدف",
        widget=forms.Select,
    )
