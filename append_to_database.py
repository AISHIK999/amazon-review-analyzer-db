import pymysql

RED = '\033[91m'
RESET = '\033[0m'


def check_db():
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'rootpass',
        'charset': 'utf8mb4',
    }
    try:
        init_conn = pymysql.connect(**db_config)
        with init_conn.cursor() as cursor:

            create_db_query = "CREATE DATABASE IF NOT EXISTS review_db;"
            cursor.execute(create_db_query)
            init_conn.commit()

            init_conn.select_db('review_db')

            create_table_query = """
                CREATE TABLE IF NOT EXISTS Review (
                    ASIN VARCHAR(10) PRIMARY KEY,
                    REVIEWER VARCHAR(50),
                    RATING INT,
                    TITLE VARCHAR(100),
                    DESCRIPTION TEXT,
                    DATE DATETIME,
                    SCORE DECIMAL(3,2)
                );
                    """
            cursor.execute(create_table_query)
            init_conn.commit()

    except pymysql.err.OperationalError:
        print(
            f"{RED}Error connecting to database!{RESET}\n\
            Try running the following command and try again:\n\n\
            sudo docker-compose up --build -d")
        exit()


def append_to_database(conn):
    with conn.cursor() as cursor:
        # delete_query = "DELETE FROM Review;"
        # cursor.execute(delete_query)
        # conn.commit()
        insert_query = """
          LOAD DATA LOCAL INFILE 'temp/reviews.csv'
          INTO TABLE Review
          FIELDS TERMINATED BY ','
          ENCLOSED BY '"'
          LINES TERMINATED BY '\n'
          IGNORE 1 ROWS
          (@asin, @reviewer, @rating, @title, @description, @date, @score)
          SET ASIN = @asin, Reviewer = @reviewer, Rating = @rating, Title = @title, Description = @description, Date = STR_TO_DATE(@date, '%m/%d/%Y'), Score = @score;
        """

        cursor.execute(insert_query)
        conn.commit()


def db_connect():
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'rootpass',
        'db': 'review_db',
        'charset': 'utf8mb4',
        'local_infile': True,
    }
    return pymysql.connect(**db_config)


if __name__ == "__main__":
    check_db()
    conn = db_connect()
    append_to_database(conn)
