from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum


def register_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        course_id = request.POST.get('course')
        image = request.FILES.get('image')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return render(request, 'items/student.html', {
                'courses': courses,
                'error': 'Selected course does not exist.'
            })

        if name and course and sex and phone and address and email:
            student = Student.objects.create(
                name=name,
                email=email,
                address=address,
                phone=phone,
                sex=sex,
                course=course,
                image=image
            )
            return redirect('start_payment', student_id=student.id)

        return render(request, 'items/student.html', {
            'courses': courses,
            'error': 'All fields are required.'
        })

    return render(request, 'items/student.html', {'courses': courses})


def start_payment(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'items/payment.html', {'student': student, 'amount': student.course.fee})

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        payment_reference = request.POST.get('reference')

        student = get_object_or_404(Student, id=student_id)

        Payment.objects.create(
            student=student,
            amount=student.course.fee,
            Payment_method='paystack',
            payment_reference=payment_reference
        )

        return render(request, 'items/payment_success.html', {
            'student': student,
            'reference': payment_reference
        })

    return redirect('dashboard')



def dashboard(request):
    students = Student.objects.all()
    payments = Payment.objects.all()
    total_students = students.count()
    total_paid = payments.aggregate(total=Sum('amount'))['total'] or 0

    context = {
        "students": students,
        "payments": payments,
        "total_students": total_students,
        "total_paid": total_paid,
    }

    return render(request, 'items/dashboard.html', context)
