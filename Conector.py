import psycopg2
import csv

conector1 = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = '1234',
                dbname = 'dvdrental', 
                port = '5434'
            ) # alternativamente dbname='arriendos'


conector2 = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = '1234',
                dbname = 'xtage', 
                port = '5432'
            )

def tabla_a_csv(nombre_tabla, conector):
    cursor = conector.cursor()
    cursor.execute("Select * FROM "+nombre_tabla+" LIMIT 0")
    lista_campos = [desc[0] for desc in cursor.description]
    cursor.execute("SELECT * from "+nombre_tabla+";")
    data = cursor.fetchall()
    with open('archivos/'+nombre_tabla+'.csv', 'w') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(lista_campos)
        for fila in data:
            writer.writerow(fila)


def csv_a_tabla(nombre_archivo,
                nombre_tabla,
                campos_origen,
                campos_destino,
                conector):
    cursor = conector.cursor()
    with open('archivos/'+nombre_archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        campos_archivo = next(reader)
        indices_campos = []
        for campo in campos_origen:
            indices_campos.append(campos_archivo.index(campo))
        campos = ""
        for elemento in campos_destino:
            campos+=elemento+","
        campos = campos.rstrip(",")
        for fila in reader:
            valores=""
            for indice in indices_campos:
                if str(fila[indice])!="":
                    valor="'"+str(fila[indice]).strip()+"',"
                else:
                    valor="null,"
                valores+=valor
            valores=valores.rstrip(",")
            query = "INSERT INTO "+nombre_tabla+" ("+campos+") VALUES ("+valores+");"
            print("Ejecutando Query: " + query)
            cursor.execute(query)
            query = "SELECT setval('"+nombre_tabla+"_id_seq', (SELECT MAX(id) FROM "+nombre_tabla+"));"
            cursor.execute(query)
        conector.commit()
        conector.close()




tabla_a_csv('film', conector1)
tabla_a_csv('language', conector1)
tabla_a_csv('category', conector1)
tabla_a_csv('inventory', conector1)
tabla_a_csv('rental', conector1)
tabla_a_csv('actor', conector1)
tabla_a_csv('film_actor', conector1)
tabla_a_csv('film_category', conector1)

#------------------------------------------------------------------------------
# tabla category
# con modelo:
'''
class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
'''
#campos_category=['category_id','name','last_update']
#seleccion_campos_category = ['category_id','name','last_update']
#campos_categoria = ['id', 'nombre', 'ultima_actualizacion']
#csv_a_tabla('category.csv', 'servicio_categoria', seleccion_campos_category, campos_categoria, conector2)


#------------------------------------------------------------------------------
# tabla rental
# con modelo:
'''
class Arriendo(models.Model):
    fecha_arriendo = models.DateTimeField()
    id_cliente = models.IntegerField()
    fecha_devolucion = models.DateTimeField(null=True)
    id_empleado = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    #related
    #inventario = models.ForeignKey(Inventario, null=True, on_delete=models.CASCADE)

    #temp
    temporal_inventario = models.IntegerField()
'''
#DESCOMENTAR LAS SIGUIENTES 4 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#campos_rental = ['rental_id','rental_date','inventory_id','customer_id','return_date','staff_id','last_update']
#seleccion_campos_rental = ['rental_id','rental_date','inventory_id','customer_id','return_date','staff_id','last_update']
#campos_arriendo = ['id', 'fecha_arriendo', 'temporal_inventario', 'id_cliente', 'fecha_devolucion', 'id_empleado', 'ultima_actualizacion']
#csv_a_tabla('rental.csv', 'servicio_arriendo', seleccion_campos_rental, campos_arriendo, conector2)


#------------------------------------------------------------------------------
# tabla language
# con modelo:
'''
class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
'''
#DESCOMENTAR LAS SIGUIENTES 4 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#campos_language = ['language_id','name','last_update']
#seleccion_campos_language = ['language_id','name','last_update']
#campos_idioma = ['id', 'nombre', 'ultima_actualizacion']
#csv_a_tabla('language.csv','servicio_idioma', seleccion_campos_language, campos_idioma, conector2)


#------------------------------------------------------------------------------
# tabla actor
# con model:
'''
class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
'''
#DESCOMENTAR LAS SIGUIENTES 4 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#campos_actor = ['actor_id','first_name','last_name','last_update']
#seleccion_campos_actor = ['actor_id','first_name','last_name','last_update']
#campos_actor = ['id', 'nombre', 'apellido', 'ultima_actualizacion']
#csv_a_tabla('actor.csv','servicio_actor', seleccion_campos_actor, campos_actor, conector2)


#------------------------------------------------------------------------------
# tabla inventory
# con model:
'''
class Inventario(models.Model):
    id_tienda = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    #related
    #pelicula = models.ForeignKey(Pelicula, null=True, on_delete=models.CASCADE)

    #temp
    temporal_pelicula= models.IntegerField()
'''
#DESCOMENTAR LAS SIGUIENTES 4 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#campos_inventory = ['inventory_id','film_id','store_id','last_update']
#seleccion_campos_inventory = ['inventory_id','film_id','store_id','last_update']
#campos_inventario = ['id', 'temporal_pelicula', 'id_tienda', 'ultima_actualizacion']
#csv_a_tabla('inventory.csv','servicio_inventario', seleccion_campos_inventory, campos_inventario, conector2)


#------------------------------------------------------------------------------
# tabla pelicula
# con model:
'''
class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    agno_publicacion = models.IntegerField()
    duracion_arriendo = models.IntegerField()
    precio_arriendo = models.DecimalField(max_digits=4, decimal_places=2, default=4.99)
    largo = models.IntegerField()
    costo_reemplazo = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    clasificacion = models.CharField(max_length=25)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    #special_features Omitido
    #full_text Omitido
    
    #related
    #idioma = models.ForeignKey(Idioma, null=True, on_delete=models.CASCADE)
    #categorias = models.ManyToManyField(Categoria)
    #actores = models.ManyToManyField(Actor)

    #temp
    temporal_idioma = models.IntegerField()
'''
#DESCOMENTAR LAS SIGUIENTES 4 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#campos_film = ['film_id','title','description','release_year','language_id','rental_duration','rental_rate','length','replacement_cost','rating','last_update','special_features','fulltext']
#seleccion_campos_film = ['film_id','title','description','release_year','language_id','rental_duration','rental_rate','length','replacement_cost','rating','last_update']
#campos_pelicula = ['id', 'titulo', 'descripcion', 'agno_publicacion', 'temporal_idioma', 'duracion_arriendo', 'precio_arriendo', 'largo', 'costo_reemplazo', 'clasificacion', 'ultima_actualizacion']
#csv_a_tabla('film.csv','servicio_pelicula', seleccion_campos_film, campos_pelicula, conector2)


#------------------------------------------------------------------------------
#DESCOMENTAR TODOS LOS #related en servicio/models.py
#LUEGO HACER EN PROYECTO DJANGO:
# python manage.py makemigrations servicio
# python manage.py migrate servicio

#LUEGO HACER EN CONSOLA POSTGRES:
# UPDATE servicio_arriendo SET inventario_id = temporal_inventario;
# UPDATE servicio_inventario SET pelicula_id = temporal_pelicula;
# UPDATE servicio_pelicula SET idioma_id = temporal_idioma;


#------------------------------------------------------------------------------
# tabla union pelicula_actores
#DESCOMENTAR LAS SIGUIENTES 3 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#seleccion_campos_film_actor = ['actor_id', 'film_id']
#campos_pelicula_actores = ['actor_id', 'pelicula_id']
#csv_a_tabla('film_actor.csv','servicio_pelicula_actores', seleccion_campos_film_actor, campos_pelicula_actores, conector2)


#------------------------------------------------------------------------------
# tabla union pelicula_categorias
#DESCOMENTAR LAS SIGUIENTES 3 LINEAS, EJECUTAR ESTE SCRIPT Y VOLVER A COMENTAR
#seleccion_campos_film_category = ['film_id', 'category_id']
#campos_pelicula_categorias = ['pelicula_id', 'categoria_id']
#csv_a_tabla('film_category.csv','servicio_pelicula_categorias', seleccion_campos_film_category, campos_pelicula_categorias, conector2)
