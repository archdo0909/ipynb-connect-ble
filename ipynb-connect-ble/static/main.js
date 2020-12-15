define(['require','base/js/namespace','base/js/dialog','jquery'],function(requirejs, IPython, dialog, $){
    var ble_connect = {
        help: "ble connect",
        icon: "fa-bluetooth",
    }

    function _on_load(){
        console.info("ble connect")

        var action_name = IPython.keyboard_manager.actions.register(ble_connect, 'connect ble')

        IPython.toolbar.add_buttons_group([action_name])
    }

    return {load_ipython_extension: _on_load};
})
