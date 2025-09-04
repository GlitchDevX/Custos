<template>
  <div class="flex justify-center items-center flex-col py-8">
    <div class="config-container">
        <slot/>
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style scoped>
.config-container {
    width: 800px;
}
@media only screen and (max-width: 900px) {
    .config-container {
        width: 100%;
    }
}
</style>