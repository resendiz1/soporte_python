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
            messagebox.showinfo('Login exitoso', f"Welcome, {usuario['name']}")

        else:
            messagebox.showerror("Error", "Las credenciales son incorrectas")

    except mysql.connector.Error as err:
        messagebox.showerror("Error en la conexion", str(err))

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()



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
entry_email.pack(pady=5, anchor="c", padx=(20,0))


#entry password
tk.Label(root, text="Contraseña: ", **estilo_label).pack(pady=(20,5), anchor="w", padx=(20,0))
entry_password = tk.Entry(root, show="*", **estilo_entry)
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












