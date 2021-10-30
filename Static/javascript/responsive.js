 

$(window).on('resize load',function(e){
    if($(window).width()<700){$('.gallerytext').attr('data-aos','fade-out')}
    else{$('.gallerytext').css('data-aos','fade-left')}
}) 
$(window).on('resize load',function(e){
    if($(window).width()<700){$('.fadeleft').attr('data-aos','fade-out')}
    else{$('.fadeleft').css('data-aos','fade-left')}
}) 


