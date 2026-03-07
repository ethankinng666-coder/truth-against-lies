#!/usr/bin/env python3
"""
Translate only the new 'strengthen' section and nav item from en.json to all languages.
Much faster than re-translating the entire file.
"""

import json
import re
import sys
import time
import copy
from deep_translator import GoogleTranslator

LANGUAGES = {
    'fr': 'fr', 'de': 'de', 'es': 'es', 'pt': 'pt',
    'ru': 'ru', 'pl': 'pl', 'no': 'no', 'sv': 'sv',
    'it': 'it', 'tr': 'tr', 'ar': 'ar',
}

LANG_NAMES = {
    'fr': 'Français', 'de': 'Deutsch', 'es': 'Español', 'pt': 'Português',
    'ru': 'Русский', 'pl': 'Polski', 'no': 'Norsk', 'sv': 'Svenska',
    'it': 'Italiano', 'tr': 'Türkçe', 'ar': 'العربية',
}

TAG_PATTERN = re.compile(r'<[^>]+>')
ENTITY_PATTERN = re.compile(r'&#?\w+;')

def protect_html(text):
    placeholders = {}
    counter = [0]
    def replace_match(match):
        key = f"__PH{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    text = TAG_PATTERN.sub(replace_match, text)
    text = ENTITY_PATTERN.sub(replace_match, text)
    return text, placeholders

def restore_html(text, placeholders):
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text

def translate_text(text, target_lang):
    if not text or not text.strip():
        return text
    protected, placeholders = protect_html(text)
    try:
        if len(protected) > 4500:
            chunks = re.split(r'(?<=[.!?])\s+', protected)
            result_parts = []
            current = ""
            for chunk in chunks:
                if len(current) + len(chunk) > 4000 and current:
                    translated = GoogleTranslator(source='en', target=target_lang).translate(current)
                    result_parts.append(translated or current)
                    current = chunk
                    time.sleep(0.3)
                else:
                    current = current + " " + chunk if current else chunk
            if current:
                translated = GoogleTranslator(source='en', target=target_lang).translate(current)
                result_parts.append(translated or current)
            result = ' '.join(result_parts)
        else:
            result = GoogleTranslator(source='en', target=target_lang).translate(protected)
            if not result:
                result = protected
            time.sleep(0.15)
    except Exception as e:
        print(f"  Warning: Translation failed: {e}", file=sys.stderr)
        result = protected
    return restore_html(result, placeholders)

def translate_value(value, target_lang, depth=0):
    """Recursively translate strings in a JSON structure."""
    if isinstance(value, str):
        translated = translate_text(value, target_lang)
        return translated
    elif isinstance(value, list):
        return [translate_value(item, target_lang, depth+1) for item in value]
    elif isinstance(value, dict):
        return {key: translate_value(val, target_lang, depth+1) for key, val in value.items()}
    return value

def main():
    base_path = '/Users/nethanellinder/code/truth-against-lies/lang/'

    # Load English source
    with open(base_path + 'en.json', 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    strengthen_en = en_data['strengthen']
    new_nav_item = en_data['nav'][9]  # "Strengthen the People"

    if len(sys.argv) > 1:
        langs = {k: v for k, v in LANGUAGES.items() if k in sys.argv[1:]}
    else:
        langs = LANGUAGES

    for lang_code, google_code in langs.items():
        print(f"\n{'='*50}", file=sys.stderr)
        print(f"Translating strengthen section to {LANG_NAMES[lang_code]} ({lang_code})", file=sys.stderr)
        print(f"{'='*50}", file=sys.stderr)

        # Load existing translation
        lang_path = base_path + f'{lang_code}.json'
        with open(lang_path, 'r', encoding='utf-8') as f:
            lang_data = json.load(f)

        # Add nav item at position 9 (after "Watch & Learn", before "What Can Be Done?")
        nav = lang_data.get('nav', [])
        if len(nav) == 10:
            translated_nav = translate_text(new_nav_item, google_code)
            nav.insert(9, translated_nav)
            lang_data['nav'] = nav
            print(f"  nav item: done", file=sys.stderr)

        # Translate the strengthen section
        print(f"  Translating strengthen section...", file=sys.stderr)
        lang_data['strengthen'] = translate_value(copy.deepcopy(strengthen_en), google_code)
        print(f"  strengthen: done", file=sys.stderr)

        # Write
        with open(lang_path, 'w', encoding='utf-8') as f:
            json.dump(lang_data, f, ensure_ascii=False, indent=4)

        print(f"Done! Written to {lang_path}", file=sys.stderr)

if __name__ == '__main__':
    main()
