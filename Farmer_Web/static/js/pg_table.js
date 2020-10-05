$(document).ready(function () {
    $('#tbl_country').DataTable({
        "processing": true,
        "ajax": "/Countries/raws",
        "columns": [
            { "data": "country_id" },
            { "data": "country" },
            { "data": "last_update" }
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
