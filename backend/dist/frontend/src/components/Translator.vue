// Translator.vue
<template>
  <div id="app">
    <h1>Translator App</h1>
    <textarea v-model="input" v-on:keyup.enter = 'translate' id='translation' placeholder = "" style = 'height : 100px; width : 300px'>
    </textarea>
    <textarea v-model="output" placeholder=""  style = 'height : 100px; width : 300px'></textarea>
    <div id="button" style='text-allign : center'>
      <button v-on:click = 'translate' style = 'height : 100; width : 200px; position : center'  > Translate </button> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      output : '',
      input : '',
      input_language : 'nl',
      output_language : 'fr'
    }
  },
  methods: {
    translate: function(input_language,output_language){
      let url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${this.input_language}&tl=${this.output_language}&dt=t&q=${this.input}`;
      axios.get(url)
              .then(response => {
                this.output = response.data[0][0][0]
              })
              .catch(e => {
                this.errors.push(e)
              })
    }   
 }
}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }
</style>