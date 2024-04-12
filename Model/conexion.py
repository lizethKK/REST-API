import psycopg

class Conexion():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=restaurantes_intele user=restaurantes password=restaurantespass host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
    
    def leer_t(self):
        with self.conn.cursor() as cur:
            data = cur.execute(""" 
                SELECT * FROM "restaurantes_data"
            """)
            return data.fetchall()
        
    def leer_u(self, state):
        with self.conn.cursor() as cur:
            data = cur.execute(""" 
                SELECT * FROM "restaurantes_data" WHERE state = %s
            """, (state,))
            return data.fetchone()

    def escribir(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "restaurantes_data" (rating, name, site, email, phone, street, city, state, lat, lng) VALUES(%(rating)s, %(name)s, %(site)s, %(email)s, %(phone)s, %(street)s, %(city)s, %(state)s, %(lat)s, %(lng)s)
            """, data)
        self.conn.commit()

    def borrar(self, state):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "restaurantes_data" WHERE state = %s
            """, (state,))
        self.conn.commit()

    def actualizar(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "restaurantes_data" SET id = %(id)s, rating = %(rating)s, name = %(name)s, site = %(site)s, email = %(email)s, phone =%(phone)s, street = %(street)s, city = %(city)s, lat = %(lat)s, lng =%(lng)s WHERE state = %(state)s
            """, data)
        self.conn.commit()

    def __def__(self):
        self.conn.close()

