import json
from googletrans import Translator

class BiharTranslator:
    def __init__(self):
        self.translator = Translator()
        self.load_translations()
        
    def load_translations(self):
        self.translations = {}
        languages = ['hi', 'mai', 'bho', 'mag', 'ur']
        for lang in languages:
            try:
                with open(f'translations/{lang}.json', 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)
            except FileNotFoundError:
                self.translations[lang] = {}
    
    def translate(self, text, target_lang='en'):
        if target_lang == 'en':
            return text
            
        # First check our local translations
        if target_lang in self.translations and text in self.translations[target_lang]:
            return self.translations[target_lang][text]
            
        # Fallback to Google Translate
        try:
            translated = self.translator.translate(text, dest=target_lang)
            return translated.text
        except:
            return text
            
    def get_supported_languages(self):
        return {
            'en': 'English',
            'hi': 'Hindi',
            'mai': 'Maithili',
            'bho': 'Bhojpuri',
            'mag': 'Magahi',
            'ur': 'Urdu'
        }