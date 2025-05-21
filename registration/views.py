# Updated views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Payment
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_POST


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

        if all([name, email, address, phone, sex, course]):
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
@require_POST
def payment_success(request):
    student_id = request.POST.get('student_id')
    payment_reference = request.POST.get('reference')

    if not student_id or not payment_reference:
        return JsonResponse({'error': 'Missing data'}, status=400)

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

    if Payment.objects.filter(payment_reference=payment_reference).exists():
        return JsonResponse({'error': 'Duplicate reference'}, status=409)

    payment = Payment.objects.create(
        student=student,
        amount=student.course.fee,
        Payment_method='paystack',
        payment_reference=payment_reference
    )

    request.session['payment_ref'] = payment.payment_reference
    request.session['student_id'] = student.id
    return JsonResponse({'redirect': '/registration/payment-success/'})


def payment_success_page(request):
    ref = request.session.pop('payment_ref', None)
    student_id = request.session.pop('student_id', None)

    if ref and student_id:
        student = get_object_or_404(Student, id=student_id)
        students = Student.objects.all()
        payments = Payment.objects.all()
        total_students = students.count()
        total_paid = payments.aggregate(total=Sum('amount'))['total'] or 0

        return render(request, 'items/payment_success.html', {
            'student': student,
            'ref': ref,
            'students': students,
            'payments': payments,
            'total_students': total_students,
            'total_paid': total_paid
        })

    return redirect('dashboard')


def dashboard(request):
    students = Student.objects.all()
    payments = Payment.objects.all()
    total_students = students.count()
    total_paid = payments.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'items/dashboard.html', {
        'students': students,
        'payments': payments,
        'total_students': total_students,
        'total_paid': total_paid,
    })
