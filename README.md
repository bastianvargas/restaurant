# Reportería de Restaurante

sistema de reportería de restaurante, basado en el consumo de un archivo .json con estructura definida previamente

## Installation

luego de clonar el proyecto se deben instalar recursivamente los paquetes requeridos en un entorno virtual

```bash
pip install -r requirements.txt
```

## Uso

se debe levantar el servidor

```bash
python manage.py runserver
```

con el servidor ya arriba, en la ruta home está disponible un formulario para adjuntar un archivo.json
el cual en el momento de enviar inmediatamente(dependiendo del tamaño del dataset) se desplegara un gráfico con información útil para la gestión del negocio   


<img width="500" alt="Captura de pantalla 2019-06-24 a la(s) 22 47 02 copia" src="https://user-images.githubusercontent.com/14500233/60065952-9004a480-96d3-11e9-8ffc-7cabd7f8c57b.png">


