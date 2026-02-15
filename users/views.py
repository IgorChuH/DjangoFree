from django.views.generic import CreateView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

"""class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']  # разрешаем GET и POST
    next_page = 'home'"""


