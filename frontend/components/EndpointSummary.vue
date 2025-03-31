<template>
  <div>
    <h1 class="mb-2">
        <span class="text-2xl font-bold pr-2">
            {{ props.title }}
        </span>
        <UBadge variant="outline">{{ props.path }}</UBadge>
    </h1>
    <p class="mb-4">
        {{ props.summary }}
    </p>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    title: {
      type: String,
      required: true
    },
    path: {
      type: String,
      required: true
    },
    summary: {
      type: String,
      required: true
    }
})
</script>

<style>

</style>