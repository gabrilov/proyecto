$(document).ready(function () {
  console.log("Script cargado");
  /****** OBJETOS ******/

  const modulo = {
    id_modulo: "",
    modulo: "",
    url: "",
  };

  const unidad = {
    id_modulo: "",
    unidad: "",
    titulo: ""
  };

  /***** VARIABLES *****/
  const URL = "http://192.168.122.232:5000";
  const cabecera = ["modulos", "unidades"];
  const editIconCell =
    '<td class="iconos edit"><span id="editar" class="material-symbols-outlined">edit</span></td>';
  const trashIconCell =
    '<td class="iconos trash""><span class="material-symbols-outlined">delete_forever</span></td>';
  const templateModulos = `
  <tr id="${modulo.id}">
    <td id="id-modulo" class="tabla-clickable">${modulo.id}</td>
    <td class="tabla-clickable">${modulo.modulo}</td>
    <td class="tabla-clickable">${modulo.url}</td>
    ${trashIconCell}
  </tr>
`;
  const templateUnidades = `
  <tr id="${unidad.id_modulo}">
    <td id="id-modulo" class="tabla-clickable">${unidad.id_modulo}</td>
    <td class="tabla-clickable">${unidad.unidad}</td>
    <td class="tabla-clickable">${unidad.titulo}</td>
    ${trashIconCell}
  </tr>
`;
  let tHeadTabla = "<th>Id</th><th>Nombre</th><th>URL</th>";
  let isUpdate = false;
  let interruptor = "modulos";

  /***** CARGA INFO INICIO *****/

  recuperarItems();

  /***** EVENTOS ******/

  $("#modulos").click(function (e) {
    if (interruptor != "modulos") {
      $("#form-modulo")[0].reset();
      $("#label2")[0].textContent = "Nombre";
      $("#label3")[0].textContent = "URL";
      tHeadTabla = "<th>Id</th><th>Nombre</th><th>URL</th>";
      interruptor = "modulos";
      recuperarItems();
    }
  });

  $("#unidades").click(function (e) {
    if (interruptor != "unidades") {
      $("#form-modulo")[0].reset();
      interruptor = "unidades";
      tHeadTabla = "<th>Modulo</th><th>Título</th><th>Unidad</th>";
      $("#label2")[0].textContent = "Título";
      $("#label3")[0].textContent = "Unidad";
      recuperarItems();
    }
  });

  $("button[type='submit']").click(function (e) {
    e.preventDefault();
    if ($("#id-modulo").val() == "") {
      $(".mensaje").css("display", "block");
      return;
    }
    modulo.id_modulo = $("#id-modulo").val();
    modulo.modulo = $("#nombre").val();
    modulo.url = $("#url").val();
    if (interruptor == "unidades") {
      unidad.id_modulo = $("#id-modulo").val();
      unidad.unidad= $("#url").val();
      unidad.titulo = $("#nombre").val();
    }
    registrarModulo();
    $("#form-modulo")[0].reset();
  });

  $("button[type='reset']").click(function (e) {
    isUpdate = false;
  });

  /***** FUNCIONES *****/

  function recuperarItems() {
    $("#thead").html(tHeadTabla);
    $.ajax({
      type: "GET",
      url: `${URL}/${interruptor}`,
      headers: {
        "access-control-allow-origin": "*",
      },
      dataType: "json",
      success: function (response) {
        let template = '';
        if (interruptor == "modulos") {
          response.modulos.forEach((item) => {
            template += populateTemplate(item);
          });
        } else {
          response.unidades.forEach((item) => {
            template += populateTemplate(item);
          });
        }
        $('#tbody').html(template);
      },
      complete: function (data) {
        $(".tabla-clickable").click(function (e) {
          const clave = $(this)[0].parentElement.getAttribute('id');
          isUpdate = true;
          if(interruptor == "unidades") {
           const claveUnidad = $(this)[0].parentElement.children[1].textContent;
           llamarUnItem(clave, claveUnidad)
          } else {
            llamarUnItem(clave);
          }
        });
        
        $(".trash").click(function (e) {
          const clave = $(this)[0].parentElement.getAttribute('id');
          if(interruptor == "unidades") {
            const claveUnidad = $(this)[0].parentElement.children[1].textContent;
            borrarModulo(clave, claveUnidad)
           } else {
             borrarModulo(clave);
           }
        });
      },
    });
  }

  function llamarUnItem(moduloId, unidadId) {
    let endpoint = `${URL}/${interruptor}/${moduloId}/${unidadId}`;
    if (interruptor == "modulos") {
      endpoint = `${URL}/${interruptor}/${moduloId}`;    
    }
    $.ajax({
      type: "GET",
      url: endpoint,
      dataType: "json",
      success: function (response) {
        if (interruptor == "modulos") {
          modulo.id_modulo = moduloId;
          modulo.modulo = response.modulo.modulo;
          modulo.url = response.modulo.url;
        } else {
          unidad.id_modulo = moduloId;
          unidad.unidad = unidadId;
          unidad.titulo = response.unidad.titulo;
        }
      },
      complete: function (data) {
        if(interruptor == "modulos") {
          $("#id-modulo").val(modulo.id_modulo);
          $("#nombre").val(modulo.modulo);
          $("#url").val(modulo.url);          
        } else {
          $("#id-modulo").val(unidad.id_modulo);
          $("#nombre").val(unidad.titulo);
          $("#url").val(unidad.unidad);  
        }
      },
    });
  }
  
  function registrarModulo() { 
    let item = modulo   
    let tipo = "POST";
    let urlRegistro = `${URL}/modulo`;
    let actualizarEndpoint = `${URL}/modulo/${item.id_modulo}`;
    if (interruptor == "unidades") {
      urlRegistro = `${URL}/unidad`
      item = unidad;
    }
    if (isUpdate) {
      if(interruptor == "unidades") {
        actualizarEndpoint = `${URL}/unidad/${item.id_modulo}/${item.unidad}`;
      }
      urlRegistro = actualizarEndpoint;
      tipo = "PUT";
    }
    $.ajax({
      type: tipo,
      headers: {
        "access-control-allow-origin": "*",
      },
      url: urlRegistro,
      data: JSON.stringify(item),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function (response) {
        recuperarItems();
      },
    });
    isUpdate = false;
  }

    // TODO: De aquí en adelante

  function borrarModulo(modId, unidadId) {
    let endpoint = `${URL}/modulo/${modId}`;
    if(interruptor == "unidades") {
      endpoint = `${URL}/unidad/${modId}/${unidadId}`
    }
    $.ajax({
      type: 'DELETE',
      url: endpoint,
      dataType: "json",
      success: function (response) {
        if (response.mensaje != "") {
          recuperarItems();
        }
      },
    });
  }

  function populateTemplate(item) {
    if (interruptor == "modulos") {
      return `
      <tr id="${item.id}">
        <td id="id-modulo" class="tabla-clickable">${item.id}</td>
        <td class="tabla-clickable">${item.modulo}</td>
        <td class="tabla-clickable">${item.url}</td>
        ${trashIconCell}
      </tr>
    `;
    } else if (interruptor == "unidades") {
      return `
      <tr id="${item.id_modulo}">
        <td id="id-modulo" class="tabla-clickable">${item.id_modulo}</td>
        <td class="tabla-clickable">${item.unidad}</td>
        <td class="tabla-clickable">${item.titulo}</td>
        ${trashIconCell}
      </tr>
    `;
    }
  }
});