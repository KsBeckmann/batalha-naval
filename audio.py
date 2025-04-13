import os
import pygame

class Audio:
    # Inicializa o mixer uma única vez
    pygame.mixer.init()
    pasta_sons = os.path.join(os.path.dirname(__file__), 'sons')

    @staticmethod
    def tocar_efeito(evento: str) -> None:
        efeitos = {
            'tiro': 'tiro.mp3',
            'acerto': 'acerto.mp3',
            'erro': 'erro.mp3',
            'escudo': 'escudo.mp3'
        }
        nome_arquivo = efeitos.get(evento)
        if nome_arquivo:
            caminho = os.path.join(Audio.pasta_sons, nome_arquivo)
            if os.path.exists(caminho):
                pygame.mixer.music.load(caminho)
                pygame.mixer.music.play()