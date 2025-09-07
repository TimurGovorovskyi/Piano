from pygame import mixer

def load_sound(keys):
    sounds = {}
    for key, filename in keys.items():
        sounds[key] = mixer.Sound(f"assets/sounds/{filename}")
    return sounds