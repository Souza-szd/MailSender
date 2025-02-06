import smtplib
from email.message import EmailMessage

# Função para enviar e-mail
def enviar_email(nome, email_destino):


    # Configurações do servidor de e-mail
    smtp_servidor = "smtp.gmail.com"  # Para Gmail
    smtp_porta = 587
    remetente_email = "a2024953055@teiacoltec.org"
    remetente_senha = "uffb lnaa bmff dwad"
    
    # Criando o e-mail
    mensagem = EmailMessage()
    mensagem["Subject"] = "Interesse em Participar de Projeto de Iniciação Científica"
    mensagem["From"] = remetente_email
    mensagem["To"] = email_destino
    
    corpo = f"""
    Prezado(a) Professor(a), {nome}!
    
    Meu nome é (nome), sou aluno do curso de Automação Industrial no Colégio Técnico da UFMG (COLTEC), e gostaria de manifestar meu interesse em ingressar em um projeto de iniciação científica sob sua orientação. Tenho grande interesse em ampliar meus conhecimentos na área científica e laboratorial, além de contribuir com as atividades e objetivos do seu laboratório. Estou motivado a aprender novas técnicas, colaborar nas pesquisas e desenvolver habilidades práticas que complementem minha formação acadêmica. Coloco-me à disposição para uma conversa ou entrevista, caso necessário. Agradeço desde já pela atenção e pela oportunidade.

Atenciosamente,
(aluno)
Telefone de contato: 31 991077099
    """
    
    mensagem.set_content(corpo)
    
    # Enviando o e-mail
    try:
         with smtplib.SMTP(smtp_servidor, smtp_porta) as servidor:
             servidor.starttls()  # Iniciar conexão segura
             servidor.login(remetente_email, remetente_senha)
             servidor.send_message(mensagem)
         print(f"E-mail enviado com sucesso para {nome} ({email_destino})!")
    except Exception as e:
         print(f"Erro ao enviar e-mail para {nome}: {e}")

# Lista de destinatários

destinatarios = [
    {"nome": "Nome professor", "email": "NomeProfessor@gmail.br"},

]


#Enviar e-mails para todos os destinatários
for destinatario in destinatarios:
    enviar_email(destinatario["nome"], destinatario["email"])

