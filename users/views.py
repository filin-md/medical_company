
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
