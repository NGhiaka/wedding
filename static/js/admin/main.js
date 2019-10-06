 $(document).ready(function() {
    $('body').removeClass('preloading');
    $('#preload').hide();
    $('.select2').select2();

    $('#mydatatable').DataTable();

    CKEDITOR.replace('id_decription');

    $('#id_time_calendar_1').datetimepicker({
        format: 'LT'
    });
    
        
})