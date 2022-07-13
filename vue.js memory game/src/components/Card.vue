<template>
  <div v-if="card.matched" class="card matched">
  </div>

  <div v-else class="card" @click="clickHandler">
    <img v-if="card.open" :src="card.image" />
    <img v-else src="https://gadalkindom.ru/wp-content/uploads/2018/11/kot.png" />

  </div>
</template>

<script>
export default {
  props: {
    card: Object
  },
  data: () => {
    return {
    }
  },
  methods: {
    clickHandler: function() {
      if (!this.card.open && !this.card.matched) {
        this.$parent.$emit('onCardOpen', this.card)
      }
    }
  }
}
</script>

<style>
.card {
  display: inline-block;
  margin: 25px;
  width: 120px;
  height: 120px;
  vertical-align: top;
  cursor: pointer;
}
.card.matched {
  cursor: default;
}
.card img {
  display: inline-block;
  width: 100%;
  height: 100%;
}
</style>