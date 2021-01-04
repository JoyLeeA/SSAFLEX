<template>
  <img @click="thankyou" src="@/assets/masterByun.png">
</template>

<script>
export default {
    name: 'Fake',
    methods: {
        thankyou: function () {
            alert('교수님 감사합니다!!!!')
        }
    },
}
</script>

<style scoped>
    img {
        width: 100%;
        transition: 0.5s ease;
    }

    img:hover {
        transform: scale(1.2);
    }
</style>