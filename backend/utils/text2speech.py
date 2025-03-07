import os
import dotenv
import uuid
import httpx
import asyncio
import fal_client
import logging

logger = logging.getLogger(__name__)
dotenv.load_dotenv()

class Text2Speech:
    def __init__(self):
        self.voice_map = {
            'english': 'vidya',
        }
        self.audio_folder = 'audios'
        
        if not os.path.exists(self.audio_folder):
            os.makedirs(self.audio_folder)

    async def generate_speech(self, text, language):
        try:
            result = await asyncio.to_thread(
                fal_client.subscribe,
                "fal-ai/playai/tts/v3",
                arguments={
                    "input": text,
                    "voice": "Jennifer (English (US)/American)"
                },
                with_logs=True,
                on_queue_update=lambda update: logger.info(f"Image generation progress: ") if isinstance(update, fal_client.InProgress) else None
            )
            audio_url = result.get("audio").get("url")
            
            async with httpx.AsyncClient() as client:
                response = await client.get(audio_url)
  
            filename = f"{str(uuid.uuid4())}.mp3"
            file_path = os.path.join(self.audio_folder, filename)
            
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            return file_path
        except Exception as e:
            print(f"Error generating speech: {str(e)}")
            raise
    
    def make_speech(self,text,language):
        result = self.generate_speech(text,language)
        return result


if __name__ == "__main__":
    text2speech = Text2Speech()
    result = asyncio.run(text2speech.make_speech("Hello, how are you?", "english"))
    print(result)