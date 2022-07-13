<template>
  <div id="app">
    <h1>Find your cat</h1>
    <Playfield :pairs="9" />
  </div>
</template>

<script>
import Playfield from './components/Playfield.vue'
export default {
  name: 'App',
  components: {
    Playfield
  }
}
</script>

<style>
#app {
  background-color: rgba(127, 255, 255, 0.753);
  width: 1050px;
  margin-top: 35px;
  text-align: center;
  margin: 0px auto;
  padding-top: 10px;
}
</style>
