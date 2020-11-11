import json
import logging
import logging.config

with open("config/log-config.json", "r") as f:
    config = json.load(f)
    logging.config.dictConfig(config)


from Robot.mouvement import Robot

log = logging.getLogger(__name__)


def main():
    r = Robot()
    r.avance(10)
    r.avance(10)


if __name__ == "__main__":
    main()