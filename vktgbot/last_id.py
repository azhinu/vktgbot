import os
from loguru import logger


def read_id(vk_domain: str) -> int:
    try:
        if not os.path.exists("./logs/%s_last_id.txt" % vk_domain): 
          with open("./logs/%s_last_id.txt" % vk_domain, 'w') as file: 
              file.write("0")
        return int(open("./logs/%s_last_id.txt" % vk_domain, "r").read())
    except ValueError:
        logger.critical(
            "The value of the last identifier is incorrect. Please check the contents of the file 'last_id.txt'."
        )
        exit()


def write_id(vk_domain: str, new_id: int) -> None:
    open("./logs/%s_last_id.txt" % vk_domain, "w").write(str(new_id))
    logger.info(f"New ID, written in the file: {new_id}")
