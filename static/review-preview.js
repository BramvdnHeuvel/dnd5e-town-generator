var previewer = new Vue({
    el: '#preVue',
    data: {
        desc: '',
        showHelp: false
    },
    computed: {
        filledInDesc: function() {
            return this.desc.replace(
                /<TOWN>/g, townName
            ).replace(
                /<SHOP>/g, shopName
            ).replace(
                /<OWNER>/g, ownerName
            ).split('\n');
        }
    }
});