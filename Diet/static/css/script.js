document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // منع إرسال النموذج بشكل تقليدي

    // جمع البيانات من النموذج
    const age = parseInt(document.getElementById('age').value);
    const weight = parseInt(document.getElementById('weight').value);
    const height = parseInt(document.getElementById('height').value);

    // التحقق من العمر
    if (age < 18 || age > 100) {
        alert('العمر يجب أن يكون بين 18 و 100 سنة.');
        return;
    }

    // التحقق من الوزن
    if (weight < 30) {
        alert('الوزن يجب أن يكون 30 كجم على الأقل.');
        return;
    }

    // التحقق من الطول
    if (height < 100 || height > 230) {
        alert('الطول يجب أن يكون بين 100 سم و 230 سم.');
        return;
    }

    // إرسال البيانات إلى الخادم (Back-end)
    const userData = {
        age: age,
        weight: weight,
        height: height,
        gender: document.getElementById('gender').value,
        allergies: document.getElementById('allergies').value,
        activity: document.getElementById('activity').value,
        goal: document.getElementById('goal').value
    };

    fetch('/submit', { // تأكد من تعديل هذا الرابط ليناسب عنوان الخادم الخاص بك
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        alert('تم إرسال البيانات بنجاح!');
        console.log('الرد من الخادم:', data);
    })
    .catch(error => {
        console.error('حدث خطأ:', error);
        alert('حدث خطأ أثناء إرسال البيانات. يرجى المحاولة مرة أخرى.');
    });
});