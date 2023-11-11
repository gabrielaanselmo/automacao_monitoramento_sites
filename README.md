# 🤖 Monitoramento de Sites
> Status do projeto: ✅ Finalizado.

O Monitoramento de Sites é um sistema automatizado que verifica regularmente a disponibilidade e o tempo de resposta dos sites. Ele envia alertas por e-mail em caso de inatividade ou alta latência, assegurando um acompanhamento contínuo e eficiente.

## 🚀 Funcionalidades

- **Automatização completa:** Verificações de disponibilidade e tempo de resposta realizadas automaticamente.
- **Alertas via e-mail:** Notificações imediatas em casos de downtime ou alta latência, mantendo você sempre informado.

## 🔄 CI/CD: Monitoramento Contínuo
Este CI/CD, implementado com GitHub Actions, realiza verificações diárias 📆, garantindo a confiabilidade contínua dos sites monitorados.

* 🕛 **Agendamento:** Executa todos os dias à meia-noite UTC.
* 🔒 **Permissões:** Leitura de conteúdos para o checkout do código.
* 💻 **Ambiente:** Execução em ambiente Ubuntu.
* 🚀 **Passos:**
  * 📥 Fazer checkout do código.
  * 🐍 Configurar Python 3.x.
  * 📦 Instalar dependências (requests).
  * ⚙️ Executar o script de monitoramento.
 
## 📬 Notificações
As notificações são disparadas automaticamente em caso de problemas identificados, sendo enviadas para o e-mail configurado. Mantenha-se sempre atualizado sobre o estado dos seus sites.

## 👉🏼 Pré-requisitos
- **Python 3.x:** A ferramenta é construída em Python, requer a versão 3.x.
- **Conta de e-mail:** Necessária para configurar o envio de alertas.

## 🛠️ Configuração

Configure as variáveis de ambiente `SENDER`, `PASSWORD`, e `REMITTEE` com as informações do remetente, senha e destinatário do e-mail.

- **SENDER:** Endereço de e-mail do remetente.
- **PASSWORD:** Senha do e-mail do remetente.
- **REMITTEE:** Endereço de e-mail do destinatário.

## ⚙️ Execução Local

Para testar localmente, você pode definir suas credenciais diretamente ou usar variáveis de ambiente:

```python
    sender = os.getenv('SENDER', "emailsender@gmail.com")
    password = os.getenv('PASSWORD', "password")
    receiver = os.getenv('REMITTEE', "email@gmai.com")
```

