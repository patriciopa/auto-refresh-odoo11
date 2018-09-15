odoo.define('crm_auto_refresh.auto_refresh', function (require) {
    "use strict";
  
    var WebClient = require('web.WebClient');
    var bus = require('bus.bus').bus;
    var utils = require('mail.utils');
    var session = require('web.session');
    var channel = 'auto_refresh_crm';

    WebClient.include({
        start: function(){
            this._super();
            bus.add_channel(channel);
            bus.on("notification", this, this.on_notification);
        },
        on_notification: function (notification) {
          for (var i = 0; i < notification.length; i++) {
             var ch = notification[i][0];
             var msg = notification[i][1];
             if (ch == channel) {
                 this.handler_msg(msg);
             }
           }
        },
        handler_msg: function(msg) {
          if (msg == 'refresh'){ 
            try {  
                var active_view = this.action_manager.inner_widget.active_view;
                var controller = this.action_manager.inner_widget.active_view.controller;
                if (active_view.type == "kanban"){
                    controller.reload();} 
                if (active_view.type == "list"){
                    controller.reload();}
                if (active_view.type == "form"){
                    controller.reload();} 
            } catch(err) {}
          }
        },
    })
});