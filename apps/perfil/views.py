from django.shortcuts import get_object_or_404, render
from contas.models import MyUser

# Create your views here.
def perfil_view(request, username):
    modelo = MyUser.objects.select_related('perfil').prefetch_related('user_postagem_forum')
    perfil = get_object_or_404(modelo, username=username)
    context = {'obj': perfil}
    return render(request, 'perfil.html', context)

def atualizar_usuario(request, username):
    user = get_object_or_404(MyUser, username=username)


