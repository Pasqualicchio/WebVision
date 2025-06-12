from flask import Flask, request, jsonify
import os
from datetime import datetime
from openpyxl import load_workbook

# Crea l'app Flask
app = Flask(__name__)

# Configura la cartella per caricare i file
UPLOAD_FOLDER = 'static/uploads/'
EXCEL_FILE = 'static/registro_foto.xlsx'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'mp4'}

# Verifica che l'estensione sia consentita
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Imposta la cartella per i file caricati
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rotta per il login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Logica per autenticazione base
    if data['username'] == 'admin' and data['password'] == 'admin123':
        return jsonify({"message": "Login riuscito!"}), 200
    else:
        return jsonify({"message": "Credenziali non valide"}), 401

# Rotta per l'upload dei file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "Nessun file inviato"}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"message": "Nessun file selezionato"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"message": "Tipo di file non consentito"}), 400
    
    # Crea la cartella di upload se non esiste
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Salvataggio del file nella cartella di destinazione
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Aggiungi i dati nel file Excel
    try:
        # Carica il file Excel (se esiste) e apri il foglio di lavoro
        if os.path.exists(EXCEL_FILE):
            wb = load_workbook(EXCEL_FILE)
        else:
            # Se il file non esiste, creane uno nuovo
            wb = load_workbook()  # Crea un nuovo workbook
            sheet = wb.active
            sheet.append(['Data', 'Utente', 'Commessa', 'Tipo file', 'Percorso', 'Commenti', 'GPS'])  # Intestazioni
            wb.save(EXCEL_FILE)
        
        # Aggiungi i dati al foglio di lavoro
        sheet = wb.active
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Aggiungi una nuova riga con i dati relativi alla foto/video
        sheet.append([current_time, 'admin', 'Commessa001', file.filename, file_path, 'Nessun commento', 'GPS_info'])
        wb.save(EXCEL_FILE)

    except Exception as e:
        return jsonify({"message": f"Errore nell'aggiornamento del file Excel: {str(e)}"}), 500

    return jsonify({"message": f"File {file.filename} caricato con successo!"}), 200

if __name__ == '__main__':
    # Avvia il server Flask
    app.run(debug=True, use_reloader=False)  # Disabilita il reloader per evitare conflitti
