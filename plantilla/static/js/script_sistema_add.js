//************************************************************************************
// Funciones adicionales para la configuración de los datatable
//************************************************************************************
var titulo_sistema = "Sistema de Gestión Copextel Granma"
//-------------------------------------------------------------------------------------
function fecha_actual(){
  fecha = new Date();
  //----------------------------------------------------------------
  dia = fecha.getDate();
  mes = fecha.getMonth() + 1;
  anno = fecha.getFullYear();
  fecha_final = dia + "/" + mes + "/" + anno;
  //----------------------------------------------------------------
  hora = fecha.getHours();
  minutos = fecha.getMinutes();
  segundos = fecha.getSeconds();
  jornada = hora >= 12 ? "PM" : "AM";
  //if (hora < 10) hora = "0" + hora;
  if (minutos < 10) minutos = "0" + minutos;
  if (segundos < 10) segundos = "0" + segundos;
  if (hora == 12)
    hora_final = hora + ":" + minutos + ":" + segundos + " " + jornada;
  else
    hora_final = hora % 12 + ":" + minutos + ":" + segundos + " " + jornada;
  //----------------------------------------------------------------
  texto = "Fecha de generación del documento: " + fecha_final + " - " + hora_final;
  return texto;
}
//-------------------------------------------------------------------------------------
// Traducción del datatable en español
var datatable_espannol = {
  "emptyTable": "No hay información",
  "lengthMenu": "Mostrar _MENU_ resultados",
  "search": "Buscar:",
  "zeroRecords": "Sin resultados encontrados",
  "info": "Mostrando _START_ a _END_ de _TOTAL_ resultados",
  "infoEmpty": "No hay resultados",
  "infoFiltered": "(Filtrado de _MAX_ resultados)",
  "loadingRecords": "Cargando...",
  "processing": "Procesando...",
  "paginate": {
    "first": "Primero",
    "last": "Ultimo",
    "next": "Siguiente",
    "previous": "Anterior"
  },
  "buttons": {
    "excel": "Excel",
    "pdf": "PDF",
    "print": "Imprimir",
    "colvis": "Visibilidad de columnas"
  }
}
//-------------------------------------------------------------------------------------
// Botón para guardar el datatable en Excel
function btn_excel(titulo_doc, columnas_exportar){
  var btn_excel =
    {
      "extend": "excelHtml5",
      "text": 'Excel',
      "titleAttr": "Guardar en Excel",
      "idText": "excel",
      "className": "btn btn-secondary",
      filename: titulo_doc,
      title: titulo_sistema,
      messageTop: titulo_doc,
      exportOptions: { columns: columnas_exportar }
    }
  return btn_excel;
}
//-------------------------------------------------------------------------------------
function add_texto(){
  var resultado = document.getElementById("info_add");
  return resultado.innerText;
}
//-------------------------------------------------------------------------------------
// Botón para guardar el datatable en PDF
function btn_pdf(titulo_doc, columnas_exportar, orientacion_hoja, info_add=0){
  //----------------------------------------------------------------------------
  var tipo_orientation = "";
  if (orientacion_hoja == "h") 
    tipo_orientation = "landscape"; //horizontal
  else {
    if (orientacion_hoja == "v") 
      tipo_orientation = "portrait"; //vertical
  }
  //----------------------------------------------------------------------------
  if (info_add == 0)
    mensaje_top = fecha_actual() + "\n \n" + titulo_doc;
  else
    mensaje_top = fecha_actual() + "\n" + add_texto() + "\n" + titulo_doc;
  //----------------------------------------------------------------------------
  var btn_pdf =
    {
      "extend": "pdfHtml5",
      "text": 'PDF',
      "titleAttr": "Guardar en PDF",
      "idText": "pdf",
      "className": "btn btn-secondary",
      filename: titulo_doc,
      title: titulo_sistema,
      messageTop: mensaje_top,
      pageSize: 'LETTER',
      orientation: tipo_orientation,
      exportOptions: { columns: columnas_exportar },
      customize: function (doc) {
        doc.styles = {
          tableHeader:{
            bold: true,
            color: "white",
            fillColor: "#d12421",
            alignment: "center",
            margin: 2
          },
          //tableBodyEven: {},
          tableBodyOdd: {fillColor: "#f3f3f3"},
          title: {
            bold: true,
            alignment: "center",
            fontSize: 14,
          },
          message: {bold: true},
        };
        //splice(1, 0) -- Logo despues del titulo 
        doc.content.splice(0, 0, {
          margin: [0, 0, 0, 5],
          alignment: 'center',
          image: 'data:image/png;base64,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'
        });
      }
    }
  return btn_pdf;
}
//-------------------------------------------------------------------------------------
// Botón para imprimir el datatable
function btn_print(titulo_doc, columnas_exportar){
  var btn_print =
    {
      "extend": "print",
      "text": 'Imprimir',
      "titleAttr": "Imprimir documento",
      "idText": "print",
      "className": "btn btn-secondary",
      filename: titulo_doc,
      title: titulo_sistema,
      messageTop: titulo_doc,
      exportOptions: { columns: columnas_exportar }
    }
  return btn_print;
}
//-------------------------------------------------------------------------------------
// Botón para la Visibilidad de columnas
function btn_colvis(){
  var btn_colvis =
    {
      "extend": "colvis",
      "text": 'Visibilidad de columnas',
      "titleAttr": "Visibilidad de columnas",
      "idText": "colvis",
      "className": "btn btn-secondary",
      columns: 'th:nth-child(n+2)'
    }
  return btn_colvis;
}
//-------------------------------------------------------------------------------------
// Configuración para desactivar el ordenamiento en columnas
function no_ordenar(columnas_a_desactivar){
  var no_ordenar =
    {
      "bSortable": false,
      "aTargets": columnas_a_desactivar
    }
  return no_ordenar;
}
//************************************************************************************
// Funciones de las gráficas
//************************************************************************************
function lenguaje_grafica(){
  var lenguaje_grafica =
    {      
      contextButtonTitle: "Menú de opciones",
      viewFullscreen:     "Ver en pantalla completa",
      exitFullscreen:     "Salir de pantalla completa",
      printChart:         "Imprimir gráfica",
      downloadPNG:        "Descargar imagen PNG",
      downloadJPEG:       "Descargar imagen JPEG",
      downloadPDF:        "Descargar documento PDF",
      downloadSVG:        "Descargar imagen SVG",
      downloadCSV:        "Descargar documento CSV",
      downloadXLS:        "Descargar documento XLS",
      viewData:           "Ver datos",
      hideData:           "Ocultar datos",
      exportData: {
        categoryHeader:     "Etiqueta",
      }
    }
  return lenguaje_grafica;
}
//-------------------------------------------------------------------------------------
function tipo_de_grafica(tipo){
  var tipo =
    {
      type: tipo
    }
  return tipo;
}
//-------------------------------------------------------------------------------------
function titulo_grafica (titulo, alineado){
  var titulo_grafica =
    {
      text: titulo,
      align: alineado
    }
  return titulo_grafica;
}
//-------------------------------------------------------------------------------------
function datos_grafica(label, color, arreglo_datos){
  var opciones_datos_grafica =
    {
      name: label,
      color: color,
      data: arreglo_datos,
      dataLabels: {
          enabled: true
      },
    }
  return opciones_datos_grafica;
}
//-------------------------------------------------------------------------------------
//menuItems: ["viewFullscreen", "printChart", "downloadPNG", "downloadJPEG", "downloadSVG", "downloadPDF", "downloadCSV" ,"downloadXLS"]
function opciones_menu_exportar(){
  var opciones_menu =
    {
      buttons: {
        contextButton: {
          menuItems: ["viewFullscreen", "printChart", "downloadXLS"]
        },
      },
    }
  return opciones_menu;
}
//-------------------------------------------------------------------------------------
function opciones_x(labels){
  var opciones_x =
    {
      min: 0,
      categories: labels,
      crosshair: true,
      title: { text: null },
      gridLineWidth: 1,
      lineWidth: 0
    }
    return opciones_x;
}
//-------------------------------------------------------------------------------------
function opciones_y(texto_eje){
  var opciones_y =
    {
      min: 0,
      title: {
          text: texto_eje,
          align: 'high'
      },
      labels: {
          overflow: 'justify'
      },
      gridLineWidth: 0
    }
    return opciones_y;
}
//-------------------------------------------------------------------------------------
function sin_creditos(){
  var creditos =
    {
      enabled: false
    }
    return creditos
}
//------------------------------------------------------------------------------------
function plotOptions_bar(){
  var plotOptions_bar =
    {
      bar: {
          borderRadius: '50%',
          dataLabels: {
              enabled: true
          },
          groupPadding: 0.1
      }
    }
    return plotOptions_bar
}
//************************************************************************************
// Gráficas implementadas
//************************************************************************************
//------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------
//************************************************************************************
// Componentes
//************************************************************************************
$(function () {
  //-------------------------------------------------------------------------------------
  $.fn.select2.defaults.set('language', 'es');
  $('.select2').select2()
  //-------------------------------------------------------------------------------------
});
 //-------------------------------------------------------------------------------------
function eliminar_generico(url_view_de_confirmacion, id, url_view_de_eliminacion, rec=0){
  if (rec==0){
    direccion = '/' + url_view_de_eliminacion + '/' + id;
  }
  else  {
    direccion = '/' + url_view_de_eliminacion + '/' + id + '/' + rec;
  }
  $.confirm({
    theme: "modern",
    icon: "fa fa-times-circle",
    type: "red",
    title: "Confirmación Requerida",
    content: 'url:/' + url_view_de_confirmacion + '/' + id,
    buttons: {
      confirm:{
        text: 'Confirmar',
        btnClass: 'btn-primary',
        action: function () {
          $.ajax({
            url: direccion,
            type: 'GET',            
            success: function(data) {
              location.reload();
            }
          })      
        },
      },
      cancel:{
        text: 'Cancelar',
        btnClass: 'btn-danger',
      },
    },
  });
}
//-------------------------------------------------------------------------------------