import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt
from PIL import Image, ImageTk




#configuramos la base de datos a usar con mysql
def conectar():

    return mysql.connector.connect(

        host="127.0.0.1",
        user="root",
        password="",
        database="inventario_prod",
        port=3306


    )


def login():
    email = entry_email.get()
    password = entry_password.get()

    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT*FROM users WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            
            pedir_soporte_formulario()

        else:
            messagebox.showerror("Error", "Las credenciales son incorrectas")

    except mysql.connector.Error as err:
        messagebox.showerror("Error en la conexion", str(err))

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()



def pedir_soporte_formulario():
    
    formulario_soporte = tk.Tk()
    formulario_soporte.title("Abrir Ticket de Soporte")
    formulario_soporte.geometry("500x700")
    formulario_soporte.configure(bg="#2f2f2f")


    #variables de estilos de las label y las entry
    estilo_label = {
        "bg": "#2f2f2f", 
        "fg": "#ffffff", 
        "font": ("Segoe UI", 14)
    }


    estilo_entry = {
        "bg": "#444444", 
        "fg": "#ffffff", 
        "insertbackground": "#ffffff", 
        "relief": "flat", 
        "width":25,
        "font": ("Segoe UI", 14),
    }

    tk.Label(formulario_soporte, text="Descripción: ", **estilo_label)


    #Text de la descripcion
    tk.Label(formulario_soporte, text="Descripcion: ", **estilo_label).pack(pady=(25,2), anchor="w", padx=(20,0))
    descripcion = tk.Text(formulario_soporte, height=5, width=40, relief="flat", font=("Segoe UI", 12), )
    descripcion.pack(pady=(10,5), anchor="c", padx=(20,0))





    tk.Label(formulario_soporte, text="Dispositivo que fallo: ", **estilo_label).pack(pady=(25,2), anchor="w", padx=(20,0))
    
    #Option menu para el dispositivo que fallo
    dispositivo_seleccionado = tk.StringVar(formulario_soporte)
    dispositivo_seleccionado.set("Dispositivo que fallo") #Valos por defecto
    #Lista de opciones
    opciones = ['Computadora','Impresora','​Otro']
    #personalizar menu desplegable


    #crear el optionMenu
    dispositivos = tk.OptionMenu(formulario_soporte, dispositivo_seleccionado, *opciones)
    dispositivos["menu"].config(bg="#444444", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", borderwidth=0,  font=("Segoe UI", 10))
    dispositivos.config(width=40, bg="#444444", fg="#ffffff", highlightthickness=0, activebackground="#555555", anchor="w")
    dispositivos.pack(pady=(10,5))
    #Option menu para el dispositivo que fallo


    if dispositivo_seleccionado.get() == "Otro":
        label_otro.pack_forget(pady=(25,2), anchor="w", padx=(20,0))



    #Aqui va el input que esta oculto hasta que se selecciona "Otro"
    label_otro = tk.Label(formulario_soporte, text="Escribe lo que fallo: ", **estilo_label)#.pack_forget(pady=(25,2), anchor="w", padx=(20,0))
    #Aqui va el input que esta oculto hasta que se selecciona "Otro"





    formulario_soporte.mainloop()






#vamos con la fokin interfaz
root = tk.Tk()
root.title('Login')
root.geometry("350x350")
root.configure(bg='#2f2f2f');

#variables de estilos de las label y las entry
estilo_label = {
    "bg": "#2f2f2f", 
    "fg": "#ffffff", 
    "font": ("Segoe UI", 14)
}


estilo_entry = {
    "bg": "#444444", 
    "fg": "#ffffff", 
    "insertbackground": "#ffffff", 
    "relief": "flat", 
    "width":25,
    "font": ("Segoe UI", 14),
}


#Icono del boton
icono_img = Image.open("login.png")
icono_img = icono_img.resize((20,20))
icono = ImageTk.PhotoImage(icono_img)


#entry del email
tk.Label(root, text="Correo electronico: ", **estilo_label).pack(pady=(20,5), anchor="w", padx=(20,0))
entry_email = tk.Entry(root, **estilo_entry)
entry_email.insert(0, 'resendiz.galleta@gmail.com')
entry_email.pack(pady=5, anchor="c", padx=(20,0))


#entry password
tk.Label(root, text="Contraseña: ", **estilo_label).pack(pady=(20,5), anchor="w", padx=(20,0))
entry_password = tk.Entry(root, show="*", **estilo_entry)
entry_password.insert(0, 'password')
entry_password.pack(pady=5, anchor="c", padx=(20,0))


#boton de inicio
btn_login = tk.Button(
    root,  
    width=150, 
    height=50, 
    command=login, 
    compound="left", 
    anchor="center", 
    bg="#ffffff",
    image=icono, 
    text=" Iniciar Sesión", 
    fg="#000000", 
    activebackground="#3a3a3a", 
    relief="flat", 
    font=("Segoe UI", 10)
)


btn_login.pack(pady=(50, 10))

root.mainloop()












