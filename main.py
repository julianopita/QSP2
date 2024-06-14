from control.controladorInscricao import ControladorInscricao
from boundary.ui import run_app



if __name__ == "__main__":
    controller = ControladorInscricao()
    run_app(controller)