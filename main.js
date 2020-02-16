const app = new Vue({
    el: '#app',
    data: {
      output : 'Hi',
      translation : '',
      input_language : 'nl',
      output_language : 'fr',
    },
    methods: {
        translate: function(input_language,output_language){
          console.log('test')  
          return this.output = this.translation,
        this.translation = ''
      }
    }
  })