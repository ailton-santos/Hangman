from django.shortcuts import render, redirect
from django.http import HttpResponse
# Importe o modelo Contato apenas se ele estiver definido em forca/models.py
from .models import Contato 

# --- Variáveis Globais de Dados ---
PALAVRAS = ['PYTHON', 'DJANGO', 'CODIGO', 'PROJETO', 'FORCA', 'SENAI', 'CREALITY']
MAX_TENTATIVAS = 6

# --- Variável de Mapeamento de Imagem (GLOBAL) ---
# Se for global, fica mais limpo. 
# 6 Tentativas Restantes -> Imagem forca1.jpg (Corpo vazio)
# 0 Tentativas Restantes -> Imagem forca7.jpg (Enforcado)
IMAGEM_MAP = {
    6: 'forca1.jpg',
    5: 'forca2.jpg',
    4: 'forca3.jpg',
    3: 'forca4.jpg',
    2: 'forca5.jpg',
    1: 'forca6.jpg',
    0: 'forca7.jpg',
}

# ----------------------------------------------------
# 1. VIEWS DE TESTE E PERSISTÊNCIA
# ----------------------------------------------------

def home(request):
    return render(request, 'forca/pagina_com_estilo.html')
    
def recebe_dados(request):
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome_do_usuario')
        if nome_digitado:
            mensagem = f"Olá usuário, {nome_digitado}! Seus dados foram recebidos."
        else:
            mensagem = "Insira seu nome"
        return HttpResponse(mensagem)
    return HttpResponse ("Não Digitado")

def contato(request):
    return render(request, 'forca/contato.html')

def salvar_contato(request):
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        email_digitado = request.POST.get('email')

        novo_contato = Contato(nome=nome_digitado, email=email_digitado)
        novo_contato.save()
        
        return redirect('listar_contatos')
    return redirect('contato')

def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'forca/listar_contatos.html', {'contatos': contatos})

# ----------------------------------------------------
# 2. VIEWS DO JOGO DA FORCA
# ----------------------------------------------------

def iniciar_jogo(request):
    import random
    
    # ... (código para iniciar jogo permanece o mesmo)
    palavra_secreta = random.choice(PALAVRAS)
    
    request.session['palavra_secreta'] = palavra_secreta
    request.session['letras_corretas'] = []
    request.session['letras_erradas'] = []
    request.session['tentativas_restantes'] = MAX_TENTATIVAS
    request.session['mensagem'] = "Novo jogo iniciado! Adivinhe a palavra."
    
    return redirect('jogar_forca')


def jogar_forca(request):
    # --- Recupera estado do jogo da sessão ---
    if 'palavra_secreta' not in request.session:
        return redirect('iniciar_jogo')

    palavra_secreta = request.session['palavra_secreta']
    letras_corretas = request.session['letras_corretas']
    letras_erradas = request.session['letras_erradas']
    tentativas_restantes = request.session['tentativas_restantes']
    mensagem = request.session['mensagem']
    
    # --- Lógica de Processamento de Tentativa (POST) ---
    if request.method == 'POST':
        letra_tentada = request.POST.get('letra', '').upper()
        
        if letra_tentada and letra_tentada.isalpha() and len(letra_tentada) == 1:
            if letra_tentada in letras_corretas or letra_tentada in letras_erradas:
                mensagem = f"Você já tentou a letra '{letra_tentada}'."
            
            elif letra_tentada in palavra_secreta:
                letras_corretas.append(letra_tentada)
                mensagem = f"Parabéns! A letra '{letra_tentada}' está na palavra."
            
            else:
                letras_erradas.append(letra_tentada)
                tentativas_restantes -= 1
                mensagem = f"A letra '{letra_tentada}' não está na palavra. {tentativas_restantes} tentativas restantes."

            request.session['letras_corretas'] = letras_corretas
            request.session['letras_erradas'] = letras_erradas
            request.session['tentativas_restantes'] = tentativas_restantes
        
        else:
            mensagem = "Por favor, digite apenas uma letra válida."

    # --- Lógica de Verificação de Fim de Jogo ---
    palavra_mascarada = "".join([l if l in letras_corretas else '_' for l in palavra_secreta])
    jogo_terminado = False
    
    if palavra_mascarada == palavra_secreta:
        mensagem = f"VOCÊ VENCEU! A palavra era: {palavra_secreta}"
        jogo_terminado = True
    elif tentativas_restantes <= 0:
        mensagem = f"VOCÊ PERDEU! A palavra secreta era: {palavra_secreta}"
        jogo_terminado = True
    
    request.session['mensagem'] = mensagem
    
    # --- Contexto para o Template (INCLUINDO A IMAGEM) ---
    
    # Obtém o nome do arquivo de imagem com base nas tentativas restantes
    nome_imagem = IMAGEM_MAP.get(tentativas_restantes, 'forca1.jpg') 

    contexto = {
        'palavra_mascarada': " ".join(palavra_mascarada),
        'letras_erradas': ", ".join(sorted(letras_erradas)),
        'tentativas_restantes': tentativas_restantes,
        'mensagem': mensagem,
        'jogo_terminado': jogo_terminado,
        'max_tentativas': MAX_TENTATIVAS,
        'nome_imagem_forca': nome_imagem, # Variável usada no HTML
    }
    
    return render(request, 'forca/forca.html', contexto)