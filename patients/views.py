import io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PatientSearchForm
from .models import Patient
from docx import Document
from django.http import HttpResponse


def home(request):
    return render(request, 'patients/home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'patients/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        from django.contrib.auth import authenticate
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'patients/login.html')

# Генерация рекомендаций в формате DOCX
def generate_recommendation(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    # Создаем документ Word
    doc = Document()
    doc.add_heading("Рекомендации по реабилитации", level=1)

    doc.add_paragraph(f"ФИО: {patient.full_name}")

    if patient.birth_date:
        age = patient.get_age()
        doc.add_paragraph(f"Дата рождения: {patient.birth_date.strftime('%d.%m.%Y')} ({age} полных лет)")
    else:
        doc.add_paragraph("Дата рождения: не указана")

    doc.add_paragraph(f"Пол: {patient.get_gender_display() or 'Не указан'}")
    doc.add_paragraph(f"Диагноз: {patient.diagnosis}")
    doc.add_paragraph(f"Рекомендации: {patient.recommendations}")

    # Сохраняем в буфер
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    # Отправляем пользователю
    response = HttpResponse(buffer.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename=recommendation_{patient.full_name}.docx'
    return response

@login_required
def my_patients(request):
    patients = Patient.objects.filter(attending_doctor=request.user)
    return render(request, 'patients/my_patients.html', {'patients': patients})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def print_doc(request):
    patients = []
    form = PatientSearchForm(request.GET or None)
    if form.is_valid() and form.cleaned_data['full_name']:
        patients = Patient.objects.filter(full_name__icontains=form.cleaned_data['full_name'])

    if 'generate' in request.GET:
        patient_id = request.GET.get('patient_id')
        patient = Patient.objects.get(id=patient_id)

        # Генерация Word-документа
        document = Document()
        document.add_heading('Рекомендации по реабилитации', 0)

        document.add_paragraph(f"Пациент: {patient.full_name}")

        if patient.birth_date:
            age = patient.get_age()
            birth_date_str = patient.birth_date.strftime('%d.%m.%Y')
            document.add_paragraph(f"Дата рождения: {birth_date_str} ({age} полных лет)")
        else:
            document.add_paragraph("Дата рождения: не указана")
            
        document.add_paragraph(f"Пол: {patient.get_gender_display() or 'Не указан'}")
        document.add_paragraph(f"Диагноз: {patient.diagnosis}")
        document.add_paragraph(f"Рекомендации: {patient.recommendations}")

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=рекомендации_{patient.id}.docx'
        document.save(response)
        return response

    return render(request, 'patients/print_doc.html', {'form': form, 'patients': patients})