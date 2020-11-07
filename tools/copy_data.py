import psycopg2
from config import config

#A function that create table in db
def create_table():
    command = (
        """
        CREATE TABLE gps5 (
            linia_id INT,
            kurs_id INT,
            pojazd_id INT,
            przystanek_id INT,
            poprzedni_przystanek_id INT,
            data_czas_zdarzenia timestamp,
            dlugosc_geograficzna varchar,
            szerokosc_geograficzna varchar,
            nazwa_linii varchar,
            numer_kursu varchar,
            przystanek_poczatkowy varchar,
            przystanek_koncowy varchar,
            nazwa_przystanku varchar,
            numer_boczny varchar,
            numer_pojazdu varchar,
            poprzedni_przystanek varchar
        );
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table 
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Table created")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#A function that insert data from csv to table in db
def csv_import():
    #command = ("\COPY gps5 FROM 'C:\Users\Waldi\Desktop\Dominika\GZM\baza\unpacked\gps_20201019.csv' DELIMITER ';' CSV HEADER;")
    csv_path = "C://Users//Waldi//Desktop//Dominika//GZM//baza//unpacked//gps_20201019.csv"
    f_contents = open(csv_path, 'r')
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        csv_import = cur.copy_from(f_contents, "gps5", sep=";")
        cur.execute(csv_import)

        cur.close()
        conn.commit()
        print("Correctly copied data from csv to table")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#A function that shows firs 10 rows
def show10_rows():
    command = ("SELECT * FROM gps5 FETCH FIRST 10 ROW ONLY;")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)
    
        conn.commit()
        print(cur.fetchone())
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#A function that convert comma to point in coordinates
def comma_convert():
    command = (
        """
        UPDATE 
            gps5
        SET 
            dlugosc_geograficzna = REPLACE (
  	            dlugosc_geograficzna,
	            ',',
	            '.'
            );
        """,
        """
        UPDATE 
            gps5
        SET 
            szerokosc_geograficzna = REPLACE (
  	            szerokosc_geograficzna,
	            ',',
	            '.'
            );
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)
        
        cur.close()
        conn.commit()
        print("Fields type updated")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#A function that convert fields type (coordinates) from varchar to double
def update_fields_type():
    command = (
        """
        ALTER TABLE gps5
	    ALTER COLUMN dlugosc_geograficzna TYPE double precision
	    USING dlugosc_geograficzna:: double precision;
        """,
        """
        ALTER TABLE gps5
	    ALTER COLUMN szerokosc_geograficzna TYPE double precision
	    USING szerokosc_geograficzna:: double precision;
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)
        
        cur.close()
        conn.commit()
        print("Fields type updated")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_table()
    #csv_import()
    #show10_rows()
    # comma_convert()
    #show10_rows()
    #update_fields_type()