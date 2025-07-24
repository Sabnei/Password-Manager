import argparse
import getpass
from crypto_utils import derive_key, get_salt
from manager import add_password, get_password, list_services, delete_password
from utils import generate_password

parser = argparse.ArgumentParser(description="Gestor de contraseñas")
subparsers = parser.add_subparsers(dest="command")

# Add
add_parser = subparsers.add_parser("add", help="Agregar una nueva contraseña")
add_parser.add_argument("service", help="Nombre del servicio")
add_parser.add_argument("-u", "--username", help="Nombre de usuario")
add_parser.add_argument("-p", "--password", help="Contraseña")

# Get
get_parser = subparsers.add_parser("get", help="Obtener una contraseña")
get_parser.add_argument("service", help="Nombre del servicio")

# List
subparsers.add_parser("list", help="Listar todos los servicios")

# Delete
delete_parser = subparsers.add_parser("delete", help="Eliminar una contraseña")
delete_parser.add_argument("service", help="Nombre del servicio")

# Generate
generate_parser = subparsers.add_parser(
    "generate", help="Generar una contraseña"
)
generate_parser.add_argument(
    "-l", "--length", help="Longitud de la contraseña", type=int, default=16
)

args = parser.parse_args()

master_password = getpass.getpass("Clave maestra: ")
salt = get_salt()
key = derive_key(master_password, salt)

if args.command == "add":
    add_password(args.service, args.username, args.password, key)
    print(f"[+]Contraseña agregada para {args.service}")

elif args.command == "get":
    record = get_password(args.service, key)
    if record:
        print(f"Usuario: {record['username']}")
        print(f"Contraseña: {record['password']}")
    else:
        print(f"[-] Contraseña no encontrada para {args.service}")

elif args.command == "list":
    services = list_services(key)
    if services:
        print("Servicios almacenados:")
        for service in services:
            print(f"  - {service}")
    else:
        print("[-] No hay servicios registrados")

elif args.command == "delete":
    if delete_password(args.service, key):
        print(f"[+] Contraseña eliminada para {args.service}")
    else:
        print(f"[-] Contraseña no encontrada para {args.service}")

elif args.command == "generate":
    password = generate_password(args.length)
    print(f"[+] Contraseña generada: {password}")

else:
    parser.print_help()
