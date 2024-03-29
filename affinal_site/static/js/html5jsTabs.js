;(function($){
  $.fn.html5jTabs = function(options){
    return this.each(function(index, value){
      var obj = $(this),
      objFirst = obj.eq(index),
      objNotFirst = obj.not(objFirst);
      
      $("#" +  objNotFirst.attr("data-toggle")).hide();
      $(this).eq(index).addClass("active");
      
      obj.click(function(evt){
        
        toggler = "#" + obj.attr("data-toggle");
        togglerRest = $(toggler).parent().find("div");
        
        togglerRest.hide().removeClass("active");
        $(toggler).show().addClass("active");

        //toggle Active Class on tab buttons
        $(this).parent("div").find("a").removeClass("active");
        $(this).addClass("active");

        return false; //Stop event Bubbling and PreventDefault
      });
    });
  };
}(jQuery));

$(function() {
  $(".sub-nav-links ul.sub-nav-ul li a").html5jTabs();
});