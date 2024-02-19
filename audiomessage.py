import pyaudio
from datetime import datetime

class AudioMessage:
    def __init__(self, db):
        self.db = db

    def create_audio(self, id_channel, id_user, duree_enregistrement=5, frequence_echantillonnage=44100, format_audio=pyaudio.paInt16, canaux=2):
        CHUNK = 1024
        p = pyaudio.PyAudio()

        stream = p.open(format=format_audio,
                        channels=canaux,
                        rate=frequence_echantillonnage,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("Enregistrement en cours...")

        frames = []

        for i in range(0, int(frequence_echantillonnage / CHUNK * duree_enregistrement)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Enregistrement terminé.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        audio_data = b''.join(frames)
        nom_fichier = f"message_audio_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
        taille_fichier = len(audio_data)
        type_mime = "audio/wav"
        time = datetime.now()

        try:
            # Insertion des données audio dans la base de données
            sql = "INSERT INTO message_audio (id_channel, id_user, time, audio_data, nom_fichier, taille_fichier, type_mime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.db.execute_query(sql, (id_channel, id_user, time, audio_data, nom_fichier, taille_fichier, type_mime))
            print("Données audio enregistrées dans la base de données avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement des données audio : {e}")