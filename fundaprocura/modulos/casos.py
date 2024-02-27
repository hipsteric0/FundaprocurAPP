import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QPlainTextEdit
import mysql.connector

def casos():
    # Crea la ventana
    dialog = QDialog()
    dialog.setWindowTitle("Registro de Casos")
    dialog.setGeometry(100, 100, 1500, 400)

    # Crea el layout
    layout = QVBoxLayout()

    # Creaa el cuadro de Información personal 
    course_group_box = QGroupBox("Infomación Personal")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Creaa el cuadro de Información accidente
    course_group_box_2 = QGroupBox("Infomación Accidente")
    course_layout_2 = QGridLayout()
    course_group_box_2.setLayout(course_layout_2)

    # Creaa el cuadro de Información pariente
    course_group_box_3 = QGroupBox("Infomación Pariente")
    course_layout_3 = QGridLayout()
    course_group_box_3.setLayout(course_layout_3)

    # Craea el cuadro del botón
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    # Crea los labels e inputs
    grupo_label = QLabel("Grupo: ")
    grupo_input = QLineEdit()
    fecha_caso_label = QLabel("Fecha caso: ")
    fecha_caso_input = QLineEdit()
    fecha_caso_input.setPlaceholderText("Formato: AAAA-MM-DD")
    ref_label = QLabel("REF: ")
    ref_input = QLineEdit()
    cedula_label = QLabel("Cedula: ")
    cedula_input = QLineEdit()
    apellidos_label = QLabel("Apellidos: ")
    apellidos_input = QLineEdit()
    nombres_label = QLabel("Nombres: ")
    nombres_input = QLineEdit()
    sexo_label = QLabel("Sexo: ")
    sexo_input = QLineEdit()
    direccion_label = QLabel("Dirección: ")
    direccion_input = QLineEdit()
    direccion_input = QPlainTextEdit()
    direccion_input.setFixedSize(250, 80)
    telefono_label = QLabel("Telefonos: ")
    telefono_input = QLineEdit()
    telefono_input = QPlainTextEdit()
    telefono_input.setFixedSize(250, 80)
    correo_label = QLabel("Correo:")
    correo_input = QLineEdit()
    locacion_don_label = QLabel("Locación don.: ")
    locacion_don_input = QLineEdit()
    locacion_don_input = QPlainTextEdit()
    locacion_don_input.setFixedSize(250, 80)
    fecha_accidente_label = QLabel("Fecha del accidente: ")
    fecha_accidente_input = QLineEdit()
    fecha_accidente_input.setPlaceholderText("Formato: AAAA-MM-DD")
    causa_label = QLabel("Causa: ")
    causa_input = QLineEdit()
    lesion_label = QLabel("Lesión: ")
    lesion_input = QLineEdit()
    fecha_nacimiento_label = QLabel("Fecha de nacimiento: ")
    fecha_nacimiento_input = QLineEdit()
    fecha_nacimiento_input.setPlaceholderText("Formato: AAAA-MM-DD")
    lugar_nacimiento_label = QLabel("Lugar de nacimiento: ")
    lugar_nacimiento_input = QLineEdit()
    lugar_nacimiento_input = QPlainTextEdit()
    lugar_nacimiento_input.setFixedSize(250, 80)
    equipo_actual_label = QLabel("Equipo actual: ")
    equipo_actual_input = QLineEdit()
    donacion_label = QLabel("Donación: ")
    donacion_input = QLineEdit()
    medidas_label = QLabel("Medidas: ")
    medidas_input = QLineEdit()
    medidas_input = QPlainTextEdit()
    medidas_input.setFixedSize(250, 80)
    medidas_instrucciones_label = QLabel("Medidias instrucciones: ")
    medidas_instrucciones_input = QLineEdit()
    medidas_instrucciones_input = QPlainTextEdit()
    medidas_instrucciones_input.setFixedSize(250, 80)
    ultima_medicion_label = QLabel("Ultima medición: ")
    ultima_medicion_input = QLineEdit()
    ultima_medicion_input.setPlaceholderText("Formato: AAAA-MM-DD")
    serie_label = QLabel("Serial: ")
    serie_input = QLineEdit()
    control_WF_label = QLabel("Control WF: ")
    control_WF_input = QLineEdit()
    nombre_familiar_label = QLabel("Nombre familiar: ")
    nombre_familiar_input = QLineEdit()
    cedula_familiar_label = QLabel("Cedula familiar: ")
    cedula_familiar_input = QLineEdit()
    direccion_familiar_label = QLabel("Dirección familiar: ")
    direccion_familiar_input = QLineEdit()
    direccion_familiar_input = QPlainTextEdit()
    direccion_familiar_input.setFixedSize(250, 80)
    telefono_familiar_label = QLabel("Telefono familiar: ")
    telefono_familiar_input = QLineEdit()
    recaudos_label = QLabel("Recaudos: ")
    recaudos_input = QLineEdit()
    recaudos_input = QPlainTextEdit()
    recaudos_input.setFixedSize(250, 80)
    observaciones_comentarios_label = QLabel("Observaciones - comentarios: ")
    observaciones_comentarios_input = QLineEdit()
    observaciones_comentarios_input = QPlainTextEdit()
    observaciones_comentarios_input.setFixedSize(250, 80)
    fk_tipo_caso_label = QLabel("Tipo de caso: ")
    fk_tipo_caso_input = QLineEdit()
    fk_clasificacion_label = QLabel("Clasificación: ")
    fk_clasificacion_input = QComboBox()
    fk_estado_label = QLabel("Estado: ")
    fk_estado_input = QComboBox()
    fk_municipio_ciudad_label = QLabel("Municipio - Ciudad: ")
    fk_municipio_ciudad_input = QLineEdit()
    fk_parentesco_label = QLabel("Parentesco familiar: ")
    fk_parentesco_input = QComboBox()


    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener clasificaciones para el combobox
    query = "SELECT id, nombre FROM fundaprocura.clasificacion"
    cursor = cnx.cursor()
    cursor.execute(query)
    clasificaciones = cursor.fetchall()
    fk_clasificacion_input.addItem("Seleccione clasificación")
    for clasificacion in clasificaciones:
        fk_clasificacion_input.addItem(str(clasificacion[1]))
    cursor.close()


    # Obtener Estados para el combobox
    query = "SELECT id, nombre FROM fundaprocura.estado"
    cursor = cnx.cursor()
    cursor.execute(query)
    estados = cursor.fetchall()
    fk_estado_input.addItem("Seleccione Estado")
    for estado in estados:
        fk_estado_input.addItem(str(estado[1]))
    cursor.close()


    # Obtener parentesco para el combobox
    query = "SELECT id, nombre FROM fundaprocura.parentesco"
    cursor = cnx.cursor()
    cursor.execute(query)
    parentescos = cursor.fetchall()
    fk_parentesco_input.addItem("Seleccione parentezco")
    for parentesco in parentescos:
        fk_parentesco_input.addItem(str(parentesco[1]))
    cursor.close()
    cnx.close()


    #Posición de los Inputs
    course_layout.addWidget(grupo_label , 0, 0)
    course_layout.addWidget(grupo_input, 0, 1)
    course_layout.addWidget(fecha_caso_label,  0, 2)
    course_layout.addWidget(fecha_caso_input, 0, 3)
    course_layout.addWidget(ref_label , 0, 4)
    course_layout.addWidget(ref_input, 0, 5)
    course_layout.addWidget(fk_clasificacion_label , 0, 6)
    course_layout.addWidget(fk_clasificacion_input, 0, 7)
    course_layout.addWidget(fk_tipo_caso_label , 1, 0)
    course_layout.addWidget(fk_tipo_caso_input, 1, 1)
    course_layout.addWidget(cedula_label, 1, 2)
    course_layout.addWidget(cedula_input, 1, 3)
    course_layout.addWidget(apellidos_label , 2, 0)
    course_layout.addWidget(apellidos_input, 2, 1)
    course_layout.addWidget(nombres_label , 3, 0)
    course_layout.addWidget(nombres_input, 3, 1)
    course_layout.addWidget(sexo_label , 3, 2)
    course_layout.addWidget(sexo_input, 3, 3)
    course_layout.addWidget(fk_estado_label , 4, 2)
    course_layout.addWidget(fk_estado_input, 4, 3)
    course_layout.addWidget(correo_label , 4, 4)
    course_layout.addWidget(correo_input, 4, 5)
    course_layout.addWidget(fecha_nacimiento_label , 4, 6)
    course_layout.addWidget(fecha_nacimiento_input, 4, 7)
    course_layout.addWidget(direccion_label , 5, 0)
    course_layout.addWidget(direccion_input, 5, 1)
    course_layout.addWidget(fk_municipio_ciudad_label , 5, 2)
    course_layout.addWidget(fk_municipio_ciudad_input, 5, 3)
    course_layout.addWidget(telefono_label , 5, 4)
    course_layout.addWidget(telefono_input, 5, 5)
    course_layout.addWidget(lugar_nacimiento_label , 5, 6)
    course_layout.addWidget(lugar_nacimiento_input, 5, 7)
    course_layout.addWidget(locacion_don_label,  6, 2)
    course_layout.addWidget(locacion_don_input, 6, 3)
    course_layout_2.addWidget(fecha_accidente_label , 1, 0)
    course_layout_2.addWidget(fecha_accidente_input, 1, 1)
    course_layout_2.addWidget(causa_label, 2, 0)
    course_layout_2.addWidget(causa_input, 2, 1)
    course_layout_2.addWidget(lesion_label , 2, 2)
    course_layout_2.addWidget(lesion_input, 2, 3)
    course_layout_2.addWidget(equipo_actual_label , 3, 0)
    course_layout_2.addWidget(equipo_actual_input, 3, 1)
    course_layout_2.addWidget(donacion_label , 4, 0)
    course_layout_2.addWidget(donacion_input, 4, 1)
    course_layout_2.addWidget(medidas_label,  5, 0)
    course_layout_2.addWidget(medidas_input, 5, 1)
    course_layout_2.addWidget(medidas_instrucciones_label , 5, 2)
    course_layout_2.addWidget(medidas_instrucciones_input, 5, 3)
    course_layout_2.addWidget(ultima_medicion_label, 5, 4)
    course_layout_2.addWidget(ultima_medicion_input, 5, 5)
    course_layout_2.addWidget(serie_label , 6, 0)
    course_layout_2.addWidget(serie_input, 6, 1)
    course_layout_2.addWidget(control_WF_label , 6, 2)
    course_layout_2.addWidget(control_WF_input, 6, 3)
    course_layout_3.addWidget(nombre_familiar_label , 13, 0)
    course_layout_3.addWidget(nombre_familiar_input, 13, 1)
    course_layout_3.addWidget(cedula_familiar_label , 14, 0)
    course_layout_3.addWidget(cedula_familiar_input, 14, 1)
    course_layout_3.addWidget(direccion_familiar_label , 14, 2)
    course_layout_3.addWidget(direccion_familiar_input, 14, 3)
    course_layout_3.addWidget(fk_parentesco_label , 14, 4)
    course_layout_3.addWidget(fk_parentesco_input, 14, 5)
    course_layout_3.addWidget(telefono_familiar_label,  15, 2)
    course_layout_3.addWidget(telefono_familiar_input, 15, 3)
    course_layout_3.addWidget(recaudos_label , 16, 0)
    course_layout_3.addWidget(recaudos_input, 16, 1)
    course_layout_3.addWidget(observaciones_comentarios_label, 17, 2)
    course_layout_3.addWidget(observaciones_comentarios_input, 17, 3)

    
    # Agrega el botón Registrar
    next_button = QPushButton("Registrar")
    next_button.setAutoDefault(False)
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    # Orden de los componentes
    layout.addWidget(course_group_box)
    layout.addWidget(course_group_box_2)
    layout.addWidget(course_group_box_3)
    layout.addWidget(buttons_group_box)
    

    # Agrega el layout en la ventana
    dialog.setLayout(layout)

    # Conecta el botón Registrar con la función insert_data
    next_button.clicked.connect(lambda: insert_data(dialog, grupo_input, fecha_caso_input, ref_input, cedula_input, apellidos_input, nombres_input,sexo_input, direccion_input, telefono_input,correo_input, locacion_don_input, fecha_accidente_input, causa_input, lesion_input, fecha_nacimiento_input, lugar_nacimiento_input, equipo_actual_input, donacion_input, medidas_input, medidas_instrucciones_input, ultima_medicion_input, serie_input, control_WF_input, nombre_familiar_input, cedula_familiar_input, direccion_familiar_input, telefono_familiar_input, recaudos_input,fk_tipo_caso_input, fk_clasificacion_input, fk_estado_input, fk_municipio_ciudad_input, fk_parentesco_input, observaciones_comentarios_input, clasificaciones, estados, parentescos))

    return dialog

#Esta función guarda la información del formulario en la BD
def insert_data(dialog, grupo_input, fecha_caso_input, ref_input, cedula_input, apellidos_input, nombres_input,sexo_input, direccion_input, telefono_input, correo_input, locacion_don_input, fecha_accidente_input, causa_input, lesion_input, fecha_nacimiento_input, lugar_nacimiento_input, equipo_actual_input, donacion_input, medidas_input, medidas_instrucciones_input, ultima_medicion_input, serie_input, control_WF_input, nombre_familiar_input, cedula_familiar_input, direccion_familiar_input, telefono_familiar_input, recaudos_input,fk_tipo_caso_input, fk_clasificacion_input, fk_estado_input, fk_municipio_ciudad_input, fk_parentesco_input, observaciones_comentarios_input, clasificaciones, estados, parentescos):
    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

     # Obtiene el valor de los inputs
    grupo = grupo_input.text()
    fecha_caso = fecha_caso_input.text() or None
    ref = ref_input.text()
    cedula = int(cedula_input.text() or 0)
    apellidos = apellidos_input.text()
    nombres = nombres_input.text()
    sexo = sexo_input.text()
    direccion = direccion_input.toPlainText()
    telefono = telefono_input.toPlainText()
    correo = correo_input.text()
    locacion_don = locacion_don_input.toPlainText()
    fecha_accidente = fecha_accidente_input.text() or None
    causa = causa_input.text()
    lesion = lesion_input.text()
    fecha_nacimiento = fecha_nacimiento_input.text() or None
    lugar_nacimiento = lugar_nacimiento_input.toPlainText()
    equipo_actual = equipo_actual_input.text()
    donacion = donacion_input.text()
    medidas = medidas_input.toPlainText()
    medidas_instrucciones = medidas_instrucciones_input.toPlainText()
    ultima_medicion = ultima_medicion_input.text() or None
    serie = serie_input.text()
    control_WF = control_WF_input.text()
    nombre_familiar = nombre_familiar_input.text()
    cedula_familiar = int(cedula_familiar_input.text() or 0)
    direccion_familiar = direccion_familiar_input.toPlainText()
    telefono_familiar = telefono_familiar_input.text()
    recaudos = recaudos_input.toPlainText()
    observaciones_comentarios = observaciones_comentarios_input.toPlainText()
    fk_tipo_caso = fk_tipo_caso_input.text()
    fk_clasificacion = 0 or None
    fk_estado = 0 or None
    fk_municipio_ciudad = fk_municipio_ciudad_input.text()
    fk_parentesco = 0 or None


    # Busca el índice de la clasificación seleccionada
    selected_calsificacion_index = fk_clasificacion_input.currentIndex()

    # Válida la clasificación seleccionada
    if selected_calsificacion_index > 0:
        fk_clasificacion = clasificaciones[selected_calsificacion_index - 1][0]


     # Busca el índice del Estado seleccioando
    selected_estado_index = fk_estado_input.currentIndex()

    # Válida el Estado seleccionado
    if selected_estado_index > 0:
        fk_estado = estados[selected_estado_index - 1][0]

    # Busca el índice del parentesco seleccioando
    selected_parentesco_index = fk_parentesco_input.currentIndex()

    # Válida el parentesco seleccionado
    if selected_parentesco_index > 0:
        fk_parentesco = parentescos[selected_parentesco_index - 1][0]


    # Inserta los datos en la BD
    query = "INSERT INTO fundaprocura.casos (grupo,tipo_caso,fecha,ref,cedula,apellidos,nombres,sexo,direccion,telefono,correo,locacion_don,fecha_accidente,causa,lesion,fecha_nacimiento,lugar_nacimiento,municipio_ciudad,equipo_actual,donacion,medidas,medidas_instrucciones,ultima_medicion,serie,control_WF,nombre_familiar,cedula_familiar,direccion_familiar,telefono_familiar,recaudos,observaciones_comentarios,fk_clasificacion,fk_esado,fk_parentesco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (grupo,fk_tipo_caso,fecha_caso,ref,cedula,apellidos,nombres,sexo,direccion,telefono,correo,locacion_don,fecha_accidente,causa,lesion,fecha_nacimiento,lugar_nacimiento,fk_municipio_ciudad,equipo_actual,donacion,medidas,medidas_instrucciones,ultima_medicion,serie,control_WF,nombre_familiar,cedula_familiar,direccion_familiar,telefono_familiar,recaudos,observaciones_comentarios,fk_clasificacion,fk_estado,fk_parentesco))
    cnx.commit()
    cursor.close()
    cnx.close()

    # Cierra la ventana
    dialog.close()