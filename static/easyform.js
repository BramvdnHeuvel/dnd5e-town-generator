var formMaker = new Vue({
    el: '#formMaker',
    data: {
        size: '',
        townName: ''
    },
    computed: {
        townLink: function() {
            return '/town/' + this.townName + '/' + this.size;
        }
    }
});