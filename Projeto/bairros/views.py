from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import loader
from .forms import BairroForm

def index(request):
    template=loader.get_template('bairros/index.html')
    context={}
    return HttpResponse(template.render(context,request))

def sobre_nos(request):
    template=loader.get_template('bairros/sobre_nos.html')
    context={}
    return HttpResponse(template.render(context,request))

def bairro(request): 
    # se for um POST, é pq a pessoa submeteu o formulário
    if request.method == 'POST':
        # Cria o formulário a partir do que você recebeu
        form = BairroForm(request.POST)
        # Verifica se é valido
        if form.is_valid():
            bairro_selecionado = form.cleaned_data['bairro']
            # Busca os dados do bairro
			# (teria que buscar no banco)
            dados = f"Isso é um exemplo de dado para o bairro {bairro_selecionado}"
                    
            # Manda pra mesma url, mas agora com os dados:
            # vc pode mandar pra outra tb
            return render(request, 'bairros/bairro.html', {'dados': dados, 'form': form})

    # Se for um get, cria um form novo
    else:
        form = BairroForm()
        return render(request, 'bairros/bairro.html', {'form': form})
