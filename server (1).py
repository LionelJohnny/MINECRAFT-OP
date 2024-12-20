# Server.py Versiones disponibles
# forge, mohist, fabric, vanilla, paper

# Puedes instalar mohist después de instalar forge desde el menú de gestionar
# Puedes instalar paper después de instalar vanilla desde el menú de gestionar
# Puedes instalar purpur después de instalar fabric desde el menú de gestionar

# Regiones de ngrok
# Código          Lugar
#-----------      ---------------------------
# ap	          Asia / Pacífico (Singapore)
# au		      Australia (Sydney)
# eu		      Europa (Frankfurt)
# in		      India (Mumbai)
# jp		      Japón (Tokyo)
# sa		      Sudamérica (São Paulo)
# us		      Estados unidos (Ohio)
# us-cal-1	      Estados unidos (California)




def download_latest_release(download_path='.'):
    mirror = "https://elyxdev.github.io/latest"
    try:
        pet = requests.get(mirror)
        pet.raise_for_status()  # Lanza una excepción si el status code no es 200
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar descargar el archivo: {e}")
        return None
    if pet.status_code == 200:
        data = pet.json()
        url = data.get('latest')
        version = url.split("/")[-1]
        if version in glob.glob("*.msp"):
            return version
        else:
            os.system("rm *.msp")
            print("Actualizando tu versión de MSP...")
            time.sleep(1.5)
        pathto = os.path.join(download_path, version)
        with open(pathto, 'wb') as archivo:
            archivo.write(requests.get(url).content)
        return version










