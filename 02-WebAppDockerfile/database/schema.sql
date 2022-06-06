create database if not exists modulos;

use modulos;

create table if not exists modulos (
  id_modulo varchar(6) primary key not null,
  modulo varchar(200) not null,
  url varchar(250)
) engine = InnoDB;

create table if not exists unidades (
  id_modulo varchar(6) not null,
  unidad tinyint not null,
  titulo varchar(255) not null,
  primary key (id_modulo, unidad),
  constraint fk_unidades_modulos foreign key(id_modulo) references modulos(id_modulo) on delete restrict on update cascade
) engine = InnoDB;


/*  **** Dummy data **** */
insert into
  modulos
values(
    "ASO",
    "Administración de Sistemas Operativos",
    "#"
  ),
  (
    "ASGBD",
    "Administración de Sistemas Gestores de Base de Datos",
    "#"
  ),
  (
    "SRI",
    "Servicios de Red e Internet",
    "#"
  ),
  (
    "IAW",
    "Implantación de Aplicaciones Web",
    "#"
  ),
  (
    "SAD",
    "Seguridad y Alta Disponibilidad",
    "#"
  ),
  (
    "EIE",
    "Empresa e Iniciativa Emprendedora",
    "#"
  );
insert into
  unidades
values
  (
    "ASO",
    1,
    "Servicios de acceso y administración remota"
  ),
  (
    "ASO",
    2,
    "Administración de servidores de impresión"
  ),
  (
    "ASO",
    3,
    "Administración de servicios de directorio"
  ),
  (
    "IAW",
    1,
    "Instalación de servidores de aplicaciones web"
  ),
  (
    "IAW",
    2,
    "Programación de documentos web utilizando lenguajes de script de servidor"
  ),
  (
    "IAW",
    3,
    "Acceso a bases de datos desde lenguajes de script de servidor"
  );
