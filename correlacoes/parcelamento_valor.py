from utils import DatabaseHelper


def main():
    conn = DatabaseHelper.get_instance()
    print(conn)


if __name__ == '__main__':
    main()
