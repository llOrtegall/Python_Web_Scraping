import time
from selenium import webdriver

dirrecionesIP = {
  "Porteria": "172.20.1.49",
  "Contabilidad": "172.20.1.171",
  "Desarrollo": "172.20.1.67",
  "Aux_Comercial": "172.20.1.66",
  "Cartera": "172.20.1.68",
  "Contabilidad_02": "172.20.1.124",
  "Director_De_Oficina": "172.20.1.169",
  "Auditoria_Yumbo": "172.20.1.151",
  "Talonarios": "172.20.1.36",
  "Almacen": "172.20.1.176",
  "Tesoreria": "172.20.1.170",
  "Gestion_Humana":"172.20.1.37"
}

while True:
  
  Usuario = 'admin'
  Contrasena = 'oLUoXnsQ'
  driver = webdriver.Edge()
  for nameTelefono, ipTelefono in dirrecionesIP.items():
    #Inicia El Web Driver Visualmente
    print("Se Revisará Teléfono: " + nameTelefono )
    ### TODO: Datos de ingreso a la página
    driver.get('http://'+ipTelefono+'/')
    time.sleep(1) # esperar 1 seg para la pág
    user = driver.find_element("xpath", '/html/body/div/form/table/tbody/tr[3]/td[2]/input')
    password = driver.find_element("xpath", '/html/body/div/form/table/tbody/tr[4]/td[2]/input[1]')
    user.send_keys(Usuario)
    password.send_keys(Contrasena)
    login_btn = driver.find_element("xpath", '/html/body/div/form/table/tbody/tr[5]/td/input[1]').click()
    time.sleep(1) # Tiempo para que valide las credenciales
    ### ??? Asginamos el estado de la Cuenta 1 y Cuenta 2 por el momento esta con validaciones de (strings)
    Acount_01 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[2]/td[3]").text
    Acount_02 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[3]/td[3]").text
    
    ### TODO: Este Código Activará La Cuenta, Cuando Reporte Un Error. 
    if(Acount_01.__contains__('Desactivado') and Acount_02.__contains__('Desactivado')):
      print("Cuenta_01 y Cuenta_02 ==> Estan Desactivadas, Se Activará Cuenta 1")
      try:
        ### TODO: Vamos a la cuenta
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[2]/div[2]/label")
        cuenta.click()
        time.sleep(2) # tiempo para cargar la cuenta
        ### ? AUTOMATICAMENTE EL SE ENCONTRARÁ EN LA CUENTA 1 la cual debemos activar
        ### TODO Activamos la linea 1
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select")
        linea.click()
        activeLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[2]")
        activeLine.click()
        # ? confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        time.sleep(5)
        
        ### TODO: Vamos a Estado
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/label").click()
        time.sleep(5) # para que cargue estado
        state01 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[2]/td[3]").text
        print("Cuenta 1 Activada Correctamente y El Estado Es: " + state01)
        salir = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/div/div/label").click()
      except:
        ("error al activar la cuenta 1")
    elif(Acount_01.__contains__('Error') and Acount_02.__contains__('Error')):
      print("Cuenta_01 y Cuenta_02 ==> Estan Desactivadas, Se Activará Cuenta 1")
      try:
        ### TODO: Vamos a la cuenta
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[2]/div[2]/label")
        cuenta.click()
        time.sleep(2) # tiempo para cargar la cuenta
        ### ? AUTOMATICAMENTE EL SE ENCONTRARÁ EN LA CUENTA 1 la cual debemos activar
        ### TODO Activamos la linea 1
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select")
        linea.click()
        activeLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[2]")
        activeLine.click()
        # ? confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        time.sleep(5)
        
        ### TODO: Vamos a Estado
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/label").click()
        time.sleep(5) # para que cargue estado
        state01 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[2]/td[3]").text
        print("Cuenta 1 Activada Correctamente y El Estado Es: " + state01)
        salir = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/div/div/label").click()
      except:
        ("error al activar la cuenta 1")
    elif(Acount_01.__contains__('Error de registo') and Acount_02.__contains__('Desactivado')):
      # ! ERROR (En Cuenta_01) ==> DEBEMOS ACTIVAR SEGUNDA CUENTA Y DESACTIVAR PRIMERA
      print("Cuenta # 1 => Tiene Estado: " + Acount_01 + ", Se Activará La Cuenta 2")
      try:
        ### TODO: Vamos a la cuenta
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[2]/div[2]/label")
        cuenta.click()
        time.sleep(1) # tiempo para cargar cuenta
        ### TODO: Seleccionamos la cuenta 2
        cuenta2 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select").click()
        selectCuenta2 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select/option[2]").click()
        ### TODO Activamos la linea 
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select").click()
        activeLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[2]").click()
        # ? Confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        time.sleep(5)
        ### TODO: Vamos a la cuenta
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[2]/div[2]/label").click()
        time.sleep(1) # para cargar la cuenta
        ### TODO: Seleccionamos la cuenta 1
        cuenta1 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select").click()
        selectCuenta1 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select/option[1]").click()
        ### TODO Desactivamos la linea 
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select").click()
        desactiveLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[1]").click()
        # ? Confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        ### TODO: Vamos a Estado
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/label").click()
        time.sleep(1)
        state01 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[3]/td[3]").text
        print("Cuenta 1 Desactivada, Cuenta 2 Activada y El Estado Es: " + state01)
        salir = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/div/div/label").click()
      except:
        print("Error Al Activar La Cuenta 2")
    elif(Acount_02.__contains__('Error de registo') and Acount_01.__contains__('Desactivado')):
      # ! ERROR (En Cuenta_02) ==> DEBEMOS ACTIVAR PRIMERA CUENTA Y DESACTIVAR SEGUNDA
      print("Cuenta_02 Tiene Estado: " + Acount_02 + ", Se Activará La Cuenta 1")
      try:
        ### TODO: Vamos a la cuenta
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[2]/div[2]/label").click()
        time.sleep(1) # para cargar la pag
        ### TODO Activamos la linea 
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select").click()
        activeLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[2]").click()
        # ? Confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        time.sleep(5)
        ### TODO: Seleccionamos la cuenta 2
        cuenta2 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select").click()
        selectCuenta2 = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[2]/td[3]/select/option[2]").click()
        ### TODO Desactivamos la linea 
        linea = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select").click()
        desactiveLine = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/table/tbody[1]/tr[4]/td[3]/select/option[1]").click()
        # ? Confirmarmos
        confirm = driver.find_element("xpath", "/html/body/div/div[3]/div[3]/form/div/input[1]").click()
        time.sleep(5)
        ### TODO: Vamos a la Estado
        cuenta = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/label").click()
        state01 = driver.find_element("xpath", "/html/body/div/div[3]/div[2]/table/tbody[7]/tr[2]/td[3]").text
        print("Cuenta 1 Desactivada, Cuenta 2 Activada y El Estado Es: " + state01)
        salir = driver.find_element("xpath", "/html/body/div/div[2]/div[2]/div/div/label").click()
        time.sleep(2)
      except:
        print("Error Al Activar La Cuenta 1")
    else:
      print("Teléfono: " +nameTelefono+ " Con Ip: "+ipTelefono+" Se Encuentra En Estado OK")
      
    print('=======================================================================================')  
    
  driver.close()
  
  print('================= Revisión Terminada Se Volverá a Ejecutar En 10 min ===================')
  time.sleep(600)