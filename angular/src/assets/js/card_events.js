
function initPromotions() {
    $('#list').click(function(event){event.preventDefault();$('#products .item').addClass('list-group-item');});
    $('#grid').click(function(event){event.preventDefault();$('#products .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');}); 
    
}

function initChoice() {
    $('#list_choice').click(function(event){event.preventDefault();$('#products .item').addClass('list-group-item');});
    $('#grid_choice').click(function(event){event.preventDefault();$('#products .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');}); 
}