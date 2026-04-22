import requests
import urllib.parse

# Tu token de API de Scrape.do
token = "<token>"

# El nombre de usuario de Instagram que queremos scrapear
username = "andrespaida_"

# Construir la URL de la API de Instagram para obtener información del perfil
profile_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"

# Codificar la URL para que pueda pasarse de forma segura como parámetro
encoded_url = urllib.parse.quote_plus(profile_url)

# Construir la URL de solicitud de Scrape.do para evitar bloqueos y restricciones de inicio de sesión
api_url = f"https://api.scrape.do/?token={token}&url={encoded_url}"

# Enviar la solicitud a través de Scrape.do
response = requests.get(api_url)

# Analizar la respuesta JSON
data = response.json()

# Extraer los datos del usuario de la respuesta JSON
user_data = data["data"]["user"]

# Imprimir información detallada del perfil de Instagram
print("=== Información detallada del perfil de Instagram ===")
print("Nombre de usuario:", user_data["username"])  # El nombre de usuario de Instagram
print("Nombre completo:", user_data["full_name"])  # El nombre completo del usuario
print("Biografía:", user_data["biography"])  # El texto de la biografía del perfil

# Extraer la biografía con cualquier entidad incrustada (p. ej., menciones, hashtags)
print("Biografía con entidades:", user_data["biography_with_entities"]["raw_text"])

# URL externa (por ejemplo, enlace al sitio web en el perfil)
print("URL externa:", user_data["external_url"])

# URL de la foto de perfil en alta resolución
print("URL de la imagen de perfil:", user_data["profile_pic_url_hd"])

# Información relacionada con negocios
print("Categoría de negocios:", user_data["business_category_name"])  # Categoría de negocio si aplica
print("Nombre de la categoría:", user_data["category_name"])  # Categoría general asociada con el perfil
print("¿Es una cuenta comercial?:", user_data["is_business_account"])  # Indicador booleano para cuentas de empresa

# Estado de privacidad y verificación
print("Es privado:", user_data["is_private"])  # Indicador booleano para cuentas privadas
print("Está Verificad@:", user_data["is_verified"])  # Indicador booleano para cuentas verificadas

# Estadísticas de interacción (Engagement)
print("Número de seguidores:", user_data["edge_followed_by"]["count"])  # Número de seguidores
print("Número de seguidos:", user_data["edge_follow"]["count"])  # Número de personas a las que sigue la cuenta
print("Número total de publicaciones:", user_data["edge_owner_to_timeline_media"]["count"])  # Número total de publicaciones