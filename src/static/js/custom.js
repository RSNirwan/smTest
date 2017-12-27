jQuery(init);
function init(){
  var mirror = $('.mirror');
  var widgets = $('.widgets');
  var users_widgets = [];
  var user_name = '{{ name|safe }}';
  var widget_list = JSON.parse('{{ widget_list_as_string|safe }}');
  if ('{{ config|safe }}' != ""){
    var previous_user_config = JSON.parse('{{ config|safe }}');
    renderusers_widgets(previous_user_config);
    users_widgets = previous_user_config;
  }

  //console.log(user_name)
  //renderusers_widgets(previous_user_config)


  $('.tool').draggable({
    helper: 'clone',
  });
  mirror.droppable({
    drop: function(event, ui) {
      var widget = {
        _id: (new Date).getTime(),
        position: ui.position
      };
      widget.position.left -= widgets.width()

      for (var i=0; i<widget_list.length+1; i++){
        if (i==widget_list.length){
          return;
        }
        if (ui.helper.hasClass( widget_list[i] )){
          widget.type = widget_list[i];
          break;
        }
      }
      users_widgets.push(widget);
      renderusers_widgets(users_widgets);
    }
  });
  function renderusers_widgets(users_widgets){
    mirror.empty()
    for( var d in users_widgets){
      var widget = users_widgets[d];
      var html = '<h3>'+widget.type+'</h3>';
      var dom = $(html).css({
        'position': ' absolute',
        'top': widget.position.top,
        'left': widget.position.left 
      }).draggable({
        stop: function(event, ui) {
          //console.log(ui);
          var id = ui.helper.attr('id');
          for (var i in users_widgets) {
            if(users_widgets[i]._id == id) {
              users_widgets[i].position = ui.position;
              users_widgets[i].position.left += widgets.width();
            }
          }
        }
      }).attr('id', widget._id);
      mirror.append(dom);
    }
  }
  $("#resetConfig").click(function(event){
    users_widgets = [];
    renderusers_widgets(users_widgets);
  });
  $("#saveConfig").click(function(event){
    $.ajax({
      type:"POST",
      url:"/post_config/",
      data:{"users_widgets":JSON.stringify(users_widgets),
            "name":user_name}
      // data:{"users_widgets":users_widgets}
    })
  });



  //following functions copy paste from //https://docs.djangoproject.com/en/2.0/ref/csrf/
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });
}
