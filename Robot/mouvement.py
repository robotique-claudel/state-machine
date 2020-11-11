"""
Module pour le mouvement du robot
"""
import logging

from .State.state import State


log = logging.getLogger(__name__)

class Robot:
    """Classe representant un robot"""

    def __init__(self):
        self.cur_state: State = None
        self.states: list = []


    def avance(self, unit: int) -> None:
        """Fait avancer le robot"""
        log.debug(f"Avance du robot {unit}")

    def recule(self, unit: int) -> None:
        """Fait reculer le robot"""
        log.debug(f"Recule du robot {unit}")

    def droite(self, angle: int) -> None:
        """Fait tourner le robot a droite"""
        log.debug(f"Tourne a droite par {angle} degres")

    def gauche(self, angle: int) -> None:
        """Fait tourner le robot a gauche"""
        log.debug(f"Tourne a gauche par {angle} degres")
