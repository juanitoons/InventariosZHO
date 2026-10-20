import reflex as rx

def cotizacion():
    return rx.box(
        rx.vstack(
            rx.text("VA A LA HOJA"),
            rx.text("ZHO (GG)",color_scheme="green")
        ),
        bg="#12141a",
        border="1px solid #232733",
        border_radius="10px",
        padding="24px",
        width="50%",
    )