from database import Database
import pyaudio
from datetime import datetime
from pydub import AudioSegment
import io

class AudioMessage:
    def __init__(self, db):
        self.db = db

    def create_audio(self, id_channel, id_user, duree_enregistrement=5, frequence_echantillonnage=44100, format_audio=pyaudio.paInt16, canaux=2):
        CHUNK = 1024
        p = pyaudio.PyAudio()
        #record
        stream = p.open(format=format_audio,
                        channels=canaux,
                        rate=frequence_echantillonnage,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("recording...")

        frames = []

        for i in range(0, int(frequence_echantillonnage / CHUNK * duree_enregistrement)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("recording is over.")

        stream.stop_stream()
        stream.close()
        p.terminate()
        #end record and save audio file
        audio_data = b''.join(frames)
        nom_fichier = f"message_audio_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
        taille_fichier = len(audio_data)
        type_mime = "audio/wav"
        time = datetime.now()

        try:
            #audio data in database
            sql = "INSERT INTO message_audio (id_channel, id_user, time, audio_data, nom_fichier, taille_fichier, type_mime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.db.execute_query(sql, (id_channel, id_user, time, audio_data, nom_fichier, taille_fichier, type_mime))
            print("Audio data saved in the database successfully.")
        except Exception as e:
            print(f"Error recording audio data : {e}")

    def delete_audio(self, id_audio):
        query = "DELETE FROM message_audio WHERE id = %s"
        self.db.execute_query(query, (id_audio,))

        
    def play_audio(self, id_audio):
        try:
            # Recover audio data from database
            sql = "SELECT audio_data FROM message_audio WHERE id = %s"
            result = self.db.fetch_all(sql, (id_audio,))
            audio_data = result[0][0]  # The query returns a tuple with a single element (audio_data)

            # Convert audio data to AudioSegment
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))

            #audio playback
            audio_segment.play()

        except Exception as e:
            print(f"Error playing audio from database : {e}")

if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="310104", database="myDiscord")
    test = AudioMessage(db)
    """test.create_audio(1,1)"""
    test.play_audio(1)