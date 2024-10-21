from pacotes.google_auxiliar import (habilitar_login_servicos)
# =============================================================================
# Parametros de entrada
# =============================================================================
SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/gmail.readonly",
]
SERVICE_ACCOUNT_FILE = "/Users/laertejt/Projetos/labFin/labfin-rotina/src/meuconsultor/principal/json-google/laerte_takeuti.json"
from google.oauth2 import service_account
# =============================================================================
# #Para autenticar no service_account
# =============================================================================
def habilitar_login_servicos(SCOPES, SERVICE_ACCOUNT_FILE):
    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return credentials
# Exemplo para listar os primeiros 10 arquivos no Google Drive
def listar_arquivos(drive_service):
    results = drive_service.files().list(
        pageSize=10, fields="files(id, name)"
    ).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f"{item['name']} ({item['id']})")

# =============================================================================
# #Inicio
# =============================================================================
def main():
    credentials = habilitar_login_servicos(SCOPES, SERVICE_ACCOUNT_FILE)
    # Criar um serviço para acessar o Google Drive
    from googleapiclient.discovery import build
    drive_service = build('drive', 'v3', credentials=credentials)
    listar_arquivos(drive_service)


if __name__ == "__main__":
    main()
