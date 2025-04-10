from django.shortcuts import render
from .forms import ContactForm
from .prompt import get_nutrition_plan

def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # استخراج البيانات
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            preference = form.cleaned_data['preference']
            other_preference = form.cleaned_data['other_preference']
            allergy = form.cleaned_data['allergy']
            other_allergy = form.cleaned_data['other_allergy']
            activity_level = form.cleaned_data['activity_level']
            goal = form.cleaned_data['goal']

            # قاموس لتحويل القيم الإنجليزية إلى عربية
            gender_dict = {'M': 'ذكر', 'F': 'أنثى', 'O': 'أخرى'}
            preference_dict = {
                'vegetarian': 'نباتي',
                'vegan': 'نباتي صرف',
                'omnivore': 'آكل كل شيء',
                'keto': 'نظام الكيتو',
                'paleo': 'نظام باليو'
            }
            allergy_dict = {
                'nuts': 'المكسرات',
                'gluten': 'الغلوتين',
                'dairy': 'منتجات الألبان',
                'seafood': 'المأكولات البحرية',
                'other': 'أخرى'
            }
            activity_level_dict = {
                'sedentary': 'قليل النشاط (لا تمارس رياضة)',
                'light': 'نشاط خفيف (تمارس رياضة 1-3 أيام في الأسبوع)',
                'moderate': 'نشاط متوسط (تمارس رياضة 3-5 أيام في الأسبوع)',
                'active': 'نشيط (تمارس رياضة 6-7 أيام في الأسبوع)',
                'very_active': 'نشيط جدًا (تمارس رياضة مكثفة يوميًا)'
            }
            goal_dict = {
                'weight_loss': 'فقدان الوزن',
                'weight_gain': 'زيادة الوزن',
                'maintenance': 'الحفاظ على الوزن',
                'muscle_building': 'بناء العضلات'
            }

            # تحويل القيم إلى العربية
            gender_arabic = gender_dict.get(gender, gender)
            preference_arabic = [preference_dict.get(item, item) for item in preference]
            allergy_arabic = [allergy_dict.get(item, item) for item in allergy]
            activity_level_arabic = activity_level_dict.get(activity_level, activity_level)
            goal_arabic = goal_dict.get(goal, goal)

            # إضافة التفضيلات الغذائية والحساسية المكتوبة يدويًا إذا تم إدخالها
            if other_preference.strip():
                preference_arabic.append(other_preference.strip())
            
            if other_allergy.strip():
                allergy_arabic.append(other_allergy.strip())

            # استدعاء دالة `get_nutrition_plan`
            data = get_nutrition_plan(age, gender_arabic, height, weight, preference_arabic, allergy_arabic, activity_level_arabic, goal_arabic)
            plan = data["plan"]

            # إرسال البيانات إلى القالب
            return render(request, 'success.html', {
                'age': age,
                'gender': gender_arabic,
                'height': height,
                'weight': weight,
                'preference': preference_arabic,
                'allergy': allergy_arabic,
                'activity_level': activity_level_arabic,
                'goal': goal_arabic,
                'plan': plan
            })

    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
