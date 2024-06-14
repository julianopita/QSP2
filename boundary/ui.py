import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from control.controladorInscricao import ControladorInscricao as controller

sessionAluno = ""
class App:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Seleção de Disciplinas")
        self.root.geometry("600x400")
        self.selected_student = None

        #Seleção de estudante
        self.show_student_selection_window()

    def show_student_selection_window(self):
        self.student_selection_window = tk.Toplevel(self.root)
        self.student_selection_window.title("Selecione o estudante")
        self.student_selection_window.geometry("400x300")

        tk.Label(self.student_selection_window, text="Selecione um estudante para continuar:").pack(pady=10)

        self.student_tree = ttk.Treeview(self.student_selection_window, columns=("Matricula", "Nome"), show='headings')
        self.student_tree.pack(fill=tk.BOTH, expand=True)

        self.student_tree.heading("Matricula", text="Matricula")
        self.student_tree.heading("Nome", text="Nome")

        for aluno in self.controller.listaAlunos():
            self.student_tree.insert("", "end", values=(aluno.matricula, aluno.nome))

        tk.Button(self.student_selection_window, text="Select", command=self.select_student).pack(pady=10)

    def select_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showwarning("Erro", "Por favor, selecione um estudante")
            return
        student = self.student_tree.item(selected_item, "values")
        self.selected_student = [student[0]]
        self.controller.selecionarAluno(self.selected_student)
        sessionAluno = self.selected_student        
        self.student_selection_window.destroy()
        self.show_course_selection_window()

        #Frame
    def show_course_selection_window(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(frame, text="Selecione as disciplinas dentre as disponíveis.\nMantenha a tecla <Control> pressionada para selecionar mais de uma:")
        self.label.pack(pady=10)
        
        #Treeview          
        self.tree = ttk.Treeview(frame, columns=("Codigo", "Titulo", "Semestre", "Creditos", "PreRequisitos", "Turma", "Vagas", "Dia", "HoraInicio", "HoraFim", "Professor", "Sala"), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Define headings
        self.tree.heading("Codigo", text="Código")
        self.tree.heading("Titulo", text="Título")
        self.tree.heading("Semestre", text="Semestre")
        self.tree.heading("Creditos", text="Créditos")
        self.tree.heading("PreRequisitos", text="Pré Requisitos")
        self.tree.heading("Turma", text="Turma")
        self.tree.heading("Vagas", text="Vagas")
        self.tree.heading("Dia", text="Dia")
        self.tree.heading("HoraInicio", text="Hora Início")
        self.tree.heading("HoraFim", text="Hora Fim")
        self.tree.heading("Professor", text="Professor")
        self.tree.heading("Sala", text="Sala")


        # Define column widths
        self.tree.column("Codigo", width=50)
        self.tree.column("Titulo", width=150)
        self.tree.column("Semestre", width=5)
        self.tree.column("Creditos", width=5)
        self.tree.column("PreRequisitos", width=150)
        self.tree.column("Turma", width=5)
        self.tree.column("Vagas", width=5)
        self.tree.column("Dia", width=50)
        self.tree.column("HoraInicio", width=30)
        self.tree.column("HoraFim", width=30)
        self.tree.column("Professor", width=100)
        self.tree.column("Sala", width=10)

        self.items = self.controller.mostrarListaDisciplinas()
        for item in self.items:
            self.tree.insert("", "end", values=(item.codigo, item.titulo, item.semestre, item.creditos, item.preRequisitos, item.idTurma, item.vagas, item.diaSem, item.horaIn, item.horaFim, item.professorNome, item.salaNumero))

        self.submit_button = tk.Button(frame, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        selected_indices = self.tree.selection()
        selected_items = [self.tree.item(item, "values") for item in selected_indices]
        if not selected_items:
            messagebox.showerror("Problemas na seleção", "Você precisa selecionar alguma disciplina para continuar!")
        else:    
            success, message, unavailable_courses = self.controller.handle_selection(selected_items)
            if success:
                self.show_confirmation_window(selected_items)
            else:
                if unavailable_courses:
                    self.show_waitlist_window(unavailable_courses)
                else:
                    messagebox.showerror("Problemas na seleção", message)
                self.tree.selection_remove(self.tree.selection())

    def show_confirmation_window(self, selected_courses):
        self.confirmation_window = tk.Toplevel(self.root)
        self.confirmation_window.title("Confirmação da seleção")
        self.confirmation_window.geometry("800x400")

        tk.Label(self.confirmation_window, text="Por favor, confira a sua seleção:").pack(pady=10)

        columns = ("Codigo", "Titulo", "Semestre", "Creditos", "PreRequisitos", "Turma", "Vagas", "Dia", "HoraInicio", "HoraFim", "Professor", "Sala")
        tree = ttk.Treeview(self.confirmation_window, columns=columns, show='headings')
        tree.pack(fill=tk.BOTH, expand=True)

        # Define headings
        for col in columns:
            tree.heading(col, text=col)

        # Define column widths
        tree.column("Codigo", width=50)
        tree.column("Titulo", width=150)
        tree.column("Semestre", width=5)
        tree.column("Creditos", width=5)
        tree.column("PreRequisitos", width=0)
        tree.column("Turma", width=5)
        tree.column("Vagas", width=5)
        tree.column("Dia", width=50)
        tree.column("HoraInicio", width=30)
        tree.column("HoraFim", width=30)
        tree.column("Professor", width=100)
        tree.column("Sala", width=10)


        # Insert selected courses
        for course in selected_courses:
            tree.insert("", "end", values=course)

        frame = tk.Frame(self.confirmation_window)
        frame.pack(pady=10)

        confirm_button = tk.Button(frame, text="Confirmar", command=lambda: self.confirm_selection(selected_courses))
        confirm_button.pack(side=tk.LEFT, padx=5)

        restart_button = tk.Button(frame, text="Reiniciar", command=self.restart_selection)
        restart_button.pack(side=tk.LEFT, padx=5)

    def confirm_selection(self, selected_courses):
        self.controller.realizarInscricao(selected_courses)
        messagebox.showinfo("Confirmação", "Sua seleção foi confirmada.")
        self.confirmation_window.destroy()        

    def restart_selection(self):
        self.confirmation_window.destroy()

    def show_waitlist_window(self, unavailable_courses):
        waitlist_window = tk.Toplevel(self.root)
        waitlist_window.title("Selecionar lista de espera")
        waitlist_window.geometry("400x300")

        tk.Label(waitlist_window, text="As seguintes disciplinas estão cheias.\nVocê gostaria de entrar na lista de espera?").pack(pady=10)

        self.waitlist_vars = {}
        for course in unavailable_courses:
            frame = tk.Frame(waitlist_window)
            frame.pack(fill=tk.X, padx=10, pady=5)
            tk.Label(frame, text=course.titulo).pack(side=tk.LEFT)
            var = tk.StringVar(value="no")
            self.waitlist_vars[course.titulo] = var
            tk.Radiobutton(frame, text="Sim", variable=var, value="yes").pack(side=tk.LEFT)
            tk.Radiobutton(frame, text="Não", variable=var, value="no").pack(side=tk.LEFT)

        tk.Button(waitlist_window, text="Enviar", command=lambda: self.submit_waitlist(waitlist_window)).pack(pady=20)

    def submit_waitlist(self, waitlist_window):
        waitlist_choices = {course: var.get() == "yes" for course, var in self.waitlist_vars.items()}
        student_id = sessionAluno
        #student_id = self.controller.selecionarAluno  
        posicaoListaEspera = self.controller.handle_waitlist(waitlist_choices, student_id)

        if posicaoListaEspera:
            waitlist_message = "\n".join([f"Disciplina: {course}, Posição: {position}" for course, position in posicaoListaEspera.items()])
            messagebox.showinfo("Lista de espera", f"Você foi adicionado à lista de espera:\n{waitlist_message}")
        
        else:
            messagebox.showinfo("Lista de espera", "Você não foi adicionado a nenhuma lista de espera")
        
        waitlist_window.destroy()
        

def run_app(controller):
    root = tk.Tk()
    app = App(root, controller)
    root.mainloop()