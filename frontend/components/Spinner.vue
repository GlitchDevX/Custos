<template>
  <div class="flex flex-row items-center gap-2 py-4 px-2">
    <div class="spinner" />
    <span>{{ props.label }}</span>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    label: {
      type: String,
      required: true
    }
})
</script>

<style scoped>
.spinner {
    border: 4px solid var(--ui-bg-accented);
    border-top: 4px solid var(--ui-primary);
    height: 25px;
    width: 25px;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
@keyframes spin {
    to {
        rotate: 360deg;
    }
}
</style>