import reflex as rx
from ..components.solicitudes_form import solicitudes_form
from ..components.cotizasion import cotizacion
from ..states.solicitud_state import SolicitudState


def solicitudes():
    
    return  rx.vstack(
            rx.hstack(
                rx.button(
                    "Nueva solicitud",
                    bg=rx.cond(SolicitudState.tab_activa == "nueva", "#1c202b", "transparent"),
                    color=rx.cond(SolicitudState.tab_activa == "nueva", "white", "#9ca3af"),
                    border=rx.cond(SolicitudState.tab_activa == "nueva", "1px solid #3b4254", "1px solid transparent"),
                    border_radius="20px",
                    padding_x="18px",
                    font_weight="bold",
                    size="2",
                    on_click=lambda: SolicitudState.set_tab("nueva"),
                ),
                rx.button(
                    "Mis solicitudes",
                    bg=rx.cond(SolicitudState.tab_activa == "mis_solicitudes", "#1c202b", "transparent"),
                    color=rx.cond(SolicitudState.tab_activa == "mis_solicitudes", "white", "#9ca3af"),
                    border=rx.cond(SolicitudState.tab_activa == "mis_solicitudes", "1px solid #3b4254", "1px solid transparent"),
                    border_radius="20px",
                    padding_x="18px",
                    font_weight="bold",
                    size="2",
                    on_click=lambda: SolicitudState.set_tab("mis_solicitudes"),
                ),
                spacing="2",
                margin_bottom="12px",
            ),
            rx.hstack(
                solicitudes_form(),
                cotizacion(),
                spacing="2",
                margin_bottom="12px",
                width="100%",
            ),
            width="100%",
        )