# Исполняющий файл
from RT_driver import RTDriver

if __name__ == "__main__":
    rutube_parse = RTDriver()

    try:
        rutube_parse.get_link("https://rutube.ru/")
        rutube_parse.login_to_rutube()
        # rutube_parse.find_video("Каневский")
    except Exception as e:
        print(f"We have some errors: {e}")
    finally:
        rutube_parse.quit()
