from email import message_from_binary_file
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from AppUsuario.forms import SignUpForm


"""
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
"""

"""
def signup(request):
    dicctionary = {}
   # dicctionary.update(login2(request))
    print(dicctionary)
    if request.method == 'POST': 
            username = request.POST.get('username', False)
            if User.objects.filter(username=username).exists():
                respuesta = {"mensaje" : "Ya existe usuario."}
                return render(request,'registration/signup.html',respuesta)

            password = request.POST.get('password', False)
            mail = request.POST.get('mail', False)
            if User.objects.filter(email=mail).exists():
                respuesta = {"mensaje" : "Ya existe correo."}
                return render(request,'registration/signup.html',respuesta)
            createacc =    User.objects.create_user(username, mail, password)
            createacc.save()
            respuesta = {"mensaje" : "Cuenta creada correctamente."}
            return render(request,'registration/signup.html',respuesta)
    return render(request,'registration/signup.html', dicctionary)
"""

"""
def signup(request):
    if request.method == "POST":
        mi_formulario = UserCreationForm(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            username = mi_formulario.cleaned_data.get("username")
            password = mi_formulario.cleaned_data.get("password")
            user = User.objects.create(username,password)
            user.save()
            return redirect("inicio")
    users=User.objects.all()
    contexto = {
        "form" : UserCreationForm(),
        "users" : users,
    }
    return render(request,"registration/signup.html",contexto)
    """

def signup(request):
    if request.method == "POST":
        mi_formulario = SignUpForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            messages.info(request,"Usuario registrado correctamente, inicie sesion para disfrutar de nuestra pagina!")
        else:
            messages.info(request,"Contraseña o usuario incorrecto")
        return redirect("signup")
    contexto = {
        "form" : SignUpForm(),
    }
    return render(request,"registration/signup.html",contexto)