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
    
    Meu nome é Arthur Souza Santos, sou aluno do curso de Automação Industrial no Colégio Técnico da UFMG (COLTEC), e gostaria de manifestar meu interesse em ingressar em um projeto de iniciação científica sob sua orientação. Tenho grande interesse em ampliar meus conhecimentos na área científica e laboratorial, além de contribuir com as atividades e objetivos do seu laboratório. Estou motivado a aprender novas técnicas, colaborar nas pesquisas e desenvolver habilidades práticas que complementem minha formação acadêmica. Coloco-me à disposição para uma conversa ou entrevista, caso necessário. Agradeço desde já pela atenção e pela oportunidade.

Atenciosamente,
Arthur Souza Santos
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
    {"nome": "Adaises Simone Maciel da Silva", "email": "adaisesmaciel@ufmg.br"},
    {"nome": "Ana Elisa Cruz Correa", "email": "aecorrea@teiacoltec.org"},
    {"nome": "Ana Luiza Costa Cruz Borges", "email": "analuiza@vet.ufmg.br"},
    {"nome": "Ana Maria Alves Saraiva", "email": "anasaraiva@ufmg.br"},
    {"nome": "Ana Paula de Carvalho Teixeira", "email": "anapaula.cta1@gmail.com"},
    {"nome": "Ana Paula Meneses Alves", "email": "apmeneses@gmail.com"},
    {"nome": "Ana Paula Sampaio Caldeira", "email": "anapaula.sampaiocaldeira@gmail.com"},
    {"nome": "Ana Lucia Brunialti Godard", "email": "brunialt@ufmg.br"},
    {"nome": "Andre Augusto Gomes Faraco", "email": "andrefaraco@ufmg.br"},
    {"nome": "Andrey Pereira Lage", "email": "alage@vet.ufmg.br"},
    {"nome": "Anna Christina de Almeida", "email": "aca2006@ica.ufmg.br"},
    {"nome": "Anna Paula Vencato", "email": "apvencato@gmail.com"},
    {"nome": "Antonio Jose Lopes Alves", "email": "ajlacoltec@ufmg.br"},
    {"nome": "Antonio Pereira Magalhaes Junior", "email": "antonio.magalhaes.ufmg@gmail.com"},
    {"nome": "Aristobolo Mendes da Silva", "email": "aristobolo@ufmg.br"},
    {"nome": "Aristobolo Mendes da Silva", "email": "aristobolosilva@gmail.com"},
    {"nome": "Belisa Vieira da Silveira", "email": "bvsilveira@unaerp.br"},
    {"nome": "Bernardo de Mattos Viana", "email": "bernardomviana@ufmg.br"},
    {"nome": "Bernardo de Mattos Viana", "email": "bernardomviana@yahoo.com"},
    {"nome": "Bernardo Lages Rodrigues", "email": "bernardo@qui.ufmg.br"},
    {"nome": "Bruna Figueiredo Manzo", "email": "brunaamancio@yahoo.com.br"},
    {"nome": "Camilla Henriques Maia de Camargos", "email": "camillahmcamargos@gmail.com"},
    {"nome": "Carla Jorge Machado", "email": "carlajm@ufmg.br"},
    {"nome": "Carlos Augusto de Oliveira Junior", "email": "carlosoliveira@cca.ufpb.br"},
    {"nome": "Claudia Regina Vieira", "email": "claudia.vieira@ufabc.edu.br"},
    {"nome": "Cleiton Lopes Aguiar", "email": "cleiton-aguiar@ufmg.br"},
    {"nome": "Daniel Fernandes Macedo", "email": "damacedo@dcc.ufmg.br"},
    {"nome": "Daniela Chemim de Melo", "email": "danichemim@gmail.com"},
    {"nome": "Daniele Kasper", "email": "daniele@biof.ufrj"},
    {"nome": "Dawit Albieiro Pinheiro Goncalves", "email": "dawit@ufmg.br"},
    {"nome": "Dayse Carvalho da Silva Martins", "email": "daysecsm@yahoo.com"},
    {"nome": "Debora Silvano Moreira", "email": "moreiradebora@yahoo.com"},
    {"nome": "Demerson Arruda Sanglard", "email": "sanglard@ufmg.br"},
    {"nome": "Diego Gomes Rocha", "email": "diegogr@ufmg.br"},
    {"nome": "Diego Gomes Rocha", "email": "diegogr.ufmg@gmail.com"},
    {"nome": "Diogo Montes Vidal", "email": "vidal@qui.ufmg.br"},
    {"nome": "Diogo Montes Vidal", "email": "diogomvidal@gmail.com"},
    {"nome": "Douglas Batista Mazzinghy", "email": "dmazzinghy@demin.ufmg.br"},
    {"nome": "Elaine Miguel Delvivo Farao", "email": "elainebiofis@yahoo.com.br"},
    {"nome": "Elaine Miguel Delvivo Farao", "email": "elaine.delvivo@ufms.br"},
    {"nome": "Elaine Miguel Delvivo Farao", "email": "elainemiguel@ufj.edu.br"},
    {"nome": "Arthur", "email": "arthurthegreatking19@gmail.com"},

]


#Enviar e-mails para todos os destinatários
for destinatario in destinatarios:
    enviar_email(destinatario["nome"], destinatario["email"])

