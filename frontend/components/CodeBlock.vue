<template>
  <div class="codeblock-wrapper p-4 rounded-lg">
    <pre class="text-sm">{{ props.content }}</pre>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    content: {
        type: String,
        required: true
    }
})
</script>

<style scoped>
.codeblock-wrapper {
    background: var(--ui-color-neutral-800);
}
</style>