from django.contrib.auth import login, logout
from django.db.models import Q
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *


class MessageList(ListView):
    model = Message
    context_object_name = 'messages'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'messages_and_files/list_of_messages.html'  # поменял имя шаблона

    def get_queryset(self):
        # Показываю только сообщения текущего пользователя
        if self.request.user.pk:
            return Message.objects.filter(Q(sender=self.request.user) | Q(recipient=self.request.user)).distinct()
        return

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Список вопросов'  # Дополнительная переменная
    #     context['categories'] = Category.objects.all()
    #     return context


# class MessageDetail(DetailView):
#     model = Message
#     context_object_name = 'message'
#     template_name = 'questions/one_question.html'  # поменял имя шаблона
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # переменная со списоком категорий
#         context['categories'] = self.get_object().category.all()
#         return context


class AddMessage(CreateView):
    form_class = CreateMessageForm
    template_name = 'messages_and_files/create_message.html'
    success_url = reverse_lazy('messages_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('messages_list')

    else:
        form = UserLoginForm()
    return render(request, 'messages_and_files/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('messages_list')


def download_file(request, pk):
    msg = Message.objects.get(pk=pk)
    return FileResponse(msg.msg_file, as_attachment=True)
