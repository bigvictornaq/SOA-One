$(document).ready(function () {
    $('#tbl_pocoyo').DataTable({
        "processing": true,
        "ajax": "/Clients/paises",
        "columns": [
            { "data": "Numero_c" },
            { "data": "Pais" }  
        ],
        "dom":'Bfrtilp',
        "buttons":[
            {
                "extend":'pdfHtml5',
                "text":'<i class="fas fa-file">PDF</i>',
                "titleAttr":'Exportar a PDF',
                "className":'btn btn-danger'
            },
            {
                "extend":'print',
                "text":'<i class="fas fa-print">Print</i>',
                "titleAttr":'Print',
                "className":'btn btn-info'
            },
        ]
    });

});
