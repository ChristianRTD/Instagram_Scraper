from playwright.sync_api import sync_playwright
import json

USERNAME = "andrespaida_"

# Tus cookies reales aquí
COOKIES = [
    {
        "name": "sessionid",
        "value": "TU_SESSION_ID",
        "domain": ".instagram.com",
        "path": "/"
    },
    {
        "name": "csrftoken",
        "value": "TU_CSRF_TOKEN",
        "domain": ".instagram.com",
        "path": "/"
    },
    {
        "name": "ds_user_id",
        "value": "TU_USER_ID",
        "domain": ".instagram.com",
        "path": "/"
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # False para ver el navegador
    context = browser.new_context()

    # Agregar cookies
    context.add_cookies(COOKIES)

    page = context.new_page()

    # Ir al perfil
    url = f"https://www.instagram.com/{USERNAME}/"
    page.goto(url)

    # Esperar a que cargue contenido
    page.wait_for_selector("header")

    # Extraer datos básicos
    username = page.locator("h2").first.inner_text()
    bio = page.locator("div.-vDIg span").inner_text()

    # Seguidores (puede variar según idioma)
    stats = page.locator("ul li span").all_inner_texts()

    print("=== DATOS DEL PERFIL ===")
    print("Usuario:", username)
    print("Bio:", bio)
    print("Stats:", stats)

    browser.close()
    