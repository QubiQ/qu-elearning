odoo.define('qu_elearning_track_time.calulcatiempo', function(require) {
'use strict';
var ajax = require('web.ajax');
//var rpc = require('web.rpc');



$(document).ready(function(){
  var track_time_fullscreen = document.getElementById("elearning_tracking_time_fullscreen");
  if (track_time_fullscreen)
  {
    var slide_id = $('.o_wslides_fs_sidebar_list_item.active').attr('data-id')
    setInterval(function() {
        ajax.jsonRpc('/slides/update_invested_time','call',{'slide_id': slide_id,'time': 6000}).then(function(data){
              slide_id = $(".o_wslides_fs_sidebar_list_item.active").attr('data-id')
              });
          }, 6000);
        
      }
  var track_time= document.getElementById("elearning_tracking_time");
  if (track_time)
    {
      var slide_id = document.location.pathname.split('/').pop().split('-').pop()
      setInterval(function() {
        ajax.jsonRpc('/slides/update_invested_time','call',{'slide_id': slide_id,'time': 6000}).then(function(data){
            });
        }, 6000);
        
    }
  });

});