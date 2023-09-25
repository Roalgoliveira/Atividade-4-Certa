from django.shortcuts import render, redirect
from .models import Menções_honrosas, Top_5

def home(request):
  honras = Menções_honrosas.objects.all()
  tops = Top_5.objects.all()
  print(honras)
  print(tops)
  return render(request, "home.html", context={ "honras": honras, "tops": tops})





def adicionar_jogador_h(request):
  if request.method == "POST":
    #Adicionar um novo jogador usando os valores do formulário
    Menções_honrosas.objects.create(
      nome = request.POST["nome"],
      gols = request.POST["gols"],
      partidas = request.POST["partidas"],
      titulos = request.POST["titulos"],
    )
    return redirect("home")
  return render(request, "forms.html", context={"action":"Adicionar"})


def update_jogador_h(request, id):

  j_h = Menções_honrosas.objects.get(id = id)
  if request.method == "POST":
    #Atualizar um jogador usando os valores do formulário
    j_h.nome = request.POST["nome"]
    j_h.gols = request.POST["gols"]
    j_h.partidas = request.POST["partidas"]
    j_h.titulos = request.POST["titulos"]
    j_h.save()
    
    return redirect("home")
  return render(request, "forms.html", context={"action":"Atualizar","j_h":j_h})


def delete_jogador_h(request, id):

  j_h = Menções_honrosas.objects.get(id = id)
  if request.method == "POST":
    #Deletar um jogador usando os valores do formulário
    if "confirm" in request.POST:
      j_h.delete()
    
    return redirect("home")
  return render(request, "are_you_sure.html", context={"j_h":j_h})





def adicionar_jogador_top(request):
  if request.method == "POST":
    Top_5.objects.create(
      nome = request.POST["nome"],
      gols = request.POST["gols"],
      partidas = request.POST["partidas"],
      titulos = request.POST["titulos"],
    )
    return redirect("home")
  return render(request, "forms.html", context={"action":"Adicionar"})
  
                
def update_jogador_top(request, id):

  j_top = Top_5.objects.get(id = id)
  if request.method == "POST":
    j_top.nome = request.POST["nome"]
    j_top.gols = request.POST["gols"]
    j_top.partidas = request.POST["partidas"]
    j_top.titulos = request.POST["titulos"]
    j_top.save()
    
    return redirect("home")
  return render(request, "forms_top.html", context={"action":"Atualizar","j_top":j_top})


def delete_jogador_top(request, id):

  j_top = Top_5.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      j_top.delete()
    
    return redirect("home")
  return render(request, "are_you_sure_top.html", context={"j_top":j_top})