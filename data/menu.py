import pygame
import os

# ---------------------------------------------------------
# Función para cargar imágenes desde hud y escalarlas
# ---------------------------------------------------------
def load_hud(name, scale=0.6):
    path = os.path.join("data", "images", "hud", name)
    img = pygame.image.load(path).convert_alpha()

    # Escalar imagen
    w, h = img.get_size()
    new_size = (int(w * scale), int(h * scale))
    img = pygame.transform.scale(img, new_size)

    return img

# ---------------------------------------------------------
# Cache de botones (lazy-load)
# ---------------------------------------------------------
buttons = None

def init_buttons():
    """Inicializa los botones después de que pygame.display esté listo"""
    global buttons
    if buttons is None:
        buttons = {
            "play": {
                "normal": load_hud("en_play.png"),
                "hover": load_hud("en_play_select.png")
            },
            "options": {
                "normal": load_hud("en_options.png"),
                "hover": load_hud("en_options_select.png")
            },
            "credits": {
                "normal": load_hud("en_credits.png"),
                "hover": load_hud("en_credits_select.png")
            },
            "exit": {
                "normal": load_hud("en_exit.png"),
                "hover": load_hud("en_exit_select.png")
            }
        }
    return buttons

# Orden vertical de los botones
button_order = ["play", "options", "credits", "exit"]

# ---------------------------------------------------------
# Dibuja los botones y devuelve sus rects
# ---------------------------------------------------------
def draw_menu_buttons(screen, width=1920, height=1080):
    btns = init_buttons()  # Inicializar botones en primer uso
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Tomamos tamaño del primer botón
    btn_w, btn_h = btns["play"]["normal"].get_size()
    spacing = 20

    total_height = len(button_order) * (btn_h + spacing) - spacing
    start_y = (height - total_height) // 2

    rects = {}

    for index, name in enumerate(button_order):
        y = start_y + index * (btn_h + spacing)
        x = 0  # pegados a la izquierda

        rect = pygame.Rect(x, y, btn_w, btn_h)
        rects[name] = rect

        # Hover
        if rect.collidepoint(mouse_x, mouse_y):
            img = btns[name]["hover"]
        else:
            img = btns[name]["normal"]

        screen.blit(img, (x, y))

    return rects

# ---------------------------------------------------------
# Menú principal
# ---------------------------------------------------------
def main_menu(screen, width=1920, height=1080):
    running = True

    while running:
        rects = draw_menu_buttons(screen, width, height)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # ESC *ya no sale*
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

            # Clic izquierdo
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()

                if rects["play"].collidepoint(mx, my):
                    print("[MENU] Play presionado (aún sin acción)")

                if rects["options"].collidepoint(mx, my):
                    print("[MENU] Options presionado (aún sin acción)")

                if rects["credits"].collidepoint(mx, my):
                    print("[MENU] Credits presionado (aún sin acción)")

                # ✔ Aquí si cierra
                if rects["exit"].collidepoint(mx, my):
                    running = False
                # nota: el menu esta muy inprovisado, solo para pruebas

        screen.fill((0, 0, 0))
        draw_menu_buttons(screen, width, height)
        pygame.display.flip()
